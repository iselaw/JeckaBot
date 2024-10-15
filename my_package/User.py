import sqlite3

from telebot import types

from Login import bot
from my_package.Admin import Admin


class User:

    @staticmethod
    def get_balance(message):
        balance = 0
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT balance FROM Users where userId=" + str(message.chat.id)):
            balance = x[0]
        db.close()
        return balance

    @staticmethod
    def settings_menu(message):
        muteStatus = 2
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT mute FROM Users WHERE userId=" + str(message.chat.id)):
            muteStatus = x[0]
        db.close()
        settings_menu = types.InlineKeyboardMarkup()
        if muteStatus == 0:
            key_silence = types.InlineKeyboardButton(text='Установить мут', callback_data='silence')
        else:
            key_silence = types.InlineKeyboardButton(text='Снять мут', callback_data='silence')
        settings_menu.add(key_silence)
        bot.send_message(message.chat.id, 'Доступные тебе настройки', reply_markup=settings_menu)
        Admin.admin_notification(message, "Вызвал панель настроек")

    @staticmethod
    def game_menu(message):
        keygame = types.InlineKeyboardMarkup()
        key_Game0 = types.InlineKeyboardButton(text='Кто хочет стать миллионером?', callback_data='millionaire')
        keygame.add(key_Game0)
        key_Game1 = types.InlineKeyboardButton(text='Камень,Ножницы,Бумага', callback_data='game_rps')
        keygame.add(key_Game1)
        key_Game2 = types.InlineKeyboardButton(text='Слот-машина', callback_data='SlotMachine')
        keygame.add(key_Game2)
        key_Game3 = types.InlineKeyboardButton(text='Блекджек', callback_data='BlackJack')
        keygame.add(key_Game3)
        key_Quest = types.InlineKeyboardButton(text='Путешествие Жеки', callback_data='Quest')
        keygame.add(key_Quest)
        key_StatGame = types.InlineKeyboardButton(text='Статистика', callback_data='StatGame')
        keygame.add(key_StatGame)
        bot.send_message(message.chat.id, 'Во что сыграем?\nВаш Баланс: ' + str(User.get_balance(message)),
                         reply_markup=keygame)
        Admin.admin_notification(message, "Пошел играть")
        Admin.update_statistic(message, "game")

    @staticmethod
    def apps_menu(message):
        apps_menu = types.InlineKeyboardMarkup()
        key_game = types.InlineKeyboardButton(text='Играть', callback_data='game')
        key_music = types.InlineKeyboardButton(text='Музыка', callback_data='music')
        key_weather = types.InlineKeyboardButton(text='Погода', callback_data='weather')
        key_horoscope = types.InlineKeyboardButton(text='Гороскоп', callback_data='horoscope')
        key_para = types.InlineKeyboardButton(text='Поиск любви', callback_data='love_search')
        apps_menu.row(key_game, key_weather)
        apps_menu.row(key_music, key_horoscope)
        apps_menu.row(key_para)
        bot.send_message(message.chat.id, 'Чем желаешь заняться?', reply_markup=apps_menu)
        Admin.admin_notification(message, "Вызвал панель приложений")

    def get_statistic(call):
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        try:
            cur.execute(
                "UPDATE Users SET (nickname) = '" + str(call.message.chat.first_name) + "'" + " WHERE userId = " + str(
                    call.message.chat.id))
            db.commit()
        except:
            print("error update nickname")
        static = []
        staticMessage = ""
        for x in cur.execute(
                "Select count(*) from users where balance>5000 and active=1"):
            amount = x[0]
        if amount >= 10:
            for x in cur.execute(
                    "Select nickname, balance from users where balance>5000 and active=1 ORDER BY balance DESC Limit 10"):
                static.append(x[0])
                static.append(x[1])
        else:
            for x in cur.execute(
                    "Select nickname, balance from users where balance>5000 ORDER BY balance DESC Limit 10"):
                static.append(x[0])
                static.append(x[1])
        count = 0
        while count < 20:
            if count % 2 == 0:
                staticMessage = staticMessage + str((count + 1) // 2 + 1) + ". " + str(static[count])
            else:
                staticMessage = staticMessage + ": " + str(static[count]) + '\n'
            count = count + 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Самые успешные люди:\n" + staticMessage)
        db.close()

    @staticmethod
    def mute_tumbler(message):
        muteStatus = 3
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT mute FROM Users WHERE userId=" + str(message.chat.id)):
            muteStatus = x[0]
        db.close()
        if muteStatus == 0:
            User.mute(message)
        else:
            User.un_mute(message)

    @staticmethod
    def mute(message):
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        cur.execute("UPDATE Users SET mute = 1 WHERE userId = " + str(message.chat.id))
        db.commit()
        db.close()
        bot.send_message(message.chat.id, 'Хорошо, помолчим. Если захочешь поболтать, введи /on')
        Admin.admin_notification(message, "Замутил бота")

    @staticmethod
    def un_mute(message):
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        cur.execute("UPDATE Users SET mute = 0 WHERE userId = " + str(message.chat.id))
        db.commit()
        db.close()
        bot.send_message(message.chat.id, 'Привет, мы снова можем поболтать')
        Admin.admin_notification(message, "Размутил бота")

    @staticmethod
    def insert_user_id(message, standard_point):
        UserId = 0
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        si = str(message.from_user.first_name)
        sz = message.chat.id
        for s in cur.execute("SELECT * FROM Users WHERE userId =" + str(sz)):
            UserId = s[0]
        if UserId == 0:
            cur.execute("INSERT INTO Users (userId, nickname, balance, active) VALUES (?, ?, ?, ?);",
                        (sz, f"{si}", standard_point, 1))
            db.commit()
        db.close()

    @staticmethod
    def user_handler(call):
        if call.data == "StatGame":
            User.get_statistic(call)
            Admin.update_statistic(call.message, "StatGame")
        elif call.data == "silence":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            User.mute_tumbler(call.message)