import sqlite3

from telebot import types
from Login import *


@bot.message_handler(commands=["off"])
def mute(message, res=False):
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    cur.execute("UPDATE Users SET mute = 1 WHERE userId = " + str(message.chat.id))
    db.commit()
    db.close()
    bot.send_message(message.chat.id, 'Хорошо, помолчим. Если захочешь поболтать, введи /on')
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    if (isAdmin == False):
        bot.send_message(admin[0], message.from_user.first_name + " - Замутил бота")
        bot.send_message(admin[1], message.from_user.first_name + " - Замутил бота")
        bot.send_message(admin[2], message.from_user.first_name + " - Замутил бота")


@bot.message_handler(commands=["on"])
def unmute(message, res=False):
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    cur.execute("UPDATE Users SET mute = 0 WHERE userId = " + str(message.chat.id))
    db.commit()
    db.close()
    bot.send_message(message.chat.id, 'Привет, мы снова можем поболтать')
    isAdmin = False
    for x in admin:
        if message.chat.id == x:
            isAdmin = True
    if (isAdmin == False):
        bot.send_message(admin[0], message.from_user.first_name + " - Размутил бота")
        bot.send_message(admin[1], message.from_user.first_name + " - Размутил бота")
        bot.send_message(admin[2], message.from_user.first_name + " - Размутил бота")


@bot.message_handler(commands=["muteORunmute"])
def muteunmute(message, res=False):
    muteStatus = 3
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    for x in cur.execute("SELECT mute FROM Users WHERE userId=" + str(message.chat.id)):
        muteStatus = x[0]
    db.close()
    if muteStatus == 0:
        mute(message)
    else:
        unmute(message)
