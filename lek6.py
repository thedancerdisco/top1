# #переменные и типы данных
# my_name: str = "Marat"
# num: int = 112
# pi: float = 3.14
# flag: bool = True
# num +=10

# # условия if elif else
# if num % 2 == 0:
#     print('hello')
# elif num < 100:
#     print('yes')
# else:
#     print('goodbye')

# #операторы and or
# print(1 and 0) #false
# print(1 or 0)# true

# print(True == 1)

# #ввод и  вывод данных
# age: int = int(input("help text"))
# print(age, 1, "hello", sep="*", end='\t')
# print("hello")


# #коллекции
# nums: list[int | float | str] = [1,2,3,4, "hello", 3.14]
# names: tuple[str] = {"alina", Masha}
# uniq_nums: set[int] = (2,3,4)
# print(nums[3])
# nums.append(100)
# nums.sort(reverse=True)# по убыванию
# nums.pop()#удаляет элемент с конца или по индексу


#split разделяет (метод строки) строки  /разбивает по пробелам на элементы списка(по умолчанию через пробел)

# stroka: list[str] = "hello, my friend. i glad"
# senten: list[str] = stroka.split()

# # join из списка делает строку /метод строки

# senten1: str = "*".join(senten)
# print(senten)
# print(senten1)

# #списки lists
# for el in senten:
#     print(el)
# #внутри 1 цикла нельзя изменить элементы. внутри range поменяются элементы если их изменить
# for i in range(len(senten)):
#     print(senten[i])

# i: = 0
# while i< len(senten):
#     print(senten[i])
#     i+=1

# 2d lists список списков
# twod_nums: list[list[int]] = [
#     [1,2,3],
#     [10,11,12],
#     [21,31,41]
#]
#3 способа распечатки матрицы
# for i in range(len(twod_nums)):
#     for j in range(len(twod_nums[i])):
#         print(twod_nums[i][j])

# i: int = 0

# while i< len(twod_nums):
#     j: int = 0
#     while j< len(twod_nums[i]):
#         print(twod_nums[i][j])
#         j+=1
#     i+=1

# for i in twod_nums:
#     for j in i:
#         print(j)



# задача по рисованию стоб диагр из списка чисел
# userin: list[str] = input().split()
# for i in range (len(userin)):
#     userin[i] = int(userin[i])
# for num in userin:
#    print('*'*num)

#

#     print()


# name: str = 'Marat'
# surname: str = 'gataullin'
# list1: list[int]=[10,20,30]
# list2: list[int] = ['f','d']
# print(name+surname)
# print(name*3)
# print(list1+list2)


userip: list[str] = [int(el) for el in input().split('.')]
flag: bool = True
if len(userip) !=4 :
    flag=False
else:
    for i in range (len(userip)):
        if not 0<=userip[i]<=255:
            flag=False
            break
print(flag)
