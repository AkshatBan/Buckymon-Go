-- This script tests whether the database is working as intended by inserting test rows into each table

INSERT INTO User (u_name, u_score) Values ('Superuser', 0);
INSERT INTO User (u_name, u_score) Values ('Aaron', 0);
INSERT INTO User (u_name, u_score) Values ('Belle', 0);
INSERT INTO User (u_name, u_score) Values ('Charlie', 0);
INSERT INTO User (u_name, u_score) Values ('Daniella', 0);

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

INSERT INTO Completes (completes_u_id, completes_e_id) VALUES (10000002, 40000001); -- Aaron completes Speed Friending
INSERT INTO Completes (completes_u_id, completes_e_id) VALUES (10000003, 40000002); -- Belle completes Farmer's Market

INSERT INTO Achieves (achieves_u_id, achieves_a_id) VALUES (10000002, 20000004); -- Aaron achieves 'Complete your first event'
INSERT INTO Achieves (achieves_u_id, achieves_a_id) VALUES (10000002, 20000003); -- Aaron achieves 'So, what's your major?'
INSERT INTO Achieves (achieves_u_id, achieves_a_id) VALUES (10000003, 20000004); -- Belle achieves 'Complete your first event'


--Bascom Hall
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Good Luck!', 1, 'Rub Honest Abe''s foot for good luck!', 'Tradition');

--Union South
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Bowling!', 3, 'Go Bowling at the Union South bowling alley.', 'Social');

--Memorial Union
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Live Music', 5, 'See live music at the iconic Memorial Union Terrace', 'Tourism');

--Taco Bell
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Cantina Chicken', 3, 'Try an item off the new cantina chicken menu at Taco Bell', 'Tourism');

--Nick
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Excecise at the Nick', 4, 'Get a 30 minute workout in at the Nicholas Recreation Center.', 'Active');

--Camp Randall
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Varsity!', 3, 'Sing Varsity with fellow badgers at Camp Randall.', 'Tradition');

--Bakke
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Climb Mount Mendota', 6, 'Try out the climbing wall at the state of the art Bakke Recreation center.', 'Active');

--Kohl Center
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Go to a game!', 8, 'Watch a sporting event at the Kohl Center.', 'Social');

--Music Hall
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Night at the Opera', 5, 'Watch UW Madison music students perform in an opera.', 'Social');

--CS Buildin
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Rockhopper', 1, 'Log in to a linux machine in the rockhopper lab.', 'Education');

--Capitol Building
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Farmer''s Market', 3, 'The must-see largest outdoor farmer''s market in the world!', 'Tourism');

--Chazen 
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Take in the art', 3, 'Walk the galleries of the Chazen modern art museum.', 'Tourism');

--Carillon Tower
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Can you hear the bells?', 1, 'Listen for the bells to ring on the quarter hour.', 'Tradition');

--Agricultural hall
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Agricvtvre?', 2, 'Admire the over century old building that houses the school of agriculture.', 'Education');

--Stock pavilion
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Moo', 5, 'Try to find some cows at the stock pavilion', 'Active');

--Babcock Hall
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Daily Scoop', 3, 'Get a scoop of world famous Babcock Hall ice cream.', 'Tourism');

--Field House
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Bump, Set, Spike!', 5, 'Visit the home of the 2022 national champion volleyball team!', 'Tradition');

--Business school
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Get down to business', 5, 'Have a study session at the business library.', 'Education');

--Memorial Library
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Caged Up', 4, 'Lock yourself in a cage at the memorial library', 'Education');

--Red Gym
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Up in arms', 1, 'Learn the storied history of the iconic Red Gym', 'Tradition');

--Kwik Trip
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Half a dozen', 2, 'Get a pack of glazed donuts from Kwik Trip, be sre to share with friends!', 'Social');

--Discovery Building
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Dinosaurs?!', 2, 'Take in the mesozoic gardens at the discovery building', 'Education');

--Botanical gardens
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Walk in the park', 5, 'Meet a friend and walk through the UW Madison botanical gardens.', 'Active');

--Observatory overlook
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('I can see for miles and miles', 3, 'Watch the sunset from the top of observatory hill', 'Tourism');

--Washburn observatory
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Starry night', 3, 'Tour the historic Washburn Observatory', 'Tradition');

--Allen centennial gardens
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Save the bees', 4, 'Find the bee colony at the Allen Centennial Gardens.', 'Active');

--Peace Park
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Peace', 6, 'Visit State Street from Peace Park', 'Tourism');

--Lakeshore path
INSERT INTO Events (e_name, e_score, e_desc, l_id) VALUES ('Walkin on Sunshine', 4, 'Escape the city and take a stroll down the lakeshore path.', 'Active');




