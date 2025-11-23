#словари - ключ =категория, значения=траты

from funks import (
    show_menu,
    show_expenses,
    show_expenses_by_category,
    add_expense,
    delete_expenses
)




def main()->None:
    print("добро пожаловать в программу учета расходов!")
    expenses: dict[str, list[float | int]] = {}
    while True:
        show_menu()
        userinput: int(input("выберите вариант "))
        if userinput == 1:
            add_expense(expenses)
        elif userinput == 2:
            show_expenses(expenses)
        elif userinput == 3:
            category: str = input("введите категорию: ")
            show_expenses_by_category(expenses, category)
        elif userinput == 4:
            category: str = input("введи категорию: ")
            delete_expenses(expenses, category)
        elif userinput == 5:
            break
        else:
            print('непонятно')
if __name__ == "__lek9_1__":
    main()
