
def Task_Proc21():
    print(
        '''
        Proc21. Описать функцию sum_range(a, b), находящую сумму всех целых чисел от A до B включительно (a и b – целые). 
        Если a > b, то выбрасывать исключение. 
        С помощью функции sum_range() найти суммы для пяти пар случайных чисел. 
        '''
        )

def Run_Proc21(a,b):
    print("Сумма всех целых чисел от {0} до {1} включительно  равна {2}".format(a,b,sum_range(a,b)))

def sum_range(a,b):
    try:
        sum=0;
        if a>b:
            raise Exception("a > b")
        for item in range(a, b+1):
            sum+=item
        return sum
    except Exception as ex:
        print("Общее исключение")
        print(ex)


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork001 import main
    main()
# end if