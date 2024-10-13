import random
import sqlite3
from time import sleep

from telebot import types

from Login import bot
from my_package.Admin import Admin


class SlotMachine:

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
        balance = SlotMachine.get_balance(message)
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
    def slotMachine(message, bet_value):
        bet = bet_value
        slot1 = ""
        slot2 = ""
        slot3 = ""
        point = 0
        randSlot = random.randint(0, 100)
        if randSlot <= 20:
            slot1 = "💰"
        elif randSlot <= 43:
            slot1 = "🍌"
        elif randSlot <= 71:
            slot1 = "🍋"
        elif randSlot > 71:
            slot1 = "🍒"
        randSlot = random.randint(0, 100)
        if randSlot <= 20:
            slot2 = "💰"
        elif randSlot <= 43:
            slot2 = "🍌"
        elif randSlot <= 71:
            slot2 = "🍋"
        elif randSlot > 71:
            slot2 = "🍒"
        randSlot = random.randint(0, 100)
        if randSlot <= 20:
            slot3 = "💰"
        elif randSlot <= 43:
            slot3 = "🍌"
        elif randSlot <= 71:
            slot3 = "🍋"
        elif randSlot > 71:
            slot3 = "🍒"
        result = slot1 + slot2 + slot3
        if slot1 == slot2 == slot3:
            if slot1 == "💰":
                point = bet * 100
            if slot1 == "🍌":
                point = bet * 10
            if slot1 == "🍋":
                point = bet * 5
            if slot1 == "🍒":
                point = bet * 3
            isBankrupt, balance = SlotMachine.update_score(bet, point, message)
            if not isBankrupt:
                result = "Ты выиграл \n{}".format(result) + "\n" + "Баланс: " + str(balance) + "(+" + str(
                    point) + ")"
            else:
                result = "bankrupt"
        else:
            point = bet * (-1)
            isBankrupt, balance = SlotMachine.update_score(bet, point, message)
            if not isBankrupt:
                result = "Увы, но ты проиграл \n{}".format(result) + "\n" + "Баланс: " + str(balance) + "(" + str(
                    point) + ")"
            else:
                result = "bankrupt"
        return result

    @staticmethod
    def SlotBet(message, result):
        key_casino = types.InlineKeyboardMarkup()
        key_bet10 = types.InlineKeyboardButton(text='Ставка 10', callback_data='SlotBet10')
        key_casino.add(key_bet10)
        key_bet50 = types.InlineKeyboardButton(text='Ставка 50', callback_data='SlotBet50')
        key_casino.add(key_bet50)
        key_slot_exit = types.InlineKeyboardButton(text='В другой раз', callback_data='slot_exit')
        key_casino.add(key_slot_exit)
        if result == "first":
            bot.send_message(message.chat.id, 'Сыграем ?', reply_markup=key_casino)
        elif result == "bankrupt":
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                  text="К сожалению, твой баланс не позволяет сделать ставку")
        else:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                  text=result)
            sleep(0.5)
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                  text=result, reply_markup=key_casino)

    @staticmethod
    def sm_handler(call):
        if call.data == "SlotMachine":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбрано: Слот-машина\nВаш баланс: " + str(SlotMachine.get_balance(call.message)))
            SlotMachine.SlotBet(call.message, "first")
            Admin.update_statistic(call.message, "SlotMachine")
        elif call.data == "SlotBet10":
            result = SlotMachine.slotMachine(call.message, 10)
            SlotMachine.SlotBet(call.message, result)
        elif call.data == "SlotBet50":
            result = SlotMachine.slotMachine(call.message, 50)
            SlotMachine.SlotBet(call.message, result)
        elif call.data == "slot_exit":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Приходи еще")