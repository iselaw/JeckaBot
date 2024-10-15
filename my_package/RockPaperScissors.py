import random
import sqlite3

from telebot import types

from Login import bot
from my_package.Admin import Admin


class RockPaperScissors:

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
    def update_score(point, message):
        balance = RockPaperScissors.get_balance(message)
        balance = balance + point
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        cur.execute("UPDATE Users SET balance = " + str(balance) + " WHERE userId = " + str(message.chat.id))
        db.commit()
        db.close()
        return balance

    @staticmethod
    def game_rps(message, result):
        keygame1 = types.InlineKeyboardMarkup()
        key_Stone = types.InlineKeyboardButton(text='Камень🤜', callback_data='Stone')
        keygame1.add(key_Stone)
        key_Scissors = types.InlineKeyboardButton(text='Ножницы✌️', callback_data='Scissors')
        keygame1.add(key_Scissors)
        key_Paper = types.InlineKeyboardButton(text='Бумага✋', callback_data='Paper')
        keygame1.add(key_Paper)
        key_gameexit = types.InlineKeyboardButton(text='В другой раз', callback_data='gameexit')
        keygame1.add(key_gameexit)
        if result == "first":
            bot.send_message(message.chat.id, "Играем?", reply_markup=keygame1)
        else:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                  text=result, reply_markup=keygame1)

    @staticmethod
    def rps_handler(call):
        if call.data == "Scissors":
            choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
            Scissors = 'Ножницы✌️'
            if Scissors == choice:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Боевая ничья!')
                result = "Боевая ничья!"
            else:
                if choice == 'Бумага✋':
                    balance = RockPaperScissors.update_score(20, call.message)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Поздравляю с победой! У меня была {}.'.format(
                                              choice) + '\nВаш баланс: ' + str(
                                              balance) + '(+20)')
                    result = 'Поздравляю с победой! У меня была {}.'.format(choice) + '\nВаш баланс: ' + str(
                        balance) + '(+20)'
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Извините, но Вы проиграли 😢. У меня  {}.'.format(
                                              choice))
                    result = 'Извините, но Вы проиграли 😢. У меня  {}.'.format(choice)
            RockPaperScissors.game_rps(call.message, result)
        elif call.data == "Stone":
            choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
            Stone = 'Камень🤜'
            if Stone == choice:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Боевая ничья!')
                result = "Боевая ничья!"
            else:
                if choice == 'Ножницы✌️':
                    balance = RockPaperScissors.update_score(20, call.message)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Поздравляю с победой! У меня была {}.'.format(
                                              choice) + '\nВаш баланс: ' + str(
                                              balance) + '(+20)' + '\nВаш баланс: ' + balance + '(+20)')
                    result = 'Поздравляю с победой! У меня была {}.'.format(choice) + '\nВаш баланс: ' + str(
                        balance) + '(+20)'
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Извините, но Вы проиграли 😢. У меня  {}.'.format(choice))
                    result = 'Извините, но Вы проиграли 😢. У меня  {}.'.format(choice)
            RockPaperScissors.game_rps(call.message, result)
        elif call.data == "Paper":
            choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
            Paper = 'Бумага✋'
            if Paper == choice:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Боевая ничья!')
                result = "Боевая ничья!"
            else:
                if choice == 'Камень🤜':
                    balance = RockPaperScissors.update_score(20, call.message)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Поздравляю с победой! У меня была {}.'.format(
                                              choice) + '\nВаш баланс: ' + str(balance) + '(+20)')
                    result = 'Поздравляю с победой! У меня была {}.'.format(choice) + '\nВаш баланс: ' + str(
                        balance) + '(+20)'
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Извините, но Вы проиграли 😢. У меня  {}.'.format(
                                              choice))
                    result = 'Извините, но Вы проиграли 😢. У меня  {}.'.format(choice)
            RockPaperScissors.game_rps(call.message, result)
        elif call.data == "gameexit":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Приходи еще")
        elif call.data == "game_rps":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбрано: Камень, Ножницы, Бумага\nВаш баланс: " + str(
                                      RockPaperScissors.get_balance(call.message)))
            RockPaperScissors.game_rps(call.message, "first")
            Admin.update_statistic(call.message, "game_rps")
