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
-- Table structure for table `edu_subject`
--

DROP TABLE IF EXISTS `edu_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edu_subject` (
  `idx` int NOT NULL AUTO_INCREMENT,
  `subject_title` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `subject_main_idea` text COLLATE utf8mb3_unicode_ci,
  `subject_main_1` text COLLATE utf8mb3_unicode_ci,
  `subject_main_2` text COLLATE utf8mb3_unicode_ci,
  `subject_main_3` text COLLATE utf8mb3_unicode_ci,
  `subject_goal` text COLLATE utf8mb3_unicode_ci,
  `subject_goal_detail` text COLLATE utf8mb3_unicode_ci,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_subject`
--

LOCK TABLES `edu_subject` WRITE;
/*!40000 ALTER TABLE `edu_subject` DISABLE KEYS */;
INSERT INTO `edu_subject` VALUES (1,'파이썬 프로그래밍 기초 Part 1','','','','','',''),(2,'파이썬 프로그래밍 기초 Part 2','','','','','',''),(3,'알고리즘과 프로그래밍 Part 1','- 문제를 효율적으로 해결하기 위해서는 문제를 추상화하고, 프로그래밍을 위한 알고리즘을 설계한다.\n- 데이터 모델링을 하기 위해 문제 해결에 필요한 데이터 간의 관계를 분석하고, 정의한다.\n- 프로그래밍을 통한 자동화는 다양한 학문 분야의 문제를 해결하는 데 도움을 준다.','- 문제 분해와 모델링\n- 정렬, 탐색 알고리즘\n- 자료형\n- 표준입출력과 파일입출력\n- 다차원 데이터 활용\n- 제어 구조의 응용\n- 클래스와 인스턴스','- 문제를 분해하고 모델링하기\n- 알고리즘의 수행 과정 및 효율성 비교 · 분석하기\n- 문제 해결에 적합한 자료형과 입출력 구조를 활용하여 프로그램 작성하기\n- 복잡한 문제를 해결하기 위해 제어 구조와 다차원 데이터 구조를 복합적으로 활용하기\n- 클래스를 정의하고 인스턴스를 생성하여 문제 해결에 적합한 객체를 구현하기','- 문제 해결 모델을 구성하고 적극적으로 표현하는 자세\n- 알고리즘 효율의 가치와 영향력을 인식하고 적극적으로 탐구하는 태도\n- 다양한 학문 분야의 문제 해결을 위해 설계한 알고리즘을 프로그램으로 구현하는 실천적 자세\n- 디지털 사회의 민주시민으로서 협력적 문제 해결력의 중요성을 인식하는 자세','1. 복잡한 문제를 해결 가능한 작은 문제로 분해하고 모델링한다.\n2. 데이터를 정렬하는 다양한 알고리즘의 특징과 효율을 비교 · 분석한다.\n3. 데이터를 탐색하는 다양한 알고리즘의 특징과 효율을 비교 · 분석한다.\n4. 자료형의 종류와 특성을 알고, 접합한 자료형을 선택하여 프로그램을 작성한다.\n5. 표준입출력과 파일입출력을 활용한 프로그램을 작성한다.\n6. 다차원 데이터 구조를 활용한 프로그램을 작성한다.\n7. 다양한 제어 구조를 복합적으로 활용한 프로그램을 작성한다.\n8. 객체를 구현하는 클래스와 인스턴스를 활용하여 프로그램을 작성한다.\n9. 실생활 및 다양한 학문 분야의 문제 해결을 위한 프로그램을 협력적으로 설계 · 구현한다.\n10. 문제 해결을 위한 프로그램의 성능을 평가하고 공유한다.','- 복잡한 문제를 분석하는 단계에서 좀 더 작은 문제로 분해하는 과정을 수행하며, 해결하기 용이하도록 단순화나 구조화하는 모델링 단계를 수행할 수 있어야 한다. 작은 문제의 해결 결과를 종합하는 과정에서 작은 문제를 모두 수행했을 때 전체 문제 해결이 원활하게 이루어지는지, 오류가 없는지를 확인할 수 있어야 한다.\n- 여러 가지 정렬, 탐색 알고리즘을 적용하여 실생활의 간단한 데이터의 정렬, 탐색 문제를 해결할 수 있어야 한다. 정렬, 탐색 알고리즘의 수행 과정을 분석해보고 문제에 따라 알고리즘의 효율성이 다를 수 있음을 설명할 수 있어야 한다.\n- 실생활의 사례를 활용하여 객체 지향의 기본 개념을 이해하고 필요성을 설명할 수 있어야 한다. 클래스와 객체를 생성하고 문제 해결을 위한 프로그램 구현에 활용할 수 있어야 한다.'),(4,'알고리즘과 프로그래밍 Part 2','','','','','',''),(5,'인공지능 Part 1','','','','','',''),(6,'인공지능 Part 2','','','','','','');
/*!40000 ALTER TABLE `edu_subject` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-04 13:40:55
