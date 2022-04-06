from cmath import nan
import utils

def Task_Task2list():
    print(
        '''
        Task2. Обработка списков. Для списков, заполненных случайными числами в диапазоне значений от –20 до 20, выводите сформированные списки до и после обработки по заданию.
\t- Сформируйте список list_c. Увеличить все нечетные числа, содержащиеся в списке, на исходное значение последнего нечетного числа. Если нечетные числа в списке отсутствуют, то оставить список без изменений. Вывести упорядоченную по убыванию копию списка 
\t- Сформируйте список list_c. Возвести в квадрат все его локальные минимумы (то есть числа, меньшие своих соседей)
\t- Сформируйте список list_c. Удалить из списка все одинаковые элементы, оставив их первые вхождения
\t- Сформируйте список list_c. Вставить элемент с нулевым значением перед минимальным и после максимального элемента списка
 '''
        )

def Run_Task2list():
    my_list = []
    for r in range(20):
        my_list.append(0)

    utils.fill_list(my_list,-20,20)

    print("Task1")
    tmp_list = list(my_list)
    utils.show_list(tmp_list,"Before Task1")
    utils.show_list(task1(tmp_list),"After Task1")

    print("Task2")
    tmp_list = list(my_list)
    utils.show_list(tmp_list,"Before Task2")
    utils.show_list(task2(tmp_list),"After Task2")

    print("Task3")
    tmp_list = list(my_list)
    utils.show_list(tmp_list,"Before Task3")
    utils.show_list(task3(tmp_list),"After Task3")

    print("Task4")
    tmp_list = list(my_list)
    utils.show_list(tmp_list,"Before Task4")
    utils.show_list(task4(tmp_list),"After Task4")

def task1(_list:list):
    try:
        pass
        #1
        delta = 0
        _list.reverse()
        for item in _list:
            if(item%2==1):
                delta = item
                break

        cnt = len(_list)
        for i in range(0, cnt):
            if(_list[i]%2==1):
                _list[i]+=delta

        #2
        return sorted(_list)

    except Exception:
        print("Общее исключение")

def task2(_list):
    try:
        pass

        answer_list = list(_list)
        cnt = len(_list)
        index=-1
        for i in range(0, cnt-1):
            if(i>0 & (i+1)!=cnt ):

                left_index=i-1;
                right_index=i+1;
                if(left_index==_list[i]):
                    left_index = i-2
                    while(left_index>0):
                        if(_list[left_index]==_list[i]):
                            left_index-=1
                        else:
                            break
                if(_list[i]==right_index):
                    right_index = i+2
                    while(right_index<cnt):
                        if(_list[i]==_list[right_index]):
                            right_index+=1
                        else:
                            break
                    if(right_index==cnt):
                        right_index-=1

                if(_list[left_index]>_list[i]<_list[right_index]):
                    if(index!=-1):
                        answer_list[index]*=answer_list[index]
                    index = i

        if(index!=-1):
            answer_list[index]*=answer_list[index]
        
        return answer_list

    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task3(_list:list):
    try:
        pass
        cnt = len(_list)
        i=0
        while(i<cnt):
            j=i+1
            while(j<cnt):
                pass
                if(_list[i]==_list[j]):
                    _list.pop(j)
                    cnt=-1   
                j+=1             
            i+=1
        
        return _list

    except Exception:
        print("Общее исключение")

def task4(_list:list):
    try:
        pass
        
        cnt = len(_list)
        # min_index=0
        # max_index=0
        # for i in range(0, cnt-1):
        #     if(_list[min_index]>_list[i]):
        #         min_index=i
        #     if(_list[max_index]<_list[i]):
        #         max_index=i

        min_index = _list.index(min(_list))
        max_index = _list.index(max(_list))

        if(min_index>max_index):
            _list.insert(min_index,0)
        if(max_index<cnt):
            _list.insert(max_index+1,0)
        else:
            list.append(0)
        if(min_index<max_index):
            _list.insert(min_index,0)
        
        return _list

    except Exception:
        print("Общее исключение")


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork002 import main
    main()
# end if