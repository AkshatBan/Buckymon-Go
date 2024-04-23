-- Create and enter into database
CREATE DATABASE Buckymon_Go_DB;
USE Buckymon_Go_DB;
-- Following 4 tables are the entities
CREATE TABLE User (
    u_id INT NOT NULL auto_increment,
    u_name VARCHAR(255) UNIQUE,
    u_score INT NULL,
    u_num_events INT NULL,
    PRIMARY KEY (u_id, u_name)
);
ALTER TABLE User auto_increment = 10000001;

CREATE TABLE Achievements (
    a_id INT NOT NULL auto_increment,
    a_name VARCHAR(255) NULL,
    a_score INT NULL,
    a_desc TEXT,
    a_tag VARCHAR(255) NULL,
    a_num_events INT NULL,
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
    e_tag VARCHAR(255) NULL,
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
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Bascom Hall', 43.0753, -89.4034); -- 30000001
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Wisconsin State Capitol Building', 43.0747, -89.3841); -- 30000002
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Waters Residence Hall', 43.07710731424237, -89.40707544855557); -- 30000003
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Gordon Dining and Event Hall', 43.07139974516165, -89.39868700437934); -- 30000004
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Union South', 43.0720, -89.4076); -- 30000005
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Memorial Union', 43.7062, -89.4000); -- 30000006
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Taco Bell Cantina', 43.0751, -89.3943); -- 30000007
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Nicholas Recreation Center', 43.0707, -89.3989); -- 30000008
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Bakke Recreation Center', 43.0767, -89.4201); -- 30000009
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Camp Randall Memorial Arch', 43.0711, -89.4094); -- 30000010
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Kohl Center', 43.0694, -89.396972); -- 30000011
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Music Hall', 43.0746, -89.4013); -- 30000012
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Computer Science Building', 43.0712, -89.4066); -- 30000013
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Chazen Art Museum', 43.073885, -89.399632); -- 30000014
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Carillon Tower', 43.07610606403628, -89.40505738646713); -- 30000015
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Agricultural Hall', 43.07552117476707, -89.41030164416945); -- 30000016
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Stock Pavilion', 43.075111055496706, -89.41516087597715); -- 30000017
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Babcock Hall Dairy Store', 43.07502717300505, -89.41382232771528); -- 30000018
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Wisconsin Field House', 43.068286873850056, -89.4126676476076); -- 30000019
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Wisconsin School of Business', 43.07308218737385, -89.40092169988056); -- 30000020
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Memorial Library', 43.0753807999997, -89.39847899307212); -- 30000021
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Red Gym', 43.076032149722764, -89.39841829728448); -- 30000022
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Kwik Trip', 43.06986770715015, -89.40922840005312); -- 30000023
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Wisconsin Discovery Building', 43.073225219619125, -89.40771376930945); -- 30000024
INSERT INTO Locations (l_name, l_lat, l_long) Values ('University of Wisconsin Botanical Gardens', 43.07365346736112, -89.40410001626894); -- 30000025
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Observatory Drive Outlook', 43.07662892776181, -89.40883412821086); -- 30000026
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Washburn Observatory', 43.076210778208214, -89.4086620187763); -- 30000027
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Allen Centennial Garden', 43.07676741144372, -89.41294461576284); -- 30000028
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Peace Park', 43.0749268686802, -89.392638586702); -- 30000029
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Lakeshore Path', 43.07756511084374, -89.40561113790231); -- 30000030

-- Starter Events
-- Bascom Hall
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Good Luck!', 1, 'Rub Honest Abe''s foot for good luck!', 'tradition',30000001);
-- Gordon Dining and Event Hall
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Speed Friending', 1, 'Make friends in a fun and socially low-stakes environment!', 'social', 30000004);
-- Wisconsin State Capitol Building
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Farmer''s Market', 3, 'The must-see largest outdoor farmer''s market in the world!', 'tourism', 30000002);
--Union South
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Bowling!', 3, 'Go Bowling at the Union South bowling alley.', 'social', 30000005);
--Memorial Union
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Live Music', 5, 'See live music at the iconic Memorial Union Terrace.', 'tourism', 30000006);
--Taco Bell
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Cantina Chicken', 3, 'Try an item off the new cantina chicken menu at Taco Bell.', 'tourism', 30000007);
--Nick
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Excecise at the Nick', 4, 'Get a 30 minute workout in at the Nicholas Recreation Center.', 'athletic', 30000008);
--Camp Randall
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Varsity!', 3, 'Sing Varsity with fellow badgers at Camp Randall.', 'tradition', 30000010);
--Bakke
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Climb Mount Mendota', 6, 'Try out the climbing wall at the state of the art Bakke Recreation center.', 'athletic', 30000009);
--Kohl Center
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Go to a game!', 8, 'Watch a sporting event at the Kohl Center.', 'social', 30000011);
--Music Hall
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Night at the Opera', 5, 'Watch UW Madison music students perform in an opera.', 'social', 30000012);
--CS Building
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Rockhopper', 1, 'Log in to a linux machine in the rockhopper lab.', 'educational', 30000013);
--Chazen 
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Take in the art', 3, 'Walk the galleries of the Chazen modern art museum.', 'tourism', 30000014);
--Carillon Tower
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Can you hear the bells?', 1, 'Listen for the bells to ring on the quarter hour.', 'tradition', 30000015);
--Agricultural hall
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Agricvltvre?', 2, 'Admire the over century old building that houses the school of agriculture.', 'educational', 30000016);
--Stock pavilion
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Moo', 5, 'Try to find some cows at the stock pavilion.', 'athletic', 30000017);
--Babcock Hall
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Daily Scoop', 3, 'Get a scoop of world famous Babcock Hall ice cream.', 'tourism', 30000018);
--Field House
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Bump, Set, Spike!', 5, 'Visit the home of the 2022 national champion volleyball team!', 'tradition', 30000019);
--Business school
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Get down to business', 5, 'Have a study session at the business library.', 'educational', 30000020);
--Memorial Library
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Caged Up', 4, 'Lock yourself in a cage at the memorial library.', 'educational', 30000021);
--Red Gym
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Up in arms', 1, 'Learn the storied history of the iconic Red Gym.', 'tradition', 30000022);
--Kwik Trip
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Half a dozen', 2, 'Get a pack of glazed donuts from Kwik Trip, be sure to share with friends!', 'social', 30000023);
--Discovery Building
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Dinosaurs?!', 2, 'Take in the mesozoic gardens at the discovery building', 'educational', 30000024);
--Botanical gardens
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Walk in the park', 5, 'Meet a friend and walk through the UW Madison botanical gardens.', 'athletic', 30000025);
--Observatory overlook
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('I can see for miles and miles', 3, 'Watch the sunset from the top of observatory hill', 'tourism', 30000026);
--Washburn observatory
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Starry night', 3, 'Tour the historic Washburn Observatory', 'tradition', 30000027);
--Allen centennial gardens
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Save the bees', 4, 'Find the bee colony at the Allen Centennial Gardens.', 'athletic', 30000028);
--Peace Park
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Peace', 6, 'Visit State Street from Peace Park', 'tourism', 30000029);
--Lakeshore path
INSERT INTO Events (e_name, e_score, e_desc, e_tag, l_id) VALUES ('Walkin'' on Sunshine', 4, 'Escape the city and take a stroll down the lakeshore path.', 'athletic', 30000030);






-- Event Quantity Achievements
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('Complete your first event', 1, 'The first step is always the hardest. Have an extra point on us for getting through your first event!', '', 1);
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('Complete 5 Events', 1, 'Unlocked when you have completed 5 events on Campus or in Madison.', '', 5);
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('Complete 10 Events', 2, 'Unlocked when you have completed 10 events on Campus or in Madison.', '', 10);
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('Complete 15 Events', 3, 'Unlocked when you have completed 15 events on Campus or in Madison.', '', 15);
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('Complete 20 Events', 4, 'Unlocked when you have completed 20 events on Campus or in Madison.', '', 20);
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('Complete 25 Events', 5, 'Unlocked when you have completed 25 events on Campus or in Madison.', '', 25);
-- Event type Achievements
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('So, what''s your major?', 3, 'Complete your first social event.', 'social', 0);
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('Sightseeing!', 1, 'Complete your first tourism event', 'tourism', 0);
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('Resist the Freshman 15', 1, 'Complete your first athletic event', 'athletic', 0);
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('U-Rah-Rah!', 1, 'Complete your first badger or Madison tradition event', 'tradition', 0);
INSERT INTO Achievements (a_name, a_score, a_desc, a_tag, a_num_events) Values ('Keeping that 4.0', 1, 'Complete your first education event', 'educational', 0);