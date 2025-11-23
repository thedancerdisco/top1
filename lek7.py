#task3
#вставитьь разделитель между каждым символом строки текста
# print(input().join(input())) #соединяет кажд  симв через разделит

#task4 строка текста содерж цел числа, из данн строки формир список чисел. сортирует
# и выводит данн список по возраст
# nums_list: list[int] = [int(num) for num in input().split()]

# nums_list.sort()
# print(nums_list)
# nums_list.reverse()
# print(nums_list)

#второй способ
# nums_list: list[int] = [int(num) for num in input().split()]

# print(sorted(nums_list), sorted(nums_list, reverse=True), sep='\n')

#task5
# string: list[str] = [num for num in input().split()]
# print(len(max(string)))

# print(len(max(input().split(), key=len)))

#task7
# string: list[int] = [int(num) for num in input().split()]
# k:int = 0
# for i in range(len(string)):
#         for j in range(i+1,len(string)):
#             if string[i] == string[j]:
#                 k+=1
# print(k)

#task8 дана матрица. заполнить случайными числами найти среднеепо каждой строке
import random
matrix: list[list[int]]=[]
n: int = int(input('vvedi kol-vo strok '))
m: int = int(input('vvedi kol-vo stolbov '))
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j]=random.randint(1, 100)
print(matrix)
for i in range(n):
    print(int(sum(matrix[i])/len(matrix[i])))
