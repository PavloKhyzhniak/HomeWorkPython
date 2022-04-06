--
-- File generated with SQLiteStudio v3.3.3 on Вт апр 5 18:44:30 2022
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

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


-- Index: sqlite_autoindex_User_1
DROP INDEX IF EXISTS sqlite_autoindex_User_1;

CREATE INDEX sqlite_autoindex_User_1 ON User (
    Id COLLATE BINARY
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
