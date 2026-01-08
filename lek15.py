# try-except. reduce. Zip. JSON. CSV.
# ошибка - ситуация, при которой программа не может продолжить работу
# ОШибки бывают синтаксические и во время выполнения run time error
# примеры ошибок - деление на 0, неверный индекс списка, обращение к несуществующему ключу словаря
# конструкция try / except
# try:
    # код который может вызвать ошибку
# except типошибки:
    # обработка ошибки
# try:
#     num: int = int(input())
#     num2: int = int(input())
#     print(num/num2)
#     # print(len(num))
# # except ValueError as e:
# #     print(f"введи число!\n ошибка {e}")
# # except ZeroDivisionError:
# #     print("делить на 0 нельзя")
# except Exception as e:
#     print(f"ошибка: {e}")
# else:
#     print("кспех")


# try:
#     num: int = int(input())
#     num2: int = int(input())
#     print(num/num2)
#     # print(len(num))
# # except ValueError as e:
# #     print(f"введи число!\n ошибка {e}")
# # except ZeroDivisionError:
# #     print("делить на 0 нельзя")
# except Exception as e:
#     print(f"ошибка: {e}")
# finally:
#     print("кспех")


# def calc(a:int, b: int, op:str)->float:
#     try:
#         if op =="+":
#             return a+b
#         elif op == "/":
#             return a/b
#         else:
#             raise ValueError("неизвестная операция")
#     except Exception as e:
#         print(f"error: {e}")
#     # except ZeroDivisionError:
#     #     print("деление на ноль запрещено")
#     # except ValueError as e:
#     #     print(e)

# print(calc(2,3,"-"))


# функция reduce может пригодится если надо свести спислк к какому то числу, напремер перемножить все числа
# from functools import reduce
# arr = list(range(1,5+1))
# multiply = lambda a,b,c: a+b+c
# print(reduce(multiply, arr))


# что делает функция зип
# функция объединяет  несколко последовательностей(списки кортежи, строки)
# создает кортежи  изэлементов, стоящих на 1 и том же индексе
# останавливается по самой короткой последователности
# nums: list[int] = [1,2,3,4,5]
# words: list[str] = ["a", "b", "c"]
# cities: list[str] = ["moscow", "kazan", "omsk"]
# popul: list[int] = [20_000_000, 1300000, 900_000]
# pop_dict: dict[str, int] = {}
# # for city, pop in zip(cities, popul):
# #     pop_dict[city] = pop
# print(pop_dict)
# a=zip(cities, popul)
# c_1, p_1 = zip(*list(a))
# print(c_1, p_1)



# import csv
# with open("data.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     print(reader)
#     pri=list(reader)
#     # for row in pri:
#     #     print(row)
#     # print(pri)
#     pri_list =list(zip(*pri))
# # print(pri_list)
#     data={}
#     for col in pri_list:
#         data[col[0]] = col[1:]
#     print(data)
# print(file)
# file.close()



# import csv
# with open("data.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)

#     content=list(reader)

#     print(content)

# with open("output.csv", "x",newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerows(content)




# import json
# with open("example.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
# # with open("example.json", "r", encoding="utf-8") as file:
# with open("output.json", "w",encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False)
# print(data)
# print(type(data))





def generate_report(json_path:str)->dict[str,int]
with open(json_path, "r", encoding="utf-8") as file:
    result:dict[str, int]
    data = json.load(file)

    for task in data:
        if not result.get(task["assignee"]):
            result[task["assignee"]]=1
        else:
            result[task["assignee"]]+=1
    return result
print(generate_report("practise.json"))
