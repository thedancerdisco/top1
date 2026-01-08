# from functools import reduce

# def calculate_total(cart):
#     item_totals = map(lambda x: x[0] * x[1], cart)
#     return reduce(lambda x, y: x + y, item_totals, 0)

# cart = [(10.99, 2), (5.49, 4), (3.99, 1)]
# print(calculate_total(cart))

# from functools import reduce
# names: list[str] = ["ivanov", "petrov", "sidorov"]
# majors: list[str] = ["seller", "manager", "director"]
# salary:list[float] = ["50_000", "70_000", "100_000"]
# def combine_employee_data(*args):
#     combine = zip(*args)
#     return list(map(lambda x: f"{x[0]} - {x[1]}: {x[2]}", combine))

# print(combine_employee_data(names, majors, salary))

# is_even = lambda x: x % 2 == 0
# print(is_even(4))
# to_upper = lambda y: y.upper()
# print(to_upper("@er"))
# last_char = lambda z: z[-1]
# print(to_upper(last_char("qwertyuiop")))


# from typing import Callable, Any
# arr = [1,2,3,4,5]
# def make_transform(func:  Callable[[int],int], a:list[int])->list[Any]:
#     b = list(func(x) for x in a)
#     print(b)

# def double(x: int) -> int:
#     return x * 2
# def minus_one(x: int) -> int:
#     return x - 1
# make_transform(double, arr)
# print()
# make_transform(minus_one, arr)
# print()
# print(list(map(double,arr)))


students = [
{"name": "Анна", "score": 88},
{"name": "Павел", "score": 95},
{"name": "Игорь", "score": 72},
{"name": "Марина", "score": 91},
]
stud = list(filter(lambda x: x["score"]>85, sorted(students, key = lambda x: x["score"] )))
print(list(map(lambda x: x["name"].upper(), stud)))
