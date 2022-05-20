CREATE TABLE IF NOT EXISTS users (
    uid integer PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE IF NOT EXISTS tx (
    tx_id integer PRIMARY KEY,
    uid integer NOT NULL,
    tx_date date NOT NULL,
    price float NOT NULL,
    status tinyint NOT NULL,
    motion text,
    description text
);