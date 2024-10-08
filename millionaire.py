import random
import sqlite3
from time import sleep

from telebot import types
from Login import *
from OthersGameMethods import *


def startMillionaire(message, balance, isStarting, messageId, res=False):
    if isStarting == True:
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
    Question = randomQuestion(message, balance, int(milMas[2]))
    if messageId == 0:
        bot.send_message(chat_id=message.chat.id, text=Question, reply_markup=keyboard)
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=messageId,
                              text=Question, reply_markup=keyboard)


def randomQuestion(message, balance, numberQuestion, res=False):
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    id = 0
    question = ''
    for rand in cur.execute(
            'SELECT id, question FROM Question WHERE id IN (SELECT ID FROM Question ORDER BY RANDOM() LIMIT 1)'):
        id = rand[0]
        question = rand[1]
    db.close()
    x = open('millionaire//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
    x.write(str(balance) + '\n' + str(id) + '\n' + str(numberQuestion))
    x.close()
    return question


def winMillionaire(message, res=False):
    isWin = False
    milMas = []
    ff = open('millionaire//player' + str(message.chat.id) + '.txt', 'r', encoding='UTF-8')
    for s in ff:
        milMas.append(s.strip().lower())
    ff.close()
    if int(milMas[2]) == 10:
        isWin = True
    return isWin


def checkAnswer(message, code, res=False):
    milMas = []
    answer = 0
    isTrueAnswer = False
    ff = open('millionaire//player' + str(message.chat.id) + '.txt', 'r', encoding='UTF-8')
    for s in ff:
        milMas.append(s.strip().lower())
    ff.close()
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    for rand in cur.execute(
            'SELECT answer FROM Question WHERE id = ' + milMas[1]):
        answer = rand[0]
    db.close()
    if answer == code:
        isTrueAnswer = True
    return isTrueAnswer


def resultMillionaire(call, isTrueAnswer, res=False):
    if isTrueAnswer == False:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Неправильный ответ :(")
        sleep(3)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        millionaire(call.message)
    else:
        isWin = winMillionaire(call.message)
        if isWin == False:
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
            startMillionaire(call.message, int(milMas[0]) + 100000, False, call.message.message_id)
        else:
            Balance = getBalance(call.message)
            db = sqlite3.connect('db/JeckaBot.db')
            cur = db.cursor()
            cur.execute(
                "UPDATE Users SET balance = " + str(Balance + 500) + " WHERE userId = " + str(call.message.chat.id))
            db.commit()
            db.close()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Правильный ответ!" + '\n' + "Выигрыш: " + str(1000000) + "$")
            sleep(2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Поздравляю! Вы ответили правильно на все 10 вопросов." + '\n' + "В качестве приза Вы получаете 500 очков на баланс" + '\n' + "Баланс: " + str(
                                      Balance + 500) + " (+500)")
            x = open('millionaire//player' + str(call.message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write("0" + '\n' + "0" + '\n' + "1")
            x.close()
            sleep(4)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            millionaire(call.message)


def millionaire(message, res=False):
    keygame = types.InlineKeyboardMarkup()
    key_startgame = types.InlineKeyboardButton(text='Начать игру', callback_data='startMillionaire')
    keygame.add(key_startgame)
    bot.send_message(chat_id=message.chat.id, text='Ну что, начнём зарабатывать умом?', reply_markup=keygame)

