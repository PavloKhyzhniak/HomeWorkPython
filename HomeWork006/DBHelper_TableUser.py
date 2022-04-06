# работаем с SQLite
# https://python-scripts.com/sqlite
import datetime
import os
import sqlite3
import sys
from typing import Iterable

from DBHelper_Base import DBHelper_Base


class DBHelper_TableUser(DBHelper_Base):
    def create_table_user(database_path, table_name):   
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS """ + table_name + """ (
        Id         INTEGER      PRIMARY KEY AUTOINCREMENT
                            NOT NULL
                            UNIQUE,
    FirstName  VARCHAR (40) NOT NULL,
    SecondName VARCHAR (40),
    LastName   VARCHAR (40) NOT NULL,
    BirthDate  DATE,
    AddressId  INT          REFERENCES Address (Id) 
        )
        """)
        print('create table: Ok\n')


    def insert(database_path, data:tuple):    
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Вставляем данные в таблицу
        res = cursor.execute(
            """INSERT INTO User 
                  (FirstName,SecondName,LastName,BirthDate,AddressId)
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
        "INSERT INTO User (FirstName,SecondName,LastName,BirthDate,AddressId) VALUES (?,?,?,?,?)",
        datas
        )

        conn.commit()
        print('insert many: Ok\n')


    def print_list_special(list):
        for (ID,Id, FirstName,SecondName,LastName,BirthDate,AddressId) in list:
            print(f"| {str(ID):5} | {str(Id):5} | {str(FirstName):10} | {str(SecondName):10} | {str(LastName):10} | {str(BirthDate):10} | {str(AddressId):10} |")


    def print_list_special2(list):
        for row in list:
            print(f"| {str(row[0]):5} | {str(row[1]):5} | {str(row[2]):25} | {str(row[3]):25} | {str(row[4]):25} | {str(row[5]):25} | {str(row[6]):25} |")



    def test(database_path):
        # DBHelper_Base.drop_table(database_path,'Address')   
        # DBHelper_Base.insert(database_path, ('Mira', 80,2))    
        # DBHelper_Base.insertmany(database_path,[('Mira', 80,2)]])
        DBHelper_Base.update_by(database_path,'User','LastName',('Grogg','Groove'))    
        DBHelper_Base.delete_by(database_path,'User','LastName','Groove')
        list = DBHelper_Base.find_by(database_path,'User','LastName','Jera')
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.find_by_like(database_path,'User','LastName','%il%')
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.getAll(database_path,'User','FirstName')
        DBHelper_Base.print_list(list)
            
        # DBHelper_TableDoctors.create_table_address(database_path, table_name)   
        DBHelper_TableUser.insert(database_path,('Billy','Villy','Tilly',datetime.date(2007, 12, 5).strftime('%Y-%m-%d'),4))
        list = DBHelper_Base.getAll(database_path,'User','SecondName')
        DBHelper_Base.print_list(list)
        
        # Вставляем множество данных в таблицу используя безопасный метод "?"
        datas = [
('Billy','Gorette','Tulka',datetime.date(1987, 12, 5).strftime('%Y-%m-%d'),4),
('Fred','Jokerrina','Meffa',datetime.date(2007, 11, 15).strftime('%Y-%m-%d'),4),
('Liza','Dillayla','Askola',datetime.date(1987, 2, 5).strftime('%Y-%m-%d'),4),
('Sonya','Agafa','Surta',datetime.date(2007, 12, 5).strftime('%Y-%m-%d'),4),
('Freya','Polina','Marmelka',datetime.date(1987, 1, 25).strftime('%Y-%m-%d'),4),
('Ella','Richardson','Olka',datetime.date(1997, 10, 5).strftime('%Y-%m-%d'),4),
('Kelly','Geela','Nutta',datetime.date(2004, 12, 5).strftime('%Y-%m-%d'),4),
('Vika','Nilla','Kasseya',datetime.date(2017, 12, 5).strftime('%Y-%m-%d'),4)
        ]

        DBHelper_TableUser.insertmany(database_path,datas)
        list = DBHelper_Base.getAll(database_path,'User','')
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.getAll(database_path,'User','')
        DBHelper_TableUser.print_list_special(list)
        list = DBHelper_Base.getAll(database_path,'User','')
        DBHelper_TableUser.print_list_special2(list)


pywinauto_path = os.path.abspath(__file__)
pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
database_path = pywinauto_path + "/HomeWork006/db/SQLite_Hospital.db"
DBHelper_TableUser.test(database_path)
