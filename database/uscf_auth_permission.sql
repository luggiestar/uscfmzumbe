-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: uscf
-- ------------------------------------------------------
-- Server version	5.7.44-log

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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add level',6,'add_level'),(22,'Can change level',6,'change_level'),(23,'Can delete level',6,'delete_level'),(24,'Can view level',6,'view_level'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add unit',8,'add_unit'),(30,'Can change unit',8,'change_unit'),(31,'Can delete unit',8,'delete_unit'),(32,'Can view unit',8,'view_unit'),(33,'Can add department',9,'add_department'),(34,'Can change department',9,'change_department'),(35,'Can delete department',9,'delete_department'),(36,'Can view department',9,'view_department'),(37,'Can add programme',10,'add_programme'),(38,'Can change programme',10,'change_programme'),(39,'Can delete programme',10,'delete_programme'),(40,'Can view programme',10,'view_programme'),(41,'Can add student',11,'add_student'),(42,'Can change student',11,'change_student'),(43,'Can delete student',11,'delete_student'),(44,'Can view student',11,'view_student'),(45,'Can add student committee',12,'add_studentcommittee'),(46,'Can change student committee',12,'change_studentcommittee'),(47,'Can delete student committee',12,'delete_studentcommittee'),(48,'Can view student committee',12,'view_studentcommittee'),(49,'Can add committee',13,'add_committee'),(50,'Can change committee',13,'change_committee'),(51,'Can delete committee',13,'delete_committee'),(52,'Can view committee',13,'view_committee'),(53,'Can add year',14,'add_year'),(54,'Can change year',14,'change_year'),(55,'Can delete year',14,'delete_year'),(56,'Can view year',14,'view_year'),(57,'Can add position',15,'add_position'),(58,'Can change position',15,'change_position'),(59,'Can delete position',15,'delete_position'),(60,'Can view position',15,'view_position'),(61,'Can add semister',16,'add_semister'),(62,'Can change semister',16,'change_semister'),(63,'Can delete semister',16,'delete_semister'),(64,'Can view semister',16,'view_semister'),(65,'Can add semester',17,'add_semester'),(66,'Can change semester',17,'change_semester'),(67,'Can delete semester',17,'delete_semester'),(68,'Can view semester',17,'view_semester'),(69,'Can add bill',18,'add_bill'),(70,'Can change bill',18,'change_bill'),(71,'Can delete bill',18,'delete_bill'),(72,'Can view bill',18,'view_bill'),(73,'Can add student bill',19,'add_studentbill'),(74,'Can change student bill',19,'change_studentbill'),(75,'Can delete student bill',19,'delete_studentbill'),(76,'Can view student bill',19,'view_studentbill'),(77,'Can add student bill payment',20,'add_studentbillpayment'),(78,'Can change student bill payment',20,'change_studentbillpayment'),(79,'Can delete student bill payment',20,'delete_studentbillpayment'),(80,'Can view student bill payment',20,'view_studentbillpayment'),(81,'Can add account',21,'add_account'),(82,'Can change account',21,'change_account'),(83,'Can delete account',21,'delete_account'),(84,'Can view account',21,'view_account'),(85,'Can add Event Collection',22,'add_eventcollection'),(86,'Can change Event Collection',22,'change_eventcollection'),(87,'Can delete Event Collection',22,'delete_eventcollection'),(88,'Can view Event Collection',22,'view_eventcollection'),(89,'Can add Event',23,'add_event'),(90,'Can change Event',23,'change_event'),(91,'Can delete Event',23,'delete_event'),(92,'Can view Event',23,'view_event'),(93,'Can add Event Committee',24,'add_eventcommittee'),(94,'Can change Event Committee',24,'change_eventcommittee'),(95,'Can delete Event Committee',24,'delete_eventcommittee'),(96,'Can view Event Committee',24,'view_eventcommittee'),(97,'Can add Event Bill',25,'add_eventbill'),(98,'Can change Event Bill',25,'change_eventbill'),(99,'Can delete Event Bill',25,'delete_eventbill'),(100,'Can view Event Bill',25,'view_eventbill');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29 21:04:26
