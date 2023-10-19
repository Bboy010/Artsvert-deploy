-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 09 juil. 2023 à 01:23
-- Version du serveur : 10.4.27-MariaDB
-- Version de PHP : 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `artsvert_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `admins`
--

CREATE TABLE `admins` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `admins`
--

INSERT INTO `admins` (`id`, `name`, `email`, `password`, `created_at`, `updated_at`) VALUES
(1, 'Le Peintre', 'lepeintre@gmail.com', 'sha256$fXsmKlZucQZInQW5$9877180ecbb72f91392f9740ff567d805b53a518a7665cb8d0ffae2e4d39265b', '2023-07-05 15:34:53', '2023-07-05 15:34:53'),
(2, 'Bboyart', 'bboyart@gmail.com', 'sha256$66EPhUFpomGxdDjr$26ba6bbe6f76e31a38603e2c21ff11842b249cffad7566e10ed7678c0b222c24', '2023-07-05 15:35:18', '2023-07-05 15:35:18');

-- --------------------------------------------------------

--
-- Structure de la table `artists`
--

CREATE TABLE `artists` (
  `id` int(11) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `tel` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `picture_url` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `artists`
--

INSERT INTO `artists` (`id`, `firstname`, `lastname`, `email`, `tel`, `country`, `city`, `picture_url`, `password`, `created_at`, `updated_at`) VALUES
(1, 'HONGO', 'Anderson', 'hongo@gmail.com', '07-78-46-13-31', 'Ivory Coast', 'Abidjan', 'static/images/profile_pictures/4.multiply.png','sha256$XTqdtGogVJi2qCYL$15d9975f03bc0de60950ace02f146643c961839280040416c3c5190f965e7d9e', '2023-07-05 15:56:30', '2023-07-05 15:56:30'),
(2, 'BALLO', 'Mamadou', 'mamadouballo@gmail.com', '05-45-21-13-11', 'Ivory Coast', 'Bouake','static/images/profile_pictures/3.multiply.png', 'sha256$3X8BgKRqgaRUcgYa$d622b8c2bf21c27232750c0885739e1bf3854b49961572223ca5d80cb51a2e6f', '2023-07-05 16:00:17', '2023-07-05 16:00:17');

-- --------------------------------------------------------

--
-- Structure de la table `artworks`
--

CREATE TABLE `artworks` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(200) NOT NULL,
  `image_url` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `artist_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `artworks`
--

INSERT INTO `artworks` (`id`, `name`, `description`, `image_url`, `price`, `artist_id`, `category_id`, `created_at`, `updated_at`) VALUES
(1, 'Why', 'Peinture acrylique\r\n370L x 395H cm\r\n2018', 'static/images/painting/paint-1.jpg', 250, 2, 1, '2023-07-06 00:30:20', '2023-07-06 00:30:20'),
(2, 'Bella', 'Digital draw\r\n21L x 29,7H cm\r\n2023', 'static/images/print/print-1.png', 500, 1, 2, '2023-07-06 02:29:47', '2023-07-06 02:29:47'),
(3, 'Adja', ' Modeling\r\n87 x 38 x 32 cm\r\n2018', 'static/images/sculpture/sculpture-3.jpg', 800, 2, 3, '2023-07-06 07:21:02', '2023-07-06 07:21:02'),
(4, 'Rolex', 'Acrylic paint\r\n23L x 29,5H cm\r\n2022 ', 'static/images/painting/paint-4.jpg', 345, 2, 1, '2023-07-06 14:03:43', '2023-07-06 14:03:43'),
(5, 'Friends', 'Acrylic paint\r\n22L x 29H cm\r\n2023\r\n', 'static/images/painting/paint-6.jpg', 410, 2, 1, '2023-07-06 18:32:48', '2023-07-06 18:32:48'),
(6, 'Karidjatou', 'Acrylic paint\r\n25L x 32H cm\r\n2017', 'static/images/painting/paint-2.jpg', 510, 2, 1, '2023-07-06 18:35:15', '2023-07-06 18:35:15'),
(7, 'Twofaces ', 'Acrylic paint\r\n23L x 29,5H cm\r\n2022 ', 'static/images/painting/paint-5.jpg', 320, 2, 1, '2023-07-06 18:37:11', '2023-07-06 18:37:11'),
(8, 'Natty', 'Acrylic paint\r\n23L x 29,5H cm\r\n2017 ', 'static/images/painting/paint-3.jpg', 379, 2, 1, '2023-07-06 18:40:02', '2023-07-06 18:40:02'),
(9, 'Maya', 'Modeling\r\n87 x 35 x 30 cm\r\n2018 ', 'static/images/sculpture/sculpture-1.jpg', 230, 2, 3, '2023-07-06 23:12:21', '2023-07-06 23:12:21'),
(10, 'Uncle', 'Digital painting\r\n21L x 29,7H cm\r\n2023\r\n60', 'static/images/print/print-3.png', 45, 1, 2, '2023-07-07 17:36:46', '2023-07-07 17:36:46');

-- --------------------------------------------------------

--
-- Structure de la table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `categories`
--

INSERT INTO `categories` (`id`, `label`, `created_at`, `updated_at`) VALUES
(1, 'painting', '2023-07-05 17:29:31', '2023-07-05 17:29:34'),
(2, 'print', '2023-07-05 17:30:15', '2023-07-05 17:30:17'),
(3, 'sculpture', '2023-07-05 17:30:43', '2023-07-05 17:30:45');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Index pour la table `artists`
--
ALTER TABLE `artists`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Index pour la table `artworks`
--
ALTER TABLE `artworks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `artist_id` (`artist_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Index pour la table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `artists`
--
ALTER TABLE `artists`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `artworks`
--
ALTER TABLE `artworks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pour la table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `artworks`
--
ALTER TABLE `artworks`
  ADD CONSTRAINT `artworks_ibfk_1` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`id`),
  ADD CONSTRAINT `artworks_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
