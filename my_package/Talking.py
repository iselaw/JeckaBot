import os
import random

from fuzzywuzzy import fuzz


class Talking:

    @staticmethod
    def answer(text, mas):
        text = text.lower().strip()
        try:
            valumeMas = len(mas) - 1
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
                            if elementNumber != valumeMas:
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
                return answer, maximumSimilarity
            else:
                return 'Не понял, перефразируй', 0
        except:
            return 'Не совсем понял вопрос', 0