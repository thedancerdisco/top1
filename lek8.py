# from typing import Any
# population: dict[str, Any] = {
#     'Moscow':14_000_000,
#     'kazan':1300000,
#     'saint-petersburg': 9000000,
# }
# print(population['kazan'])
# print(population.get('paris', "no key"))

# from typing import Any
# population: dict[str, Any] = {
#     'Moscow':14_000_000,
#     'kazan':1300000,
#     'saint-petersburg': 9000000,
# }
# print(population['kazan'])
# p_pop: Any =  population.get('paris', "no key") #int | str
# print(p_pop)
# if p_pop:
#     print('////')
# else:
#     print(population.get('moscow'))

from typing import Any
population: dict[str, Any] = {
    'Moscow':14_000_000,
    'kazan':1300000,
    'saint-petersburg': 9000000,
}
# print(population['kazan'])
# p_pop: Any =  population.get('paris', "no key") #int | str
# print(p_pop)
# if p_pop:
#     print('////')
# else:
#     print(population.get('moscow'))

# print(population.keys())
# print(population.values())
# print(population.items())

# for i,v in population.items():
#     print(i,v)


# print(population['kazan'])
# p_pop: Any =  population.get('paris', "no key") #int | str
# print(p_pop)
# print(population.pop('zimbabve'))
# print(population)

# population_2 = {
#     'kazan': 'qwerty',
#     'paris': 10000000
# }
# population.update(population_2)
# print(population)

# for el in population:
#     print(el)

# def say_hello(name:str="enpty")->None:
#     print('hello,', name)

# def my_max(a: int, b:int) -> int:
#     """
#     возвращает макс число из 2
#     """
#     if a>b:
#         return a
#     return b
# my_max(5,3)
# say_hello('marat')

# x:int = 10
# def func()->None:
#     x=5
#     print(x)

# func()
# print(x)

# x:int = 10
# def func()->None:
#     global x
#     x=5
#     print(x)

# func()
# print(x)

# x:int = 10
# def func(x:int)->None:
#     x += 5
#     print(x)

# func(x)
# print(x)

#ползователь вводит строку текста, сколько раз встре каждое слово и вывести в виде словаря
# words: list[str] = input('vvedi stroku ').split()
# words_count: dict[str, int] = {}
# for el in words:
#     words_count[el] = 0
# print(words_count)
# for el in words:
#     words_count[el]+=1
# print(words_count)

# words: list[str] = input('vvedi stroku ').split()
# words_count: dict[str, int] = {el: 0 for el in words}

# for el in words:
#     words_count[el]+=1
# print(words_count)

#есть словарь с товарами и ценами. пусть пользователь введет название товара, а мы выведем цену.
#если товара нет, сообщить что отсутствует
#хлеб 60, молоко 80, сыр 150
# prices: dict[str, int] = {
#     'молоко':80
#     "хлеб": 60
#     "сыр": 150
# }
# u_i: str = input()
# if u_i in prices:
#     print(prices[u_i])
# print('sorry')

# напиите функцию , которая принимает список  оценок и возвращает ср знач.
#  исполз эту функ для вывода ср балла
def average(grades: list[int])->float:
    return(sum(grades)/len(grades))
students = {
    "Анна": [5,4,5,5],
    "Борис":[3,4,4,5]
}
for name, marks in students.items():
    print(name, "->", average(marks))
