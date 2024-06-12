-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 12 juin 2024 à 14:53
-- Version du serveur : 8.2.0
-- Version de PHP : 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `banque`
--
CREATE DATABASE IF NOT EXISTS `banque`;
USE `banque`;
-- --------------------------------------------------------

--
-- Structure de la table `client`
--

DROP TABLE IF EXISTS `client`;
CREATE TABLE IF NOT EXISTS `client` (
  `id_client` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `pin` varchar(200) NOT NULL,
  `solde` int NOT NULL,
  `num_compte` varchar(10) NOT NULL,
  `identifiant` varchar(20) NOT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `last_seen` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id_client`),
  UNIQUE KEY `num_compte` (`num_compte`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`id_client`, `nom`, `prenom`, `pin`, `solde`, `num_compte`, `identifiant`, `is_admin`, `last_seen`, `created_at`, `updated_at`) VALUES
(1, 'N', 'Philippe', '827ccb0eea8a706c4c34a16891f84e7b', 10000, '003001', 'melo', 0, NULL, '2024-05-20 13:52:36', '2024-05-25 19:56:03'),
(2, 'Aboubacar', 'Diallo', '827ccb0eea8a706c4c34a16891f84e7b', 10000, '003002', 'diallo', 0, NULL, '2024-05-20 14:32:50', '2024-05-27 12:54:03');

-- --------------------------------------------------------

--
-- Structure de la table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction` (
  `id_transaction` int NOT NULL AUTO_INCREMENT,
  `montant` int NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  `matricule_transaction` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `compte_emmeteur` varchar(10) NOT NULL,
  `compte_recepteur` varchar(10) NOT NULL,
  `etat` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id_transaction`),
  UNIQUE KEY `matricule_transaction` (`matricule_transaction`),
  KEY `compte_emmeteur` (`compte_emmeteur`),
  KEY `compte_recepteur` (`compte_recepteur`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
