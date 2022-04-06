# работаем с SQLite
# https://python-scripts.com/sqlite
import datetime
import os
import sqlite3
import sys
from typing import Iterable

from DBHelper_Base import DBHelper_Base


class DBHelper_TableVisit(DBHelper_Base):
    def create_table_visit(database_path, table_name):   
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS """ + table_name + """ (
        Id        INTEGER  PRIMARY KEY AUTOINCREMENT
                       UNIQUE
                       NOT NULL,
    DoctorId           REFERENCES Doctors (Id) 
                       NOT NULL,
    PatientId          REFERENCES Patient (Id) 
                       NOT NULL,
    Price     INT      DEFAULT (1000) 
                       NOT NULL,
    Date      DATETIME NOT NULL 
        )
        """)
        print('create table: Ok\n')


    def insert(database_path, data:tuple):    
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Вставляем данные в таблицу
        res = cursor.execute(
            """INSERT INTO Visit 
                  (DoctorId,PatientId,Price,Date)
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
        "INSERT INTO Visit (DoctorId,PatientId,Price,Date) VALUES (?,?,?,?)",
        datas
        )

        conn.commit()
        print('insert many: Ok\n')


    def print_list_special(list):
        for (ID,Id, DoctorId,PatientId,Price,Date) in list:
            print(f"| {str(ID):5} | {str(Id):5} | {str(DoctorId):10} | {str(PatientId):10} | {str(Price):10} | {str(Date):10} |")


    def print_list_special2(list):
        for row in list:
            print(f"| {str(row[0]):5} | {str(row[1]):5} | {str(row[2]):25} | {str(row[3]):25} | {str(row[4]):25} | {str(row[5]):25} |")



    def test(database_path):
        # DBHelper_Base.drop_table(database_path,'Address')   
        # DBHelper_Base.insert(database_path, ('Mira', 80,2))    
        # DBHelper_Base.insertmany(database_path,[('Mira', 80,2)]])
        DBHelper_Base.update_by(database_path,'Visit','DoctorId',(4,3))    
        DBHelper_Base.delete_by(database_path,'Visit','DoctorId',2)
        list = DBHelper_Base.find_by(database_path,'Visit','DoctorId',4)
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.find_by_like(database_path,'Visit','DoctorId','%5%')
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.getAll(database_path,'Visit','PatientId')
        DBHelper_Base.print_list(list)
            
        # DBHelper_TableDoctors.create_table_address(database_path, table_name)   
        DBHelper_TableVisit.insert(database_path,(4,5,1234,datetime.date(2007, 12, 5).strftime('%Y-%m-%d')))
        list = DBHelper_Base.getAll(database_path,'Visit','Price')
        DBHelper_Base.print_list(list)
        
        # Вставляем множество данных в таблицу используя безопасный метод "?"
        datas = [
(2,3,356,datetime.date.today().strftime('%Y-%m-%d')),
(3,4,346,datetime.date.today().strftime('%Y-%m-%d')),
(4,5,345,datetime.date.today().strftime('%Y-%m-%d')),
(5,6,1456,datetime.date.today().strftime('%Y-%m-%d')),
(6,7,326,datetime.date.today().strftime('%Y-%m-%d')),
(7,8,3116,datetime.date.today().strftime('%Y-%m-%d')),
(8,9,3411,datetime.date.today().strftime('%Y-%m-%d')),
(9,1,156,datetime.date.today().strftime('%Y-%m-%d'))
        ]

        DBHelper_TableVisit.insertmany(database_path,datas)
        list = DBHelper_Base.getAll(database_path,'Visit','')
        DBHelper_Base.print_list(list)
        list = DBHelper_Base.getAll(database_path,'Visit','')
        DBHelper_TableVisit.print_list_special(list)
        list = DBHelper_Base.getAll(database_path,'Visit','')
        DBHelper_TableVisit.print_list_special2(list)

pywinauto_path = os.path.abspath(__file__)
pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
database_path = pywinauto_path + "/HomeWork006/db/SQLite_Hospital.db"
DBHelper_TableVisit.test(database_path)
