import os
import sys
import DBHelper_SQLite_Hospital
import DBHelper_TableAddress
import DBHelper_TableDoctors
import DBHelper_TablePatient
import DBHelper_TableUser
import DBHelper_TableVisit

def Task_Task1():
    print(
        '''
\tЗадача 1. Разработайте консольное приложение с использованием базы данных SQLite3. Выполните запросы по заданию. 
'''
        )

list_items = []            # список

def Run_Task1():
    pass
    task1()
    

def task1():
    try:
        pass     
        pywinauto_path = os.path.abspath(__file__)
        pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
        database_path = pywinauto_path + "/HomeWork006/db/SQLite_Hospital.db"
        input('Press Any Enter to See Special Request')
        DBHelper_SQLite_Hospital.DBHelper_SQLite_Hospital.test(database_path)
        # input('Press Any Enter to See Table Address')
        # DBHelper_TableAddress.DBHelper_TableAddress.test(database_path)
        # input('Press Any Enter to See Table Doctors')
        # DBHelper_TableDoctors.DBHelper_TableDoctors.test(database_path)
        # input('Press Any Enter to See Table Patient')
        # DBHelper_TablePatient.DBHelper_TablePatient.test(database_path)
        # input('Press Any Enter to See Table User')
        # DBHelper_TableUser.DBHelper_TableUser.test(database_path)
        # input('Press Any Enter to See Table Visit')
        # DBHelper_TableVisit.DBHelper_TableVisit.test(database_path)

    except Exception as ex:
        print("Общее исключение")
        print(ex)


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork006 import main
    main()
# end if