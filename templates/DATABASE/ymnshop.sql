-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 08 May 2023, 13:38:04
-- Sunucu sürümü: 10.4.25-MariaDB
-- PHP Sürümü: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `ymnshop`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `title` text NOT NULL,
  `type` text NOT NULL,
  `content` text NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `products`
--

INSERT INTO `products` (`id`, `title`, `type`, `content`, `created_date`) VALUES
(12, 'DENEME 1', 'mohammad_kashim', '<p>DENEME 1&nbsp;DENEME 1&nbsp;DENEME 1&nbsp;DENEME 1&nbsp;DENEME 1</p>\r\n', '2023-05-08 11:24:58'),
(13, 'DENEME 2 ', 'mohammad_kashim', '<p>DENEME 2&nbsp;&nbsp;DENEME 2&nbsp;&nbsp;DENEME 2&nbsp;&nbsp;DENEME 2&nbsp;&nbsp;DENEME 2&nbsp;</p>\r\n', '2023-05-08 11:25:09');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `username`, `password`) VALUES
(13, 'Mohammad Kashim', 'mohammad_kashim@outlook.com', 'mohammad_kashim', '$5$rounds=535000$.aTMBxf8uRFUCLL.$lF6WmiPBTEitETryrM88wJbNTeBINNvOxgZ2cz0nem0'),
(14, 'Asım Yuksel', 'asimyuksel@sdu.edu.tr', 'Asım_Yuksel', '$5$rounds=535000$cbPSX2YJz6MobWlr$s7BItNQx9IAG/YydtBZ5tZGCaEGB9u5tfHmS4IsLehC');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
