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
-- Table structure for table `edu_classroom`
--

DROP TABLE IF EXISTS `edu_classroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edu_classroom` (
  `idx` int NOT NULL AUTO_INCREMENT,
  `title` varchar(300) COLLATE utf8mb3_unicode_ci NOT NULL,
  `object_idx` int NOT NULL,
  `previous_classroom_idx` int NOT NULL,
  `level_1_problems` json DEFAULT NULL,
  `level_2_problems` json DEFAULT NULL,
  `level_3_problems` json DEFAULT NULL,
  `level_1_problems_scores` json DEFAULT NULL,
  `level_2_problems_scores` json DEFAULT NULL,
  `level_3_problems_scores` json DEFAULT NULL,
  `level_1_num_of_problems` int DEFAULT '0',
  `level_2_num_of_problems` int DEFAULT '0',
  `level_3_num_of_problems` varchar(45) COLLATE utf8mb3_unicode_ci DEFAULT '0',
  `total_score` int DEFAULT '0',
  `score_is_show` int DEFAULT '0',
  PRIMARY KEY (`idx`),
  KEY `object_idx` (`object_idx`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_classroom`
--

LOCK TABLES `edu_classroom` WRITE;
/*!40000 ALTER TABLE `edu_classroom` DISABLE KEYS */;
INSERT INTO `edu_classroom` VALUES (1,'변수와 자료형의 이해와 활용',1,0,'[1, 2, 3, 4]','[6, 7, 8, 9]','[11, 12]','[\"10\", \"10\", \"10\", \"10\"]','[\"10\", \"10\", \"10\", \"10\"]','[\"10\", \"10\"]',4,4,'2',100,0),(2,'연산자의 이해와 활용',2,1,'[16, 17, 18, 19]','[21, 22, 23, 24]','[26, 27]','[\"10\", \"10\", \"10\", \"10\"]','[\"10\", \"10\", \"10\", \"10\"]','[\"10\", \"10\"]',4,4,'2',100,0),(3,'선택 제어문의 이해와 활용',3,2,'[31, 32, 33, 34]','[36, 37, 38, 39]','[41, 42]','[\"10\", \"10\", \"10\", \"10\"]','[\"10\", \"10\", \"10\", \"10\"]','[\"10\", \"10\"]',4,4,'2',100,0),(4,'반복 제어문의 이해와 활용',4,3,'[46, 47, 48, 49]','[51, 52, 53, 54]','[56, 57]','[\"10\", \"10\", \"10\", \"10\"]','[10, \"10\", \"10\", \"10\"]','[\"10\", \"10\"]',4,4,'2',100,0),(5,'반복 제어문의 이해와 활용',4,3,'[46, 47, 48, 49]','[51, 52, 53, 54]','[56, 57]','[\"10\", \"10\", \"10\", \"10\"]','[10, \"10\", \"10\", \"10\"]','[\"10\", \"10\"]',4,4,'2',100,1);
/*!40000 ALTER TABLE `edu_classroom` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-29 19:43:06
