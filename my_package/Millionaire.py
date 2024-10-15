import sqlite3
from time import sleep

from telebot import types
from Login import *
from my_package.Admin import Admin


class Millionaire:

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
    def update_score(bet, point, message):
        isBankrupt = False
        balance = Millionaire.get_balance(message)
        if balance >= bet:
            balance = balance + point
            db = sqlite3.connect('../resources/db/JeckaBot.db')
            cur = db.cursor()
            cur.execute("UPDATE Users SET balance = " + str(balance) + " WHERE userId = " + str(message.chat.id))
            db.commit()
            db.close()
        else:
            isBankrupt = True
        return isBankrupt, balance

    @staticmethod
    def start_millionaire(message, balance, is_starting, message_id):
        if is_starting:
            x = open('millionaire//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write("0" + '\n' + "0" + '\n' + "1")
            x.close()
        milMas = []
        ff = open('millionaire//player' + str(message.chat.id) + '.txt', 'r', encoding='UTF-8')
        for s in ff:
            milMas.append(s.strip().lower())
        ff.close()
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyA = types.InlineKeyboardButton(text='A', callback_data='A')
        keyB = types.InlineKeyboardButton(text='B', callback_data='B')
        keyC = types.InlineKeyboardButton(text='C', callback_data='C')
        keyD = types.InlineKeyboardButton(text='D', callback_data='D')
        keyboard.row(keyA, keyB, keyC, keyD)
        Question = Millionaire.random_question(message, balance, int(milMas[2]))
        if message_id == 0:
            bot.send_message(chat_id=message.chat.id, text=Question, reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message_id,
                                  text=Question, reply_markup=keyboard)

    @staticmethod
    def random_question(message, balance, number_question):
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        id = 0
        question = ''
        for rand in cur.execute(
                'SELECT id, question FROM Question WHERE id IN (SELECT ID FROM Question ORDER BY RANDOM() LIMIT 1)'):
            id = rand[0]
            question = rand[1]
        db.close()
        x = open('millionaire//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
        x.write(str(balance) + '\n' + str(id) + '\n' + str(number_question))
        x.close()
        return question

    @staticmethod
    def win_millionaire(message):
        isWin = False
        milMas = []
        ff = open('millionaire//player' + str(message.chat.id) + '.txt', 'r', encoding='UTF-8')
        for s in ff:
            milMas.append(s.strip().lower())
        ff.close()
        if int(milMas[2]) == 10:
            isWin = True
        return isWin

    @staticmethod
    def check_answer(message, code):
        milMas = []
        answer = 0
        is_true_answer = False
        ff = open('millionaire//player' + str(message.chat.id) + '.txt', 'r', encoding='UTF-8')
        for s in ff:
            milMas.append(s.strip().lower())
        ff.close()
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for rand in cur.execute(
                'SELECT answer FROM Question WHERE id = ' + milMas[1]):
            answer = rand[0]
        db.close()
        if answer == code:
            is_true_answer = True
        return is_true_answer

    @staticmethod
    def result_millionaire(call, is_true_answer):
        if not is_true_answer:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Неправильный ответ :(")
            sleep(3)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Millionaire.millionaire_start(call.message)
        else:
            isWin = Millionaire.win_millionaire(call.message)
            if not isWin:
                milMas = []
                ff = open('millionaire//player' + str(call.message.chat.id) + '.txt', 'r', encoding='UTF-8')
                for s in ff:
                    milMas.append(s.strip().lower())
                ff.close()
                x = open('millionaire//player' + str(call.message.chat.id) + '.txt', 'w', encoding='UTF-8')
                x.write(str(int(milMas[0]) + 100000) + '\n' + milMas[1] + '\n' + str(int(milMas[2]) + 1))
                x.close()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Правильный ответ!" + '\n' + "Выигрыш: " + str(
                                          int(milMas[0]) + 100000) + "$")
                sleep(1)
                Millionaire.start_millionaire(call.message, int(milMas[0]) + 100000, False, call.message.message_id)
            else:
                balance = Millionaire.get_balance(call.message)
                db = sqlite3.connect('../resources/db/JeckaBot.db')
                cur = db.cursor()
                cur.execute(
                    "UPDATE Users SET balance = " + str(balance + 500) + " WHERE userId = " + str(call.message.chat.id))
                db.commit()
                db.close()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Правильный ответ!" + '\n' + "Выигрыш: " + str(1000000) + "$")
                sleep(2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Поздравляю! Вы ответили правильно на все 10 вопросов." + '\n' + "В качестве приза Вы получаете 500 очков на баланс" + '\n' + "Баланс: " + str(
                                          balance + 500) + " (+500)")
                x = open('millionaire//player' + str(call.message.chat.id) + '.txt', 'w', encoding='UTF-8')
                x.write("0" + '\n' + "0" + '\n' + "1")
                x.close()
                sleep(4)
                bot.delete_message(call.message.chat.id, call.message.message_id)
                Millionaire.millionaire_start(call.message)

    @staticmethod
    def millionaire_start(message):
        keygame = types.InlineKeyboardMarkup()
        key_startgame = types.InlineKeyboardButton(text='Начать игру', callback_data='start_millionaire')
        keygame.add(key_startgame)
        bot.send_message(chat_id=message.chat.id, text='Ну что, начнём зарабатывать умом?', reply_markup=keygame)

    @staticmethod
    def millionaire_handler(call):
        if call.data == "millionaire":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Millionaire.millionaire_start(call.message)
            Admin.update_statistic(call.message, "millionaire")
        elif call.data == "start_millionaire":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Millionaire.start_millionaire(call.message, 0, True, 0)
        elif call.data == "A":
            is_true_answer = Millionaire.check_answer(call.message, 1)
            Millionaire.result_millionaire(call, is_true_answer)
        elif call.data == "B":
            is_true_answer = Millionaire.check_answer(call.message, 2)
            Millionaire.result_millionaire(call, is_true_answer)
        elif call.data == "C":
            is_true_answer = Millionaire.check_answer(call.message, 3)
            Millionaire.result_millionaire(call, is_true_answer)
        elif call.data == "D":
            is_true_answer = Millionaire.check_answer(call.message, 4)
            Millionaire.result_millionaire(call, is_true_answer)