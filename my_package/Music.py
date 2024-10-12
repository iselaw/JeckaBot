import sqlite3

from fuzzywuzzy import fuzz
from telebot import types
from telebot.types import InputMediaAudio

from Login import *


class Music:

    @staticmethod
    def audio_processing(message, isFirstAudio):
        key_like = types.InlineKeyboardButton(text='❤', callback_data='audioLike')
        key_nextTrack = types.InlineKeyboardButton(text='>>>', callback_data='audionext')
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(key_like)
        keyboard.add(key_nextTrack)
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for rand in cur.execute('SELECT * FROM Music WHERE ID IN (SELECT ID FROM Music ORDER BY RANDOM() LIMIT 1)'):
            audioo = rand[5]
            Music.nextAudio(message, audioo, keyboard, isFirstAudio)
        db.close()

    @staticmethod
    def nextAudio(message, audioo, keyboard, isFirstAudio):
        if not isFirstAudio:
            bot.edit_message_media(chat_id=message.chat.id, message_id=message.message_id, media=InputMediaAudio(audioo),
                                   reply_markup=keyboard)
        if isFirstAudio:
            bot.send_audio(chat_id=message.chat.id, audio=audioo, reply_markup=keyboard)

    @staticmethod
    def LikePlayList(message):
        try:
            MessageChatId = str(message.chat.id)
            MessageGroupId = MessageChatId.split('-', 1)[1]
            db = sqlite3.connect('../resources/db/PlayList.db')
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

            if isNew:
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
            db = sqlite3.connect('../resources/db/PlayList.db')
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
            if isNew:
                Track_id = message.audio.file_id
                Track_Unique = message.audio.file_unique_id
                db.execute(
                    "INSERT INTO " + "pList_" + MessageChatId + " (Performer, Title, FileId, UniqueId) VALUES (?, ?, ?, ?);",
                    (Track_performer, Track_title, Track_id, Track_Unique))
                db.commit()
                bot.send_message(message.chat.id, Track_performer + " - " + Track_title + " - Трек сохранен ")
            db.close()

    @staticmethod
    def PlayList(message):
        try:
            MessageChatId = str(message.chat.id)
            MessageGroupId = MessageChatId.split('-', 1)[1]
            db = sqlite3.connect('../resources/db/PlayList.db')
            Plist = db.cursor()
            try:
                for s1 in Plist.execute("SELECT FileId FROM " + "pList_" + MessageGroupId):
                    audioo = s1[0]
                    bot.send_audio(chat_id=message.chat.id, audio=audioo)
            except:
                bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                      text="Ваш плейлист пуст")
            db.close()
        except:
            db = sqlite3.connect('../resources/db/PlayList.db')
            Plist = db.cursor()
            try:
                for s1 in Plist.execute("SELECT FileId FROM " + "pList_" + MessageChatId):
                    audioo = s1[0]
                    bot.send_audio(chat_id=message.chat.id, audio=audioo)
            except:
                bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                      text="Ваш плейлист пуст")
            db.close()

    @staticmethod
    def audio_record(message, musicList):
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        track = str(message.audio.file_unique_id)
        Track_performer = message.audio.performer
        Track_title = message.audio.title
        isNew = True
        UniqueId_list = []
        for UniqueId in cur.execute('SELECT UniqueId FROM Music WHERE UniqueId LIKE ?', ('%' + track + '%',)):
            UniqueId_list.append(UniqueId[0])
            UniqueId_list1 = UniqueId_list[0]
            if str(UniqueId_list1) == str(message.audio.file_unique_id):
                isNew = False
                bot.send_message(message.chat.id, Track_performer + " - " + Track_title + " - Такой трек уже есть ")

        if isNew:
            Track_id = message.audio.file_id
            Track_Unique = message.audio.file_unique_id
            Track_Name = message.audio.file_name
            db.execute("INSERT INTO Music (Name, Performer, Title, UniqueId, FileId) VALUES (?, ?, ?, ?, ?);",
                       (Track_Name, Track_performer, Track_title, Track_Unique, Track_id))
            db.commit()
            bot.send_message(message.chat.id, Track_performer + " - " + Track_title + " - Трек сохранен ")
            musicList.append(Track_performer + Track_title)
        db.close()

    @staticmethod
    def audio_text_set(message, musicList):
        if 'включи ' in message.text.lower():
            maximumSimilarity = 0
            maxMusicName = ''
            varFileId = ''
            index = message.text.lower().find("включи ")
            musicName = (message.text.lower())[index:]
            for q in musicList:
                degreeOfSimilarity = (fuzz.token_sort_ratio(musicName, q))
                if degreeOfSimilarity > maximumSimilarity:
                    maximumSimilarity = degreeOfSimilarity
                    maxMusicName = q
            if maximumSimilarity == 0:
                bot.send_message(message.chat.id, 'Прости, я не смог найти в библиотеке ничего подходящего')
            else:
                db = sqlite3.connect('../resources/db/JeckaBot.db')
                cur = db.cursor()
                for s in cur.execute("SELECT FileId FROM Music where Performer||Title=" + "'" + maxMusicName + "'"):
                    varFileId = s[0]
                db.close()
                bot.send_audio(chat_id=message.chat.id, audio=varFileId)

    @staticmethod
    def music_handler(call):
        if call.data == "audionext":
            Music.audio_processing(call.message, False)
        elif call.data == "musicStart":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="А вот и музыка")
            Music.audio_processing(call.message, True)
        elif call.data == "audioLike":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text='Готово')
            Music.LikePlayList(call.message)
        elif call.data == "musicList":
            Music.PlayList(call.message)