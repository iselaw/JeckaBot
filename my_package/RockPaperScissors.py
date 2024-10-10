import random
import sqlite3

from telebot import types

from Login import bot
from statistic import updateStatistic


class RockPaperScissors:

    @staticmethod
    def getBalance(message):
        balance = 0
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT balance FROM Users where userId=" + str(message.chat.id)):
            balance = x[0]
        db.close()
        return balance

    @staticmethod
    def updateScore(point, message):
        balance = RockPaperScissors.getBalance(message)
        balance = balance + point
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        cur.execute("UPDATE Users SET balance = " + str(balance) + " WHERE userId = " + str(message.chat.id))
        db.commit()
        db.close()
        return balance

    @staticmethod
    def GameSSP(message, itog, res=False):
        keygame1 = types.InlineKeyboardMarkup()
        key_Stone = types.InlineKeyboardButton(text='Камень🤜', callback_data='Stone')
        keygame1.add(key_Stone)
        key_Scissors = types.InlineKeyboardButton(text='Ножницы✌️', callback_data='Scissors')
        keygame1.add(key_Scissors)
        key_Paper = types.InlineKeyboardButton(text='Бумага✋', callback_data='Paper')
        keygame1.add(key_Paper)
        key_gameexit = types.InlineKeyboardButton(text='В другой раз', callback_data='gameexit')
        keygame1.add(key_gameexit)
        if itog == "first":
            bot.send_message(message.chat.id, "Играем?", reply_markup=keygame1)
        else:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                  text=itog, reply_markup=keygame1)

    @staticmethod
    def rps_handler(call):
        if call.data == "Scissors":
            choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
            Scissors = 'Ножницы✌️'
            if Scissors == choice:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Боевая ничья!')
                itog = "Боевая ничья!"
            else:
                if choice == 'Бумага✋':
                    balance = RockPaperScissors.updateScore(20, call.message)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Поздравляю с победой! У меня была {}.'.format(
                                              choice) + '\nВаш баланс: ' + str(
                                              balance) + '(+20)')
                    itog = 'Поздравляю с победой! У меня была {}.'.format(choice) + '\nВаш баланс: ' + str(
                        balance) + '(+20)'
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Извините, но Вы проиграли 😢. У меня  {}.'.format(
                                              choice))
                    itog = 'Извините, но Вы проиграли 😢. У меня  {}.'.format(choice)
            RockPaperScissors.GameSSP(call.message, itog)
        elif call.data == "Stone":
            choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
            Stone = 'Камень🤜'
            if Stone == choice:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Боевая ничья!')
                itog = "Боевая ничья!"
            else:
                if choice == 'Ножницы✌️':
                    balance = RockPaperScissors.updateScore(20, call.message)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Поздравляю с победой! У меня была {}.'.format(
                                              choice) + '\nВаш баланс: ' + str(
                                              balance) + '(+20)' + '\nВаш баланс: ' + balance + '(+20)')
                    itog = 'Поздравляю с победой! У меня была {}.'.format(choice) + '\nВаш баланс: ' + str(
                        balance) + '(+20)'
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Извините, но Вы проиграли 😢. У меня  {}.'.format(choice))
                    itog = 'Извините, но Вы проиграли 😢. У меня  {}.'.format(choice)
            RockPaperScissors.GameSSP(call.message, itog)
        elif call.data == "Paper":
            choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
            Paper = 'Бумага✋'
            if Paper == choice:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Боевая ничья!')
                itog = "Боевая ничья!"
            else:
                if choice == 'Камень🤜':
                    balance = RockPaperScissors.updateScore(20, call.message)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Поздравляю с победой! У меня была {}.'.format(
                                              choice) + '\nВаш баланс: ' + str(balance) + '(+20)')
                    itog = 'Поздравляю с победой! У меня была {}.'.format(choice) + '\nВаш баланс: ' + str(
                        balance) + '(+20)'
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Извините, но Вы проиграли 😢. У меня  {}.'.format(
                                              choice))
                    itog = 'Извините, но Вы проиграли 😢. У меня  {}.'.format(choice)
            RockPaperScissors.GameSSP(call.message, itog)
        elif call.data == "gameexit":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Приходи еще")
        elif call.data == "GameSSP":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбрано: Камень, Ножницы, Бумага\nВаш баланс: " + str(
                                      RockPaperScissors.getBalance(call.message)))
            RockPaperScissors.GameSSP(call.message, "first")
            updateStatistic(call.message, "GameSSP")
