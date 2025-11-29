from typing import Any

def linear_search(elements: list[Any], elem: Any)-> int | str:
    for i in range(len(elements)):
        if elements[i] == elem:
            return i
    return "не найдено"

def binary_search(elements: list[int], elem: int)-> bool:
    elements.sort()
    start: int = 0
    end: int = len(elements) - 1

    for i in range(len(elements)):
        mid_index: int = start + (end - start) // 2
        if elements[mid_index] == elem:
            return True
        elif elements[mid_index] > elem:
            end = mid_index - 1
        else:
            start = mid_index + 1

    return False

def bubble_search(elements: list[int | float], reverse: bool = False)-> None:
    for i in range(len(elements)-1):
        is_sorted: bool = True
        for j in range(len(elements)-1-i):
            if reverse:
                if elements[j] <= elements[j+1]:
                    elements[j], elements[j+1] = elements[j+1], elements[j]
                    is_sorted = False
            else:
                if elements[j] >= elements[j+1]:
                    elements[j], elements[j+1] = elements[j+1], elements[j]
                    is_sorted = False

        if is_sorted:
            break

def get_min(elements: list[Any])->None:
    if not elements:
        print("empty list")
        return
    min_el = elements[0]
    for i in range(1, len(elements)):
        if elements[i] <= min_el:
            min_el = elements[i]
    print(f"минимальный элемент: {min_el}")

def get_max(elements: list[Any])->None:
    if not elements:
        print("empty list")
        return
    max_el = elements[0]
    for i in range(1, len(elements)):
        if elements[i] >= max_el:
            max_el = elements[i]
    print(f"максимальный элемент: {max_el}")

def get_avg(elements: list[Any])->None:
    summa: float = 0
    dlina: float = 0
    for i in range(len(elements)):
        summa+=elements[i]
        dlina+=1
    print(f"среднее значение: {summa/dlina}")

def get_median(elements: list[Any])->None:
    bubble_search(elements)
    if len(elements) % 2 == 0:
        med:float = (elements[len(elements)//2]+elements[(len(elements)//2)+1])/2
    else:
        med = elements[(len(elements)+1)//2-1]
    print(f"медианное значение: {med}")

def show_menu()->None:

    print("выбери действие ")
    print("1. найти число линейный поиск")
    print("2.найти число бинарный поиск")
    print("3.отсортировать пузырьком")
    print("4. найти минимальное число")
    print("5. найти максимальное число")
    print("6. найти среднее занчение ")
    print("7. найти медиану")
    print("8.выйти")

if __name__ == "__main__":
    user_nums: list[int | float] = [float(num)  for num in input('vvedi spisok ').split()]
    while True:
        show_menu()
        user_input: str = input('viberi punkt menu ')
        if user_input == "1":
            search_num: float = float(input("vvedi chislo: "))
            print(linear_search(user_nums, search_num))
        elif user_input == "2":
            search_num: float = float(input("vvedi chislo: "))
            print(binary_search(user_nums, search_num))
        elif user_input == "3":
            bubble_search(user_nums)
            print(user_nums)
        elif user_input == "4":
            get_min(user_nums)
        elif user_input == "5":
            get_max(user_nums)
        elif user_input == "6":
            get_avg(user_nums)
        elif user_input == "7":
            get_median(user_nums)
        elif user_input == "8":
            break
        else:
            print("неизвестная команда")
