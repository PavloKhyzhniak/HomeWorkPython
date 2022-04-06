import random
import sys

from install_and_import import install_and_import
install_and_import('PIL')

try:
    from MainHomeWork001 import MainHomeWork001
    from MainHomeWork002 import MainHomeWork002
    from MainHomeWork003 import MainHomeWork003
    from MainHomeWork004 import MainHomeWork004
    from MainHomeWork005 import MainHomeWork005
    from MainHomeWork006 import MainHomeWork006
except ImportError:
    import os.path
    pywinauto_path = os.path.abspath(__file__)
    pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
    
    pywinauto_path1=pywinauto_path+"\\HomeWork001"
    sys.path.append(pywinauto_path1)
    import MainHomeWork001

    pywinauto_path2=pywinauto_path+"\\HomeWork002"
    sys.path.append(pywinauto_path2)
    import MainHomeWork002

    pywinauto_path3=pywinauto_path+"\\HomeWork003"
    sys.path.append(pywinauto_path3)
    import MainHomeWork003

    pywinauto_path4=pywinauto_path+"\\HomeWork004"
    sys.path.append(pywinauto_path4)
    import MainHomeWork004

    pywinauto_path5=pywinauto_path+"\\HomeWork005"
    sys.path.append(pywinauto_path5)
    import MainHomeWork005

    pywinauto_path6=pywinauto_path+"\\HomeWork006"
    sys.path.append(pywinauto_path6)
    import MainHomeWork006

def main():
    print(f'{__name__}: начало работы\n')
    random.seed()

    Task_StudentInfo()
    while(1):
        Task_HomeWork()
        choose = int(input("""
\033[0m \033[34;47mВыберите пункт:\033[0m """))
        if choose == 1:
            MainHomeWork001.main()
        elif choose == 2:
            MainHomeWork002.main()
        elif choose == 3:
            MainHomeWork003.main()
        elif choose == 4:
            MainHomeWork004.main()
        elif choose == 5:
            MainHomeWork005.main()
        elif choose == 6:
            MainHomeWork006.main()
        elif choose == 0:
            break


def Task_HomeWork():
    print('''\t\033[0m \033[34;47mMENU\033[0m
    1 - Home Work №01 on 06.03.2022
    2 - Home Work №02 on 13.03.2022
    3 - Home Work №03 on 20.03.2022
    4 - Home Work №04 on 27.03.2022
    5 - Home Work №05 on 03.04.2022
    6 - Home Work №06 on 10.04.2022
    0 - Exit from Programm
    ''')

def Task_StudentInfo():
    print('''\t\033[0m \033[34;47mДомашнии работы\033[0m
Выполнил ст.гр.ВПУ911 Хижняк Павел
\033[0m \033[34;47mКА "ШАГ" г.Донецк ДНР
\033[0m
    ''')



# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    main()
# end if
