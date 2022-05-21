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
    motion text,
    description text
);

CREATE TABLE IF NOT EXISTS tx (
    txid integer PRIMARY KEY AUTOINCREMENT,
    uid integer NOT NULL,
    tx_date datetime NOT NULL,
    price float NOT NULL,
    motion text,
    description text
);