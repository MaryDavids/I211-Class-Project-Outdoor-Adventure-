DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS members;

CREATE TABLE members(
    id_mem INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30),
    date_of_birth VARCHAR(11),
    email VARCHAR(30),
    address VARCHAR(70),
    phone VARCHAR(12)
)ENGINE=INNODB;


insert into members(name,date_of_birth,email,address,phone) values 
("John Smith","1990-12-27","jsmith@hotmail","74 N. Rockland Lane Williamsburg.. VA 23185","317-541-2827"),
("Roda Bentley","1983-9-16","rbentley@gmail.com","38 Thatcher Laneman.. SC 29349","967-221-0210"),
("Sheila Rhodes","1994-10-12","sherhodes@yahoo.com","364 Snake Hill St. Andover..MA 01810","569-264-8982"),
("Sope Kolawole","1998-10-07","skolawole@gmail.com","7535 S. Fairground Drive Wheeling.. WV 26003","710-595-2889"),
("Jake Whitehouse","1776-12-06","jw@yahoo.com", "7161 East Lane Attleboro MA 02703","404-795-5505"),
("Sadie Disney","1995-10-09","sd@gmail.com","535 Logan Circle Saugus.. MA 01906","628-777-2719"),
("James Brown","2000-03-08","jbrown@hotmail.com","2401  Hermitage ct.","317-652-8306"),
("Mary Imoleoluwa Davids","2023-04-07","davidsma@iu.edu","3674 Pickwick Cir, Plainfield, IN 46168","3176528306");


CREATE TABLE trips (
id_trip INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
location VARCHAR(30),
length INT,
level VARCHAR(15),
start_date VARCHAR(11),
cost VARCHAR(5) NOT NULL,
leader VARCHAR(20),
description VARCHAR(300)
)ENGINE=INNODB;

-- ALTER TABLE trips MODIFY name VARCHAR(50); 


insert into trips(name,location,length,level,start_date,cost,leader,description ) values 
("Crazy Rapids Rafting","Grand Canyon",3,"Advanced","2023-04-08","$40","John Smith","Need swim vests"),
("Scuba Steve's Reef Adventure","Yellowood State Park",1,"Beginner","2023-04-01","$50","Roda Bentley","Need scuba gear"),
("Old Knobstone Trail Hike","Knobstone Lake Trail",5,"Beginner","2023-04-07","$10","Sheila Rhodes","Need hiking shoes and water bottle"),
("Treehouse Building","Turpertine Creek Tree Houses", 7,"Intermediate","2023-04-07", "$60","Sope Kolawole","Need safety kit and supervision"),
("Carson's Canoe Camping","White River",9,"Intermediate","2023-05-03","$30","Jake Whitehouse","Need swim vests "),
("Texas Horseback Riding","Stone Creek Ranch",3,"Beginner","2023-05-19","$40","Sadie Disney","Need protective gear and shoes");


CREATE TABLE attendance(
id_trip INT NOT NULL,
id_mem INT NOT NULL,
FOREIGN KEY(id_trip) REFERENCES trips(id_trip),
FOREIGN KEY(id_mem) REFERENCES members(id_mem)
)ENGINE=INNODB;

INSERT INTO attendance values
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(2,7),
(4,8);
