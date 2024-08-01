-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: new_schema
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `credentials`
--

DROP TABLE IF EXISTS `credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `credentials` (
  `USN` varchar(10) DEFAULT NULL,
  `USERNAME` varchar(20) DEFAULT NULL,
  `PASS` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credentials`
--

LOCK TABLES `credentials` WRITE;
/*!40000 ALTER TABLE `credentials` DISABLE KEYS */;
INSERT INTO `credentials` VALUES ('1bi22is1','user1','bit1'),('1bi22is2','user2','bit2'),('1bi22is3','user3','bit3'),('1bi22is4','user4','bit4'),('1bi22is5','user5','bit5'),('1bi22is6','user6','bit6'),('1bi22is7','user7','bit7'),('1bi22is8','user8','bit8'),('1bi22is9','user9','bit9'),('1bi22is10','user10','bit10'),('1bi22is11','user11','bit11'),('1bi22is12','user12','bit12'),('1bi22is13','user13','bit13'),('1bi22is14','user14','bit14'),('1bi22is15','user15','bit15'),('1bi22is16','user16','bit16'),('1bi22is17','user17','bit17'),('1bi22is18','user18','bit18'),('1bi22is19','user19','bit19'),('1bi22is20','user20','bit20'),('1bi22is21','user21','bit21'),('1bi22is22','user22','bit22'),('1bi22is23','user23','bit23'),('1bi22is24','user24','bit24'),('1bi22is25','user25','bit25'),('1bi22is26','user26','bit26'),('1bi22is27','user27','bit27'),('1bi22is28','user28','bit28'),('1bi22is29','user29','bit29'),('1bi22is30','user30','bit30'),('1bi22is31','user31','bit31'),('1bi22is32','user32','bit32'),('1bi22is33','user33','bit33'),('1bi22is34','user34','bit34'),('1bi22is35','user35','bit35'),('1bi22is36','user36','bit36'),('1bi22is37','user37','bit37'),('1bi22is38','user38','bit38'),('1bi22is39','user39','bit39'),('1bi22is40','user40','bit40'),('1bi22is41','user41','bit41'),('1bi22is42','user42','bit42'),('1bi22is43','user43','bit43'),('1bi22is44','user44','bit44'),('1bi22is45','user45','bit45'),('1bi22is46','user46','bit46'),('1bi22is47','user47','bit47'),('1bi22is48','user48','bit48'),('1bi22is49','user49','bit49'),('1bi22is50','user50','bit50'),('1bi22is51','user51','bit51'),('1bi22is52','user52','bit52'),('1bi22is53','user53','bit53'),('1bi22is54','user54','bit54'),('1bi22is55','user55','bit55'),('1bi22is56','user56','bit56'),('1bi22is57','user57','bit57'),('1bi22is58','user58','bit58'),('1bi22is59','user59','bit59'),('1bi22is60','user60','bit60'),('1bi22is61','user61','bit61'),('1bi22is62','user62','bit62'),('1bi22is63','user63','bit63'),('1bi22is64','user64','bit64'),('1bi22is65','user65','bit65'),('1bi22is66','user66','bit66'),('1bi22is67','user67','bit67'),('1bi22is68','user68','bit68'),('1bi22is69','user69','bit69'),('1bi22is70','user70','bit70');
/*!40000 ALTER TABLE `credentials` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-16 15:37:04
