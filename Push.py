import telebot
import sqlite3
from Login import *


def push(text):
    userValue = 0
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT COUNT(id) FROM Users WHERE active=1 OR active=0"):
        userValue = x[0]
    db.close()
    count = 1
    s = 1
    print(userValue)
    while count <= userValue:
        db = sqlite3.connect('db/JeckaBot.db')
        cur = db.cursor()
        for s1 in cur.execute("SELECT userId FROM Users where id=" + str(count)):
            s = s1[0]
        db.close()
        try:
            bot.send_message(s, text)
            db = sqlite3.connect('db/JeckaBot.db')
            cur = db.cursor()
            cur.execute("UPDATE Users SET active = 1 WHERE id = " + str(count))
            db.commit()
            db.close()
            print('отправлено')
        except:
            db = sqlite3.connect('db/JeckaBot.db')
            cur = db.cursor()
            cur.execute("UPDATE Users SET active = 0 WHERE id = " + str(count))
            db.commit()
            db.close()
            print('Не отправлено')
        count = count + 1