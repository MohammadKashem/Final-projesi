from flask import Flask , render_template , flash , redirect , url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form , StringField , TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

#Kullanıcı Giriş (user login)  Decorator 
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Sayfayı Görüntülemek İçin Giriş Yapınız.","danger")
            return redirect(url_for("login"))
    return decorated_function


# Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("Ad Soyad",validators = [validators.Length(min = 3 , max = 20)])
    username = StringField("Kullanıcı Adı",validators = [validators.Length(min = 6 , max = 15)])
    email = StringField("E-mail Adresi",validators = [validators.Email(message = "Lütfen Geçerli e-mail Giriniz")])
    password = PasswordField("Parola:",validators=[
        validators.DataRequired(message = "Lütfen Bir Parola Giriniz"),
        validators.EqualTo(fieldname = "confirm",message = "Parola Geçersiz")
    ])
    confirm = PasswordField("Parola Doğrula")

class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")                                                               
    

app = Flask(__name__)
app.secret_key = "ymnshop"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "ymnshop"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

#ürün product sayfası
@app.route("/product")
def products():
    cursor = mysql.connection.cursor()

    sorgu ="Select *From products"

    result = cursor.execute(sorgu)
    if result > 0:
        products = cursor.fetchall()
        return render_template("products.html",products = products)
    else:
        return render_template("products.html")
    









@app.route("/dashboard")
@login_required
def dashboard():
    cursor = mysql.connection.cursor()
    sorgu = "Select *From products where type = %s"
    result = cursor.execute(sorgu,(session["username"],))
    if result > 0:
        products = cursor.fetchall()
        return render_template("dashboard.html",products = products)
    
    else:
        pass
         

    return render_template("dashboard.html")


#Register (Üye Olma )Alanı
@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        sorgu = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"

        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()

        flash("Başarıyla Kayıt Oldunuz..","success")
        return redirect(url_for("login"))
   


    else:
        return render_template("register.html",form = form)


#Login (Giriş Yap) İşlemi
@app.route("/login",methods = ["GET","POST"])
def login(): 
    form = LoginForm(request.form)
    if request.method == "POST":
        username = form.username.data
        password_entered = form.password.data

        cursor = mysql.connection.cursor()

        sorgu = "Select *From users where username = %s"

        result = cursor.execute(sorgu,(username,))

        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"]
            if sha256_crypt.verify (password_entered,real_password):
                flash("Giriş Başarılı","success")

                session["logged_in"] = True
                session["username"] = username


                return redirect(url_for("index"))
            else:
                flash("Parola Yanlış","danger")
                return redirect(url_for("login"))
            


        else:
            flash("Kulllanıcı Bulunamadı..","danger")
            return redirect(url_for("login"))
        
        



    return render_template("login.html",form = form)


#Logout (Çıkış Yap) işlemi
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


#Ürün Ekleme Alanı
@app.route("/addproduct",methods = ["GET","POST"])
def addproduct():
    form = ProductForm(request.form)
    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data

        cursor = mysql.connection.cursor()
        sorgu = "Insert into products(title,type,content) VALUES(%s,%s,%s)"
        cursor.execute(sorgu,(title,session["username"],content))
        mysql.connection.commit()
        cursor.close()
        flash("Ürün Eklendi","success")
        return redirect(url_for("dashboard"))
    
    return render_template("addproduct.html",form = form)

#Ürün Silme
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()

    sorgu = "Select *from products where type = %s and id = %s  "

    result = cursor.execute(sorgu,(session["username",id]))
    if result > 0:
        sorgu2 = "Delete from products where id = %s"

        cursor.execute(sorgu2,(id,))

        mysql.connection.commit()
        return redirect(url_for("dashboard"))
    

    else:
        flash("Ürün bulunamadı veya yetkiniz yok","danger")
        return redirect(url_for("index"))
    





# Ürün Form oluşturma
class ProductForm(Form):
    title = StringField("Ürün Açıklaması",validators = [validators.Length(min = 1 , max = 100)])
    content = TextAreaField("Ürün İçeriği",validators = [validators.Length(min = 10 , max = 1000)])





#Detay Sayfası
@app.route("/product/<string:id>")
def product(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select *from products where id = %s"

    result = cursor.execute(sorgu,(id,))
    if result > 0:
        product = cursor.fetchone()
        return render_template("product.html",product = product)
    
    else:
        return render_template("product.html")







if __name__ == "__main__":   
    app.run(debug=True) 

