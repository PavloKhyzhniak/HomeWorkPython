# работаем с SQLite
# https://python-scripts.com/sqlite
import sqlite3
import sys
from typing import Iterable

class DBHelper_Table:
    def create_table_albums(database_path, table_name):   
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        cursor.execute(
        """CREATE TABLE IF NOT EXISTS """ + table_name + """ (
               id integer PRIMARY KEY AUTOINCREMENT, 
               title text, 
               artist text, 
               release_date text,
               publisher text, 
               media_type text)
        """)
        print('create table: Ok\n')


    def drop_table(database_path,table_name):   
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Пример создания таблицы
        cursor.execute(
        """DROP TABLE 
        """ + table_name)
        print('delete table: Ok\n')


    def insert(database_path, data:tuple):    
        conn = sqlite3.connect(database_path) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()   # cursor CURrent Set Of Rows

        # Вставляем данные в таблицу
        res = cursor.execute(
            """INSERT INTO albums 
                  (title, artist, release_date, publisher, media_type)
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
        "INSERT INTO albums (title, artist, release_date, publisher, media_type) VALUES (?,?,?,?,?)",
        datas
        )

        conn.commit()
        print('insert many: Ok\n')

    
    def update_artist(database_path,data:Iterable):    
        # Обновление записей
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        sql = """
        UPDATE albums 
        SET artist = ? 
        WHERE artist = ?
        """

        cursor.execute(sql, data)
        conn.commit()
        print('update: Ok\n')


    def delete_by_artist(database_path,artist):
        # удаление записей
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        sql = "DELETE FROM albums WHERE artist = '" + artist + "'"
        cursor.execute(sql)
        conn.commit()
        print('delete: Ok\n')


    def find_by_artist(database_path,artist):
        # чтение данных
        conn = sqlite3.connect(database_path)
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        sql = "SELECT * FROM albums WHERE artist=?"
        cursor.execute(sql, [artist])
        print('select: Ok\n')
        return cursor.fetchall() # or use fetchone()
        

    def getAll(database_path,order_by):
        # чтение данных
        conn = sqlite3.connect(database_path)
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        print('select: Ok\n')
        if(order_by==''):
            return cursor.execute("SELECT rowid, * FROM albums")
        else:
            return cursor.execute("SELECT rowid, * FROM albums ORDER BY " + order_by)

    def find_by_title_like(database_path,like_str):
        # чтение данных
        conn = sqlite3.connect(database_path)
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        sql = "SELECT * FROM albums WHERE title LIKE '" + like_str + "'"
        cursor.execute(sql)
        
        print('select: Ok\n')
        return cursor.fetchall()


    def print_list(list):
        for row in list:
            print(row)


    def print_list_special(list):
        for (_id,title,artist,release_date,publisher,media_type) in list:
            print(f"| {_id:5} | {title:25} |")


    def print_list_special2(list):
        for row in list:
            print(f"| {row[0]:5} | {row[1]:25} | {row[2]:20} | {row[3]:12} | {row[4]:15} |")

DBHelper_Table.create_table_albums(sys.path[0] + "/db/mydatabase.db",'albums')
DBHelper_Table.drop_table(sys.path[0] + "/db/mydatabase.db",'albums')
DBHelper_Table.create_table_albums(sys.path[0] + "/db/mydatabase.db",'albums')
DBHelper_Table.insert(sys.path[0] + "/db/mydatabase.db",('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3'))

# Вставляем множество данных в таблицу используя безопасный метод "?"
albums = [
    ('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
    ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
    ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
    ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')
]

DBHelper_Table.insertmany(sys.path[0] + "/db/mydatabase.db",albums)
DBHelper_Table.update_artist(sys.path[0] + "/db/mydatabase.db",('John Doe', 'Andy Hunter'))
DBHelper_Table.delete_by_artist(sys.path[0] +"/db/mydatabase.db",'John Doe')
answer_list = DBHelper_Table.find_by_artist(sys.path[0] +"/db/mydatabase.db",("Red"))
DBHelper_Table.print_list(answer_list)
answer_list = DBHelper_Table.getAll(sys.path[0] +"/db/mydatabase.db",'artist')
DBHelper_Table.print_list(answer_list)
answer_list = DBHelper_Table.find_by_title_like(sys.path[0] +"/db/mydatabase.db",'The%')
DBHelper_Table.print_list_special(answer_list)
DBHelper_Table.print_list_special2(answer_list)


