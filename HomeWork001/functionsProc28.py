
def Task_Proc28():
    print(
        '''
        Proc28. Описать функцию is_prime(n), возвращающую True, если параметр n является простым числом, и False в противном случае (число, большее 1, называется простым, если оно не имеет положительных делителей, кроме 1 и самого себя). 
        Если параметр n <= 1 то выбрасывать исключение. 
        C помощью функции is_prime() найти количество простых чисел среди 15 случайных чисел в диапазоне от -120 до 250.
        '''
        )

def Run_Proc28(a):
    return is_prime(a)

def is_prime(a):
    try:
        if a<=1:
            raise Exception("параметр n <= 1, а у нас он = {0} ".format(a))
        for item in range(2,a//2):
            if a%item==0: 
                print(f'{a} - не простое число')
                return False
        print(f'{a} - простое число')
        return True

    except Exception as ex:
        print("Общее исключение")
        print(ex)


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork001 import main
    main()
# end if