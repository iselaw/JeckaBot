import sqlite3
import random
from time import sleep
from telebot import types
from Login import bot
from my_package.Admin import Admin


class BlackJack:

    @staticmethod
    def get_balance_bj(message):
        balance = 0
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT balance FROM Users where userId=" + str(message.chat.id)):
            balance = x[0]
        db.close()
        return balance

    @staticmethod
    def update_score_bj(bet, point, message):
        isBankrupt = False
        balance = BlackJack.get_balance_bj(message)
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
    def save_player_data(chat_id, bet, player_score, result):
        with open(f'../resources/bjSaves//player{chat_id}.txt', 'w', encoding='UTF-8') as f:
            f.write(f"{bet}\n{player_score}\n{result}")

    @staticmethod
    def load_player_data(chat_id):
        with open(f'../resources/bjSaves//player{chat_id}.txt', 'r', encoding='UTF-8') as f:
            return [line.strip().lower() for line in f]

    @staticmethod
    def bj_bet(message, result):
        keyBJ = types.InlineKeyboardMarkup()
        bets = [50, 100, 200]
        for bet in bets:
            keyBJ.add(types.InlineKeyboardButton(text=f'Ставка {bet}', callback_data=f'BlackJack{bet}'))
        keyBJ.add(types.InlineKeyboardButton(text='В другой раз', callback_data='bj_exit'))
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=result, reply_markup=keyBJ)

    @staticmethod
    def bj_get_card(message, total, result):
        key_bj_get_card = types.InlineKeyboardMarkup()
        key_bj_get_card.add(types.InlineKeyboardButton(text='Еще карту', callback_data='BlackJackGetCardYes'))
        key_bj_get_card.add(types.InlineKeyboardButton(text='Хватит', callback_data='BlackJackGetCardNo'))
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                              text=f'Сумма: {total}\n{result}\nЕще карту?', reply_markup=key_bj_get_card)
        sleep(2)

    @staticmethod
    def black_jack_first(message, bet):
        isBankrupt, balance = BlackJack.update_score_bj(bet, -bet, message)
        player_score, result = 0, ""
        if not isBankrupt:
            pool_card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"]
            for _ in range(2):
                player_score, result = BlackJack.random_card(pool_card, player_score, result)

            if player_score == 21:
                isBankrupt, balance = BlackJack.update_score_bj(bet, 2 * bet, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, result)
                BlackJack.bj_bet(message, f'Ты выиграл, набрав {player_score} \n{result}\nБаланс: {balance}(+{bet})')
            else:
                BlackJack.save_player_data(message.chat.id, bet, player_score, result)
                BlackJack.bj_get_card(message, player_score, result)
        else:
            BlackJack.bj_bet(message, "К сожалению, Ваших средств недостаточно, чтобы сделать ставку")

    @staticmethod
    def black_jack_next(message, get_card):
        pool_card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"]
        bd_data = BlackJack.load_player_data(message.chat.id)
        bet, player_score, result = int(bd_data[0]), int(bd_data[1]), bd_data[2]

        if get_card:
            player_score, result = BlackJack.random_card(pool_card, player_score, result)
            if player_score == 21:
                isBankrupt, balance = BlackJack.update_score_bj(bet, 2 * bet, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, result)
                BlackJack.bj_bet(message, f'Ты выиграл, набрав {player_score} \n{result}\nБаланс: {balance}(+{bet})')
            elif player_score > 21:
                isBankrupt, balance = BlackJack.update_score_bj(bet, 0, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, result)
                BlackJack.bj_bet(message, f'Ты проиграл, набрав {player_score} \n{result}\nБаланс: {balance}(-{bet})')
            else:
                BlackJack.save_player_data(message.chat.id, bet, player_score, result)
                BlackJack.bj_get_card(message, player_score, result)
        else:
            botScore, botresult = 0, ""
            for _ in range(2):
                botScore, botresult = BlackJack.random_card(pool_card, botScore, botresult)
            while botScore <= player_score:
                botScore, botresult = BlackJack.random_card(pool_card, botScore, botresult)

            if botScore > 21:
                isBankrupt, balance = BlackJack.update_score_bj(bet, 2 * bet, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, result)
                BlackJack.bj_bet(message,
                                f'Ты выиграл, Жека-крупье набрал {botScore} \n{botresult}\nТвой Баланс: {balance}(+{bet})')
            elif botScore == player_score:
                isBankrupt, balance = BlackJack.update_score_bj(bet, bet, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, result)
                BlackJack.bj_bet(message,
                                f'Ничья, Жека-крупье набрал {botScore} \n{botresult}\nТвой Баланс: {balance}(+0)')
            else:
                if botScore <= 21:
                    isBankrupt, balance = BlackJack.update_score_bj(bet, 0, message)
                BlackJack.save_player_data(message.chat.id, bet, 0, result)
                BlackJack.bj_bet(message,
                                f'Ты проиграл, Жека-крупье набрал {botScore} \n{botresult}\nТвой Баланс: {balance}(-{bet})')

    @staticmethod
    def random_card(pool_card, player_score, result):
        random_card = random.choice(pool_card)
        card_values = {
            "a": (11 if player_score < 11 else 1, "🃏"),
            10: (10, "🔟"), 9: (9, "9️⃣"), 8: (8, "8️⃣"),
            7: (7, "7️⃣"), 6: (6, "6️⃣"), 5: (5, "5️⃣"),
            4: (4, "4️⃣"), 3: (3, "3️⃣"), 2: (2, "2️⃣")
        }
        value, symbol = card_values[random_card]
        player_score += value
        result += symbol
        return player_score, result

    @staticmethod
    def bj_handler(call):
        if call.data == "BlackJackGetCardYes":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Жека-крупье вытаскивает карту из колоды")
            BlackJack.black_jack_next(call.message, True)

        elif call.data == "BlackJackGetCardNo":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Очередь Жеки-крупье тянуть карты")
            BlackJack.black_jack_next(call.message, False)

        elif call.data == "BlackJack50":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Ставка 50\nВаш баланс: " + str(int(BlackJack.get_balance_bj(call.message)) - 50))
            BlackJack.black_jack_first(call.message, 50)
        elif call.data == "BlackJack100":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Ставка 100\nВаш баланс: " + str(int(BlackJack.get_balance_bj(call.message)) - 100))
            BlackJack.black_jack_first(call.message, 100)
        elif call.data == "BlackJack200":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Ставка 200\nВаш баланс: " + str(int(BlackJack.get_balance_bj(call.message)) - 200))
            BlackJack.black_jack_first(call.message, 200)
        elif call.data == "BlackJack":
            BlackJack.bj_bet(call.message, "Выбрано: Блекджек\nВаш баланс: " + str(BlackJack.get_balance_bj(call.message)))
            Admin.update_statistic(call.message, "BlackJack")
        elif call.data == "bj_exit":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Приходи еще")