import sys
import csv

def Task_Task1():
    print(
        '''
        •	Task1. Для файла text.txt, приведенного в папке задания реализуйте обработки (файл скопируйте в Ваш проект при создании проекта): 
\to	Перевести текст из исходного файла в нижний регистр, сохранить в файле lowers.txt
\to	В файле lowers.txt подсчитать количество строк, слов, определить максимальную длину слова и список слов максимальной длины, минимальную длину слова и список слов минимальной длины, сохраните списки слов в файлах longest.txt и shortest.txt соответственно для слов максимальной и минимальной длины 
\to	Сформируйте словарь из слов файла lowers.txt – ключом является слово, значением – количество вхождений этого слова в текст. Сохраните этот словарь в формате CSV, имя файла words.csv 
'''
        )

def Run_Task1():
    pass
    task1("..\\HomeWork003\\text.txt","..\\HomeWork003\\lowers.txt")
    task2("..\\HomeWork003\\lowers.txt")
    task3("..\\HomeWork003\\lowers.txt","..\\HomeWork003\\words.csv")

def task1(file_name,file_name_dest):
    try:
        pass
        print(f"Read file:{file_name}")
        # Считаем и выведем в консоль файл построчно, без явного использования readline()
        with open(sys.path[0] + "\\" + file_name, "r", encoding='utf-8') as file:
            with open(sys.path[0] + "\\" + file_name_dest, "w", encoding='utf-8') as file_res:
                for line in file:
                    print(line, end="")
                    file_res.write(line.lower())
        # end with
        print()

    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task2(file_name):
    try:
        pass
        print(f"Read file:{file_name}")
        shortest = list()
        longest = list()
        cnt_rows = 0
        cnt_words = 0
        len_shortest = 0
        len_longest = 0

        # Считаем и выведем в консоль файл построчно, без явного использования readline()
        with open(sys.path[0] + "\\" + file_name, "r", encoding='utf-8') as file:
            for line in file:
                print(line, end="")
                cnt_rows+=1
                words = line.split()
                for word in words:
                    cnt = len(word)
                    if(cnt==0):
                        continue
                    cnt_words+=1

                    if(len_longest<cnt):
                        len_longest = cnt
                        longest = list()
                    if(len_longest == cnt):
                        longest.append(word)

                    if(len_shortest==0):
                        len_shortest = cnt
                    if(len_shortest>cnt):
                        len_shortest = cnt
                        shortest = list()
                    if(len_shortest == cnt):
                        shortest.append(word)
        # end with
        print()

        print(f'Count Rows = {cnt_rows}')
        print(f'Count Words = {cnt_words}')
        print(f'Length longest word = {len_longest}')
        print(f'Length shortest word = {len_shortest}')
        with open(sys.path[0] + "\\" + 'longest.txt', "w", encoding='utf-8') as file_longest:
            pass
            for item in longest:
                file_longest.write(item + '\n')
            print(longest)
            
        with open(sys.path[0] + "\\" + 'shortest.txt', "w", encoding='utf-8') as file_shortest:
            pass
            for item in shortest:
                file_shortest.write(item + '\n')
            print(shortest)

    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task3(file_name,file_name_dest):
    try:
        pass
        words_dict= dict()
        with open(sys.path[0] + "\\" + file_name, "r", encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if(len(word)==0):
                        continue
                    if(word in words_dict.keys()):
                        words_dict.update({word:words_dict[word]+1})
                    else:
                        words_dict.update({word:1})
               
        with open(sys.path[0] + "\\" + file_name_dest, "w", encoding='UTF-8', newline="") as file:
            columns = ["word", "count"]
            writer = csv.DictWriter(file, fieldnames=columns)

            # запись заголовка - строка с именами ключей
            writer.writeheader()

            for word,cnt in words_dict.items():
                # собственно запись в файл writerow()
                writer.writerow({"word":word, "count":cnt})
        # end with

    except Exception:
        print("Общее исключение")



# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork003 import main
    main()
# end if