# Шаг 1

Напишем код для создания таблиц в базе данных и сохраним его в файле `init.sql`
(используется СУБД `SQLite3`)

_Таблица_ `users` _(данные о пользователях)_
```sql
CREATE TABLE users (
    telegram_id INTEGER PRIMARY KEY,
    username TEXT,
    reg_date TEXT
)
```

_Таблица_ `messages` _(все поступившие боту сообщения)_
```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    telegram_id INTEGER,
    message_text TEXT,
    date_time TEXT,
    FOREIGN KEY (telegram_id) 
    REFERENCES users(telegram_id) 
);
```

_Таблица_ `attachments` _(все нетекстовые данные, поступившие боту )_
```sql
CREATE TABLE attachments (
    id INTEGER PRIMARY KEY,
    message_id INTEGER,
    telegram_file_id TEXT,
    file_name TEXT,
    FOREIGN KEY (message_id)
    REFERENCES messages(id) 
);
```


