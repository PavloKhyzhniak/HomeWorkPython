--
-- File generated with SQLiteStudio v3.3.3 on Вт апр 5 18:13:48 2022
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

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


-- Index: sqlite_autoindex_Patient_1
DROP INDEX IF EXISTS sqlite_autoindex_Patient_1;

CREATE INDEX sqlite_autoindex_Patient_1 ON Patient (
    Id COLLATE BINARY
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
