dic: dict[str, int] = {}
while True:
        key = input('введи название категории ')
        if not key:
            break
        dic[key] = int(input("веди сумму покупок по категории "))
def get_total(products: dict[str, int])->None:
        print(f"всего товаров: {len(products)}\n общая сумма: {sum(products.values())}")
get_total(dic)
