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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-22 12:05:33.663855'),(2,'contenttypes','0002_remove_content_type_name','2024-10-22 12:05:33.710697'),(3,'auth','0001_initial','2024-10-22 12:05:33.835698'),(4,'auth','0002_alter_permission_name_max_length','2024-10-22 12:05:33.835698'),(5,'auth','0003_alter_user_email_max_length','2024-10-22 12:05:33.851322'),(6,'auth','0004_alter_user_username_opts','2024-10-22 12:05:33.851322'),(7,'auth','0005_alter_user_last_login_null','2024-10-22 12:05:33.851322'),(8,'auth','0006_require_contenttypes_0002','2024-10-22 12:05:33.851322'),(9,'auth','0007_alter_validators_add_error_messages','2024-10-22 12:05:33.866955'),(10,'auth','0008_alter_user_username_max_length','2024-10-22 12:05:33.866955'),(11,'auth','0009_alter_user_last_name_max_length','2024-10-22 12:05:33.866955'),(12,'auth','0010_alter_group_name_max_length','2024-10-22 12:05:33.882609'),(13,'auth','0011_update_proxy_permissions','2024-10-22 12:05:33.898213'),(14,'auth','0012_alter_user_first_name_max_length','2024-10-22 12:05:33.898213'),(15,'registration','0001_initial','2024-10-22 12:05:34.226328'),(16,'admin','0001_initial','2024-10-22 12:05:34.289233'),(17,'admin','0002_logentry_remove_auto_add','2024-10-22 12:05:34.304858'),(18,'admin','0003_logentry_add_action_flag_choices','2024-10-22 12:05:34.304858'),(19,'sessions','0001_initial','2024-10-22 12:05:34.336107'),(20,'registration','0002_alter_user_options_alter_programme_unique_together_and_more','2024-10-22 12:07:08.399627'),(21,'registration','0003_committee_studentcommittee','2024-10-22 13:10:45.313111'),(22,'registration','0004_year_year_only one year to be current','2024-10-22 13:43:06.892600'),(23,'registration','0005_position','2024-10-24 13:21:51.669003'),(24,'registration','0006_semister_remove_year_only one year to be current_and_more','2024-10-26 12:02:29.620568'),(25,'registration','0007_semester_delete_semister_and_more','2024-10-26 12:30:42.025716'),(26,'registration','0008_bill_studentbill_studentbillpayment_and_more','2024-10-26 13:39:44.146081'),(27,'registration','0009_alter_studentbillpayment_created_by','2024-10-26 13:48:30.905663'),(28,'registration','0010_bill_semester_alter_studentbill_unique_together_and_more','2024-10-26 14:17:29.893114'),(29,'registration','0011_alter_bill_unique_together','2024-10-26 14:28:56.730966'),(30,'registration','0012_alter_bill_name','2024-10-26 14:39:28.725049'),(31,'registration','0013_account_alter_studentbill_status','2024-10-26 15:27:54.884809'),(32,'registration','0014_studentbill_paid_amount_studentbillpayment_method','2024-10-26 16:34:46.065603'),(33,'registration','0015_alter_studentbill_paid_amount','2024-10-27 13:13:18.801434'),(34,'registration','0016_event_eventcommittee_eventcollection_eventbill','2024-10-28 16:23:36.763031'),(35,'registration','0017_rename_end_date_event_event_date_and_more','2024-10-29 06:03:28.543065'),(36,'registration','0018_alter_eventcollection_options_remove_event_semester_and_more','2024-10-29 10:07:41.170229'),(37,'registration','0019_eventbill_status','2024-10-29 10:16:27.545868'),(38,'registration','0020_eventcollection_method','2024-10-29 10:19:51.496845'),(39,'registration','0021_alter_eventbill_amount_and_more','2024-10-29 13:29:12.626243'),(40,'registration','0022_alter_eventcommittee_unique_together','2024-10-29 14:11:26.930006'),(41,'registration','0023_alter_eventcommittee_unique_together','2024-10-29 14:15:25.671779'),(42,'registration','0024_rename_collected_amount_eventcollection_paid_amount','2024-10-29 14:36:45.541991'),(43,'registration','0025_remove_eventcollection_projection','2024-10-29 14:40:10.090756');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29 21:04:27
