-- This script tests whether the database is working as intended by inserting test rows into each table

INSERT INTO User (u_first_name, u_last_name, u_score) Values ('Aaron', 'Smith', 0);
INSERT INTO User (u_first_name, u_last_name, u_score) Values ('Belle', 'Jones', 0);
INSERT INTO User (u_first_name, u_last_name, u_score) Values ('Charlie', 'Bradbury', 0);
INSERT INTO User (u_first_name, u_last_name, u_score) Values ('Daniella', 'Johns', 0);

INSERT INTO Achievements (a_name, a_score, a_desc) Values ('Complete 5 Events', 7, 'This achievement is unlocked when you have completed 5 events on Campus or in Madison.');
INSERT INTO Achievements (a_name, a_score, a_desc) Values ('Complete 10 Events', 12, 'This achievement is unlocked when you have completed 10 events on Campus or in Madison.');
INSERT INTO Achievements (a_name, a_score, a_desc) Values ('So, what''s your major?', 3, 'This achievement is unlocked when you have completed your first social event.');
INSERT INTO Achievements (a_name, a_score, a_desc) Values ('Complete your first event', 1, 'The first step is always the hardest. Have an extra point on us for getting through your first event!');

INSERT INTO Locations (l_name, l_lat, l_long) Values ('Bascom Hall', 0,0);
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Capitol Building', 0,0);
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Waters Residence Hall', 0,0);
INSERT INTO Locations (l_name, l_lat, l_long) Values ('Gordon''s Dining Hall', 0,0);

INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Speed Friending', 1, 'Make friends in a fun and socially low-stakes environment!', 30000004);
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Farmer''s Market', 3, 'The must-see largest outdoor farmer''s market in the world!', 30000002);
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Good Luck!', 1, 'Rub Honest Abe''s foot for good luck!', 30000001);

INSERT INTO Completes (completes_u_id, completes_e_id) VALUES (10000002, 40000001); -- Belle completes Speed Friending
INSERT INTO Completes (completes_u_id, completes_e_id) VALUES (10000003, 40000002); -- Charlie completes Farmer's Market

INSERT INTO Achieves (achieves_u_id, achieves_a_id) VALUES (10000002, 20000004); -- Belle achieves 'Complete your first event'
INSERT INTO Achieves (achieves_u_id, achieves_a_id) VALUES (10000002, 20000003); -- Belle achieves 'So, what's your major?'
INSERT INTO Achieves (achieves_u_id, achieves_a_id) VALUES (10000003, 20000004); -- Charlie achieves 'Complete your first event'