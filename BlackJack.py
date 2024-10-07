import sqlite3
import random
from time import sleep
from telebot import types
from Login import bot

class BlackJack:

    @staticmethod
    def getBalanceBJ(message):
        Balance = 0
        db = sqlite3.connect('db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT balance FROM Users where userId=" + str(message.chat.id)):
            Balance = x[0]
        db.close()
        return Balance

    @staticmethod
    def updateScoreBJ(bet, point, message):
        isBankrot = False
        Balance = BlackJack.getBalanceBJ(message)
        if Balance >= bet:
            Balance = Balance + point
            db = sqlite3.connect('db/JeckaBot.db')
            cur = db.cursor()
            cur.execute("UPDATE Users SET balance = " + str(Balance) + " WHERE userId = " + str(message.chat.id))
            db.commit()
            db.close()
        else:
            isBankrot = True
        return isBankrot, Balance

    @staticmethod
    def save_player_data(chat_id, bet, player_score, itog):
        with open(f'bjSaves//player{chat_id}.txt', 'w', encoding='UTF-8') as f:
            f.write(f"{bet}\n{player_score}\n{itog}")

    @staticmethod
    def load_player_data(chat_id):
        with open(f'bjSaves//player{chat_id}.txt', 'r', encoding='UTF-8') as f:
            return [line.strip().lower() for line in f]

    @staticmethod
    def BJBet(message, itog, res=False):
        keyBJ = types.InlineKeyboardMarkup()
        bets = [50, 100, 200]
        for bet in bets:
            keyBJ.add(types.InlineKeyboardButton(text=f'Ставка {bet}', callback_data=f'BlackJack{bet}'))
        keyBJ.add(types.InlineKeyboardButton(text='Вдругой раз', callback_data='krutkonec'))
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=itog, reply_markup=keyBJ)

    @staticmethod
    def BJGetCard(message, sum, itog, res=False):
        keyBJGetCard = types.InlineKeyboardMarkup()
        keyBJGetCard.add(types.InlineKeyboardButton(text='Еще карту', callback_data='GetCardYes'))
        keyBJGetCard.add(types.InlineKeyboardButton(text='Хватит', callback_data='GetCardNo'))
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                              text=f'Сумма: {sum}\n{itog}\nЕще карту?', reply_markup=keyBJGetCard)
        sleep(2)

    @staticmethod
    def BlackJackFirst(message, bet):
        isBankrot, Balance = BlackJack.updateScoreBJ(bet, -bet, message)
        playerScore, itog = 0, ""
        if not isBankrot:
            poolCard = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"]
            for _ in range(2):
                playerScore, itog = BlackJack.randomCard(poolCard, playerScore, itog)

            if playerScore == 21:
                isBankrot, Balance = BlackJack.updateScoreBJ(bet, 2 * bet, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, itog)
                BlackJack.BJBet(message, f'Ты выиграл, набрав {playerScore} \n{itog}\nБаланс: {Balance}(+{bet})')
            else:
                BlackJack.save_player_data(message.chat.id, bet, playerScore, itog)
                BlackJack.BJGetCard(message, playerScore, itog)
        else:
            BlackJack.BJBet(message, "К сожалению, Ваших средств недостаточно, чтобы сделать ставку")

    @staticmethod
    def BlackJackNext(message, getCard):
        poolCard = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"]
        bd_data = BlackJack.load_player_data(message.chat.id)
        bet, playerScore, itog = int(bd_data[0]), int(bd_data[1]), bd_data[2]

        if getCard:
            playerScore, itog = BlackJack.randomCard(poolCard, playerScore, itog)
            if playerScore == 21:
                isBankrot, Balance = BlackJack.updateScoreBJ(bet, 2 * bet, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, itog)
                BlackJack.BJBet(message, f'Ты выиграл, набрав {playerScore} \n{itog}\nБаланс: {Balance}(+{bet})')
            elif playerScore > 21:
                isBankrot, Balance = BlackJack.updateScoreBJ(bet, 0, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, itog)
                BlackJack.BJBet(message, f'Ты проиграл, набрав {playerScore} \n{itog}\nБаланс: {Balance}(-{bet})')
            else:
                BlackJack.save_player_data(message.chat.id, bet, playerScore, itog)
                BlackJack.BJGetCard(message, playerScore, itog)
        else:
            botScore, botItog = 0, ""
            for _ in range(2):
                botScore, botItog = BlackJack.randomCard(poolCard, botScore, botItog)
            while botScore <= playerScore:
                botScore, botItog = BlackJack.randomCard(poolCard, botScore, botItog)

            if botScore > 21:
                isBankrot, Balance = BlackJack.updateScoreBJ(bet, 2 * bet, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, itog)
                BlackJack.BJBet(message,
                                f'Ты выиграл, Жека-крупье набрал {botScore} \n{botItog}\nТвой Баланс: {Balance}(+{bet})')
            elif botScore == playerScore:
                isBankrot, Balance = BlackJack.updateScoreBJ(bet, bet, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, itog)
                BlackJack.BJBet(message,
                                f'Ничья, Жека-крупье набрал {botScore} \n{botItog}\nТвой Баланс: {Balance}(+0)')
            else:
                if botScore <= 21:
                    isBankrot, Balance = BlackJack.updateScoreBJ(bet, 0, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, itog)
                BlackJack.BJBet(message,
                                f'Ты проиграл, Жека-крупье набрал {botScore} \n{botItog}\nТвой Баланс: {Balance}(-{bet})')

    @staticmethod
    def randomCard(poolCard, playerScore, itog):
        randomCard = random.choice(poolCard)
        card_values = {
            "a": (11 if playerScore < 11 else 1, "🃏"),
            10: (10, "🔟"), 9: (9, "9️⃣"), 8: (8, "8️⃣"),
            7: (7, "7️⃣"), 6: (6, "6️⃣"), 5: (5, "5️⃣"),
            4: (4, "4️⃣"), 3: (3, "3️⃣"), 2: (2, "2️⃣")
        }
        value, symbol = card_values[randomCard]
        playerScore += value
        itog += symbol
        return playerScore, itog