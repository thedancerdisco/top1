"""задача 1"""
# spisok: list[int]  = [3, -2, 7, 10, -5, 6]
# print(f"минимальное число {min(spisok)}")
# print(f"максимальное число  {max(spisok)}")
# print(f"среднее число  {round(sum(spisok)/len(spisok), 5)}")
# print(f" положителные числа {list(filter(lambda x: x>0, spisok))}")
# print(f" сглаженный список  {[spisok[i-1] + spisok[i] + spisok[i+1] for i in range(1, len(spisok)-1)]}")


"""задача 2"""
# stud: list[dict] = [
# {"name": "Анна", "score": 91},
# {"name": "Павел", "score": 75},
# {"name": "Игорь", "score": 82}
# ]
# print( list(
#             map(
#             lambda x:x["name"].upper(),
#             filter(
#                 lambda x:x["score"]>=80,
#                 sorted(
#                     stud, key = lambda x: x["score"]
#                       )
#                   )
#                 )
#             )
#      )


"""задача 3"""
# stroka: str = "Hello World"
# vowels = "aeiouAEIOU"
# def obrabotka(text:str)-> int:
#     i = 0
#     for let in vowels:
#         if let in stroka:
#             i+=1
#     return  f"количество гласных {i}, \n количество согласных { abs(len(obrabotka1.no_space)-i)}"

# def obrabotka1(text:str)-> str:
#     obrabotka1.no_space = text.replace(" ", "")
#     rev_true = text[::-1]
#     return f"строка без пробелов {obrabotka1.no_space}, \n строка в обратном порядке { rev_true}"
# print(obrabotka1(stroka),   "\n", obrabotka(stroka))


"""задача 4 """
# from typing import Callable
# a = int(input("введи первое число "))
# b = int(input("введи второе число "))
# c = input("введи операцию ")
# def calc(op: str )->Callable[[int, int],int]:
#     if op == "+":
#         return lambda a, b: a + b
#     if op == "*":
#         return lambda a, b: a * b
#     if op == "max":
#         return lambda a, b: a if a > b else b
#     raise ValueError("Неизвестный оператор")
# op = calc(c)
# print(op(a,b))


"""задача 5 """
# from typing import List, Tuple, Dict, Callable
# def move_robot(commands: List[str]) -> Tuple[int, int]:
#     x, y = 0, 0
#     moves: Dict[str, Callable[[int, int], Tuple[int, int]]] = {
#     "up": lambda x, y: (x, y + 1),
#     "down": lambda x, y: (x, y - 1),
#     "left": lambda x, y: (x - 1, y),
#     "right": lambda x, y: (x + 1, y),
#     }
#     for cmd in commands:
#         x, y =   moves[cmd](x, y)
#     return x, y
# print(move_robot(["up",  "left"]))


"""задача 6"""
# from typing import List, Callable
# def bubble_sort(nums: List[int], comp: Callable[[int, int], bool]) -> List[int]:
#     arr = nums[:]
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if comp(arr[j], arr[j+1]):
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# print(bubble_sort([5, 2, 7, 3], lambda a, b: a > b))


"""Задача 7"""
from typing import List
def linear_search(nums: List[int], target: int) -> int:
    for i, n in enumerate(nums):
        if n == target:
            return i
    return -1

def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target: return mid
        if nums[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1
nums = [3, 8, 1, 6]
print("Линейный:", linear_search(nums, 6))
nums_sorted = sorted(nums)
print("Бинарный:", binary_search(nums_sorted, 6))
print("сортироанный список ", nums_sorted)



"""задача 8"""
# matrix: list[list[int]] = [
# [1, 2, 3],
# [4, 5, 6],
# ]

# def sum_strok(a:list[list[int]])->list[int]:
#     print (f"сумма по строкам {[sum(i) for i in a]}")

# def sum_stolb(a:list[list[int]])->list[int]:
#     print(f"сумма по столбцам {[sum(i) for i in zip(*a)]}")

# def transpon(a:list[list[int]])->list[list[int]]:
#     print("транспонированная матрица")
#     a_t:list[tuple[int]] = list(zip(*a))
#     for i in range(len(a_t)):
#         for j in range (len(a_t[i])):
#             print(a_t[i][j], end=' ')
#         print()

# sum_stolb(matrix)
# transpon(matrix)
# sum_strok(matrix)
