
def Task_Task3dictionary():
    print(
        '''
        Task3. Обработка словарей. Разработайте функцию, в которой используется словарь с названиями ряда государств и их столицами. Функция должна обеспечивать:
\t- вывод столицы заданного государства;
\t- вывод государства, столицей которого является заданный город.
Если заданного государства или города в словаре нет, на экран должно выводиться соответствующее сообщение.
'''
        )

def Run_Task3dictionary():
    
    getCountries()
    country = input("Введите страну из приведенных выше: ")
    getCountryTown(country)
    print()

    getCountryTowns()
    countrytown = input("Введите город из приведенных выше: ")
    getCountry(countrytown)
    print()
    
countries = {"Австралия":"Канберра",
"Австрия":"Вена",
"Азербайджан":"Баку",
"Албания":"Тирана",
"Алжир":"Алжир",
"Ангола":"Луанда",
"Андорра":"Андорра-ла-Велья",
"Антигуа и Барбуда":"Сент-Джонс",
"Аргентина":"Буэнос-Айрес",
"Армения":"Ереван",
"Афганистан":"Кабул",
"Багамы":"Нассау",
"Бангладеш":"Дакка",
"Барбадос":"Бриджтаун",
"Беларусь":"Минск",
"Белиз":"Бельмопан",
"Бельгия":"Брюссель",
"Бенин":"Порто-Ново",
"Болгария":"София",
"Боливия":"Сукре",
"Босния и Герцеговина":"Сараево",
"Ботсвана":"Габороне",
"Бразилия":"Бразилиа",
"Бруней":"Бандар-Сери-Багаван",
"Буркина Фасо":"Уагадугу",
"Бурунди":"Бужумбура",
"Бутан":"Тхимпху",
"Вануату":"Порт-Вила",
"Ватикан":"Ватикан",
"Великобритания":"Лондон",
"Венгрия":"Будапешт",
"Венесуэла":"Каракас",
"Восточный":"Тимор	Дили",
"Вьетнам":"Ханой",
"Габон":"Либревиль",
"Гаити":"Порт-о-Пренс",
"Гайана":"Джорджтаун",
"Гамбия":"Банжул",
"Гана":"Аккра",
"Гватемала":"Гватемала",
"Гвинея":"Конакри",
"Гвинея-Бисау":"Бисау",
"Германия":"Берлин",
"Гондурас":"Тегусигальпа",
"Гренада":"Сент-Джорджес",
"Греция":"Афины",
"Грузия":"Тбилиси",
"Дания":"Копенгаген",
"Джибути":"Джибути",
"Доминика":"Розо",
"Доминиканская Республика":"Санто-Доминго",
"Египет":"Каир",
"Замбия":"Лусака",
"Зимбабве":"Хараре",
"Израиль":"Иерусалим",
"Индия":"Нью-Дели",
"Индонезия":"Джакарта",
"Иордания":"Амман",
"Ирак":"Багдад",
"Иран":"Тегеран",
"Ирландия":"Дублин",
"Исландия":"Рейкьявик",
"Испания":"Мадрид",
"Италия":"Рим",
"Йемен":"Сана",
"Кабо-Верде":"Прая",
"Казахстан":"Астана",
"Камбоджа":"Пномпень",
"Камерун":"Яунде",
"Канада":"Оттава",
"Катар":"Доха",
"Кения":"Найроби",
"Кипр":"Никосия",
"Киргизия":"Бишкек",
"Кирибати":"Южная Тарава",
"Китай":"Пекин",
"Колумбия":"Санта-Фе-де-Богота",
"Коморы":"Морони",
"Конго":"демократическая республика	Киншаса",
"Конго":"республика	Браззавиль",
"Коста-Рика":"Сан-Хосе",
"Кот-д`Ивуар":"Ямусукро",
"Куба":"Гавана",
"Кувейт":"Эль-Кувейт",
"Лаос":"Вьентьян",
"Латвия":"Рига",
"Лесото":"Масеру",
"Либерия":"Монровия",
"Ливан":"Бейрут",
"Ливия":"Триполи",
"Литва":"Вильнюс",
"Лихтенштейн":"Вадуц",
"Люксембург":"Люксембург",
"Маврикий":"Порт-Луи",
"Мавритания":"Нуакшот",
"Мадагаскар":"Антананариву",
"Македония":"Скопье",
"Малави":"Лилонгве",
"Малайзия":"Куала-Лумпур",
"Мали":"Бамако",
"Мальдивы":"Мале",
"Мальта":"Валлетта",
"Марокко":"Рабат",
"Маршалловы Острова":"Маджуро",
"Мексика":"Мехико",
"Мозамбик":"Мапуту",
"Молдавия":"Кишинев",
"Монако":"Монако",
"Монголия":"Улан-Батор",
"Мьянма":"Найпьидо",
"Намибия":"Виндхук",
"Науру":"официальной столицы не имеет",
"Непал":"Катманду",
"Нигер":"Ниамей",
"Нигерия":"Абуджа",
"Нидерланды":"Амстердам",
"Никарагуа":"Манагуа",
"Новая Зеландия":"Веллингтон",
"Норвегия":"Осло",
"Объединенные Арабские Эмираты":"Абу-Даби",
"Оман":"Маскат",
"Пакистан":"Исламабад",
"Палау":"Мелекеок",
"Панама":"Панама",
"Папуа - Новая Гвинея":"Порт-Морсби",
"Парагвай":"Асунсьон",
"Перу":"Лима",
"Польша":"Варшава",
"Португалия":"Лиссабон",
"Россия":"Москва",
"Руанда":"Кигали",
"Румыния":"Бухарест",
"Сальвадор":"Сан-Сальвадор",
"Самоа":"Апиа",
"Сан-Марино":"Сан-Марино",
"Сан-Томе и Принсипи":"Сан-Томе",
"Саудовская Аравия":"Эр-Рияд",
"Свазиленд":"Мбабане",
"Северная Корея":"Пхеньян",
"Сейшелы":"Виктория",
"Сенегал":"Дакар",
"Сент-Винсент и Гренадины":"Кингстаун",
"Сент-Китс и Невис":"Бастер",
"Сент-Люсия":"Кастри",
"Сербия":"Белград",
"Сингапур":"Сингапур",
"Сирия":"Дамаск",
"Словакия":"Братислава",
"Словения":"Любляна",
"Соединенные Штаты Америки":"Вашингтон",
"Соломоновы Острова":"Хониара",
"Сомали":"Могадишо",
"Судан":"Хартум",
"Суринам":"Парамарибо",
"Сьерра-Леоне":"Фритаун",
"Таджикистан":"Душанбе",
"Таиланд":"Бангкок",
"Танзания":"Додома",
"Того":"Ломе",
"Тонга":"Нукуалофа",
"Тринидад и Тобаго":"Порт-оф-Спейн",
"Тувалу":"Фунафути",
"Тунис":"Тунис",
"Туркмения":"Ашхабад",
"Турция":"Анкара",
"Уганда":"Кампала",
"Узбекистан":"Ташкент",
"Украина":"Киев",
"Уругвай":"Монтевидео",
"Федеративные штаты Микронезии":"Паликир",
"Фиджи":"Сува",
"Филиппины":"Манила",
"Финляндия":"Хельсинки",
"Франция":"Париж",
"Хорватия":"Загреб",
"Центрально-Африканская Республика":"Банги",
"Чад":"Нджамена",
"Черногория":"Подгорица",
"Чехия":"Прага",
"Чили":"Сантьяго",
"Швейцария":"Берн",
"Швеция":"Стокгольм",
"Шри-Ланка":"Коломбо",
"Эквадор":"Кито",
"Экваториальная Гвинея":"Малабо",
"Эритрея":"Асмэра",
"Эстония":"Таллин",
"Эфиопия":"Аддис-Абеба",
"Южная Корея":"Сеул",
"Южно-Африканская Республика":"Претория",
"Ямайка":"Кингстон",
"Япония":"Токио"}

def getCountries():
    '''Get All Countries.'''
    try:
        print("Countries")
        for item in countries.keys():
            print(item);
        print()

    except Exception:
        print("Общее исключение")

def getCountryTown(country):
    '''Return Main Town current Country.'''
    try:
        print(f"Main Town in Country {country}")
        print(countries.get(country,"key not found"))

    except Exception:
        print("Общее исключение")

def getCountryTowns():
    '''Get All Country Towns.'''
    try:
        print("Country Towns")
        for item in countries.values():
            print(item)
        print()

    except Exception:
        print("Общее исключение")

def getCountry(countrytown):
    '''Return Country by current Country Town.'''
    try:
        print(f"Country with Country Town {countrytown}")
        flag = False
        for key,value in countries.items():
            if(value == countrytown):
                flag = True
                print(key)
                break
        if(flag==False):
            print(f"Do not found Country with this Country Town {countrytown}")

    except Exception:
        print("Общее исключение")

# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork003 import main
    main()
# end if