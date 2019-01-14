-- DROP TABLE IF EXISTS calc;
-- CREATE TABLE IF NOT EXISTS calc
-- (id_calc INTEGER PRIMARY KEY not null, name varchar(255) not null);


DROP TABLE IF EXISTS calc_log;
CREATE TABLE IF NOT EXISTS calc_log
(time integer null, id_calc integer not null, status integer not null, name varchar(255) not null, startdate datetime not null, enddate datetime null, calcdate datetime not null );

DROP TABLE IF EXISTS calc_stage;
CREATE TABLE IF NOT EXISTS calc_stage
(id_stage INTEGER PRIMARY KEY not null, name varchar(255) not null, id_calc integer not null,
FOREIGN KEY (id_calc) REFERENCES calc (id_calc) ON DELETE CASCADE ON UPDATE NO ACTION);


DROP TABLE IF EXISTS log_stage;
CREATE TABLE IF NOT EXISTS log_stage
(id_calc INTEGER PRIMARY KEY not null, name_calc varchar(255) not null, name_stage varchar(255) not null,status integer not null,startdate datetime not null,enddate datetime null,
FOREIGN KEY (id_calc) REFERENCES calc (id_calc) ON DELETE CASCADE ON UPDATE NO ACTION);


