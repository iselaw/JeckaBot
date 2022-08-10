import random
import sqlite3
from time import sleep

from telebot import types
from Login import *
from OthersGameMethods import *


def BJBet(message, itog, res=False):
    keyBJ = types.InlineKeyboardMarkup()
    key_BJbet50 = types.InlineKeyboardButton(text='Ставка 50', callback_data='BlackJack50')
    keyBJ.add(key_BJbet50)
    key_BJbet100 = types.InlineKeyboardButton(text='Ставка 100', callback_data='BlackJack100')
    keyBJ.add(key_BJbet100)
    key_BJbet200 = types.InlineKeyboardButton(text='Ставка 200', callback_data='BlackJack200')
    keyBJ.add(key_BJbet200)
    key_BJexit = types.InlineKeyboardButton(text='Вдругой раз', callback_data='krutkonec')
    keyBJ.add(key_BJexit)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                          text=itog, reply_markup=keyBJ)


def BJGetCard(message, sum, itog, res=False):
    keyBJGetCard = types.InlineKeyboardMarkup()
    key_BJGetCardYes = types.InlineKeyboardButton(text='Еще карту', callback_data='GetCardYes')
    keyBJGetCard.add(key_BJGetCardYes)
    key_BJGetCardNo = types.InlineKeyboardButton(text='Хватит', callback_data='GetCardNo')
    keyBJGetCard.add(key_BJGetCardNo)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                          text='Сумма: ' + str(sum) + '\n' + itog + '\nЕще карту?', reply_markup=keyBJGetCard)
    sleep(2)

def BlackJackFirst(message, bet):
    isBankrot, Balance = updateScore(bet, -bet, message)
    playerScore = 0
    itog = ""
    if isBankrot == False:
        poolCard = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"]
        playerScore, itog = randomCard(poolCard, playerScore, itog)
        playerScore, itog = randomCard(poolCard, playerScore, itog)
        if playerScore == 21:
            isBankrot, Balance = updateScore(bet, 2 * bet, message)
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + "0" + '\n' + "0")
            x.close()
            BJBet(message,
                  'Ты выиграл, набрав ' + str(playerScore) + ' \n{}'.format(itog) + "\n" + "Баланс: " + str(
                      Balance) + "(+" + str(bet) + ")")
        else:
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + str(playerScore) + '\n' + itog)
            x.close()
            BJGetCard(message, playerScore, itog)
    else:
        BJBet(message, "К сожалению, Ваших средств недостаточно, чтобы сделать ставку")


def BlackJackNext(message, getCard):
    poolCard = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"]
    bjmas = []
    ff = open('bjSaves//player' + str(message.chat.id) + '.txt', 'r', encoding='UTF-8')
    for s in ff:
        bjmas.append(s.strip().lower())
    ff.close()
    bet = int(bjmas[0])
    playerScore = int(bjmas[1])
    itog = bjmas[2]
    if getCard == True:
        playerScore, itog = randomCard(poolCard, playerScore, itog)
        if playerScore == 21:
            isBankrot, Balance = updateScore(bet, 2 * bet, message)
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + "0" + '\n' + "0")
            x.close()
            BJBet(message,
                  'Ты выиграл, набрав ' + str(playerScore) + ' \n{}'.format(itog) + "\n" + "Баланс: " + str(
                      Balance) + "(+" + str(bet) + ")")
        if playerScore > 21:
            isBankrot, Balance = updateScore(bet, 0, message)
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + "0" + '\n' + "0")
            x.close()
            BJBet(message,
                  'Ты проиграл, набрав ' + str(playerScore) + ' \n{}'.format(itog) + "\n" + "Баланс: " + str(
                      Balance) + "(" + str(-bet) + ")")
        if playerScore < 21:
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + str(playerScore) + '\n' + itog)
            x.close()
            BJGetCard(message, playerScore, itog)
    if getCard == False:
        botItog = ""
        botScore = 0
        botScore, botItog = randomCard(poolCard, botScore, botItog)
        botScore, botItog = randomCard(poolCard, botScore, botItog)
        while botScore <= playerScore:
            botScore, botItog = randomCard(poolCard, botScore, botItog)
        if botScore > 21:
            isBankrot, Balance = updateScore(bet, 2 * bet, message)
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + "0" + '\n' + "0")
            x.close()
            BJBet(message, 'Ты выиграл, Жека-крупье набрал ' + str(botScore) + ' \n{}'.format(
                botItog) + "\n" + "Твой Баланс: " + str(
                Balance) + "(+" + str(bet) + ")")
        if botScore == playerScore:
            isBankrot, Balance = updateScore(bet, bet, message)
            x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
            x.write(str(bet) + '\n' + "0" + '\n' + "0")
            x.close()
            BJBet(message, 'Ничья, Жека-крупье набрал ' + str(botScore) + ' \n{}'.format(
                botItog) + "\n" + "Твой Баланс: " + str(
                Balance) + "(+" + str(0) + ")")
        if botScore > playerScore:
            if botScore <= 21:
                isBankrot, Balance = updateScore(bet, 0, message)
                x = open('bjSaves//player' + str(message.chat.id) + '.txt', 'w', encoding='UTF-8')
                x.write(str(bet) + '\n' + "0" + '\n' + "0")
                x.close()
                BJBet(message, 'Ты проиграл, Жека-крупье набрал ' + str(botScore) + ' \n{}'.format(
                    botItog) + "\n" + "Твой Баланс: " + str(
                    Balance) + "(-" + str(bet) + ")")


def randomCard(poolCard, playerScore, itog):
    randomCard = random.choice(poolCard)
    if randomCard == "a":
        if playerScore < 11:
            playerScore = playerScore + 11
            itog = itog + "🃏"
        else:
            playerScore = playerScore + 1
            itog = itog + "🃏"
    if randomCard == 10:
        playerScore = playerScore + randomCard
        itog = itog + "🔟"
    if randomCard == 9:
        playerScore = playerScore + randomCard
        itog = itog + "9️⃣"
    if randomCard == 8:
        playerScore = playerScore + randomCard
        itog = itog + "8️⃣"
    if randomCard == 7:
        playerScore = playerScore + randomCard
        itog = itog + "7️⃣"
    if randomCard == 6:
        playerScore = playerScore + randomCard
        itog = itog + "6️⃣"
    if randomCard == 5:
        playerScore = playerScore + randomCard
        itog = itog + "5️⃣"
    if randomCard == 4:
        playerScore = playerScore + randomCard
        itog = itog + "4️⃣"
    if randomCard == 3:
        playerScore = playerScore + randomCard
        itog = itog + "3️⃣"
    if randomCard == 2:
        playerScore = playerScore + randomCard
        itog = itog + "2️⃣"
    return playerScore, itog
