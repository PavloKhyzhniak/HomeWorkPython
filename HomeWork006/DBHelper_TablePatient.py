# работаем с SQLite
# https://python-scripts.com/sqlite
import os
import sqlite3
import sys
from typing import Iterable

from DBHelper_Base import DBHelper_Base


class DBHelper_TablePatient(DBHelper_Base):
    def create_table_patient(database_path, table_name):   
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS """ + table_name + """ (
        Id     INTEGER PRIMARY KEY AUTOINCREMENT
                   UNIQUE
                   NOT NULL,
    UserId         REFERENCES User (Id) 
                   NOT NULL
        )
        """)
        print('create table: Ok\n')


    def insert(database_path, data:tuple):    
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Вставляем данные в таблицу
        res = cursor.execute(
            """INSERT INTO Patient 
                  (UserId)
              VALUES (
            """ + str(data) +")"
        )

        # Сохраняем изменения
        conn.commit()
        print('insert: Ok\n')


    def insertmany(database_path,datas:Iterable):
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        cursor.executemany(
        "INSERT INTO Patient ( UserId) VALUES (?)",
        datas
        )

        conn.commit()
        print('insert many: Ok\n')


    def print_list_special(list):
        for (ID,Id, UserId) in list:
            print(f"| {str(ID):5} | {str(Id):5} | {str(UserId):10} |")


    def print_list_special2(list):
        for row in list:
            print(f"| {str(row[0]):5} | {str(row[1]):5} | {str(row[2]):25} |")



    def test(database_path):
        # DBHelper_Base.drop_table(database_path,'Address')   
        # DBHelper_Base.insert(database_path, ('Mira', 80,2))    
        # DBHelper_Base.insertmany(database_path,[('Mira', 80,2)]])
        DBHelper_Base.update_by(database_path,'Patient','UserId',(1,2))    
        DBHelper_Base.delete_by(database_path,'Patient','UserId',6)
        list = DBHelper_Base.find_by(database_path,'Patient','UserId',4)
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.find_by_like(database_path,'Patient','UserId','%1%')
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.getAll(database_path,'Patient','UserId')
        DBHelper_Base.print_list(list)
            
        # DBHelper_TableDoctors.create_table_address(database_path, table_name)   
        DBHelper_TablePatient.insert(database_path,(6))
        list = DBHelper_Base.getAll(database_path,'Patient','UserId')
        DBHelper_Base.print_list(list)
        
        # Вставляем множество данных в таблицу используя безопасный метод "?"
        datas = [
        (4,),
        (5,),
        (6,),
        (7,),
        (8,)
        ]

        DBHelper_TablePatient.insertmany(database_path,datas)
        list = DBHelper_Base.getAll(database_path,'Patient','UserId')
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.getAll(database_path,'Patient','UserId')
        DBHelper_TablePatient.print_list_special(list)
        list = DBHelper_Base.getAll(database_path,'Patient','UserId')
        DBHelper_TablePatient.print_list_special2(list)

pywinauto_path = os.path.abspath(__file__)
pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
database_path = pywinauto_path + "/HomeWork006/db/SQLite_Hospital.db"
DBHelper_TablePatient.test(database_path)
