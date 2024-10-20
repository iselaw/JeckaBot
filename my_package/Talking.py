import os
import random
import sqlite3
from Login import bot, admin
from fuzzywuzzy import fuzz


class Talking:

    @staticmethod
    def answer(message, mas):
        muteStatus = 2
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT mute FROM Users WHERE userId=" + str(message.chat.id)):
            muteStatus = x[0]
        db.close()
        if muteStatus == 0:
            text = message.text.lower().strip()
            try:
                volumeMas = len(mas) - 1
                if os.path.exists('../resources/data/boltun.txt'):
                    maximumSimilarity = 0
                    elementNumber = 0
                    questionNumber = 0
                    for q in mas:
                        if 'u: ' in q:
                            # С помощью fuzzywuzzy получаем, насколько похожи две строки
                            degreeOfSimilarity = (fuzz.token_sort_ratio(q.replace('u: ', ''), text))
                            if degreeOfSimilarity > maximumSimilarity:
                                maximumSimilarity = degreeOfSimilarity
                                if elementNumber != volumeMas:
                                    questionNumber = elementNumber
                        elementNumber = elementNumber + 1
                    isQuestion = False
                    count = 1
                    while not isQuestion:
                        if 'u: ' not in mas[questionNumber + count]:
                            count = count + 1
                        if 'u: ' in mas[questionNumber + count]:
                            isQuestion = True
                    answerNumber = random.randint(1, count - 1)
                    answer = mas[questionNumber + answerNumber]
                    bot.send_message(message.chat.id, answer)
                    isAdmin = message.chat.id in admin
                    if not isAdmin:
                        for x in admin:
                            try:
                                bot.send_message(x, message.chat.first_name + "\n" + text + "\n" +answer)
                            except:
                                bot.send_message(x, message.chat.title + "\n" + text + "\n" +answer)
                else:
                    bot.send_message(message.chat.id, 'Не понял, перефразируй')
            except:
                bot.send_message(message.chat.id, 'Не совсем понял вопрос')