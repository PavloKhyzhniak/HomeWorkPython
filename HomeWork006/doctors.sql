--
-- File generated with SQLiteStudio v3.3.3 on Вт апр 5 16:57:08 2022
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

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


-- Index: sqlite_autoindex_Doctors_1
DROP INDEX IF EXISTS sqlite_autoindex_Doctors_1;

CREATE INDEX sqlite_autoindex_Doctors_1 ON Doctors (
    Id COLLATE BINARY
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
