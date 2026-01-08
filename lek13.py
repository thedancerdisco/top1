# def task1()->None:
#     nums: list[int |float]=[float(x) for x in input().split()]

#     print("max:", max(nums))
#     print("min:", min(nums))
#     print("average:", sum(nums)/len(nums))

#     print("polozitelnie:", list(filter(lambda x:x>=0, nums)))

#     print("sglazennyi spisok:", [nums[i]+nums[i-1] for i in range(1, len(nums)) ])
# task1()



# students: list[dict[str, str | int]] = [
#     {"name":"Anna", "score": 91},
#     {"name":"Pavel", "score": 75},
#     {"name":"Igor", "score": 82},
# ]

# def task2(students: list[dict[str, str | int]])->list[str]:
#     sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
#     print(sorted_students)
#     filtered_studs = list(filter(lambda x: x["score"]>=80, sorted_students))
#     return[x["name"].upper() for x in filtered_studs]
# print(task2(students))



# def bubble_sort(students: list[dict[str, str | int]])->None:
#        for i in range(len(students)):
#         is_sorted: bool = True
#         list_sorted: bool = True
#         for j in range(len(students)-1):
#             if students[j]["score"]< students[j+1]["score"]:
#                 students[j], students[j+1] = students[j+1],students[j]
#                 list_sorted = False
#         if list_sorted:
#             break
# students: list[dict[str, str | int]] = [
#     {"name":"Anna", "score": 91},
#     {"name":"Pavel", "score": 75},
#     {"name":"Igor", "score": 82},
# ]
# def task2(students: list[dict[str, str | int]])->list[str]:
#     bubble_sort(students)
#     filtered_studs = list(filter(lambda x: x["score"]>=80, students))
#     return[x["name"].upper() for x in filtered_studs]
# print(task2(students))





strok: str = "Hello World"
def task3(string: str)->None:
    vowels: str = "aeioy"
    print("glasnye: ", len(list(filter(lambda x: x in vowels or x in vowels.upper(), string))))
    print("soglasnye: ", len(list(filter(lambda x: x not in vowels and x not in vowels.upper(), string))))
    print("revers:", string[::-1])
    print(string.replace(" ", ""))
task3(strok)


#task4
# def make_operator(operator: str) ->callable:
#     if operator == "*":
#         return lambda x, y: x*y
#     elif operator =="+":
#         return lambda x, y: x+y
#     elif operator =="max":
#         return lambda x, y: x if x>y else y
#     pass
# op:callable = make_operator("+")
# print(op(2,4))




# task 5
# def mov_robot(commands:list[str])->tuple[int]:
#     coords: tuple[int] = (0,0)
#     cmds:dict[str, callable] = {
#         "up":lambda x,y:(x, y+1)
#         "down" lambda x,y:(x, y-1)
#         "left" lambda x,y:(x-1, y)
#         "right" lambda x,y:(x+1,y),
#     }
#     for cmds in commands:
#         coords = cmds[cmd](coords[0], coords[1])
#     return coords
# ala = ["up", "up"]
# дописать из фото

# task6 дописать из фото
# from typing import Iterable, Callable
# def bubble_sort(iterable: Iterable[int], comp: Callable[[float, float],None])->None:
#     for i in range(len(iterable)):
#         list_sorted: bool = True
#         for j in range(len(iterable)-1):
#             if students[j]["score"]< students[j+1]["score"]:
#                 students[j], students[j+1] = students[j+1],students[j]
#                 list_sorted = False
#         if list_sorted:
#             break
# nums = [5,2,14,1,22,13]
# comp = lambda x,y: x>y
# bubble_sort(nums, comp)
# print(nums)





# task 7
array: list[int] = [3,8,1,6]
a: int = 6
def linear_search(elements: list[int], elem: int)-> int:
    for i in range(len(elements)):
        if elements[i] == elem:
            return i
    return "не найдено"
def binary_search(elements: list[int], elem: int)->int:
    elements.sort()
    start: int = 0
    end: int = len(elements) - 1

    for i in range(len(elements)):
        mid_index: int = start + (end - start) // 2
        if elements[mid_index] == elem:
            return mid_index
        elif elements[mid_index] > elem:
            end = mid_index - 1
        else:
            start = mid_index + 1

    return False
print(linear_search(array, a))
print(binary_search(array, a))
