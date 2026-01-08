def hello():
    pass

print(hello)

hello2 = lambda x: x*x
print(hello2(4))


hello2 = lambda x, y: x == y
print(hello2(4))

hello2 = lambda x, y: x **2 if  y%2 ==0  else x**3
print(hello(2,4))

list1=["1", "2"]
print(list1)
list2=list(map(int, list1))
print(list2)

nums = [1,2,3,4,5]
newnums = list(filter(lambda x:x%2 == 0, nums))


from typing import Callable
is_even:callable = lambda x:x%2 == 0
toupper: Callable[[str], str]: lambda x: x.upper()
lastchar: Callable[[str], str]: lambda x: x[-1]


def apply(func: callable, iterable: Iterable):
    for i in range(iterable):
        iterable[i] = func(iterable[i])

def sq(x: int | float)-> int |float:
    return x*x

def trans(n):
    return lambda x: x**n
triple = trans(3)
