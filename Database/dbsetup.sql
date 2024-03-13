-- Create and enter into database
CREATE DATABASE Buckymon_Go_DB;
USE Buckymon_Go_DB;
-- Following 4 tables are the entities
CREATE TABLE User (
    u_id INT NOT NULL auto_increment,
    u_name VARCHAR(255) NULL,
    u_score INT NULL,
    PRIMARY KEY (u_id)
);

CREATE TABLE Achievements (
    a_id INT NOT NULL auto_increment,
    a_name VARCHAR(255) NULL,
    a_score INT NULL,
    a_desc TEXT,
    PRIMARY KEY (a_id)
);

CREATE TABLE Locations (
    l_id INT NOT NULL auto_increment,
    l_name VARCHAR(255),
    l_lat DECIMAL(11, 8),
    l_long DECIMAL(11, 8),
    PRIMARY KEY (l_id)
);

CREATE TABLE Events (
    e_id INT NOT NULL auto_increment,
    e_name VARCHAR(255) NULL,
    e_score INT NULL,
    e_desc TEXT,
    l_id INT,
    PRIMARY KEY (e_id),
    FOREIGN KEY (l_id) REFERENCES Locations(l_id)
);

-- Following 2 tables are relationships
CREATE TABLE Achieves (
    u_id INT,
    a_id INT,
    PRIMARY KEY (u_id, a_id),
    FOREIGN KEY (u_id) REFERENCES User(u_id),
    FOREIGN KEY (a_id) REFERENCES Achievements(a_id)
);

CREATE TABLE Completes (
    u_id INT,
    e_id INT,
    PRIMARY KEY (u_id, e_id),
    FOREIGN KEY (u_id) REFERENCES User(u_id),
    FOREIGN KEY (e_id) REFERENCES Events(e_id)
);