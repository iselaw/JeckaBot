import random
import sqlite3
from time import sleep

from telebot import types

from Login import bot
from statistic import updateStatistic


class SlotMachine:

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
    def updateScore(bet, point, message):
        isBankrupt = False
        balance = SlotMachine.getBalance(message)
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
    def slotMachine(message, betValue):
        bet = betValue
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
        itog = slot1 + slot2 + slot3
        if slot1 == slot2 == slot3:
            if slot1 == "💰":
                point = bet * 100
            if slot1 == "🍌":
                point = bet * 10
            if slot1 == "🍋":
                point = bet * 5
            if slot1 == "🍒":
                point = bet * 3
            isBankrupt, balance = SlotMachine.updateScore(bet, point, message)
            if not isBankrupt:
                itog = "Ты выиграл \n{}".format(itog) + "\n" + "Баланс: " + str(balance) + "(+" + str(
                    point) + ")"
            else:
                itog = "bankrupt"
        else:
            point = bet * (-1)
            isBankrupt, balance = SlotMachine.updateScore(bet, point, message)
            if not isBankrupt:
                itog = "Увы, но ты проиграл \n{}".format(itog) + "\n" + "Баланс: " + str(balance) + "(" + str(
                    point) + ")"
            else:
                itog = "bankrupt"
        return itog

    @staticmethod
    def SlotBet(message, itog, res=False):
        keykazino = types.InlineKeyboardMarkup()
        key_bet10 = types.InlineKeyboardButton(text='Ставка 10', callback_data='SlotBet10')
        keykazino.add(key_bet10)
        key_bet50 = types.InlineKeyboardButton(text='Ставка 50', callback_data='SlotBet50')
        keykazino.add(key_bet50)
        key_krutexit = types.InlineKeyboardButton(text='В другой раз', callback_data='krutkonec')
        keykazino.add(key_krutexit)
        if itog == "first":
            bot.send_message(message.chat.id, 'Сыграем ?', reply_markup=keykazino)
        elif itog == "bankrupt":
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                  text="К сожалению, твой баланс не позволяет сделать ставку")
        else:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                  text=itog)
            sleep(0.5)
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                  text=itog, reply_markup=keykazino)

    @staticmethod
    def sm_handler(call):
        if call.data == "SlotMachine":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбрано: Слот-машина\nВаш баланс: " + str(SlotMachine.getBalance(call.message)))
            SlotMachine.SlotBet(call.message, "first")
            updateStatistic(call.message, "SlotMachine")
        elif call.data == "SlotBet10":
            itog = SlotMachine.slotMachine(call.message, 10)
            SlotMachine.SlotBet(call.message, itog)
        elif call.data == "SlotBet50":
            itog = SlotMachine.slotMachine(call.message, 50)
            SlotMachine.SlotBet(call.message, itog)
