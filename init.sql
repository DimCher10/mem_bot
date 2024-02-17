CREATE TABLE IF NOT EXISTS users (
    telegram_id INTEGER PRIMARY KEY,
    username TEXT,
    reg_date TEXT
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    telegram_id INTEGER,
    is_incoming INTEGER,
    message_text TEXT,
    date_time TEXT,
    FOREIGN KEY (telegram_id) 
    REFERENCES users(telegram_id) 
);


CREATE TABLE IF NOT EXISTS attachments (
    id INTEGER PRIMARY KEY,
    message_id INTEGER,
    telegram_file_id TEXT,
    file_name TEXT,
    FOREIGN KEY (message_id)
    REFERENCES messages(id) 
);

CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY,
    file_id TEXT UNIQUE
)