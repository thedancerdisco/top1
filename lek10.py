# nums: list[int] = [10,20,30,40,100]
# greeting: str = "hellom it's me"

# nums2:list[int] = nums[1:3:]
# nums2[0] = 300
# print(nums[1:3:])
# print(greeting[0:5])
# print(greeting[:5:])
# print(nums[::-1])
# print(nums2)


# from typing import Any
# a: list[int] = [1,2,3,4,5,6,7,8,9]
# num: int = 9
# def linear_search(elements: list[Any], elem: Any)-> int | str:
#     for i in range(len(elements)):
#         if elements[i] == elem:
#             return i

#     return "не найдено"

# print(linear_search(a,num))

# if __name__ == "__main__":
#     # что бы исполнение происходило толькло тогда, когда исполняется сам файл. этот файл.когда вызываешьиздругогофайла - не исполнялось
#     elements: list[Any] = [1,2,3.14, True, 200]
#     print(linear_search(elements, "D"))


# def binary_search(elements: list[int], elem: int)-> bool:
#     elements.sort()
#     start: int = 0
#     end: int = len(elements)-1

#     for i in range(len(elements)):
#         mid_index: int = start + (end - start) // 2
#         if elements(mid_index) == elem:
#             return True
#         elif elements[mid_index] > elem:
#             end = mid_index - 1
#         else:
#             start = mid_index + 1

#     return False


# if __name__ == "__main__":
#     # что бы исполнение происходило толькло тогда, когда исполняется сам файл. этот файл.когда вызываешьиздругогофайла - не исполнялось
#     nums: list[int] = [100,200,300, 1,4,5,17]
#     print(binary_search(nums, 17))


# def bubble_search(elements: list[int | float])-> None:
#     for i in range(len(elements)-1):
#         is_sirted: bool = True
#         for j in range(len(elements)-1-i):
#             if elements[j] <= elements[j+1]:
#                 elements[j], elements[j+1] = elements[j+1], elements[j]
#                 is_sirted = False
#         if is_sirted:
#             break
#         print(elements)



# if __name__ == "__main__":
#     # что бы исполнение происходило толькло тогда, когда исполняется сам файл. этот файл.когда вызываешьиздругогофайла - не исполнялось
#     nums: list[int] = [100,200,300, 1,4,5,17]
#     print(bubble_search(nums))
#     print(nums)



def show_menu()->None:
    print("выбери действие")
    print("1. найти число линейный поиск")
    print("2.найти число бинарный поиск")
    print("3.отсортировать пузырьком")
    print("4.выйти")

if __name__ == "__main__":
    user_nums: list[int | float] = [for num in  input('vvedi spisok').split]
while True:
    show_menu()
    user_input: str = input('viberi punkt menu')

    if
