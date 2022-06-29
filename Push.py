import telebot
import sqlite3
from Login import *


def push(text):
    userValue = 0
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT COUNT(id) FROM Users WHERE active=1 OR active=0"):
        userValue = x[0]
    count = 1
    while count <= userValue:
        for s1 in cur.execute("SELECT userId FROM Users where id=" + str(count)):
            s = s1[0]
        try:
            bot.send_message(s, text)
            cur.execute("UPDATE Users SET active = 1 WHERE userId = " + str(s))
            db.commit()
        except:
            cur.execute("UPDATE Users SET active = 0 WHERE userId = " + str(s))
            db.commit()
        count = count + 1
    db.close()
