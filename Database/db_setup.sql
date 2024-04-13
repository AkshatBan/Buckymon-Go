-- Create and enter into database
CREATE DATABASE Buckymon_Go_DB;
USE Buckymon_Go_DB;
-- Following 4 tables are the entities
CREATE TABLE User (
    u_id INT NOT NULL auto_increment,
    u_name VARCHAR(255) UNIQUE,
    u_score INT NULL,
    PRIMARY KEY (u_id, u_name)
);
ALTER TABLE User auto_increment = 10000001;

CREATE TABLE Achievements (
    a_id INT NOT NULL auto_increment,
    a_name VARCHAR(255) NULL,
    a_score INT NULL,
    a_desc TEXT,
    PRIMARY KEY (a_id)
);
ALTER TABLE Achievements auto_increment = 20000001;

CREATE TABLE Locations (
    l_id INT NOT NULL auto_increment,
    l_name VARCHAR(255),
    l_lat DECIMAL(11, 8),
    l_long DECIMAL(11, 8),
    PRIMARY KEY (l_id)
);
ALTER TABLE Locations auto_increment = 30000001;

CREATE TABLE Events (
    e_id INT NOT NULL auto_increment,
    e_name VARCHAR(255) NULL,
    e_score INT NULL,
    e_desc TEXT,
    l_id INT,
    PRIMARY KEY (e_id),
    FOREIGN KEY (l_id) REFERENCES Locations(l_id)
);
ALTER TABLE Events auto_increment = 40000001;

-- Following 2 tables are relationships
CREATE TABLE Achieves (
    achieves_u_id INT,
    achieves_a_id INT,
    PRIMARY KEY (achieves_u_id, achieves_a_id),
    FOREIGN KEY (achieves_u_id) REFERENCES User(u_id),
    FOREIGN KEY (achieves_a_id) REFERENCES Achievements(a_id)
);

CREATE TABLE Completes (
    completes_u_id INT,
    completes_e_id INT,
    PRIMARY KEY (completes_u_id, completes_e_id),
    FOREIGN KEY (completes_u_id) REFERENCES User(u_id),
    FOREIGN KEY (completes_e_id) REFERENCES Events(e_id)
);

-- Adding starter data to the database 
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Bascom Hall', 0,0);
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Capitol Building', 0,0);
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Waters Residence Hall', 0,0);
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Gordon''s Dining Hall', 0,0);

INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Speed Friending', 1, 'Make friends in a fun and socially low-stakes environment!', 30000004);
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Farmer''s Market', 3, 'The must-see largest outdoor farmer''s market in the world!', 30000002);
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Good Luck!', 1, 'Rub Honest Abe''s foot for good luck!', 30000001);