-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: actual16_opsweb
-- ------------------------------------------------------
-- Server version	5.1.73

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `actual16_opsweb`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `actual16_opsweb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `actual16_opsweb`;

--
-- Table structure for table `assets`
--

DROP TABLE IF EXISTS `assets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `assets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(30) DEFAULT NULL,
  `private_ip` varchar(30) DEFAULT NULL,
  `public_ip` varchar(30) NOT NULL,
  `mem_total` varchar(32) DEFAULT NULL,
  `cpu_num` varchar(30) DEFAULT NULL,
  `cpu_model` text,
  `disk` varchar(30) DEFAULT NULL,
  `machine_room` varchar(32) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  UNIQUE KEY `private_ip` (`private_ip`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assets`
--

LOCK TABLES `assets` WRITE;
/*!40000 ALTER TABLE `assets` DISABLE KEYS */;
INSERT INTO `assets` VALUES (12,'iZq1zotf9u5xo9Z','172.18.188.228','','7872','2','Intel(R) Xeon(R) CPU E5-2682 v4 @ 2.50GHz','137',NULL,'2017-12-10 16:54:08','2017-12-10 16:54:08'),(13,'monkey-hostname','10.0.0.132','112.74.164.107','8000','4',NULL,'100','酒仙桥','2017-12-10 17:35:02','2017-12-10 17:35:02');
/*!40000 ALTER TABLE `assets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mem_monitor`
--

DROP TABLE IF EXISTS `mem_monitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mem_monitor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(30) NOT NULL,
  `mem_free` varchar(30) NOT NULL,
  `create_time` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1461 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mem_monitor`
--

LOCK TABLES `mem_monitor` WRITE;
/*!40000 ALTER TABLE `mem_monitor` DISABLE KEYS */;
INSERT INTO `mem_monitor` VALUES (1432,'iZq1zotf9u5xo9Z-2','7616','1512455716'),(1433,'iZq1zotf9u5xo9Z-4','7616','1512455717'),(1434,'iZq1zotf9u5xo9Z-2','7616','1512455718'),(1435,'iZq1zotf9u5xo9Z-1','7616','1512455719'),(1436,'iZq1zotf9u5xo9Z-4','7616','1512455736'),(1437,'iZq1zotf9u5xo9Z-2','7616','1512455737'),(1438,'iZq1zotf9u5xo9Z-1','7616','1512455742'),(1439,'iZq1zotf9u5xo9Z-1','7616','1512455754'),(1440,'iZq1zotf9u5xo9Z-2','7616','1512455755'),(1441,'iZq1zotf9u5xo9Z-3','7616','1512455756'),(1442,'iZq1zotf9u5xo9Z-1','7616','1512455757'),(1443,'iZq1zotf9u5xo9Z-2','7616','1512455758'),(1444,'iZq1zotf9u5xo9Z-4','7616','1512455759'),(1445,'iZq1zotf9u5xo9Z-4','7616','1512455760'),(1446,'iZq1zotf9u5xo9Z-3','7616','1512455761'),(1447,'iZq1zotf9u5xo9Z-3','7616','1512455762'),(1448,'iZq1zotf9u5xo9Z-2','7616','1512455763'),(1449,'iZq1zotf9u5xo9Z-3','7616','1512455764'),(1450,'iZq1zotf9u5xo9Z-3','7616','1512455765'),(1451,'iZq1zotf9u5xo9Z-1','7616','1512455766'),(1452,'iZq1zotf9u5xo9Z-3','7616','1512455768'),(1453,'iZq1zotf9u5xo9Z-2','7616','1512455769'),(1454,'iZq1zotf9u5xo9Z-2','7616','1512455770'),(1455,'iZq1zotf9u5xo9Z-3','7616','1512455771'),(1456,'iZq1zotf9u5xo9Z-3','7616','1512455772'),(1457,'iZq1zotf9u5xo9Z-2','7616','1512455773'),(1458,'iZq1zotf9u5xo9Z-1','7616','1512455774'),(1459,'iZq1zotf9u5xo9Z-1','7616','1512455775'),(1460,'iZq1zotf9u5xo9Z-1','7616','1512455776');
/*!40000 ALTER TABLE `mem_monitor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nginxlog`
--

DROP TABLE IF EXISTS `nginxlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nginxlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(25) NOT NULL,
  `status` varchar(3) NOT NULL,
  `x` varchar(25) NOT NULL,
  `y` varchar(25) NOT NULL,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nginxlog`
--

LOCK TABLES `nginxlog` WRITE;
/*!40000 ALTER TABLE `nginxlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `nginxlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `cn_name` varchar(30) NOT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(30) NOT NULL,
  `position` varchar(30) DEFAULT NULL,
  `role` varchar(32) NOT NULL,
  `password` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (11,'monkey','郑彦生','13260071987','monkey@reboot.com','运维开发','admin','e10adc3949ba59abbe56e057f20f883e'),(12,'yangjianjiang','杨建江','13260071987','yangjianjiang@reboot.com','运维总监','admin','e10adc3949ba59abbe56e057f20f883e'),(20,'zhaohongye','赵宏业','13260071987','zhaohongye1@reboot.com','运维','common','e10adc3949ba59abbe56e057f20f883e'),(21,'jianghong','江宏','13260071987','jianghong@reboot.com','运维开发','admin','e10adc3949ba59abbe56e057f20f883e'),(23,'wangmeng','王蒙','13260071987','wangmeng@reboot.com','学生','common','e10adc3949ba59abbe56e057f20f883e');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-14 22:32:19
