
from string import digits
import functionsTask1TVShopGUI


def main():
    print(f'{__name__}: начало работы\n')


    Task_ClassWork005()
    while(1):
        Task_HomeWork005()
        cnt = input("""
\033[0m \033[34;47mВыберите пункт:\033[0m """)
        choose = -1
        if(cnt in digits):
            choose = int(cnt)
        if choose == 1:
            pass
            functionsTask1TVShopGUI.Task_Task1()
            functionsTask1TVShopGUI.Run_Task1()

        elif choose == 2:
            pass
#            functionsTask2.Task_Task2()
#            functionsTask2.Run_Task2()

        elif choose == 3:
            pass
#            functionsTask3.Task_Task3()
#            functionsTask3.Run_Task3()
    
        elif choose == 4:
            pass
    
        elif choose == 0:
            # from MainHomeWork import main
            # main()
            break


def Task_HomeWork005():
    print('''\t\033[0m \033[34;47mMENU\033[0m
    1 - Task1.
    0 - Exit from Programm
    ''')

def Task_ClassWork005():
    print('''\t\033[0m \033[34;47mТеоретическая часть
\033[0m
•	Понятие о графическом интерфейсе пользователя, встроенный модуль tkinter 
•	Создание окна приложения 
•	Экранные кнопки – объекты класса Button
•	Некоторые свойства кнопок
•	Назначение функции-обработчика команды кнопки
•	Вывод статического текста – объект класса Label
•	Изменение данных в элементах отображения (виджетах) – классы StringVar, IntVar, DoubleVar, BooleanVar 
•	Привязка Var – объектов к виджетам, свойство textvariable
•	Изменение свойств виджета при помощи метода config() виджета
•	Позиционирование виджетов в окне, метод pack() – позиционирование по сторонам окна
•	Позиционирование элементов методом place()
•	Позиционирование элементов методом grid()
•	Задание размеров элементов интерфейса пользователя
•	Использование стандартной функции reduce() для накопления сумм в коллекции
•	Использование Label для вывода изображений
•	Использование Entry для ввода данных
•	Использование флажка Checkbutton
•	Использование переключателей с зависимой фиксацией Radiobutton
•	Элемент интерфейса Listbox
•	Элемент интерфейса ComobBox
•	Создание меню в приложении средствами tkinter



\033[0m \033[34;47mПрактическая часть
\033[0m
\tРазработайте приложение Python с использованием Tkinter.
''')



# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    # from Main import main
    main()
# end if
