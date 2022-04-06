--
-- File generated with SQLiteStudio v3.3.3 on Вт апр 5 13:03:11 2022
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


-- Index: sqlite_autoindex_Address_1
DROP INDEX IF EXISTS sqlite_autoindex_Address_1;

CREATE INDEX sqlite_autoindex_Address_1 ON Address (
    Id COLLATE BINARY
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
