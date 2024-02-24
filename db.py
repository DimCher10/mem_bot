import sqlite3
from datetime import datetime


def register_user(user_id):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    now = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
    cursor.execute("INSERT OR IGNORE INTO users(user_id, now) VALUES(?, ?)", (telegram_id, reg_date))
    connection.commit()


def save_photo(file_id):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO images (file_id) VALUES (?)", (file_id,))
    connection.commit()
    return cursor.lastrowid

def get_image_file_id(id):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute("SELECT file_id FROM images WHERE id = ?",(id,))
    file_id = cursor.fetchone()
    return file_id[0]

def get_memes(number=5):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute("SELECT file_id FROM images LIMIT ?", (number,))
    return cursor.fetchall()


def add_moderator(user_id):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO roles VALUES (?,?)", (user_id))

def get_current_id():
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(id) FROM images;")
    return cursor.fetchone()[0]+1