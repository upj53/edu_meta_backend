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
-- Table structure for table `edu_user`
--

DROP TABLE IF EXISTS `edu_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edu_user` (
  `idx` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(30) COLLATE utf8mb3_unicode_ci NOT NULL,
  `usertype` varchar(20) COLLATE utf8mb3_unicode_ci NOT NULL,
  `password` varchar(100) COLLATE utf8mb3_unicode_ci NOT NULL,
  `username` varchar(50) COLLATE utf8mb3_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb3_unicode_ci NOT NULL,
  `current_classroom` int NOT NULL,
  `teacherid` varchar(30) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idx`),
  UNIQUE KEY `userid` (`userid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_user`
--

LOCK TABLES `edu_user` WRITE;
/*!40000 ALTER TABLE `edu_user` DISABLE KEYS */;
INSERT INTO `edu_user` VALUES (1,'teacher','teacher','$2b$12$33qzuriC8SAv4oD.JSssEuWWvkfXwVWesIaybM38.ElE5RnXp.f/W','교사샘플계정','teacher@email.com',0,''),(2,'student1','student','$2b$12$ZH5LmQU9J/FLogrUK8G/N.jTVn9DQI5VknfIEf0OQ2xaNHXfNqIzO','학생1','student1@email.com',5,'teacher'),(3,'student2','student','$2b$12$BxTyURmSyrSpwWzt4eSQ/.dnHU2egon.8ff2q28CDk7GMj0RS97i.','학생2','student2@email.com',4,'teacher'),(4,'student3','student','$2b$12$oGZy7VpDK8IrrHZ6f9OWOee4/DtIqhvXBgwKfESBTBD1QRl5qyPo.','학생3','student3@email.com',4,'teacher');
/*!40000 ALTER TABLE `edu_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-29 19:43:07
