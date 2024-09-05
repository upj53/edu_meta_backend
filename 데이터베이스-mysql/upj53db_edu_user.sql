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
  PRIMARY KEY (`idx`),
  UNIQUE KEY `userid` (`userid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_user`
--

LOCK TABLES `edu_user` WRITE;
/*!40000 ALTER TABLE `edu_user` DISABLE KEYS */;
INSERT INTO `edu_user` VALUES (1,'user1','student','$2b$12$WqRuWQNHjnH5BFUlywB9RealVDwYVO3eKW4sykfVLCgIbvcBAc1CS','나건국','user1-update@email.com',4),(2,'user2','student','$2b$12$lbaWifgZGrWHqygY9Eglju4BbMXn8w7VdHqBqd1b/jkeMf0.Xmq8e','송광진','user2@example.com',4),(3,'admin1','teacher','$2b$12$JA.5h.k0cKo/TC12z36uTOQkl6mtlfNYq9pAf9cpI05UC9Ro8mqU.','관리자1','admin1@email.com',0),(4,'user3','student','$2b$12$vQw5dJkpMM2shi1CJ6FaueY8MMaOc9JfoRxtIcFZhle3r4tKb6y0i','허철수','esther@gmail.com',4),(5,'user4','student','$2b$12$c/5wmXDhpFFtIo8whgtypeyQnudEDHhw0bCZGQqPxznpmRqfH0fAC','이능동','test4@email.com',4),(6,'user5','student','$2b$12$lGctvcd85zK9o/vZUOL1feJCHoKicuVbwje49zfvRbCvwjKDlPhMi','김연수','user5@email.com',4),(9,'user6','student','$2b$12$7s67HBsq6MNte9/KYhAYfOVCUMMzhd182F2eQ6ymsXRMCmedvWZcG','이승리','user6@email.com',4),(10,'admin2','teacher','$2b$12$3IlC1AKiGN6alq8LgLvOmeP1HwhqDZY.gWykWiSk4VTdlaiQ6/dnK','관리자2','admin2@email.com',0),(11,'admin3','teacher','$2b$12$2EmaTBTmmC75QwFU3kxvye0mPPjQlOJiA4Fg02W9UWQsBARdEKMVG','관리자3','admin3@email.com',0),(12,'student1','student','$2b$12$paOpMlDfPtgvbMnk5MBLmuvN0Fgzxaj.ju8rNdKMuJHF7Buwo0k2u','학생1','student1@email.com',0),(13,'student2','student','$2b$12$Ax0GUJr1tvbYsXJfhP6.oOwaBMhTElIYpNqAHZ66IrsKTZzfG/pgi','학생2','student2@email.com',0),(14,'student3','student','$2b$12$20SyDLbOmxOZPFLFPNwQPucw2cLMby1vhwvkKCo8czzVwCSZppRFu','학생3','student3@email.com',0),(15,'student4','student','$2b$12$rVw23hjzelMTqFJ18KTYCOs/YF8xCdw24Y/I1OwSlKTpZk1BlQUoS','학생4','student4@email.com',0),(16,'student5','student','$2b$12$DMnqwi57uqSJHSTp.AHU4.S4AEymXVrHfd.6zzrQRttVnYYyYlFBK','학생5','student5@email.com',0),(17,'student6','student','$2b$12$V4zUjfzFKKfzGILzq7N18OFVtRGaXYFz/SKX35g2X8lupu0p9SRem','학생6','student6@email.com',0),(18,'student7','student','$2b$12$sb3Teu1HshSnJa.eozAfEOiH3Jm7B4kV9uZh/jfESyCx5c77IWy7K','학생7','student7@email.com',0),(19,'student8','student','$2b$12$OFdyibYlBl5In7m8voRkQeUlyRkGJOI/BYxcy6mJVt6NFW7LDCvEi','학생8','student8@email.com',0),(20,'student9','student','$2b$12$gtaKYoXC6pVJykr9eE7f/OHbhZILEorKFKYqxw9lTZp9zpZaPoj3G','학생9','student9@email.com',0),(21,'student10','student','$2b$12$oHYlQqaV60cSDrznarenK.Dk1GN6/fXxUuqVIE50HiZDtt0EKI4vm','학생10','student10@email.com',0),(22,'student11','student','$2b$12$2tHYduQx4.AyZjXogG.uyOHEXNshaVTGII8FdIPXuNk/EuMM.77/q','학생11','student11@email.com',0),(23,'student12','student','$2b$12$QC9vSXrdP0d7qS590XTH2e1t0ULmyHBLB6rVcxFwTw3B.mAPeAzhu','학생12','student12@email.com',0),(24,'student13','student','$2b$12$7Ek5fZTYrQwSTa/ZDYWtCuDmLUCoe342N9ivPp90hrUyZFz1uZfya','학생13','student13@email.com',0),(25,'student14','student','$2b$12$74xd1QW3VNNX1fVOzi7hOeaY6GwtpJhk54yvc6t2KyLpntEO0A8eK','학생14','student14@email.com',0),(26,'student15','student','$2b$12$xG2GTDkNXjW6/ETy29G6ve7nUwPlcupyiENhZ4EcuMsZMlyovJG3a','학생15','student15@email.com',0),(27,'student16','student','$2b$12$HdzCghuoJfOoYHIh887Gs.qNhtFQPAD0TupjEw8Bo6z39vEih9SN2','학생16','student16@email.com',0),(28,'student17','student','$2b$12$3IwZaNmEeCfe0CdMS83IfOk4y7c8X4Y3zveNaSVK4ySVrGEu02km6','학생17','student17@email.com',0),(29,'student18','student','$2b$12$B0J0WyO2EJgOyiq242lGnOeU5JMf.ZTKoDURMV4IZZGNeqr0Tqdyu','학생18','student18@email.com',0),(30,'student19','student','$2b$12$fzyG4kZLVJHLvKl9cvzw0uFYukVzxkZm3Ap3yEgsCCd1ilulatBU.','학생19','student19@email.com',0),(31,'student20','student','$2b$12$Qi3vnZXD4N8UZrm/p.91Ye16zE9kzzJCBL3KbhtpXSZAjkVw4ZQLq','학생20','student20@email.com',0),(32,'teacher1','teacher','$2b$12$EkPJytH1.lQAkaDRg739AO5kUyGdieNvh83bYp5F/9LxLL9JDZaFm','교사1','teacher1@email.com',0),(33,'teacher2','teacher','$2b$12$TtlxFFxypvWsnWYjQByFYOEnntlJz/shTqB9hfxasOVxu4c.2Fmfa','교사2','teacher2@email.com',0),(34,'teacher3','teacher','$2b$12$1u7verHdg7NsUmZ7tZ92ieMVL5FSZKmyP2LTLF1.poa5sHtQpqpA2','교사3','teacher3@email.com',0),(35,'teacher4','teacher','$2b$12$EP4LMfJqsK9PTTXLEC1kAeEKx9C/20kh3QjYDGT6j/WlxnrVz7EgG','교사4','teacher4@email.com',0),(36,'teacher5','teacher','$2b$12$NgDDkFAyQ5X0C7igicVQ7u8DgrzmOBspBsLrTkzef48z5gCuLsvYG','교사5','teacher5@email.com',0),(37,'teacher6','teacher','$2b$12$W/9zgKrn3X.NJsKYorLWr.fYqyDNmACARgucqiTvjDe5qId4garNq','교사6','teacher6@email.com',0),(38,'teacher7','teacher','$2b$12$/EZnoE6yZo5s7LcFeaDuq.lQ1AXeChoZOxuml4f4b0QRwTHRzw8tC','교사7','teacher7@email.com',0),(39,'teacher8','teacher','$2b$12$icW7JyMqTwv9h3CnaDYb9uvplfKyNi90MsdLZD5fga78xdaRDi2rq','교사8','teacher8@email.com',0),(40,'teacher9','teacher','$2b$12$jIb/MLZBoRaySb25HxqjlOJY5Rg2bfIGHOSyN1w4LVuYx463rwGcm','교사9','teacher9@email.com',0),(41,'teacher10','teacher','$2b$12$mVbiKAulV81Jr.ZelhPGtuHls.YgjuP/UguVOKj9N23L7KeYyZC96','교사10','teacher10@email.com',0),(42,'teacher11','teacher','$2b$12$6uac2bW0W2phdr1G3oK9UetYRDazfEGmBKrVvj0jsFM32rYq9Yr.S','교사11','teacher11@email.com',0),(43,'teacher12','teacher','$2b$12$iDOwJsnurQQJ7aGvKkxyRel81iEO.9VlVhCJ56Wy4ReJIVK/wSvGq','교사12','teacher12@email.com',0),(44,'teacher13','teacher','$2b$12$PTFlmfCuLugNhae1oeDo3OLf3ZRwax1mA26dbSAGcCrgZOf4rJxfy','교사13','teacher13@email.com',0),(45,'teacher14','teacher','$2b$12$4wHoRo1K14n5tTWxvHGZQuQdX8H8YnBuGuWEPLPfjOsaDO3u/d9pW','교사14','teacher14@email.com',0),(46,'teacher15','teacher','$2b$12$g239JFmiTS7mmEVqjp7TEOrCn2kIIP.VeyLcpnXth0E5WxSGvQfZm','교사15','teacher15@email.com',0),(47,'teacher16','teacher','$2b$12$tFU..gJTxgPMUw374VG.xuazjlvPfMxxekpVzmSUipGNYC9UoasSS','교사16','teacher16@email.com',0),(48,'teacher17','teacher','$2b$12$KNKck4ip6.4uu6j02AEOSuqTUQhA/7BT.7Vd2.Ofc1tac7tF8McGq','교사17','teacher17@email.com',0),(49,'teacher18','teacher','$2b$12$GXHZQKzHscZBuY.v4oTYVueqS/2iykVgomBxt5DnYQoj6JroK1MIC','교사18','teacher18@email.com',0),(50,'teacher19','teacher','$2b$12$6wm4z.Mu/ot65cait/rJt.xJ/9u0rrS.zkf1mvpCgbdb.6awuxBuW','교사19','teacher19@email.com',0),(51,'teacher20','teacher','$2b$12$LS57gQIVujG0ct.iEPv4c.xsoxOu.a7s5SC/SepJv.X7KVuWqQ/rS','교사20','teacher20@email.com',0),(57,'user7','student','$2b$12$yc4tpbd7bqVgc.sudOBOxepe0p0W..VufKU2LGAVbEE650iPi/csK','user7','user7@email.com',4),(58,'user8','student','$2b$12$U68AM3b/v8nktVPkotTsi.wPuWLnRLAhtlvBjZdrJQZ25SNOTCuQ.','user8','user8@email.com',5),(59,'user9','student','$2b$12$OWEwUOsCyEXQrmk3xQ8.Ne95qdrVRV2YTdfSJVByiLfYDuJpgiKgG','user9','user9@email.com',0),(60,'student','student','$2b$12$PvMowbudIZPJ02Q25WjlhOxLR88/VextKHa9xCMcdkBqoMQDpr/2O','student','student@email.com',5);
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

-- Dump completed on 2024-09-04 13:40:54
