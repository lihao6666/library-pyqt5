-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: 111.230.138.45    Database: library
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `book` (
  `book_id` char(10) NOT NULL,
  `type` varchar(20) DEFAULT NULL,
  `book_name` varchar(40) NOT NULL,
  `author` varchar(30) NOT NULL,
  `press` varchar(20) NOT NULL,
  `amount` decimal(3,0) DEFAULT NULL,
  `total` decimal(3,0) DEFAULT NULL,
  PRIMARY KEY (`book_id`),
  KEY `type` (`type`),
  CONSTRAINT `book_ibfk_1` FOREIGN KEY (`type`) REFERENCES `category` (`type`),
  CONSTRAINT `book_chk_1` CHECK ((`amount` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES ('A0003-1','马列毛','共产党宣言','马克斯、恩格斯','中国人民出版社',20,20),('C0002-1','社会科学总论','天才在左疯子在右','高铭','武汉大学出版社',9,10),('I0000-1','文学','水浒传上第一版','施耐庵','中国人民出版社',9,10),('I0001-2','文学','水浒传下','施耐庵','中国人民出版社',10,10),('I0004-2','文学','红楼梦第二版','曹雪芹','中国人民出版社',10,10),('T0005--5','工业技术','数据库','王珊','10',10,10);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `book_view`
--

DROP TABLE IF EXISTS `book_view`;
/*!50001 DROP VIEW IF EXISTS `book_view`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `book_view` AS SELECT 
 1 AS `book_id`,
 1 AS `book_name`,
 1 AS `total`,
 1 AS `amount`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `borrow`
--

DROP TABLE IF EXISTS `borrow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `borrow` (
  `lib_id` decimal(10,0) DEFAULT NULL,
  `book_id` char(10) NOT NULL,
  `start_time` date DEFAULT NULL,
  `ddl` date DEFAULT NULL,
  PRIMARY KEY (`book_id`),
  KEY `lib_id` (`lib_id`),
  CONSTRAINT `borrow_ibfk_1` FOREIGN KEY (`lib_id`) REFERENCES `lib_card` (`lib_id`),
  CONSTRAINT `borrow_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrow`
--

LOCK TABLES `borrow` WRITE;
/*!40000 ALTER TABLE `borrow` DISABLE KEYS */;
INSERT INTO `borrow` VALUES (123123,'C0002-1','2019-06-11','2019-06-11'),(123124,'I0000-1','2019-06-12','2019-08-01');
/*!40000 ALTER TABLE `borrow` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`lh`@`%`*/ /*!50003 TRIGGER `borrow_insert` AFTER INSERT ON `borrow` FOR EACH ROW begin
declare c int;
set c = (select amount from book where book_id=new.book_id);
update book set amount = c-1 where book_id = new.book_id;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`lh`@`%`*/ /*!50003 TRIGGER `borrow_del` AFTER DELETE ON `borrow` FOR EACH ROW begin
declare a int;
set a =(select amount from book where book_id=old.book_id);
update book set amount=a+1 where book_id=old.book_id;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `category` (
  `type_num` char(1) DEFAULT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`type`),
  UNIQUE KEY `type_num` (`type_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES ('A','马列毛'),('B','哲学宗教'),('C','社会科学总论'),('D','政治、法律'),('E','军事'),('F','经济'),('G','文化、科学、教育'),('H','语言、文字'),('I','文学'),('J','艺术'),('K','历史、地理'),('N','自然科学总论'),('O','数理科学与化学'),('P','天文学、地球科学'),('Q','生物科学'),('R','医药、卫生'),('S','农业科学'),('T','工业技术'),('U','交通运输'),('V','航空、航天'),('X','环境安全'),('Z','综合性图书');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lib_card`
--

DROP TABLE IF EXISTS `lib_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lib_card` (
  `lib_id` decimal(10,0) NOT NULL,
  `balance` decimal(6,1) DEFAULT NULL,
  PRIMARY KEY (`lib_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lib_card`
--

LOCK TABLES `lib_card` WRITE;
/*!40000 ALTER TABLE `lib_card` DISABLE KEYS */;
INSERT INTO `lib_card` VALUES (123123,20.0),(123124,15.0),(123125,15.0);
/*!40000 ALTER TABLE `lib_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reader`
--

DROP TABLE IF EXISTS `reader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `reader` (
  `stu_no` char(10) NOT NULL,
  `stu_name` varchar(20) NOT NULL,
  `phone` char(11) DEFAULT NULL,
  `lib_id` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`stu_no`),
  KEY `lib_id` (`lib_id`),
  CONSTRAINT `reader_ibfk_1` FOREIGN KEY (`lib_id`) REFERENCES `lib_card` (`lib_id`),
  CONSTRAINT `reader_ibfk_2` FOREIGN KEY (`stu_no`) REFERENCES `users` (`stu_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reader`
--

LOCK TABLES `reader` WRITE;
/*!40000 ALTER TABLE `reader` DISABLE KEYS */;
INSERT INTO `reader` VALUES ('2017214880','李浩','18518980507',123123),('2017214881','余钱','13636322809',123124),('2017214882','李恒','15236433205',123125);
/*!40000 ALTER TABLE `reader` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `stu_no` char(10) NOT NULL,
  `passwd` varchar(30) DEFAULT NULL,
  `privilege` decimal(1,0) DEFAULT NULL,
  PRIMARY KEY (`stu_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('2013214880','123456',1),('2017214880','123456',0),('2017214881','123456',0),('2017214882','12345',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `book_view`
--

/*!50001 DROP VIEW IF EXISTS `book_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`lh`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `book_view` AS select `book`.`book_id` AS `book_id`,`book`.`book_name` AS `book_name`,`book`.`total` AS `total`,`book`.`amount` AS `amount` from `book` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-12 17:56:22
