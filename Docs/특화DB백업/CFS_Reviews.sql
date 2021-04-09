-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: CFS
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

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
-- Table structure for table `Reviews`
--

DROP TABLE IF EXISTS `Reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Reviews` (
  `review_id` int NOT NULL AUTO_INCREMENT,
  `campsite_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `review` varchar(1000) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`review_id`),
  KEY `FK_Campsite_TO_Reviews_1` (`campsite_id`),
  KEY `FK_user_TO_Reviews_1` (`user_id`),
  CONSTRAINT `FK_Campsite_TO_Reviews_1` FOREIGN KEY (`campsite_id`) REFERENCES `Campsite` (`campsite_id`),
  CONSTRAINT `FK_user_TO_Reviews_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reviews`
--

LOCK TABLES `Reviews` WRITE;
/*!40000 ALTER TABLE `Reviews` DISABLE KEYS */;
INSERT INTO `Reviews` VALUES (32,2293,2,'테스트nak','2021-04-05 03:11:22'),(44,225,9,'너무 재밌게 잘 놀았습니다!','2021-04-05 16:35:17'),(45,2401,10,'다양한 체험프로그램을 즐길 수 있는 캠핑장이에요~','2021-04-05 16:46:31'),(62,212,9,'주변이 조용해서 가족과 놀기 좋았어요!','2021-04-06 11:17:29'),(63,212,9,'계곡이 주변에 있어서 아이들이 좋아해요','2021-04-06 11:19:52'),(64,1385,9,'산책할 곳이 많아서 좋습니다','2021-04-06 11:21:06'),(65,393,9,'시설이 너무 좋아요!!','2021-04-06 11:26:49'),(66,202,11,'가족들과 함께 오기 좋아요~','2021-04-06 11:39:35'),(67,208,11,'아이들 데리고 놀기 좋았습니다.','2021-04-06 11:39:58'),(68,225,11,'숲 길을 걷는게 좋았네요..','2021-04-06 11:43:15'),(69,1450,11,'다슬기 잡는게 재밌었어요! 다음에 또 올게요','2021-04-06 11:44:08'),(70,1817,11,'아이들이 놀기 좋은 자연휴양림 입니다.','2021-04-06 11:44:55'),(78,1231,3,'조용히 캠핑하기 좋아요!','2021-04-06 15:13:36'),(79,2424,3,'물놀이 할 수 있어서 친구랑 가기 좋아요~','2021-04-06 15:13:53');
/*!40000 ALTER TABLE `Reviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-08  0:16:24
