# работаем с SQLite
# https://python-scripts.com/sqlite
import datetime
import os
import sqlite3
import sys
from typing import Iterable


class DBHelper_SQLite_Hospital():
    def request01(database_path,value):   
# --Выбирает информацию о пациентах с фамилиями, начинающимися на заданную параметром последовательность букв
# select u.*,a.* from Patient p
# join User u on p.UserId = u.Id 
# join Address a on a.Id = u.AddressId 
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        list = cursor.execute(
            f" select u.*,a.* from Patient p \
                join User u on p.UserId = u.Id \
                join Address a on a.Id = u.AddressId \
                where u.LastName like '{value}' \
        ")
    
        print('request: Ok\n')

        print('# --Выбирает информацию о пациентах с фамилиями, начинающимися на заданную параметром последовательность букв')
        print(f"| {'Id':5} | {'FirstName':15} | {'SecondName':15} | {'LastName':15} | {'BirthDate':10} | {'Street':15} | {'House':15} | {'Appartment':15} |")
        print(f"|-----------------------------------------------------------------------------------------------------------------------------------------|")
        for row in list:
            print(f"| {str(row[0]):5} | {str(row[1]):15} | {str(row[2]):15} | {str(row[3]):15} | {str(row[4]):10} | {str(row[7]):15} | {str(row[8]):15} | {str(row[9]):15} |")


    def request02(database_path,value):   
# --Выбирает информацию о врачах, для которых значение в поле Процент отчисления на зарплату, больше 2.3% (задавать параметром)
# select d.* from Doctors d
# join User u on d.UserId = u.Id 
# join Address a on a.Id = u.AddressId 
# where d.Rate>2.3
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        list = cursor.execute(
            f"select d.*, u.* from Doctors d \
                join User u on d.UserId = u.Id \
                join Address a on a.Id = u.AddressId \
            where d.Rate>{value} \
        ")
    
        print('request: Ok\n')

        print('# --Выбирает информацию о врачах, для которых значение в поле Процент отчисления на зарплату, больше 2.3% (задавать параметром)')
        print(f"| {'Id':5} | {'Specialization':15} | {'Rate':15} | {'FirstName':15} | {'SecondName':15} | {'LastName':15} | {'BirthDate':10} |")
        print(f"|----------------------------------------------------------------------------------------------------------------------------|")
        for row in list:
            print(f"| {str(row[0]):5} | {str(row[1]):15} | {str(row[3]):15} | {str(row[5]):15} | {str(row[6]):10} | {str(row[7]):15} | {str(row[8]):5} |")


    def request03(database_path):   
# --Выбирает информацию о приемах за некоторый период, заданный параметрами
# select v.*,u1.* , u2.* from Visit v
# join User u1 on v.PatientId = u1.Id 
# join User u2 on v.DoctorId = u2.Id 
# where v.Date > date('now','-1 month') and v.Date <  date('now','+1 month')
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        list = cursor.execute(
            f"select v.*,u1.* , u2.* from Visit v \
                join User u1 on v.PatientId = u1.Id \
                join User u2 on v.DoctorId = u2.Id \
                where v.Date > date('now','-1 month') and v.Date <  date('now','+1 month') \
        ")
    
        print('request: Ok\n')

        print('# --Выбирает информацию о приемах за некоторый период, заданный параметрами')
        print(f"| {'Doctor':75} | {'Patient':65} |")
        print(f"| {'FirstName':15} | {'SecondName':15} | {'LastName':15} | {'Price':8} | {'Visit date':10} | {'FirstName':15} | {'SecondName':15} | {'LastName':15} |")
        print(f"|-------------------------------------------------------------------------------------------------------------------------------------------------|")
        for row in list:
            print(f"| {str(row[6]):15} | {str(row[7]):15} | {str(row[8]):15} | {str(row[3]):8} | {str(row[4]):10} | {str(row[12]):15} | {str(row[13]):15} | {str(row[14]):15} |")


    def request04(database_path,value):   
