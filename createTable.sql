SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS Deaths;
DROP TABLE IF EXISTS US_Healthcare;
DROP TABLE IF EXISTS Americans;
DROP TABLE IF EXISTS Age_Group;
DROP TABLE IF EXISTS Race_and_Hispanic_Origin_Group;
DROP TABLE IF EXISTS State;

CREATE TABLE State (
    STATE_ID INT NOT NULL AUTO_INCREMENT,
	NAME VARCHAR(256) NOT NULL,
    PRIMARY KEY (STATE_ID)
);
LOAD DATA INFILE 'State.csv' 
INTO TABLE State
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE Age_Group (
    Age_Group_ID INT NOT NULL AUTO_INCREMENT,
    Type VARCHAR(256) NOT NULL,
    PRIMARY KEY (Age_Group_ID)
);

LOAD DATA INFILE 'Age_Group.csv' 
INTO TABLE Age_Group
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE Race_and_Hispanic_Origin_Group (
	Race_and_Hispanic_Origin_Group INT NOT NULL AUTO_INCREMENT,
	NAME VARCHAR(256) NOT NULL,
    Percentage_of_Population FLOAT,
    PRIMARY KEY (Race_and_Hispanic_Origin_Group)
);

LOAD DATA INFILE 'Race_and_Hispanic_Origin_Group.csv' 
INTO TABLE Race_and_Hispanic_Origin_Group
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE Americans (
    id INT NOT NULL auto_increment,
    Age_Group_ID INT NOT NULL,
    Race_and_Hispanic_Origin_Group INT NOT NULL,
    PRIMARY KEY (id, Age_Group_ID, Race_and_Hispanic_Origin_Group),
    FOREIGN KEY (Age_Group_ID) REFERENCES Age_Group (Age_Group_ID) ON DELETE CASCADE,
    FOREIGN KEY (Race_and_Hispanic_Origin_Group) REFERENCES Race_and_Hispanic_Origin_Group (Race_and_Hispanic_Origin_Group) ON DELETE CASCADE
);

LOAD DATA INFILE 'Americans.csv' 
INTO TABLE Americans
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE US_Healthcare (
	 STATE_ID INT NOT NULL,
     POPESTIMATE2019 INT,
     Medicaid_and_CHIP_Child_Enrollment INT,
     Total_Medicaid_and_CHIP_Enrollment INT,
     Medicaid_and_CHIP_Child_Enrollment_RATE FLOAT,
     Total_Medicaid_and_CHIP_Enrollment_RATE FLOAT,
     Total_Medicaid_Expense_Per_Enrollee INT,
     Total_Medicaid_Expense_Per_Child_Enrollee INT,
     PRIMARY KEY (STATE_ID),
     FOREIGN KEY (STATE_ID) REFERENCES State (STATE_ID) ON DELETE CASCADE
);

LOAD DATA INFILE 'US_Healthcare.csv' 
INTO TABLE US_Healthcare
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
;

CREATE TABLE Deaths (
    id INT NOT NULL,
    STATE_ID INT NOT NULL,
    COVID_19_Deaths INT,
    Percent_of_Total_COVID_19_Deaths FLOAT,
    PRIMARY KEY (id, STATE_ID),
    FOREIGN KEY (id) REFERENCES Americans (id) ON DELETE CASCADE,
    FOREIGN KEY (STATE_ID) REFERENCES State (STATE_ID) ON DELETE CASCADE
);

#doesn't work. Do a manual import of deaths.csv
LOAD DATA INFILE 'Deaths.csv' 
INTO TABLE Deaths
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
;

SET FOREIGN_KEY_CHECKS=1;