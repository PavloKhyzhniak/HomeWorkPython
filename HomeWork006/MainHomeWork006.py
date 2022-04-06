
from string import digits
import functionsTask1SQLiteHospital


def main():
    print(f'{__name__}: начало работы\n')


    Task_ClassWork006()
    while(1):
        Task_HomeWork006()
        cnt = input("""
\033[0m \033[34;47mВыберите пункт:\033[0m """)
        choose = -1
        if(cnt in digits):
            choose = int(cnt)
        if choose == 1:
            pass
            functionsTask1SQLiteHospital.Task_Task1()
            functionsTask1SQLiteHospital.Run_Task1()

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


def Task_HomeWork006():
    print('''\t\033[0m \033[34;47mMENU\033[0m
    1 - Task1.
    0 - Exit from Programm
    ''')

def Task_ClassWork006():
    print('''\t\033[0m \033[34;47mТеоретическая часть
\033[0m
•	Введение в работу с базой данных в Python – на примере модуля sqlite3
•	Реализация CRUD-операций

\033[0m \033[34;47mПрактическая часть
\033[0m
''')



# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    # from Main import main
    main()
# end if