# --Выбирает информацию о докторах, специальность которых задана параметром 
# select * from Doctors d 
# join User u on u.Id = d.UserId 
# join Address a on a.Id = u.AddressId 
# where d.Specialization like 'T%'
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        list = cursor.execute(
            f"select * from Doctors d \
                join User u on u.Id = d.UserId \
                join Address a on a.Id = u.AddressId \
                where d.Specialization like '{value}'\
        ")
    
        print('request: Ok\n')

        print('# --Выбирает информацию о докторах, специальность которых задана параметром ')
        print(f"| {'FirstName':15} | {'SecondName':15} | {'LastName':15} | {'BirthDate':8} | {'Specialization':10} | {'Rate':5} |")
        print(f"|---------------------------------------------------------------------------------------------------------------|")
        for row in list:
            print(f"| {str(row[5]):15} | {str(row[6]):15} | {str(row[7]):15} | {str(row[8]):8} | {str(row[1]):10} | {str(row[3]):5} |")


    def request05(database_path):   
# --Вычисляет размер заработной платы врача за каждый прием. Включает поля Фамилия врача, Имя врача, Отчество врача, Специальность врача, Стоимость приема, Зарплата. Сортировка по полю Специальность врача
# select u.*,SUM(Price*Rate/100),d.Specialization  from visit v
# join Doctors d on v.DoctorId = d.Id
# join User u on u.Id = d.UserId 
# group by v.DoctorId
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        list = cursor.execute(
            f"select u.*,SUM(Price*Rate/100),d.Specialization  from visit v \
                join Doctors d on v.DoctorId = d.Id \
                join User u on u.Id = d.UserId \
                group by v.DoctorId\
        ")
    
        print('request: Ok\n')

        print('# --Вычисляет размер заработной платы врача за каждый прием. Включает поля Фамилия врача, Имя врача, Отчество врача, Специальность врача, Стоимость приема, Зарплата. Сортировка по полю Специальность врача')
        print(f"| {'FirstName':15} | {'SecondName':15} | {'LastName':15} | {'BirthDate':8} | {'SUMMARY':10} | {'Specialization':15} |")
        print(f"|-------------------------------------------------------------------------------------------------------------------|")
        for row in list:
            print(f"| {str(row[1]):15} | {str(row[2]):15} | {str(row[3]):15} | {str(row[4]):8} | {row[6]:+10.2f} | {str(row[7]):15} |")


    def request06(database_path):   
# --Выполняет группировку по полю Дата приема. Для каждой даты вычисляет максимальную стоимость приема
# select v.*,MAX(v.Price) from Visit v
# group by v.Date
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        list = cursor.execute(
            f"select v.*,MAX(v.Price) from Visit v \
                group by v.Date\
            ")
    
        print('request: Ok\n')

        print('# --Выполняет группировку по полю Дата приема. Для каждой даты вычисляет максимальную стоимость приема')
        print(f"| {'Date':15} | {'MAX(Price)':15} |")
        print(f"|---------------------------------|")
        for row in list:
            print(f"| {str(row[4]):15} | {str(row[5]):15} |")


    def request07(database_path):   
# --Выполняет группировку по полю Специальность. Для каждой специальности вычисляет средний Процент отчисления на зарплату от стоимости приема
# select d.*,AVG(d.Rate) from Doctors d
# group by d.Specialization
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        list = cursor.execute(
            f"select d.*,AVG(d.Rate) from Doctors d \
                group by d.Specialization\
            ")
    
        print('request: Ok\n')

        print('# --Выполняет группировку по полю Специальность. Для каждой специальности вычисляет средний Процент отчисления на зарплату от стоимости приема')
        print(f"| {'Specialization':15} | {'AVG(Rate)':15} |")
        print(f"|------------------------------------------|")
        for row in list:
            print(f"| {str(row[1]):15} | {row[4]:15.2f} |")



    def test(database_path):
        DBHelper_SQLite_Hospital.request01(database_path,'H%')
        DBHelper_SQLite_Hospital.request02(database_path,2.3)
        DBHelper_SQLite_Hospital.request03(database_path)
        DBHelper_SQLite_Hospital.request04(database_path,"T%")
        DBHelper_SQLite_Hospital.request05(database_path)
        DBHelper_SQLite_Hospital.request06(database_path)
        DBHelper_SQLite_Hospital.request07(database_path)

pywinauto_path = os.path.abspath(__file__)
pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
database_path = pywinauto_path + "/HomeWork006/db/SQLite_Hospital.db"
DBHelper_SQLite_Hospital.test(database_path)
