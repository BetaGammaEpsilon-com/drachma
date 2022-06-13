CREATE TABLE IF NOT EXISTS users (
    uid integer PRIMARY KEY AUTOINCREMENT,
    name text UNIQUE NOT NULL,
    balance float NOT NULL
);

CREATE TABLE IF NOT EXISTS tx_unverified (
    txid integer PRIMARY KEY AUTOINCREMENT,
    uid integer NOT NULL,
    tx_date datetime NOT NULL,
    price float NOT NULL,
    motion text NOT NULL,
    description text,
    description_url text
);

CREATE TABLE IF NOT EXISTS tx (
    txid integer PRIMARY KEY,
    uid integer NOT NULL,
    tx_date datetime NOT NULL,
    price float NOT NULL,
    motion text NOT NULL,
    description text,
    description_url text
);

CREATE TABLE IF NOT EXISTS motions (
    motion text PRIMARY KEY,
    init_date datetime
);

INSERT INTO motions VALUES ('house', CURRENT_TIMESTAMP);
INSERT INTO motions VALUES ('eboard', CURRENT_TIMESTAMP);
INSERT INTO motions VALUES ('drachma_admin', CURRENT_TIMESTAMP);