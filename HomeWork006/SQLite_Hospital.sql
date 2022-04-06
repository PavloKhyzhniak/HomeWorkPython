--
-- File generated with SQLiteStudio v3.3.3 on Вт апр 5 16:57:54 2022
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Address
DROP TABLE IF EXISTS Address;

CREATE TABLE Address (
    Id         INTEGER      PRIMARY KEY AUTOINCREMENT
                            NOT NULL
                            UNIQUE,
    Street     VARCHAR (40) NOT NULL,
    House      INT          NOT NULL,
    Appartment INT
);

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        1,
                        'Donetsk',
                        123,
                        2
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        2,
                        'Makeevka',
                        45,
                        2
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        3,
                        'Patona',
                        23,
                        NULL
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        4,
                        'Donetsk',
                        7,
                        5
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        5,
                        'Donetsk',
                        4,
                        5
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        6,
                        'Donetsk',
                        2,
                        3
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        7,
                        'Donetsk',
                        2,
                        1
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        8,
                        'Donetsk',
                        23,
                        23
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        9,
                        'Patona',
                        67,
                        9
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        10,
                        'Patona',
                        87,
                        6
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        11,
                        'Patona',
                        9,
                        NULL
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        12,
                        'Patona',
                        8,
                        NULL
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        13,
                        'Patona',
                        2,
                        NULL
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        14,
                        'Makeevka',
                        87,
                        6
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        15,
                        'Makeevka',
                        3,
                        2
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        16,
                        'Makeevka',
                        65,
                        6
                    );

INSERT INTO Address (
                        Id,
                        Street,
                        House,
                        Appartment
                    )
                    VALUES (
                        17,
                        'Makeevka',
                        32,
                        1
                    );


-- Table: Doctors
DROP TABLE IF EXISTS Doctors;

CREATE TABLE Doctors (
    Id             INTEGER      PRIMARY KEY AUTOINCREMENT
                                NOT NULL
                                UNIQUE,
    Specialization VARCHAR (40) NOT NULL,
    UserId         INT          REFERENCES User (Id) 
                                NOT NULL,
    Rate           DOUBLE       NOT NULL
                                DEFAULT (5.5) 
                                CHECK (Rate > 0 AND 
                                       Rate < 100.0) 
);

INSERT INTO Doctors (
                        Id,
                        Specialization,
                        UserId,
                        Rate
                    )
                    VALUES (
                        1,
                        'Terapevt',
                        1,
                        5.5
                    );

INSERT INTO Doctors (
                        Id,
                        Specialization,
                        UserId,
                        Rate
                    )
                    VALUES (
                        2,
                        'Administrator',
                        6,
                        3.7
                    );

INSERT INTO Doctors (
                        Id,
                        Specialization,
                        UserId,
                        Rate
                    )
                    VALUES (
                        3,
                        'Okulist',
                        7,
                        3.8
                    );


-- Table: Patient
DROP TABLE IF EXISTS Patient;

CREATE TABLE Patient (
    Id     INTEGER PRIMARY KEY AUTOINCREMENT
                   UNIQUE
                   NOT NULL,
    UserId         REFERENCES User (Id) 
                   NOT NULL
);

INSERT INTO Patient (
                        Id,
                        UserId
                    )
                    VALUES (
                        1,
                        2
                    );

INSERT INTO Patient (
                        Id,
                        UserId
                    )
                    VALUES (
                        2,
                        5
                    );

INSERT INTO Patient (
                        Id,
                        UserId
                    )
                    VALUES (
                        3,
                        4
                    );

INSERT INTO Patient (
                        Id,
                        UserId
                    )
                    VALUES (
                        4,
                        3
                    );


-- Table: User
DROP TABLE IF EXISTS User;

CREATE TABLE User (
    Id         INTEGER      PRIMARY KEY AUTOINCREMENT
                            NOT NULL
                            UNIQUE,
    FirstName  VARCHAR (40) NOT NULL,
    SecondName VARCHAR (40),
    LastName   VARCHAR (40) NOT NULL,
    BirthDate  DATE,
    AddressId  INT          REFERENCES Address (Id) 
);

INSERT INTO User (
                     Id,
                     FirstName,
                     SecondName,
                     LastName,
                     BirthDate,
                     AddressId
                 )
                 VALUES (
                     1,
                     'Petr',
                     'Vasiliyvich',
                     'Grogg',
                     '2.10.1980',
                     2
                 );

INSERT INTO User (
                     Id,
                     FirstName,
                     SecondName,
                     LastName,
                     BirthDate,
                     AddressId
                 )
                 VALUES (
                     2,
                     'Alex',
                     'Fisher',
                     'Ditrich',
                     '23.10.1978',
                     3
                 );

INSERT INTO User (
                     Id,
                     FirstName,
                     SecondName,
                     LastName,
                     BirthDate,
                     AddressId
                 )
                 VALUES (
                     3,
                     'Ivan',
                     'Georgiy',
                     'Hillmann',
                     '12.23.1978',
                     1
                 );

INSERT INTO User (
                     Id,
                     FirstName,
                     SecondName,
                     LastName,
                     BirthDate,
                     AddressId
                 )
                 VALUES (
                     4,
                     'Eva',
                     'Fisher',
                     'Jera',
                     '23.10.1978',
                     3
                 );

INSERT INTO User (
                     Id,
                     FirstName,
                     SecondName,
                     LastName,
                     BirthDate,
                     AddressId
                 )
                 VALUES (
                     5,
                     'Lola',
                     'Herra',
                     'Hugo',
                     '23.10.1978',
                     3
                 );

INSERT INTO User (
                     Id,
                     FirstName,
                     SecondName,
                     LastName,
                     BirthDate,
                     AddressId
                 )
                 VALUES (
                     6,
                     'Alex',
                     'Hoggart',
                     'Billany',
                     '23.10.1978',
                     3
                 );

INSERT INTO User (
                     Id,
                     FirstName,
                     SecondName,
                     LastName,
                     BirthDate,
                     AddressId
                 )
                 VALUES (
                     7,
                     'Alex',
                     'Richard',
                     'Gass',
                     '23.10.1978',
                     3
                 );


-- Table: Visit
DROP TABLE IF EXISTS Visit;

CREATE TABLE Visit (
    Id        INTEGER  PRIMARY KEY AUTOINCREMENT
                       UNIQUE
                       NOT NULL,
    DoctorId           REFERENCES Doctors (Id) 
                       NOT NULL,
    PatientId          REFERENCES Patient (Id) 
                       NOT NULL,
    Price     INT      DEFAULT (1000) 
                       NOT NULL,
    Date      DATETIME NOT NULL
);

INSERT INTO Visit (
                      Id,
                      DoctorId,
                      PatientId,
                      Price,
                      Date
                  )
                  VALUES (
                      1,
                      1,
                      1,
                      2000,
                      '2021-12-4'
                  );

INSERT INTO Visit (
                      Id,
                      DoctorId,
                      PatientId,
                      Price,
                      Date
                  )
                  VALUES (
                      2,
                      3,
                      4,
                      1300,
                      '2022-04-23'
                  );

INSERT INTO Visit (
                      Id,
                      DoctorId,
                      PatientId,
                      Price,
                      Date
                  )
                  VALUES (
                      3,
                      2,
                      2,
                      1000,
                      '2021-10-5'
                  );

INSERT INTO Visit (
                      Id,
                      DoctorId,
                      PatientId,
                      Price,
                      Date
                  )
                  VALUES (
                      4,
                      3,
                      3,
                      870,
                      '2022-05-04'
                  );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
