-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for osx10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: at_school_schedule
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `at_school_schedule`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `at_school_schedule` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `at_school_schedule`;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `discord_user_id` bigint(20) DEFAULT NULL,
  `monday` tinyint(1) DEFAULT 0,
  `tuesday` tinyint(1) DEFAULT 0,
  `wednesday` tinyint(1) DEFAULT 0,
  `thursday` tinyint(1) DEFAULT 0,
  `friday` tinyint(1) DEFAULT 0,
  `mon_start_time_1` time DEFAULT NULL,
  `mon_end_time_1` time DEFAULT NULL,
  `mon_start_time_2` time DEFAULT NULL,
  `mon_end_time_2` time DEFAULT NULL,
  `mon_start_time_3` time DEFAULT NULL,
  `mon_end_time_3` time DEFAULT NULL,
  `tues_start_time_1` time DEFAULT NULL,
  `tues_end_time_1` time DEFAULT NULL,
  `tues_start_time_2` time DEFAULT NULL,
  `tues_end_time_2` time DEFAULT NULL,
  `tues_start_time_3` time DEFAULT NULL,
  `tues_end_time_3` time DEFAULT NULL,
  `wed_start_time_1` time DEFAULT NULL,
  `wed_end_time_1` time DEFAULT NULL,
  `wed_start_time_2` time DEFAULT NULL,
  `wed_end_time_2` time DEFAULT NULL,
  `wed_start_time_3` time DEFAULT NULL,
  `wed_end_time_3` time DEFAULT NULL,
  `thurs_start_time_1` time DEFAULT NULL,
  `thurs_end_time_1` time DEFAULT NULL,
  `thurs_start_time_2` time DEFAULT NULL,
  `thurs_end_time_2` time DEFAULT NULL,
  `thurs_start_time_3` time DEFAULT NULL,
  `thurs_end_time_3` time DEFAULT NULL,
  `fri_start_time_1` time DEFAULT NULL,
  `fri_end_time_1` time DEFAULT NULL,
  `fri_start_time_2` time DEFAULT NULL,
  `fri_end_time_2` time DEFAULT NULL,
  `fri_start_time_3` time DEFAULT NULL,
  `fri_end_time_3` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_servers`
--

DROP TABLE IF EXISTS `user_servers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_servers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `discord_user_id` int(11) DEFAULT NULL,
  `discord_server_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_servers`
--

LOCK TABLES `user_servers` WRITE;
/*!40000 ALTER TABLE `user_servers` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_servers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-12 19:31:46
