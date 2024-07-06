CREATE DATABASE  IF NOT EXISTS `grduated_project` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `grduated_project`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: grduated_project
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `file`
--

DROP TABLE IF EXISTS `file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `file` (
  `File_id` int NOT NULL AUTO_INCREMENT,
  `File_name` varchar(60) DEFAULT NULL,
  `User_id` int DEFAULT NULL,
  PRIMARY KEY (`File_id`),
  KEY `User_id_idx` (`User_id`),
  CONSTRAINT `User_id` FOREIGN KEY (`User_id`) REFERENCES `user` (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file`
--

LOCK TABLES `file` WRITE;
/*!40000 ALTER TABLE `file` DISABLE KEYS */;
INSERT INTO `file` VALUES (1,'test_file',1);
/*!40000 ALTER TABLE `file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `foeign_key`
--

DROP TABLE IF EXISTS `foeign_key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `foeign_key` (
  `FK_id` int NOT NULL AUTO_INCREMENT,
  `From_tbl` int NOT NULL,
  `Ref_tbl` int NOT NULL,
  `From_col` varchar(45) NOT NULL,
  `To_col` varchar(45) NOT NULL,
  `File` int DEFAULT NULL,
  PRIMARY KEY (`FK_id`),
  KEY `File_id_idx1` (`File`),
  CONSTRAINT `File_id` FOREIGN KEY (`File`) REFERENCES `file` (`File_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `foeign_key`
--

LOCK TABLES `foeign_key` WRITE;
/*!40000 ALTER TABLE `foeign_key` DISABLE KEYS */;
/*!40000 ALTER TABLE `foeign_key` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table`
--

DROP TABLE IF EXISTS `table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table` (
  `Table_id` int NOT NULL AUTO_INCREMENT,
  `Table_name` varchar(60) DEFAULT NULL,
  `Script` json DEFAULT NULL,
  `x` varchar(20) DEFAULT NULL,
  `y` varchar(20) DEFAULT NULL,
  `File` int DEFAULT NULL,
  PRIMARY KEY (`Table_id`),
  KEY `File_id_idx2` (`File`),
  CONSTRAINT `File_id2` FOREIGN KEY (`File`) REFERENCES `file` (`File_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table`
--

LOCK TABLES `table` WRITE;
/*!40000 ALTER TABLE `table` DISABLE KEYS */;
INSERT INTO `table` VALUES (1,'test_1','\"\"','100','100',1);
/*!40000 ALTER TABLE `table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `User_id` int NOT NULL AUTO_INCREMENT,
  `Mail` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'abc@gmail.com');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-06 17:39:44
