import telebot
import sqlite3
from Login import *


def push(text):
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    cur.execute('SELECT id FROM Users')
    s = cur.fetchall()
    try:
        print(s)
        print(s[0])
        print(s[1])
        bot.send_message(s[0], text)
        cur.execute("UPDATE Users SET active = 1 WHERE id = " + str(s[0]))
        db.commit()
        print("Сообщение доставлено")
    except:
        cur.execute('UPDATE Users SET active = 0 WHERE id = ' + str(s[0]))
        db.commit()
        print("Не удалось отправить сообщение")
    db.close()
