# # task1
# k: int = 0
# text: str = input("vvedi text: ")
# text_1: list [str] = text.split()
# print(f" количество слов: {len(text_1)}")
# print(f" самое длинное слово: {max(text_1, key=len)}")
# print(f'revers: {text.lower()[::-1]}')
# for i in range(len(text)):
#     if text[i] !=" ":
#         k+=1
# print(f"количество символов без пробела: {k}")



# task2
# from  typing import Any
# journal: list[dict[str, int]] = [
#  {"name": "Анна", "age": 17, "score": 91},
#  {"name": "Павел", "age": 19, "score": 75},
#  {"name": "Игорь", "age": 20, "score": 82},
#  {"name": "Саша", "age": 20, "score": 81}
# ]
# journal_1:list[dict[str, int]] = []
# def age(jur:list[dict[str, int]])->list[dict[str, int]]:
#     journal_1 = list(filter(lambda x: x["age"]>=18, jur))
#     return journal_1

# def ball(jur:list[dict[str, int]])->list[dict[str, int]]:
#     journal_1 = sorted(jur, key=lambda x:x["score"])
#     return journal_1

# def upname(jur:list[dict[str, int]])-> list[str]:
#     journal_1=list(map(lambda x: x.get("name",0).upper(), jur))
#     return journal_1
# print(upname(ball(age(journal))))


# task3
# from typing import Any

# def make_report(title: str, *sections, **totals)->Any:
#     print(f"=== {title} ===")
#     print(f"-Секции\n{"\n".join(sections) }")
#     [print(f"{key}:{val}") for key, val in totals.items()]
#     # print(f"-Итоговые суммы \n{[(key, val) for key, val in totals.items(), \n]}")
# make_report(
#     "Отчёт за месяц",
#     "Транзакций: 15",
#     "Ошибок нет",
#     food=12000,
#     transport=3500
# )



# task 4
from  typing import Any
a: float = int(input("vvedi schislo, kotoroe budesh iskat: "))
nums: list[Any] =list(map(float, input("vvedi spisok  ").split()))
for i in range(len(nums)):
    if nums[i] == a:
        lin_a : int = i
print("индекс а при линейном поиске ", lin_a)
for j in range(len(nums)-1):
    for i in range(len(nums)-1):
        if nums[i+1]>nums[i]:
            nums[i], nums[i+1] = nums[i+1],nums[i]
print("отсортированный список", nums)
start: int  = 1
end: int = len(nums)-1
m :int = 0
data: dict[Any] = {}
for i in range(len(nums)):
    m =start+(end-start)//2
    if nums[m] == a:
        binar_ind = m
    elif a<nums[m]:
        start = m+1
    else: end = m-1
print("индекс в отсортированном списке ", binar_ind )

data["linear_index"] = lin_a
data["sorted_list"] = nums
data["binary_index"] = binar_ind
[print(f"{key}: {val}") for key, val in data.items()]
