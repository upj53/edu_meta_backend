-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: upj53db
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.20.04.1

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
-- Table structure for table `edu_my_classroom`
--

DROP TABLE IF EXISTS `edu_my_classroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edu_my_classroom` (
  `idx` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(30) COLLATE utf8mb3_unicode_ci NOT NULL,
  `classroom_idx` int NOT NULL,
  `current_problem_seq` int DEFAULT '1',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `classroom_status` int DEFAULT '0',
  `time_goal_at` datetime DEFAULT NULL,
  `time_goal_status` int DEFAULT '0',
  `time_goal` datetime DEFAULT NULL,
  `time_goal_delay` json DEFAULT NULL,
  `chatgpt` json DEFAULT NULL,
  `chatgpt_dialog` json DEFAULT NULL,
  PRIMARY KEY (`idx`),
  KEY `classroom_idx` (`classroom_idx`),
  CONSTRAINT `edu_my_classroom_ibfk_1` FOREIGN KEY (`classroom_idx`) REFERENCES `edu_classroom` (`idx`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_my_classroom`
--

LOCK TABLES `edu_my_classroom` WRITE;
/*!40000 ALTER TABLE `edu_my_classroom` DISABLE KEYS */;
INSERT INTO `edu_my_classroom` VALUES (1,'user1',5,0,'2024-10-29 17:55:45','2024-10-29 17:55:51',0,'2024-10-29 17:55:51',1,'2024-10-29 18:55:51','[]','[]','[]'),(2,'user2',4,0,'2024-10-29 17:56:08','2024-10-29 17:56:13',0,'2024-10-29 17:56:13',1,'2024-10-29 18:56:13','[]','[]','[]'),(3,'student1',5,0,'2024-10-29 19:33:05','2024-10-29 19:33:09',0,'2024-10-29 19:33:09',1,'2024-10-29 20:33:09','[]','[]','[]'),(4,'student2',4,0,'2024-10-29 19:33:34','2024-10-29 19:33:42',0,'2024-10-29 19:33:42',2,'2024-10-29 21:33:42','[]','[]','[]'),(5,'student3',4,0,'2024-10-29 19:36:56','2024-10-29 19:37:01',0,'2024-10-29 19:37:01',3,'2024-10-29 22:37:01','[]','[]','[]');
/*!40000 ALTER TABLE `edu_my_classroom` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-29 19:43:08
