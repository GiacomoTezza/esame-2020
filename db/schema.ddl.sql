CREATE DATABASE IF NOT EXISTS drivingschool;
USE drivingschool;

DROP TABLE IF EXISTS Registration;
DROP TABLE IF EXISTS License;
DROP TABLE IF EXISTS Client;

CREATE TABLE License (
    ID INT AUTO_INCREMENT,
    Name VARCHAR(10) NOT NULL,
    Description VARCHAR(512),

    PRIMARY KEY (ID)
);


CREATE TABLE Client (
    ID INT AUTO_INCREMENT,
    Name VARCHAR(30) NOT NULL,
    Surname VARCHAR(30) NOT NULL,
    CF VARCHAR(30) NOT NULL,

    PRIMARY KEY (ID),
    CONSTRAINT cfUnique UNIQUE (cf)
);


CREATE TABLE Registration (
    LicenseID INT NOT NULL,
    ClientID INT NOT NULL,
    StartDate DATE NOT NULL,
    ExamStatus VARCHAR(30) NOT NULL,

    FOREIGN KEY (LicenseID) REFERENCES License(ID),
    FOREIGN KEY (ClientID) REFERENCES Client(ID),
    PRIMARY KEY (LicenseID, ClientID, StartDate)
);