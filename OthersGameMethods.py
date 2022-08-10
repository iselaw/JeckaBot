import random
import sqlite3
from time import sleep

from telebot import types
from Login import *


def getBalance(message):
    Balance = 0
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT balance FROM Users where userId=" + str(message.chat.id)):
        Balance = x[0]
    db.close()
    return Balance


def updateScore(bet, point, message):
    isBankrot = False
    Balance = getBalance(message)
    if Balance >= bet:
        Balance = Balance + point
        db = sqlite3.connect('db/JeckaBot.db')
        cur = db.cursor()
        cur.execute("UPDATE Users SET balance = " + str(Balance) + " WHERE userId = " + str(message.chat.id))
        db.commit()
        db.close()
    else:
        isBankrot = True
    return isBankrot, Balance
