import random
import os
import requests
import sqlite3
from telebot.types import InputMediaAudio
from bs4 import BeautifulSoup
from telebot import types
from Login import *


def audio_processing(message, isFirstAudio):
    key_like = types.InlineKeyboardButton(text='❤', callback_data='audioLike')
    key_nextTrack = types.InlineKeyboardButton(text='>>>', callback_data='audionext')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(key_like)
    keyboard.add(key_nextTrack)
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    for rand in cur.execute('SELECT * FROM Music WHERE ID IN (SELECT ID FROM Music ORDER BY RANDOM() LIMIT 1)'):
        audioo = rand[5]
        nextAudio(message, audioo, keyboard, isFirstAudio)
    db.close()


def nextAudio(message, audioo, keyboard, isFirstAudio):
    if isFirstAudio == False:
        bot.edit_message_media(chat_id=message.chat.id, message_id=message.message_id, media=InputMediaAudio(audioo),
                               reply_markup=keyboard)
    if isFirstAudio == True:
        bot.send_audio(chat_id=message.chat.id, audio=audioo, reply_markup=keyboard)


def LikePlayList(message):
    try:
        MessageChatId = str(message.chat.id)
        MessageGroupId = MessageChatId.split('-', 1)[1]
        db = sqlite3.connect('db/PlayList.db')
        Plist = db.cursor()
        Plist.execute("CREATE TABLE IF NOT EXISTS " + "pList_" + MessageGroupId + """(
                   Id INTEGER NOT NULL UNIQUE,
                   Performer TEXT,
                   Title TEXT,
                   FileId TEXT,
                   UniqueId TEXT,
                   PRIMARY KEY("Id" AUTOINCREMENT)
                   );
                """)
        db.commit()
        track = str(message.audio.file_unique_id)
        Track_performer = message.audio.performer
        Track_title = message.audio.title
        isNew = True
        UniqueId_list = []
        for UniqueId in Plist.execute('SELECT UniqueId FROM pList_' + MessageGroupId + '  WHERE UniqueId LIKE ?',
                                          ('%' + track + '%',)):
            UniqueId_list.append(UniqueId[0])
            UniqueId_list1 = UniqueId_list[0]
            if str(UniqueId_list1) == str(message.audio.file_unique_id):
                isNew = False
                bot.send_message(message.chat.id, Track_performer + " - " + Track_title + " - Такой трек уже есть ")

        if isNew == True:
            Track_id = message.audio.file_id
            Track_Unique = message.audio.file_unique_id
            db.execute(
                    "INSERT INTO " + "pList_" + MessageGroupId + " (Performer, Title, FileId, UniqueId) VALUES (?, ?, ?, ?);",
                    (Track_performer, Track_title, Track_id, Track_Unique))
            db.commit()
            bot.send_message(message.chat.id, Track_performer + " - " + Track_title + " - Трек сохранен ")
        db.close()
    except:
        MessageChatId = str(message.chat.id)
        db = sqlite3.connect('db/PlayList.db')
        Plist = db.cursor()
        Plist.execute("CREATE TABLE IF NOT EXISTS " + "pList_" + MessageChatId + """(
       Id INTEGER NOT NULL UNIQUE,
       Performer TEXT,
       Title TEXT,
       FileId TEXT,
       UniqueId TEXT,
       PRIMARY KEY("Id" AUTOINCREMENT)
       );
        """)
        db.commit()
        track = str(message.audio.file_unique_id)
        Track_performer = message.audio.performer
        Track_title = message.audio.title
        isNew = True
        UniqueId_list = []
        for UniqueId in Plist.execute('SELECT UniqueId FROM pList_' + MessageChatId + '  WHERE UniqueId LIKE ?',
                                      ('%' + track + '%',)):
            UniqueId_list.append(UniqueId[0])
            UniqueId_list1 = UniqueId_list[0]
            if str(UniqueId_list1) == str(message.audio.file_unique_id):
                isNew = False
                bot.send_message(message.chat.id, Track_performer + " - " + Track_title + " - Такой трек уже есть ")

        if isNew == True:
            Track_id = message.audio.file_id
            Track_Unique = message.audio.file_unique_id
            db.execute(
                "INSERT INTO " + "pList_" + MessageChatId + " (Performer, Title, FileId, UniqueId) VALUES (?, ?, ?, ?);",
                (Track_performer, Track_title, Track_id, Track_Unique))
            db.commit()
            bot.send_message(message.chat.id, Track_performer + " - " + Track_title + " - Трек сохранен ")
        db.close()


def PlayList(message):
    try:
        MessageChatId = str(message.chat.id)
        MessageGroupId = MessageChatId.split('-', 1)[1]
        db = sqlite3.connect('db/PlayList.db')
        Plist = db.cursor()
        for s1 in Plist.execute("SELECT FileId FROM " + "pList_" + MessageGroupId):
            audioo = s1[0]
            bot.send_audio(chat_id=message.chat.id, audio=audioo)
        db.close()
    except:
        db = sqlite3.connect('db/PlayList.db')
        Plist = db.cursor()
        for s1 in Plist.execute("SELECT FileId FROM " + "pList_" + MessageChatId):
            audioo = s1[0]
            bot.send_audio(chat_id=message.chat.id, audio=audioo)
        db.close()