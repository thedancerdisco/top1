def show_menu()->None:
    print("выбери действие")
    print("1. добавить в расход")
    print("2.посмотреть расходы")
    print("3.посмотреть расходы по категории")
    print("4.удалить расходы")
    print("5.выйти")


def add_expense(expenses: dict) ->None:
    category: str = input("введи категорию: ")
    expense: list[int] =[ float(num) for num in  input().split()]

    if not expenses.get(category):
        expenses[category] = expense
    else:
        for ex in expense:
            expenses[category].append(ex)
print(expenses)


def show_expenses(expenses:dict)->None:
    for key, val in expenses.items():
        print(f"{key} - {sum(val)}")

def show_expenses_by_category(expenses:dict, category: str)->None:
    print(f"{category} - {sum(expenses.get(category, 0))} ")

def delete_expenses(expenses:dict, category: str)-> None:
    if category in expenses:
        del expenses[category]
    else:
        print('нет такой категории! ')
