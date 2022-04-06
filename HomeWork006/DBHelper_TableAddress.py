# работаем с SQLite
# https://python-scripts.com/sqlite
import os
import sqlite3
import sys
from typing import Iterable

from DBHelper_Base import DBHelper_Base


class DBHelper_TableAddress(DBHelper_Base):
    def create_table_address(database_path, table_name):   
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS """ + table_name + """ (
        Id INTEGER PRIMARY KEY AUTOINCREMENT
                            NOT NULL
                            UNIQUE,
        Street     VARCHAR (40) NOT NULL,
        House      INT          NOT NULL,
        Appartment INT
        )
        """)

        print('create table: Ok\n')


    def insert(database_path, data:tuple):    
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Вставляем данные в таблицу
        res = cursor.execute(
            """INSERT INTO Address 
                  (Street, House, Appartment)
              VALUES
            """ + str(data)
        )

        # Сохраняем изменения
        conn.commit()
        print('insert: Ok\n')


    def insertmany(database_path,datas:Iterable):
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        cursor.executemany(
        "INSERT INTO Address (Street, House, Appartment) VALUES (?,?,?)",
        datas
        )

        conn.commit()
        print('insert many: Ok\n')


    def print_list_special(list):
        for (ID,Id, Street, House, Appartment) in list:
            print(f"| {str(ID):5} | {str(Id):5} | {str(Street):25} | {str(House):5} | {str(Appartment):5} |")


    def print_list_special2(list):
        for row in list:
            print(f"| {str(row[0]):5} | {str(row[1]):5} | {str(row[2]):25} | {str(row[3]):5} |")



    def test(database_path):
        # DBHelper_Base.drop_table(database_path,'Address')   
        # DBHelper_Base.insert(database_path, ('Mira', 80,2))    
        # DBHelper_Base.insertmany(database_path,[('Mira', 80,2)]])
        DBHelper_Base.update_by(database_path,'Address','Street',('mAKEEVKA','Makeevka'))    
        DBHelper_Base.delete_by(database_path,'Address','Street','mAKEEVKA')
        list = DBHelper_Base.find_by(database_path,'Address','House',2)
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.find_by_like(database_path,'Address','Street','%e%')
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.getAll(database_path,'Address','House')
        DBHelper_Base.print_list(list)
            
        # DBHelper_TableAddress.create_table_address(database_path, table_name)   
        DBHelper_TableAddress.insert(database_path,('Mira', 80,2))
        list = DBHelper_Base.getAll(database_path,'Address','House')
        DBHelper_Base.print_list(list)
        
        # Вставляем множество данных в таблицу используя безопасный метод "?"
        datas = [
        ('Mira', 60,1),
        ('Mira', 59,2),
        ('Mira', 58,3),
        ('Mira', 57,4),
        ('Mira', 56,5)
        ]

        DBHelper_TableAddress.insertmany(database_path,datas)
        list = DBHelper_Base.getAll(database_path,'Address','House')
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.getAll(database_path,'Address','Appartment')
        DBHelper_TableAddress.print_list_special(list)
        list = DBHelper_Base.getAll(database_path,'Address','House')
        DBHelper_TableAddress.print_list_special2(list)

pywinauto_path = os.path.abspath(__file__)
pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
database_path = pywinauto_path + "/HomeWork006/db/SQLite_Hospital.db"
DBHelper_TableAddress.test(database_path)
