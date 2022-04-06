--
-- File generated with SQLiteStudio v3.3.3 on Вт апр 5 19:56:42 2022
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

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


-- Index: sqlite_autoindex_Visit_1
DROP INDEX IF EXISTS sqlite_autoindex_Visit_1;

CREATE INDEX sqlite_autoindex_Visit_1 ON Visit (
    Id COLLATE BINARY
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
