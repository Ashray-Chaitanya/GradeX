-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: new_schema
-- ------------------------------------------------------
-- Server version	8.0.38

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
-- Table structure for table `1bi22is52`
--

DROP TABLE IF EXISTS `1bi22is52`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `1bi22is52` (
  `Subject` text,
  `Subject Name` text,
  `Internal` text,
  `External` text,
  `Total` text,
  `Result` text,
  `Announced /` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `1bi22is52`
--

LOCK TABLES `1bi22is52` WRITE;
/*!40000 ALTER TABLE `1bi22is52` DISABLE KEYS */;
INSERT INTO `1bi22is52` VALUES ('BCS301','MATHEMATICS FOR COMPUTER SCIENCE','45','43','88.0','P','2024-05-02'),('BCS302','DIGITAL DESIGN & COMPUTER ORGANIZATION','50','33','83.0','P','2024-05-02'),('BCS303','OPERATING SYSTEMS','45','34','79.0','P','2024-05-02'),('BCS304','DATA STRUCTURES AND APPLICATIONS','42','33','75.0','P','2024-05-02'),('BCSL305','DATA STRUCTURES LAB','31','49','80.0','P','2024-05-02'),('BSCK307','SOCIAL CONNECT AND RESPONSIBILITY','95','0','95.0','P','2024-05-02'),('BYOK359','YOGA','89','0','89.0','P','2024-05-02'),('BCS306A','OBJECT ORIENTED PROGRAMMING WITH JAVA','48','25','73.0','P','2024-05-02'),('BCS358D','DATA VISUALIZATION WITH PYTHON','47','50','97.0','P','2024-05-02');
/*!40000 ALTER TABLE `1bi22is52` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-13  9:30:59