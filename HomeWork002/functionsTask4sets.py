import random

def Task_Task4sets():
    print(
        '''
Task4. Обработка множеств. Разработайте функцию, в которой используются два множества из случайных целых чисел. Функция должна обеспечивать:
\t-	Формирование множеств – используйте операцию добавления в множество, длина каждого множества определяется генератором случайных чисел (от 5и до 23х элементов), диапазон значений элементов: -20, 20;
\t-	Вычисление пересечения множеств;
\t-	Вычисление разности множеств;
\t-	Вычисление объединения множеств;
\t-	Удаление всех отрицательных элементов из множества с меньшим количеством элементов 
'''
        )

def Run_Task4sets():
    set1 = generateRandomIntSets(random.randrange(5,23),-20,20)
    set2 = generateRandomIntSets(random.randrange(5,23),-20,20)

    showSets(set1,"Set 1")
    showSets(set2,"Set 2")

    showSets(set1.union(set2),"Union set1 with set2")
    showSets(set1.intersection(set2),"Intersection set1 with set2")
    showSets(set1.difference(set2),"Difference set1 with set2")

    if(len(set1)>len(set2)):
        removeNeg(set2)
        showSets(set2,"Set 2")
    else:
        removeNeg(set1)
        showSets(set1,"Set 1")

def removeNeg(_set:set):
    '''Remove Negative Number from Sets.'''
    _list = list()#list with element for remove
    for item in _set:
        if item < 0:
            _list.append(item)
    for item in _list:
        _set.discard(item)

random.seed()

def generateRandomIntSets(count,min,max):
    '''Generate Sets with Length and Integer Number[min;max].'''
    try:
        _sets=set()
        for r in range(count):
            _sets.add(random.randint(min,max))

        return _sets

    except Exception:
        print("Общее исключение")


def showSets(sets:set,title):
    '''Show Sets with Title.'''
    try:
        print(title)
        for item in sets:
            print(f"{item:3} ", end='');
        print()

    except Exception:
        print("Общее исключение")


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork002 import main
    main()
# end if