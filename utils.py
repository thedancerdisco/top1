from typing import Union, List, Any, Optional

def greet(name:str)->str:
    return   f"hello, {name}"


def greet(name:str)->str:
    return   f"hni hao, {name}"


def sum(num1: Union[int,float], num2: Optional[int] = 0)->int | float:
    return num1 + num2


def multi(num1: int | float, num2: int | float)->int | float:
    return num1 * num2

def print_list(arr: list[Any]) ->None:
    print(arr)

if __name__== "__lek9__":
    print_list([1,2,3])
