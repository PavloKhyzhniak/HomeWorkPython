import random
import functionsProc17
import functionsProc21
import functionsProc28


def main():
    print(f'{__name__}: начало работы\n')
    random.seed()

    Task_ClassWork001()
    while(1):
        Task_HomeWork001()
        choose = int(input("""
\033[0m \033[34;47mВыберите пункт:\033[0m """))
        if choose == 1:
            functionsProc17.Task_Proc17()
            for r in range(3):
                a = random.randint(0,100)
                b = random.randint(0,100)
                c = random.randint(0,100)
                functionsProc17.Run_Proc17(a,b,c)
            
        elif choose == 2:
            functionsProc21.Task_Proc21()
            for r in range(5):
                a = random.randint(0,100)
                #b = random.randint(a,100+a)
                b = random.randint(0,100)
                functionsProc21.Run_Proc21(a,b)
            
        elif choose == 3:
            functionsProc28.Task_Proc28()
            cnt = 0
            for r in range(0,15):
                a = random.randint(-120 , 250)
                if(functionsProc28.Run_Proc28(a)):
                    cnt+=1
            print("Было найдено из 15 случайных чисел:{0} простых чисел".format(cnt))
            
        elif choose == 0:
            pass
            break
            # from MainHomeWork import main
            # main()
            
def Task_HomeWork001():
    print('''\t\033[0m \033[34;47mMENU\033[0m
    1 - Proc17
    2 - Proc21
    3 - Proc28
    0 - Exit from Programm
    ''')

def Task_ClassWork001():
    print('''\t\033[0m \033[34;47mТеоретическая часть
\033[0m
•	Переменные в Python, типы данных в Python
•	Ввод и вывод переменных
•	Арифметические операции в Python
•	Операции сравнения в Python
•	Логические операции в Python
•	Импорт модулей, модуль math
•	Использование функций и констант из модуля math
•	Условный оператор в Python
•	Краткая форма условного оператора if cond: op
•	Полная форма условного оператора if cond: op else: op
•	Лестничная форма условного оператора if cond: op elif cond: op else: op
•	Условное выражение op1 if cond else op2
•	Циклы в Python
•	Цикл while – else
•	Цикл for – else
•	Ключевые слова break, continue
•	Ключевое слово pass
•	Функции в Python – объявление и вызов
•	Передача параметров в функцию – по значению, по имени
•	Параметры по умолчанию
•	Возврат значения из функции
•	Понятие о модулях в Python
•	Организация модуля, импорт модуля, отдельной функции из модуля
•	Обработка ошибок времени исполнения при помощи исключений в Python 
•	Синтаксис использования исключений try: except: finally:
•	Получение информации об исключении 
•	Выброс исключения – оператор raise

\033[0m \033[34;47mПрактическая часть
\033[0m
\tРазработайте консольное приложение Python в составе главного модуля main.py, модуля functions.py с функциями, указанными в задачах и модуля app.py в котором разместить функции решения задач (например, решение задачи Proc17 – в функции proc17).
\tВ функциях из модуля functions проверять корректность входных параметров. Выбрасывать исключение Exception при обнаружении некорректных значений.
\tОбрабатывать исключения в функциях модуля app, а также в функции main().
    ''')

    
# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    # from Main import main
    main()
# end if
