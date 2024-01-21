-- Unique ID
-- create table
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULt 1 UNIQUE,
	name VARCHAR(256)
	) ENGINE=INNODB;
