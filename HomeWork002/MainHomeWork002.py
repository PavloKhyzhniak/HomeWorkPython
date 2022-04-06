import random
import functionsTask1tuples
import functionsTask2list
import functionsTask3dictionary
import functionsTask4sets


def Task_HomeWork002():
    print('''\t\033[0m \033[34;47mMENU\033[0m
    1 - Task1. Обработка кортежей. 
    2 - Task2. Обработка списков. 
    3 - Task3. Обработка словарей. 
    4 - Task4. Обработка множеств. 
    0 - Exit from Programm
    ''')

def Task_ClassWork002():
    print('''\t\033[0m \033[34;47mТеоретическая часть
\033[0m
•	Понятие о кортежах, возврат из функции более одного значения
•	Перебор всех элементов кортежа
•	Использование кортежей в кортежах
•	Создание списков
•	Доступ к элементам списков
•	Основные методы списков: добавление, удаление
•	Проверка значения на присутствие в списке
•	Встроенные функции Python для работы с коллекциями
•	Вложенные списки – списки списков
•	Понятие о парах «ключ – значение»
•	Создание словарей, коллекций пар «ключ – значение»
•	Добавление и удаление элементов в словари
•	Проверка наличия элемента в словаре – по ключу
•	Перебор элементов словаря
•	Сложные словари
•	Множества в Python – понятие
•	Создание множеств
•	Перебор элементов множества
•	Добавление и удаление элементов множества
•	Операции над множествами
•	Понятие о frozen set


\033[0m \033[34;47mПрактическая часть
\033[0m
\tРазработайте консольное приложение Python в составе главного модуля main.py, модуля utils.py со вспомогательными функциями и модуля app.py в котором разместить функции решения задач.
\tИспользуйте исключения. 
\tРеализуйте меню на базе словарей для выбора решаемой задачи, пунктов в решаемых задачах. 
  ''')


def main():
    print(f'{__name__}: начало работы\n')
    random.seed()

    Task_ClassWork002()
    while(1):
        Task_HomeWork002()
        choose = int(input("""
\033[0m \033[34;47mВыберите пункт:\033[0m """))
        if choose == 1:
            pass
            functionsTask1tuples.Task_Task1tuples()
            for r in range(3):
                x1 = random.randint(-100,100)
                y1 = random.randint(-100,100)
                x2 = random.randint(-100,100)
                y2 = random.randint(-100,100)
                P,S = functionsTask1tuples.Run_Task1tuples(x1,y1,x2,y2)
                print("Периметр = {0}; Площадь = {1}; Прямоугольника с вершинами ({2};{3}) и ({4},{5})".format(P,S,x1,y1,x2,y2))
            print()
            
        elif choose == 2:
            pass
            functionsTask2list.Task_Task2list()
            functionsTask2list.Run_Task2list()
            print()                  
            
        elif choose == 3:
            pass
            functionsTask3dictionary.Task_Task3dictionary()
            functionsTask3dictionary.Run_Task3dictionary()
            print()   
                
        elif choose == 4:
            pass
            functionsTask4sets.Task_Task4sets()
            functionsTask4sets.Run_Task4sets()
            print()   
                
        elif choose == 0:
            pass
            break
           # from MainHomeWork import main
            # main()
            



# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    # from Main import main
    main()
# end if
