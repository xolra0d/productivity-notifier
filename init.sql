CREATE TABLE performance (
    timestamp DATETIME NOT NULL
                       DEFAULT CURRENT_TIMESTAMP
                       PRIMARY KEY,
    minutes   INT      NOT NULL
);
