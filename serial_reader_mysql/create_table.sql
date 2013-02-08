CREATE TABLE `arduino_temp` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `temperature` decimal(7,2) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
