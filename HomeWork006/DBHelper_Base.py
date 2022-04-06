

import sqlite3
from typing import Iterable


class DBHelper_Base:
    def drop_table(database_path,table_name):   
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        cursor.execute(
        """DROP TABLE 
        """ + table_name)
        print('delete table: Ok\n')


    def insert(database_path, data:tuple):    
        pass
        raise Exception('Not find insert methods!')


    def insertmany(database_path,datas:Iterable):
        pass
        raise Exception('Not find insertmany methods!')


    def update_by(database_path,table_name,parameter,data:Iterable):    
        # Обновление записей
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        sql = f"\
        UPDATE {table_name} \
        SET {parameter} = ? \
        WHERE {parameter} = ?\
        "

        cursor.execute(sql, data)
        conn.commit()
        print('update: Ok\n')


    def delete_by(database_path,table_name,parameter,value):
        # удаление записей
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        sql = f"DELETE FROM {table_name} WHERE {parameter} = '{value}'"
        cursor.execute(sql)
        conn.commit()
        print('delete: Ok\n')


    def find_by(database_path,table_name,parameter,value):
        # чтение данных
        conn = sqlite3.connect(database_path)
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        sql = f"SELECT * FROM {table_name} WHERE {parameter}='{value}'"
        cursor.execute(sql)
        print('select: Ok\n')
        return cursor.fetchall() # or use fetchone()
        

    def find_by_like(database_path,table_name,parameter,value):
        # чтение данных
        conn = sqlite3.connect(database_path)
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        sql = f"SELECT * FROM {table_name} WHERE {parameter} LIKE '{value}'"
        cursor.execute(sql)
        
        print('select: Ok\n')
        return cursor.fetchall()


    def getAll(database_path,table_name,order_by):
        # чтение данных
        conn = sqlite3.connect(database_path)
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        print('select: Ok\n')
        if(order_by==''):
            return cursor.execute(f"SELECT rowid as ID, * FROM {table_name}")
        else:
            return cursor.execute(f"SELECT rowid as ID, * FROM {table_name} ORDER BY " + order_by)
   

    def print_list(list):
        for row in list:
            print(row)

