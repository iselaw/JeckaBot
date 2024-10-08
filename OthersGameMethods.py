import random
import sqlite3
from time import sleep

from telebot import types
from Login import *


def getBalance(message):
    balance = 0
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT balance FROM Users where userId=" + str(message.chat.id)):
        balance = x[0]
    db.close()
    return balance


def updateScore(bet, point, message):
    isBankrot = False
    balance = getBalance(message)
    if balance >= bet:
        balance = balance + point
        db = sqlite3.connect('db/JeckaBot.db')
        cur = db.cursor()
        cur.execute("UPDATE Users SET balance = " + str(balance) + " WHERE userId = " + str(message.chat.id))
        db.commit()
        db.close()
    else:
        isBankrot = True
    return isBankrot, balance
