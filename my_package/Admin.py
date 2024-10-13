import sqlite3
from telebot import types
from Login import bot, admin


class Admin:

    @staticmethod
    def adminNotification(message, text):
        isAdmin = False
        for x in admin:
            if message.chat.id == x:
                isAdmin = True
        if not isAdmin:
            for x in admin:
                try:
                    bot.send_message(x, message.chat.first_name + " - " + text)
                except:
                    bot.send_message(x, message.chat.title + " - " + text)

    @staticmethod
    def updateStatistic(message, button):
        isAdmin = False
        for x in admin:
            if message.chat.id == x:
                isAdmin = True
        if not isAdmin:
            db = sqlite3.connect('../resources/db/JeckaBot.db')
            cur = db.cursor()
            cur.execute(
                "UPDATE Statistic SET count=count+1 where button= " + "'" + button + "'")
            db.commit()
            db.close()

    @staticmethod
    def getStatistic(message):
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                              text="Загрузка...")
        number_of_elements = 0
        number_of_elements1 = 0
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT COUNT(id) FROM Users WHERE active=1"):
            number_of_elements = x[0]
        db.close()
        statistic = "❕ Информация:\n\nАктивных чатов в боте - " + str(number_of_elements)
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT COUNT(id) FROM Users WHERE active=0"):
            number_of_elements1 = x[0]
        db.close()
        statistic = statistic + '\n' + "Неактивных чатов в боте - " + str(
            number_of_elements1) + '\n' + "Всего чатов: " + str(
            number_of_elements + number_of_elements1) + '\n\n' + "Статистика по кнопкам" + '\n'
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT namebutton, count FROM Statistic Order by count desc"):
            statistic = statistic + x[0] + ': ' + str(x[1]) + '\n'
        db.close()
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                              text=statistic)

    def cancelButton(message):
        keyCancel = types.InlineKeyboardMarkup()  # наша клавиатура
        key_cancel = types.InlineKeyboardButton(text='Отменить операцию', callback_data='cancel')  # кнопка «Да»
        keyCancel.add(key_cancel)  # добавляем кнопку в клавиатуру
        bot.send_message(message.chat.id, "Нажмите, если хотите отменить операцию", reply_markup=keyCancel)

    @staticmethod
    def push(text):
        userValue = 0
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT COUNT(id) FROM Users WHERE active=1 OR active=0"):
            userValue = x[0]
        db.close()
        count = 1
        s = 1
        print(userValue)
        while count <= userValue:
            db = sqlite3.connect('../resources/db/JeckaBot.db')
            cur = db.cursor()
            for s1 in cur.execute("SELECT userId FROM Users where id=" + str(count)):
                s = s1[0]
            db.close()
            try:
                bot.send_message(s, text)
                db = sqlite3.connect('../resources/db/JeckaBot.db')
                cur = db.cursor()
                cur.execute("UPDATE Users SET active = 1 WHERE id = " + str(count))
                db.commit()
                db.close()
                print('отправлено')
            except:
                db = sqlite3.connect('../resources/db/JeckaBot.db')
                cur = db.cursor()
                cur.execute("UPDATE Users SET active = 0 WHERE id = " + str(count))
                db.commit()
                db.close()
                print('Не отправлено')
            count = count + 1

    @staticmethod
    def admin_handler(call):
        if call.data == "cancel":
            global isPush
            isPush = False
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Операция отменена")
        elif call.data == "spam":
            global pushAdmin
            pushAdmin = str(call.message.chat.id)
            isPush = True
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Введите текст который хотите отправить")
            Admin.cancelButton(call.message)
        elif call.data == "stat":
            Admin.getStatistic(call.message)
