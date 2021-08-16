CREATE TABLE User(
    idx INTEGER PRIMARY KEY AUTOINCREMENT,
    id TEXT NOT NULL UNIQUE,
    pw TEXT NOT NULL
);

CREATE TABLE SF_machine(
    idx INTEGER  PRIMARY KEY AUTOINCREMENT,
    LED INT DEFAULT 0,
    w_level INT DEFAULT 0,
    l_level INT DEFAULT 0,
    s_level INT DEFAULT 0,
    pump BOOL DEFAULT false,
    fan_in BOOL DEFAULT false,
    fan_out BOOL DEFAULT FALSE,
    temp FLOAT DEFAULT 0,
    humi FLOAT DEFAULT 0
);

CREATE TABLE Auth(
    idx INTEGER PRIMARY KEY AUTOINCREMENT,
    uidx INT,
    sfidx INT,
    grade INT DEFAULT 0,
    FOREIGN KEY (uidx) REFERENCES User (idx),
    FOREIGN KEY (sfidx) REFERENCES SF_machine (idx)
);