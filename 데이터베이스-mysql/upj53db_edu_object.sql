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
-- Table structure for table `edu_object`
--

DROP TABLE IF EXISTS `edu_object`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edu_object` (
  `idx` int NOT NULL AUTO_INCREMENT,
  `subject_idx` int NOT NULL,
  `object_title` varchar(100) COLLATE utf8mb3_unicode_ci NOT NULL,
  `object_detail` text COLLATE utf8mb3_unicode_ci,
  PRIMARY KEY (`idx`),
  KEY `subject_idx` (`subject_idx`),
  CONSTRAINT `edu_object_ibfk_1` FOREIGN KEY (`subject_idx`) REFERENCES `edu_subject` (`idx`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_object`
--

LOCK TABLES `edu_object` WRITE;
/*!40000 ALTER TABLE `edu_object` DISABLE KEYS */;
INSERT INTO `edu_object` VALUES (1,1,'변수와 자료형','- 변수와 자료형의 종류와 특성을 알고, 적합한 자료형을 선택하여 프로그램을 작성한다.\n- 내용 1\n- 내용 2\n\n<b>HTML 태그가 될까?</b>\n\n<p style=\"color:red; font-size:20px;\">HTML 태그가 되는구나!!</p>\n\n<table style=\"border:1px solid black; margin:10px;\">\n<tr>\n<td>A</td>\n<td>B</td>\n<td>C</td>\n</tr>\n<tr>\n<td>가</td>\n<td>나</td>\n<td>다</td>\n</tr>\n</table>\n\n1. 보기 1\n2. 보기 2\n3. 보기 3\n\n**할렐루야**\n\n만세'),(2,1,'연산자','- 1차원 배열의 데이터 구조를 활용한 프로그램을 작성한다.'),(3,1,'선택 제어문','- 다양한 제어 구조를 복합적으로 활용한 프로그램을 작성한다.'),(4,1,'반복 제어문','- 다양한 제어 구조를 복합적으로 활용한 프로그램을 작성한다.'),(5,2,'함수','- 함수의 특성을 이해하고 함수를 활용한 프로그램을 작성한다.'),(6,2,'클래스와 인스턴스','- 객체를 구현하는 클래스와 인스턴스를 활용하여 프로그램을 작성한다.');
/*!40000 ALTER TABLE `edu_object` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-04 13:40:54
