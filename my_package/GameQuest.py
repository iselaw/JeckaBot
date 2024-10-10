from telebot import types
from Login import *
from statistic import updateStatistic

class GameQuest:

    @staticmethod
    def GameQuestStart(message, res=False):
        keygameQuest = types.InlineKeyboardMarkup()
        key_startQuest = types.InlineKeyboardButton(text='Да', callback_data='startQuest')
        keygameQuest.add(key_startQuest)
        key_exitQuest = types.InlineKeyboardButton(text='Нет', callback_data='exitQuest')
        keygameQuest.add(key_exitQuest)
        bot.send_message(message.chat.id, 'Привет, хочешь сыграть в игру про путешествия Жеки по волшебному миру?',
                         reply_markup=keygameQuest)

    @staticmethod
    def Questt(message, res=False):
        photo1 = open('../resources/GameQuest/putnic.jpg', 'rb')
        keygameQuest1 = types.InlineKeyboardMarkup()
        key_askTraveler = types.InlineKeyboardButton(text='Спросить что случилось', callback_data='askTraveler')
        keygameQuest1.add(key_askTraveler)
        bot.send_photo(chat_id=message.chat.id, photo=photo1,
                       caption='Однажды, в теплый светлый день, Жека вышел из своего дома за покупками на рынок '
                               'города.\n\nПо дороге в город вы встречаете напуганного путника.',
                       reply_markup=keygameQuest1)

    @staticmethod
    def Quest2(message, isFirst, res=False):
        keygameQuest2 = types.InlineKeyboardMarkup()
        key_blacksmith = types.InlineKeyboardButton(text='Пойти до Кузнеца', callback_data='blacksmith')
        keygameQuest2.add(key_blacksmith)
        key_Market = types.InlineKeyboardButton(text='Пойти на Рынок', callback_data='Market')
        keygameQuest2.add(key_Market)
        key_Castle = types.InlineKeyboardButton(text='Пойти в сторону жуткого заброшенного Замка',
                                                callback_data='Castle')
        keygameQuest2.add(key_Castle)
        if isFirst == True:
            photo1 = open('../resources/GameQuest/putnic.jpg', 'rb')
            bot.send_photo(chat_id=message.chat.id, photo=photo1,
                           caption="Путник поведал:\n\"Зря ты без оружия гуляешь по этим местам. Заброшенный Замок "
                                   "неподалеку заселили силы зла во главе с темным рыцарем Листатом. За все время "
                                   "нахождения в замке, прислужники Листата уже похитили 5 девушек из местных деревень и "
                                   "убили 4 торговцев. Когда я проходил мимо Замка, я наткнулся на группу "
                                   "скелетов-гоблинов, которые напали на меня, я еле унес от них ноги. Может мне "
                                   "показалось, но еще в небе я увидел огромного красного дракона, "
                                   "он что-то держал в лапах, что-то похожее на мешки с золотом. Советую тебе "
                                   "быть осторожнее, лучше купи снаряжение у Кузница в городе\".\nВы прибыли в город. "
                                   "Куда вы хотите отправиться?",
                           reply_markup=keygameQuest2)
        else:
            photo3 = open('../resources/GameQuest/Рынок.jpg', 'rb')
            bot.send_photo(chat_id=message.chat.id, photo=photo3,
                           caption="Хммм странно, почему-то сегодня на рынке никого нет, куда все подевались?",
                           reply_markup=keygameQuest2)

    @staticmethod
    def QuestBlacksith1(message, text, res=False):
        photo2 = open('../resources/GameQuest/kuznec.jpg', 'rb')
        keygameQuest3 = types.InlineKeyboardMarkup()
        key_CastleBlacksith = types.InlineKeyboardButton(text='Расскажи про заброшенный замок',
                                                         callback_data='CastleBlacksith')
        keygameQuest3.add(key_CastleBlacksith)
        key_MarketBlacksith = types.InlineKeyboardButton(text='Почему рынок сегодня не работает?',
                                                         callback_data='MarketBlacksith')
        keygameQuest3.add(key_MarketBlacksith)
        key_ArmorBlacksith = types.InlineKeyboardButton(text='Ты можешь продать или изготовить для меня доспехи ?',
                                                        callback_data='ArmorBlacksith')
        keygameQuest3.add(key_ArmorBlacksith)
        bot.send_photo(chat_id=message.chat.id, photo=photo2, caption=text, reply_markup=keygameQuest3)

    @staticmethod
    def QuestCastle1(message, res=False):
        photo4 = open('../resources/GameQuest/замокбездоспехов.jpg', 'rb')
        keygameQuest4 = types.InlineKeyboardMarkup()
        key_CastleOver = types.InlineKeyboardButton(text='Пойти к заброшенному замку', callback_data='CastleOver')
        keygameQuest4.add(key_CastleOver)
        key_CastleDracon = types.InlineKeyboardButton(text='Пойти к Дракону', callback_data='CastleDracon')
        keygameQuest4.add(key_CastleDracon)
        key_QuestCastle1NO = types.InlineKeyboardButton(text='Вернуться назад', callback_data='QuestCastle1NO')
        keygameQuest4.add(key_QuestCastle1NO)
        bot.send_photo(chat_id=message.chat.id, photo=photo4,
                       caption='Вы видите замок рядом с которым обитает дракон\nПойти к '
                               'Заброшенному Замку или Пойти к Дракону ?',
                       reply_markup=keygameQuest4)

    @staticmethod
    def BlacksithPurchase(message, brokenTools, res=False):
        photo7 = open('../resources/GameQuest/kuznec.jpg', 'rb')
        keygameQuest5 = types.InlineKeyboardMarkup()
        key_PriceArmor = types.InlineKeyboardButton(text='Купить доспехи ', callback_data='PriceArmor')
        keygameQuest5.add(key_PriceArmor)
        if (brokenTools == False):
            key_WoodMetal = types.InlineKeyboardButton(text='Где я могу взять металл и дерево?', callback_data='WoodMetal')
            keygameQuest5.add(key_WoodMetal)
        bot.send_photo(chat_id=message.chat.id, photo=photo7,
                       caption='Я могу Продать тебе готовые, либо сделать новые бесплатно, если ты принесешь мне дерево '
                               'или металл',
                       reply_markup=keygameQuest5)

    @staticmethod
    def ResourceExtraction(message, res=False):
        photo7 = open('../resources/GameQuest/kuznec.jpg', 'rb')
        keygameQuest6 = types.InlineKeyboardMarkup()
        key_TreeMining = types.InlineKeyboardButton(text='Отправиться добывать дерево', callback_data='TreeMining')
        keygameQuest6.add(key_TreeMining)
        key_MetalMining = types.InlineKeyboardButton(text='Отправиться добывать металл', callback_data='MetalMining')
        keygameQuest6.add(key_MetalMining)
        key_MetalMining = types.InlineKeyboardButton(text='Вернуться и купить Доспехи', callback_data='BuyArmor')
        keygameQuest6.add(key_MetalMining)
        bot.send_photo(chat_id=message.chat.id, photo=photo7,
                       caption='Я дам тебе кирку и топор, отправляйся для добычи ресурсов и потом ко мне.\nКуда '
                               'отправимся в первую очередь?',
                       reply_markup=keygameQuest6)

    @staticmethod
    def TreeMining(message, res=False):
        photo6 = open('../resources/GameQuest/лес.jpg', 'rb')
        keygameQuest7 = types.InlineKeyboardMarkup()
        key_TreeMiningON = types.InlineKeyboardButton(text='Высокое и тонкое', callback_data='TreeMiningON')
        keygameQuest7.add(key_TreeMiningON)
        key_TreeMiningExit = types.InlineKeyboardButton(text='Низкое и толстое', callback_data='TreeMiningExit')
        keygameQuest7.add(key_TreeMiningExit)
        bot.send_photo(chat_id=message.chat.id, photo=photo6,
                       caption='Вы пришли в лес\nВы видите 2 разных дерева\nПервое дерево - Высокое и тонкое\nВторое '
                               'дерево - Низкое и толстое\nКакое дерево будете рубить?',
                       reply_markup=keygameQuest7)

    @staticmethod
    def MetalMining(message, res=False):
        photo7 = open('../resources/GameQuest/shahta.jpg', 'rb')
        keygameQuest8 = types.InlineKeyboardMarkup()
        key_TreeMiningExit = types.InlineKeyboardButton(text='Из Первой жилы', callback_data='MetalMiningExit')
        keygameQuest8.add(key_TreeMiningExit)
        key_MetalMiningON = types.InlineKeyboardButton(text='Из Второй жилы', callback_data='MetalMiningON')
        keygameQuest8.add(key_MetalMiningON)
        bot.send_photo(chat_id=message.chat.id, photo=photo7,
                       caption='Вы пришли в шахту\nВы видите две разные жилы металла\nВ первой Жиле Вы видите остатки '
                               'чужой кирки и помимо металла еще какую-то примесь\nВо второй Жиле Вы видите много металла '
                               'прям на поверхности\nИз какой жили вы будете добывать металл?',
                       reply_markup=keygameQuest8)

    @staticmethod
    def Outlaw(message, res=False):
        photo7 = open('../resources/GameQuest/kuznec.jpg', 'rb')
        keygameQuest9 = types.InlineKeyboardMarkup()
        key_OutlawYes = types.InlineKeyboardButton(text='Пойти к Бандитам', callback_data='OutlawYes')
        keygameQuest9.add(key_OutlawYes)
        key_OutlawNo = types.InlineKeyboardButton(text='Вернуться назад', callback_data='OutlawNo')
        keygameQuest9.add(key_OutlawNo)
        bot.send_photo(chat_id=message.chat.id, photo=photo7,
                       caption='Доспехи стоят 100 монет, а у тебя, к сожалению, есть только 30. За 30 монет могу продать '
                               'тебе только хороший острый меч и сказать как можно раздобыть деньги.\nНа нашу деревню '
                               'часто начали нападать бандиты, их лагерь расположен за городом. Мэр города платит 100 '
                               'золотых монет тому, кто их прогонит',
                       reply_markup=keygameQuest9)

    @staticmethod
    def BanditBattle(message, res=False):
        photo8 = open('../resources/GameQuest/bandit.jpg', 'rb')
        keygameQuest10 = types.InlineKeyboardMarkup()
        key_BanditDogovor = types.InlineKeyboardButton(text='Попробовать договориться с Бандитом',
                                                       callback_data='BanditDogovor')
        keygameQuest10.add(key_BanditDogovor)
        key_BanditBattle = types.InlineKeyboardButton(text='Начать бой с Бандитом ', callback_data='BanditBattle')
        keygameQuest10.add(key_BanditBattle)
        bot.send_photo(chat_id=message.chat.id, photo=photo8,
                       caption='Вы пришли в лагерь бандитов\nПеред вами стоит самый главный бандит. Вы видите, что у него '
                               'хороший стальной шлем, но одет он в тканевые тряпки.',
                       reply_markup=keygameQuest10)

    @staticmethod
    def BanditDogovor(message, res=False):
        photo8 = open('../resources/GameQuest/bandit.jpg', 'rb')
        keygameQuest11 = types.InlineKeyboardMarkup()
        key_DieBandit = types.InlineKeyboardButton(text='Отдать все золото и вернуться к Кузнецу',
                                                   callback_data='DieBandit')
        keygameQuest11.add(key_DieBandit)
        key_BanditBattle2 = types.InlineKeyboardButton(text='Начать бой с Бандитом ', callback_data='BanditBattle2')
        keygameQuest11.add(key_BanditBattle2)
        bot.send_photo(chat_id=message.chat.id, photo=photo8,
                       caption="Кажется, разговор не состоится\n- Выворачивай карманы и пошел отсюда, пока цел!!!! ",
                       reply_markup=keygameQuest11)

    @staticmethod
    def BanditBattleExit(message, res=False):
        photo8 = open('../resources/GameQuest/bandit.jpg', 'rb')
        keygameQuest12 = types.InlineKeyboardMarkup()
        key_BlowHead = types.InlineKeyboardButton(text='Ударить мечом по голове', callback_data='BlowHead')
        keygameQuest12.add(key_BlowHead)
        key_HeartBeat = types.InlineKeyboardButton(text='Ударить мечом в сердце', callback_data='HeartBeat')
        keygameQuest12.add(key_HeartBeat)
        bot.send_photo(chat_id=message.chat.id, photo=photo8,
                       caption="Главарь Бандитов достал меч\nВыберите куда ударить бандита", reply_markup=keygameQuest12)

    @staticmethod
    def ReceivingMoney(message, res=False):
        photo11 = open('../resources/GameQuest/мертвбандит.jpg', 'rb')
        keygameQuest13 = types.InlineKeyboardMarkup()
        key_ReceivingMoney = types.InlineKeyboardButton(text='Отправиться к мэру города за наградой',
                                                        callback_data='ReceivingMoney')
        keygameQuest13.add(key_ReceivingMoney)
        bot.send_photo(chat_id=message.chat.id, photo=photo11,
                       caption="Вы нанесли сокрушительный удар Главе бандитов. Он мертв, а его подчиненые быстро "
                               "сбежали.",
                       reply_markup=keygameQuest13)

    @staticmethod
    def BlacksmithArmorPayment(message, res=False):
        photo12 = open('../resources/GameQuest/nagrada.jpg', 'rb')
        keygameQuest14 = types.InlineKeyboardMarkup()
        key_BlacksmithArmorPayment = types.InlineKeyboardButton(text='Отправиться к Кузнецу за доспехами',
                                                                callback_data='BlacksmithArmorPayment')
        keygameQuest14.add(key_BlacksmithArmorPayment)
        bot.send_photo(chat_id=message.chat.id, photo=photo12,
                       caption="Вы пришли к Мэру города\nМэр поблагодарил вас за помощь городу, дал вам положенную "
                               "награду.\nФуууух, теперь можно отправиться к кузнецу и купить у него доспехи для похода к "
                               "жуткому заброшенному замку",
                       reply_markup=keygameQuest14)

    @staticmethod
    def Castle(message, res=False):
        photo13 = open('../resources/GameQuest/Куз2нец.jpg', 'rb')
        keygameQuest15 = types.InlineKeyboardMarkup()
        key_CastleArmor = types.InlineKeyboardButton(text='Отправиться к Жуткому заброшенному замку',
                                                     callback_data='CastleArmor')
        keygameQuest15.add(key_CastleArmor)
        bot.send_photo(chat_id=message.chat.id, photo=photo13,
                       caption="Вы пришли к Кузнецу\nПривет, спасибо что прогнал бандитов. Вот держи свои доспехи. "
                               "Пожелаю успехов тебе в твоем путешествии",
                       reply_markup=keygameQuest15)

    @staticmethod
    def MistakeBroken(message, res=False):
        photo15 = open('../resources/GameQuest/brokenкирка.jpg', 'rb')
        keygameQuest16 = types.InlineKeyboardMarkup()
        key_MistakeBroken = types.InlineKeyboardButton(text='Вернуться к кузнецу', callback_data='MistakeBroken')
        keygameQuest16.add(key_MistakeBroken)
        bot.send_photo(chat_id=message.chat.id, photo=photo15,
                       caption="Вы сломали свою Кирку. Возвращайтесь к кузнецу",
                       reply_markup=keygameQuest16)

    @staticmethod
    def GotIt(message, res=False):
        photo18 = open('../resources/GameQuest/цфвфц.jpg', 'rb')
        keygameQuest17 = types.InlineKeyboardMarkup()
        key_GotIt = types.InlineKeyboardButton(text='Пойти к кузнецу за доспехами', callback_data='GotIt')
        keygameQuest17.add(key_GotIt)
        bot.send_photo(chat_id=message.chat.id, photo=photo18,
                       caption="Вы Добыли металл\nВозвращайтесь к кузнецу",
                       reply_markup=keygameQuest17)

    @staticmethod
    def СhoosePath(message, res=False):
        photo14 = open('../resources/GameQuest/pal.jpg', 'rb')
        keygameQuest18 = types.InlineKeyboardMarkup()
        key_СhoosePathCastle = types.InlineKeyboardButton(text='Заброшенный замок', callback_data='СhoosePathCastle')
        keygameQuest18.add(key_СhoosePathCastle)
        key_СhoosePathDragon = types.InlineKeyboardButton(text='Место, куда улетел дракон',
                                                          callback_data='СhoosePathDragon')
        keygameQuest18.add(key_СhoosePathDragon)
        bot.send_photo(chat_id=message.chat.id, photo=photo14,
                       caption="Вы пришли к Жуткому заброшеному замку.\nВы увидели небольшую группу скелетов около "
                               "заброшенного замка и красного дракон, в лапах у которого "
                               "мешки с золотом?\nВ какую сторону идти?",
                       reply_markup=keygameQuest18)

    @staticmethod
    def DragonDialogue(message, res=False):
        photo19 = open('../resources/GameQuest/драконзолото.jpg', 'rb')
        keygameQuest19 = types.InlineKeyboardMarkup()
        key_DragonDialogue = types.InlineKeyboardButton(text='Подойти к дракону ', callback_data='DragonDialogue')
        keygameQuest19.add(key_DragonDialogue)
        bot.send_photo(chat_id=message.chat.id, photo=photo19,
                       caption="Вы приблизлись к логову дракона и увидели, что у него полно золота\nДракон "
                               "смотрит на вас, но вроде бы не собираеться атаковать.\nДумаю, стоит приблизиться к "
                               "дракону",
                       reply_markup=keygameQuest19)

    @staticmethod
    def DragonExit(message, res=False):
        photo19 = open('../resources/GameQuest/драконзолото.jpg', 'rb')
        keygameQuest20 = types.InlineKeyboardMarkup()
        key_DragonExitGold = types.InlineKeyboardButton(text='Хочу Разбогатеть', callback_data='DragonExitGold')
        keygameQuest20.add(key_DragonExitGold)
        key_DragonExitLove = types.InlineKeyboardButton(text='Хочу Найти любовь', callback_data='DragonExitLove')
        keygameQuest20.add(key_DragonExitLove)
        key_DragonExitOver = types.InlineKeyboardButton(text='Хочу, чтобы ты служил мне ', callback_data='DragonExitOver')
        keygameQuest20.add(key_DragonExitOver)
        bot.send_photo(chat_id=message.chat.id, photo=photo19,
                       caption="Приветствую тебя, Путник. Ты достаточно храбр, раз подошел ко мне. Так и быть, исполню "
                               "одно твое желание.",
                       reply_markup=keygameQuest20)

    @staticmethod
    def SkeletonsOfbBry(message, res=False):
        photo23 = open('../resources/GameQuest/скелетыжека.jpg', 'rb')
        keygameQuest21 = types.InlineKeyboardMarkup()
        key_SkeletonsOfbBry = types.InlineKeyboardButton(text='Атаковать скелетов', callback_data='SkeletonsOfbBry')
        keygameQuest21.add(key_SkeletonsOfbBry)
        bot.send_photo(chat_id=message.chat.id, photo=photo23,
                       caption="Вы приблизились к Замку, скелеты-рыцари заметили Вас и двинулись в атаку\nВы достали меч и "
                               "готовы атаковать скелетов в ответ",
                       reply_markup=keygameQuest21)

    @staticmethod
    def Ingot(message, res=False):
        photo24 = open('../resources/GameQuest/winskelet.jpg', 'rb')
        keygameQuest22 = types.InlineKeyboardMarkup()
        key_IngotYes = types.InlineKeyboardButton(text='Подобрать свиток', callback_data='IngotYes')
        keygameQuest22.add(key_IngotYes)
        bot.send_photo(chat_id=message.chat.id, photo=photo24,
                       caption="Вы убили всех скелетов-рыцарей\nНа полу вы заметили свиток. Возьмите его",
                       reply_markup=keygameQuest22)

    @staticmethod
    def Demon(message, res=False):
        photo24 = open('../resources/GameQuest/svitok.jpg', 'rb')
        keygameQuest23 = types.InlineKeyboardMarkup()
        key_Demon = types.InlineKeyboardButton(text='Подойти к демону', callback_data='Demon')
        keygameQuest23.add(key_Demon)
        bot.send_photo(chat_id=message.chat.id, photo=photo24,
                       caption="Вы подняли свиток, раскрыли его и это оказался свиток усиления\nНадеюсь, он поможет мне в "
                               "дальнейшем пушествий по замку\nВы пошли дальше.\nВы увидели демона.",
                       reply_markup=keygameQuest23)

    @staticmethod
    def Demon2(message, res=False):
        photo25 = open('../resources/GameQuest/vulgrim.jpg', 'rb')
        keygameQuest24 = types.InlineKeyboardMarkup()
        key_Demon2 = types.InlineKeyboardButton(text='Выслушать демона', callback_data='Demon2')
        keygameQuest24.add(key_Demon2)
        bot.send_photo(chat_id=message.chat.id, photo=photo25,
                       caption="Приблизившись к демону, он обратился к вам:\n-\"Здравствуй, смертный. Меня зовут "
                               "Вульгрим. Не знаю зачем направляешься к хозяину этой башни темному рыцарю Листату, "
                               "но следующий его прислужник тебе не по зубам. Однако, я могу оказать тебе услугу\"",
                       reply_markup=keygameQuest24)

    @staticmethod
    def Demon3(message, res=False):
        photo26 = open('../resources/GameQuest/amulet.jpg', 'rb')
        keygameQuest25 = types.InlineKeyboardMarkup()
        key_DemonAmuletYes = types.InlineKeyboardButton(text='Принять Амулет', callback_data='DemonAmuletYes')
        keygameQuest25.add(key_DemonAmuletYes)
        key_DemonAmuletNo = types.InlineKeyboardButton(text='Отказаться', callback_data='DemonAmuletNo')
        keygameQuest25.add(key_DemonAmuletNo)
        bot.send_photo(chat_id=message.chat.id, photo=photo26,
                       caption="Демон протягивает какой-то амулет и говорит:\n-\"Этот артефакт позволит убить твоего "
                               "следующего противника, его имя Сашаель. Я дам тебе амулет, но взамен ты принесешь мне "
                               "сердце Сашаеля\"",
                       reply_markup=keygameQuest25)

    @staticmethod
    def Boss1(message, res=False):
        photo27 = open('../resources/GameQuest/image15.jpg', 'rb')
        keygameQuest26 = types.InlineKeyboardMarkup()
        key_BossAmuletYes = types.InlineKeyboardButton(text='Использовать Амулет для Атаки', callback_data='BossAmuletYes')
        keygameQuest26.add(key_BossAmuletYes)
        key_BossAmuletNo = types.InlineKeyboardButton(text='Атаковать без усилений', callback_data='BossAmuletNo')
        keygameQuest26.add(key_BossAmuletNo)
        key_BossExit = types.InlineKeyboardButton(text='Использовать Свиток для Атаки', callback_data='BossExit')
        keygameQuest26.add(key_BossExit)
        bot.send_photo(chat_id=message.chat.id, photo=photo27,
                       caption="Вы взяли амулет\nДемон улыбнулся и сказал:\n-\"С нетерпением жду, когда ты принесешь его "
                               "сердце мне. Не советую меня обманывать\"\nВы отправились дальше и встретили Сашаеля\nКак вы хотите его атаковать?",
                       reply_markup=keygameQuest26)

    @staticmethod
    def Demon4(message, res=False):
        photo29 = open('../resources/GameQuest/killsasha.jpg', 'rb')
        keygameQuest27 = types.InlineKeyboardMarkup()
        key_Demon4 = types.InlineKeyboardButton(text='Пойти дальше', callback_data='Demon4')
        keygameQuest27.add(key_Demon4)
        bot.send_photo(chat_id=message.chat.id, photo=photo29,
                       caption="При взмахе меча сила, амулета перетекла в ваши руки. Вы нанесли сокрушительный удар такой "
                               "силы, что броня противника разлетелась. Сашаель "
                               "упал на колени, вы просунули свою руку в отверствие в броне и достали едва бьющееся "
                               "сердце этой твари\nВы забрали сердце",
                       reply_markup=keygameQuest27)

    @staticmethod
    def Demon5(message, res=False):
        photo32 = open('../resources/GameQuest/hearth.jpg', 'rb')
        keygameQuest28 = types.InlineKeyboardMarkup()
        key_DemonHeartYes = types.InlineKeyboardButton(text='Отдать сердце', callback_data='DemonHeartYes')
        keygameQuest28.add(key_DemonHeartYes)
        key_DemonHeartNo = types.InlineKeyboardButton(text='Отказаться', callback_data='DemonHeartNo')
        keygameQuest28.add(key_DemonHeartNo)
        bot.send_photo(chat_id=message.chat.id, photo=photo32,
                       caption="Вы поднимаетесь вверх по лестнице, перед Вами появляется силуэт Вашего знакомого демона "
                               "Вульгрима.\n - \"Тебе все таки удалось победить в схватке, смертный. Кажется, "
                               "пришло время платить по долгам. Давай мое сердце\"",
                       reply_markup=keygameQuest28)

    @staticmethod
    def MainBoss(message, res=False):
        photo33 = open('../resources/GameQuest/listat.jpg', 'rb')
        keygameQuest29 = types.InlineKeyboardMarkup()
        key_MainBossNo = types.InlineKeyboardButton(text='Атаковать без усилений', callback_data='MainBossNo')
        keygameQuest29.add(key_MainBossNo)
        key_MainBossExit = types.InlineKeyboardButton(text='Использовать Свиток для Атаки', callback_data='MainBossExit')
        keygameQuest29.add(key_MainBossExit)
        bot.send_photo(chat_id=message.chat.id, photo=photo33,
                       caption="\"C тобой приятно иметь дело, что ж, надеюсь еще увидимся\"\nВы поднимаетесь на самый "
                               "верх башни\nВы оказались в комнате с огромным количеством "
                               "золота, у стены сидит связанная девушка. Вы замечаете два светящихся глаза. Видимо это "
                               "владелец башни Листат, выглядит он устрашающе. После пары секунд молчания он говорит\n\"- "
                               "Явиться сюда было глупо. Сейчас ты умрешь",
                       reply_markup=keygameQuest29)

    @staticmethod
    def VinBoss(message, res=False):
        photo35 = open('../resources/GameQuest/ЖекаВин.jpg', 'rb')
        keygameQuest30 = types.InlineKeyboardMarkup()
        key_VinBoss = types.InlineKeyboardButton(text='Освободить девушку и забрать золото', callback_data='VinBoss')
        keygameQuest30.add(key_VinBoss)
        bot.send_photo(chat_id=message.chat.id, photo=photo35,
                       caption="Вы использовали свиток и ощутили прилив сил. Вы произвели серию быстрых атак словно "
                               "берсерк и перед вами осталась лишь куча мяса противника, будто вы разделали свинью.",
                       reply_markup=keygameQuest30)

    @staticmethod
    def SashaelKill(message, res=False):
        photo31 = open('../resources/GameQuest/killsasha.jpg', 'rb')
        keygameQuest31 = types.InlineKeyboardMarkup()
        key_SashaelKill = types.InlineKeyboardButton(text='Пойти дальше', callback_data='SashaelKill')
        keygameQuest31.add(key_SashaelKill)
        bot.send_photo(chat_id=message.chat.id, photo=photo31,
                       caption="Вы использовали свиток и ощутили прилив сил. Вы произвели серию быстрых атак словно "
                               "берсерк,броня противника разлетелась словно она была изготовлена из хрусталя. Сашаель "
                               "упал на колени, вы просунули свою руку в отверствие в броне и достали едва бьющиеся "
                               "сердце этой твари\nВы забрали сердце.",
                       reply_markup=keygameQuest31)

    @staticmethod
    def SashaelKill2(message, res=False):
        photo38 = open('../resources/GameQuest/demonBlade.jpg', 'rb')
        keygameQuest32 = types.InlineKeyboardMarkup()
        key_SashaelKillYes = types.InlineKeyboardButton(text='Отдать сердце', callback_data='SashaelKillYes')
        keygameQuest32.add(key_SashaelKillYes)
        key_SashaelKillNo = types.InlineKeyboardButton(text='Отказаться', callback_data='SashaelKillNo')
        keygameQuest32.add(key_SashaelKillNo)
        bot.send_photo(chat_id=message.chat.id, photo=photo38,
                       caption="Вы встречаете демона. Он предлагает новую сделку:\n\"- Смотрю, тебе удалось победить "
                               "Сашаэля и даже забрать его сердце, что ж, я тебя недооценил. Но с владельцем этой башни "
                               "тебе не удастся справиться без артефактов. Предлагаю новую сделку. В обмен на сердце, "
                               "я дам тебе Клинок Бездны. При должном мастерстве с ним ты без проблем справишься с "
                               "Листатом\"",
                       reply_markup=keygameQuest32)

    @staticmethod
    def MainBoss2(message, res=False):
        photo34 = open('../resources/GameQuest/listat.jpg', 'rb')
        keygameQuest33 = types.InlineKeyboardMarkup()
        key_Died = types.InlineKeyboardButton(text='Атаковать без усилений', callback_data='Died')
        keygameQuest33.add(key_Died)
        key_HeartAttack = types.InlineKeyboardButton(text='Съесть сердце Сашаеля и атаковать', callback_data='HeartAttack')
        keygameQuest33.add(key_HeartAttack)
        key_ScrollAttack = types.InlineKeyboardButton(text='Использовать Свиток для Атаки', callback_data='ScrollAttack')
        keygameQuest33.add(key_ScrollAttack)
        bot.send_photo(chat_id=message.chat.id, photo=photo34,
                       caption="Вульгрим злится и говорит\n\"- Я это так не оставлю, зря ты решил со мной "
                               "поссориться.\"\nДемон исчезает на ваших глазах.\nВы поднимаетесь на самый верх башни\nВы "
                               "Поднялись на вершину башни. Вы оказались в комнате с огромным количеством золота, "
                               "у стены сидит связанная девушка. Вы замечаете два светящихся глаза. Видимо это владелец "
                               "башни Листат, выглядит он устрашающе. После пары секунд молчания он говорит\n\n\"- Придти "
                               "сюда было глупо. Сейчас ты умрешь",
                       reply_markup=keygameQuest33)

    @staticmethod
    def VinBoss2(message, res=False):
        photo42 = open('../resources/GameQuest/ЖекаВин.jpg', 'rb')
        keygameQuest34 = types.InlineKeyboardMarkup()
        key_VinBoss2 = types.InlineKeyboardButton(text='Освободить девушку и забрать золото', callback_data='VinBoss2')
        keygameQuest34.add(key_VinBoss2)
        bot.send_photo(chat_id=message.chat.id, photo=photo42,
                       caption="Вы использовали свиток и ощутили прилив сил. Вы произвели серию быстрых атак словно "
                               "берсерк и перед вами осталась лишь куча мяса противника, будто вы разделали свинью.",
                       reply_markup=keygameQuest34)

    @staticmethod
    def TenYears(message, res=False):
        photo43 = open('../resources/GameQuest/finalgood.jpg', 'rb')
        keygameQuest35 = types.InlineKeyboardMarkup()
        key_TenYears = types.InlineKeyboardButton(text='Спустя 10 лет', callback_data='TenYears')
        keygameQuest35.add(key_TenYears)
        bot.send_photo(chat_id=message.chat.id, photo=photo43,
                       caption="Вы освободили девушку и забрали золото. Вскоре, вы с ней поженились и купили огромный "
                               "дом. Вы прожили счастливую и беззаботную жизнь\nНо ....",
                       reply_markup=keygameQuest35)

    @staticmethod
    def JekaDemon(message, res=False):
        photo45 = open('../resources/GameQuest/gekaDemon.jpg', 'rb')
        keygameQuest36 = types.InlineKeyboardMarkup()
        key_JekaDemon = types.InlineKeyboardButton(text='Наброситься на врага', callback_data='JekaDemon')
        keygameQuest36.add(key_JekaDemon)
        bot.send_photo(chat_id=message.chat.id, photo=photo45,
                       caption="Вы почувствовали дикий прилив сил. От Вас начала распространяться аура тьмы. Вы никогда "
                               "не чувствовали себя сильнее, чем сейчас. Ваш противник начал пятиться назад и что-то "
                               "бормотать.",
                       reply_markup=keygameQuest36)

    @staticmethod
    def JekaDemon2(message, res=False):
        photo46 = open('../resources/GameQuest/gekaDemonBoi.jpg', 'rb')
        keygameQuest37 = types.InlineKeyboardMarkup()
        key_JekaDemon2 = types.InlineKeyboardButton(text='Продолжить', callback_data='JekaDemon2')
        keygameQuest37.add(key_JekaDemon2)
        bot.send_photo(chat_id=message.chat.id, photo=photo46,
                       caption="Вы потеряли контроль над собой\nПодошли к нему и одним уверенным движением вырвали ему "
                               "сердце и затолкали в глотку, затем вырвали ноги и руки. Пленная девушка закричала и "
                               "затряслась от страха. Вы подумали успокоить ее, но голос в вашей голове начал "
                               "шептать\n\n\"- Сожри эту мразь... Сожри это аппетитное свежее мясо.\"\n\nВаш разум "
                               "затуманился, вы набросились на девушку и начали терзать ее зубами и ногтями, вырывать из "
                               "нее куски мяса, вы никогда в жизни не ели с таким аппетитом.",
                       reply_markup=keygameQuest37)

    @staticmethod
    def MainBoss3(message, res=False):
        photo40 = open('../resources/GameQuest/listat.jpg', 'rb')
        keygameQuest38 = types.InlineKeyboardMarkup()
        key_Died2 = types.InlineKeyboardButton(text='Атаковать без усилений', callback_data='Died2')
        keygameQuest38.add(key_Died2)
        key_HeartAttack2 = types.InlineKeyboardButton(text='Съесть сердце Сашаеля и атаковать',
                                                      callback_data='HeartAttack2')
        keygameQuest38.add(key_HeartAttack2)
        bot.send_photo(chat_id=message.chat.id, photo=photo40,
                       caption="Вульгрим злится и говорит:\n\"- Я это так не оставлю, зря ты решил со мной поссориться. "
                               "Демон исчезает на ваших глазах.\"\nВы поднимаетесь на самый верх башни\nВы Поднялись на "
                               "вершину башни. Вы оказались в комнате с огромным количеством золота, у стены сидит "
                               "связанная девушка. Вы замечаете два светящихся глаза. Видимо это владелец башни Листат, "
                               "выглядит он устрашающе. После пары секунд молчания он говорит\n\n\"- Придти сюда было "
                               "глупо. Сейчас ты умрешь",
                       reply_markup=keygameQuest38)

    @staticmethod
    def TakeSword(message, res=False):
        keygameQuest39 = types.InlineKeyboardMarkup()
        key_TakeSword = types.InlineKeyboardButton(text='Взять Меч', callback_data='TakeSword')
        keygameQuest39.add(key_TakeSword)
        bot.send_message(message.chat.id,
                         'Взять меч',
                         reply_markup=keygameQuest39)

    @staticmethod
    def MainBoss4(message, res=False):
        photo39 = open('../resources/GameQuest/listatwad.jpg', 'rb')
        keygameQuest40 = types.InlineKeyboardMarkup()
        key_SwordAttack = types.InlineKeyboardButton(text='Атаковать клинком Бездны', callback_data='SwordAttack')
        keygameQuest40.add(key_SwordAttack)
        bot.send_photo(chat_id=message.chat.id, photo=photo39,
                       caption="\"C тобой приятно иметь дело, что ж, надеюсь еще увидимся\"\nВы поднимаетесь на самый "
                               "верх башни\nВы оказались в комнате с огромным количеством "
                               "золота, у стены сидит связанная девушка. Вы замечаете два светящихся глаза. Видимо это "
                               "владелец башни Листат, выглядит он устрашающе. После пары секунд молчания он "
                               "говорит\n\n\"- Придти сюда было глупо. Сейчас ты умрешь",
                       reply_markup=keygameQuest40)

    @staticmethod
    def Boss2(message, res=False):
        photo28 = open('../resources/GameQuest/image15.jpg', 'rb')
        keygameQuest41 = types.InlineKeyboardMarkup()
        key_BossAmuletNo2 = types.InlineKeyboardButton(text='Атаковать без усилений', callback_data='BossAmuletNo2')
        keygameQuest41.add(key_BossAmuletNo2)
        key_BossExit2 = types.InlineKeyboardButton(text='Использовать Свиток для Атаки', callback_data='BossExit2')
        keygameQuest41.add(key_BossExit2)
        bot.send_photo(chat_id=message.chat.id, photo=photo28,
                       caption="Вы отказались от амулета.\nДемон оскалился и сказал:\n- \"Что ж, как знаешь, посмотрим "
                               "как ты справишься с Сашаелем\"\nВы отправились дальше и встретили Сашаеля",
                       reply_markup=keygameQuest41)

    @staticmethod
    def gameQuest_handler(call):
        if call.data == "Quest":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Поиграем?")
            GameQuest.GameQuestStart(call.message)
            updateStatistic(call.message, "Quest")
        elif call.data == "startQuest":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Questt(call.message)
        elif call.data == "exitQuest":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хорошо, тогда в другой раз!")
        elif call.data == "askTraveler":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Quest2(call.message, True)
        elif call.data == "blacksmith":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.QuestBlacksith1(call.message, 'Привет. Я кузнец этого города, чем могу тебе помочь?')

        elif call.data == "Market":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Quest2(call.message, False)
        elif call.data == "Castle":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.QuestCastle1(call.message)
        elif call.data == "CastleOver":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo5 = open('../resources/GameQuest/gameOver.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo5,
                           caption='Судя по всему, впереди опасные скелеты-гоблины, про которых предупреждал '
                                   'путник\nСкелеты '
                                   'атаковали вас. Так как Вы были без доспехов, скелеты без особого труда смертельно '
                                   'ранили Вас. Вы погибли.\n\n '
                                   'Попробуйте начать с начала')
        elif call.data == "CastleDracon":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo6 = open('../resources/GameQuest/dragonOver.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo6,
                           caption='Вас заметила дракон. К сожалению или к счастью, Вы ей понравились, она посадил вас на '
                                   'цепь и '
                                   'теперь вы будете до конца жизни жить с драконом\n\nПопробуйте начать с начала')
        elif call.data == "CastleBlacksith":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.QuestBlacksith1(call.message,
                            "Это жуткое место, которое охраняют толпы скелетов и злобный дракон. Говорят, что тот дракон "
                            "охраняет много золота, но никто так и не рискнул побороть его и забрать богатства.")
        elif call.data == "MarketBlacksith":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.QuestBlacksith1(call.message,
                            "Мэр города дал всем выходной в связи с нападками бандитов, которые находятся за "
                            "городом. Сегодня работаю только я")
        elif call.data == "ArmorBlacksith":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.BlacksithPurchase(call.message, False)
        elif call.data == "PriceArmor":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Outlaw(call.message)
        elif call.data == "WoodMetal":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.ResourceExtraction(call.message)
        elif call.data == "TreeMining":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.TreeMining(call.message)
        elif call.data == "MetalMining":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.MetalMining(call.message)
        elif call.data == "BuyArmor":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.BlacksithPurchase(call.message, False)
        elif call.data == "OutlawNo":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.BlacksithPurchase(call.message, False)
        elif call.data == "OutlawYes":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.BanditBattle(call.message)
        elif call.data == "BanditDogovor":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.BanditDogovor(call.message)
        elif call.data == "BanditBattle":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.BanditBattleExit(call.message)
        elif call.data == "DieBandit":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo9 = open('../resources/GameQuest/banditубил.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo9,
                           caption="Вы отдали золото и уже собрались идти обратно в город, но глава Бандитов ударил "
                                   "мечом вас в спину.\n\nВы умерли!!! Попробуйте начать сначала")
        elif call.data == "BanditBattle2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.BanditBattleExit(call.message)
        elif call.data == "BlowHead":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo10 = open('../resources/GameQuest/banditубил.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo10,
                           caption="Весь урон на себя принял шлем, Бандит не пострадал и ударил мечом вас в шею.\n\nВы "
                                   "погибли.\nПопробуйте начать сначала")
        elif call.data == "HeartBeat":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.ReceivingMoney(call.message)
        elif call.data == "ReceivingMoney":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.BlacksmithArmorPayment(call.message)
        elif call.data == "QuestCastle1NO":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Quest2(call.message, False)
        elif call.data == "BlacksmithArmorPayment":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Castle(call.message)
        elif call.data == "CastleArmor":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.СhoosePath(call.message)
        elif call.data == "MetalMiningExit":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.MistakeBroken(call.message)
        elif call.data == "MistakeBroken":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.BlacksithPurchase(call.message, True)
        elif call.data == "TreeMiningExit":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo17 = open('../resources/GameQuest/brogenaxe.jpg', 'rb')
            keygameQuest16 = types.InlineKeyboardMarkup()
            key_MistakeBroken = types.InlineKeyboardButton(text='Вернуться к кузнецу', callback_data='MistakeBroken')
            keygameQuest16.add(key_MistakeBroken)
            bot.send_photo(chat_id=call.message.chat.id, photo=photo17,
                           caption="Вы сломали свой Топор. Возвращайтесь обратно к кузнецу",
                           reply_markup=keygameQuest16)
        elif call.data == "MetalMiningON":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.GotIt(call.message)
        elif call.data == "TreeMiningON":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo18 = open('../resources/GameQuest/дерево.jpg', 'rb')
            keygameQuest17 = types.InlineKeyboardMarkup()
            key_GotIt = types.InlineKeyboardButton(text='Пойти к кузнецу за доспехами', callback_data='GotIt')
            keygameQuest17.add(key_GotIt)
            bot.send_photo(chat_id=call.message.chat.id, photo=photo18,
                           caption="Вы Добыли Дерево\nВозвращайтесь обратно к кузнецу",
                           reply_markup=keygameQuest17)
        elif call.data == "GotIt":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo19 = open('../resources/GameQuest/Куз2нец.jpg', 'rb')
            keygameQuest15 = types.InlineKeyboardMarkup()
            key_CastleArmor = types.InlineKeyboardButton(text='Отправиться к Жуткому заброшенному замку',
                                                         callback_data='CastleArmor')
            keygameQuest15.add(key_CastleArmor)
            bot.send_photo(chat_id=call.message.chat.id, photo=photo19,
                           caption="Вы прибыли к кузнецу\nПривет, я очень рад что ты все добыл, вот держи свои доспехи",
                           reply_markup=keygameQuest15)
        elif call.data == "СhoosePathDragon":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.DragonDialogue(call.message)
        elif call.data == "DragonDialogue":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.DragonExit(call.message)
        elif call.data == "DragonExitGold":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo20 = open('../resources/GameQuest/жеказолото.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo20,
                           caption="Отныне Вы самый богатый человек Мира. Вся ваша жизнь пройдет в роскоши и "
                                   "сытости\n\nНебольшой подарок за прохождение игры\nНабор стикеров ZhekaMatuxovbot в "
                                   "средеземье\nhttps://t.me/addstickers/ZhekaMatuxovbot")
        elif call.data == "DragonExitLove":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo21 = open('../resources/GameQuest/жекалюбовь.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo21,
                           caption="Дракон достает золотую фигурку девушки из своих скоровищ и преврашает ее в живую "
                                   "девушку из ваших фантазий. Она влюбилась в Вас с первого взгляда. Вы возвращаетесь "
                                   "домой и живете долго и счастливо\n\nНебольшой подарок за прохождение игры\nНабор "
                                   "стикеров ZhekaMatuxovbot в средеземье\nhttps://t.me/addstickers/ZhekaMatuxovbot")
        elif call.data == "DragonExitOver":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo22 = open('../resources/GameQuest/жекаумер.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo22,
                           caption="Дракон полон ярости\nДракон со словами: \"Да как ты смеешь!!!\". Накинулся на вас. От "
                                   "Вас остались только доспехи")
        elif call.data == "СhoosePathCastle":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.SkeletonsOfbBry(call.message)
        elif call.data == "SkeletonsOfbBry":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Ingot(call.message)
        elif call.data == "IngotYes":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Demon(call.message)
        elif call.data == "Demon":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Demon2(call.message)
        elif call.data == "Demon2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Demon3(call.message)
        elif call.data == "DemonAmuletYes":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Boss1(call.message)
        elif call.data == "DemonAmuletNo":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Boss2(call.message)
        elif call.data == "BossAmuletYes":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Demon4(call.message)
        elif call.data == "BossAmuletNo":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo30 = open('../resources/GameQuest/killgeka.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo30,
                           caption="Вы нанесли удар по противнику, но вашей силы удара не хватило, чтобы нанести сильные "
                                   "повреждения. Противник размахнулся и резкими движениями косой разделил Ваше тело на "
                                   "три части "
                                   "\n\nВЫ ПОГИБЛИ")
        elif call.data == "BossExit":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.SashaelKill(call.message)
        elif call.data == "Demon4":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.Demon5(call.message)
        elif call.data == "DemonHeartYes":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.MainBoss(call.message)
        elif call.data == "DemonHeartNo":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.MainBoss2(call.message)
        elif call.data == "MainBossExit":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.VinBoss(call.message)
        elif call.data == "VinBoss":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo36 = open('../resources/GameQuest/finalgood.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo36,
                           caption="Вы освободили девушку и забрали золото. Вскоре, вы с ней поженились и купили огромный "
                                   "дом. Вы прожили долгую и счастливую жизнь.\n\nНебольшой подарок за прохождение "
                                   "игры\nНабор стикеров ZhekaMatuxovbot в "
                                   "средеземье\nhttps://t.me/addstickers/ZhekaMatuxovbot")
        elif call.data == "MainBossNo":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo37 = open('../resources/GameQuest/жекуубилбос.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo37,
                           caption="Вы попытались нанести удар, но Листат оказался быстрее. Он увернулся от вашей атаки и "
                                   "ловким ударом снес с плеч вашу голову. Вы погибили, а он продолжил развлекаться со "
                                   "своей пленницей.")
        elif call.data == "SashaelKill":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.SashaelKill2(call.message)
        elif call.data == "SashaelKillYes":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.MainBoss4(call.message)
        elif call.data == "SashaelKillNo":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.MainBoss3(call.message)
        elif call.data == "Died":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo41 = open('../resources/GameQuest/жекуубилбос.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo41,
                           caption="Вы попытались нанести удар, но Листат оказался быстрее. Он увернулся от нашей атаки и "
                                   "ловким ударом снес с плеч вашу голов. Вы погибили, а он продолжил развлекаться со "
                                   "своей пленницей.")
        elif call.data == "ScrollAttack":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.VinBoss2(call.message)
        elif call.data == "VinBoss2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.TenYears(call.message)
        elif call.data == "TenYears":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo44 = open('../resources/GameQuest/Умерласемья.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo44,
                           caption="Прошло десять лет. В один из прекрасных солнечных дней Вы возвращаетесь домой и "
                                   "видите ужасную картину. По дому разбросаны части тел всей вашей семьи и прислуги. А "
                                   "на стене написано кровью: Зря ты решил со мной поссориться, смертный.")
        elif call.data == "HeartAttack":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.JekaDemon(call.message)
        elif call.data == "JekaDemon":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.JekaDemon2(call.message)
        elif call.data == "JekaDemon2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo47 = open('../resources/GameQuest/gekaKing.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo47,
                           caption="Когда Вы закончили, Вы осознали, что отныне Вы являетесь хозяином этой башни. "
                                   "Вы больше никогда не сможете жить без пожирания этого вкуснейшего человеческого "
                                   "мяса.\nВы стали владыкой тьмы")
        elif call.data == "Died2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo48 = open('../resources/GameQuest/жекуубилбос.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo48,
                           caption="Вы попытались нанести удар, но Листат оказался быстрее. Он увернулся от нашей атаки и "
                                   "ловким ударом снес с плеч вашу голов. Вы погибили, а он продолжил развлекаться со "
                                   "своей пленницей.")
        elif call.data == "HeartAttack2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.JekaDemon(call.message)
        elif call.data == "SwordAttack":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo49 = open('../resources/GameQuest/bladeOfSouls.jpg', 'rb')
            keygameQuest30 = types.InlineKeyboardMarkup()
            key_VinBoss = types.InlineKeyboardButton(text='Освободить девушку и забрать золото', callback_data='VinBoss')
            keygameQuest30.add(key_VinBoss)
            bot.send_photo(chat_id=call.message.chat.id, photo=photo49,
                           caption="Вы ощутили как меч начал вибрировать, через мгновение из противника полилась "
                                   "жизненная энергия и начала подпитывать меч бездны. Вы решили не тратить времени и "
                                   "предприняли попытку атаковать. Судя по всему, меч Бездны не оставил противнику сил "
                                   "даже попытаться отбить удар. С помощью своего нового оружия вы выпотрошили Листата "
                                   "как свинью", reply_markup=keygameQuest30)
        elif call.data == "BossAmuletNo2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            photo30 = open('../resources/GameQuest/killgeka.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=photo30,
                           caption="Вы нанесли удар по противнику, но вашей силы удара не хватило, чтобы нанести сильные "
                                   "повреждения. Противник размахнулся и резкими движениями косой разделил Ваше тело на "
                                   "три части "
                                   "\n\nВЫ ПОГИБЛИ")
        elif call.data == "BossExit2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            GameQuest.SashaelKill(call.message)