# nums: list[int] = [1,3,4,5,67]
# print(type(nums))

# print(nums)

# data: dict[str, str] = {
#     "name" : "Anna",
#     "age" : "18",
#     "password": "qwerty123"
# }



# data: dict[str, str] = {
#     "sep" : "-",
#     "end" : "!",
# }


# print(*nums, **data)

# def show_params(*args, **kwargs)->None:
#     print(args)
#     print(kwargs)
#     print("positionals:", *args)
#     print("keyargs:", end=' ')
#     for key, val in kwargs.items():
#         print(f"{key}={val}", end=" ")
#     print()
# show_params("првиет", 1,3,4, True, 3.14, age=18)

# def create_profile(name:str, age:int, city:str, **kwargs)->None:
#     print(f"имя: {name}")
#     print(f"возраст: {age}")
#     print(f"город: {city}")
#     for key, val in kwargs.items():
#         print(f"{key}: {val}")

# create_profile("анна", 18, city="москва", hobby="рисование")



# def summator(*args, show_steps:bool=False)->None:
#     if show_steps:
#         steps: str = "+".join(str(arg) for arg in args)
#         print(f"{steps}={sum(args)}")
#     else:
#         print(sum(args))

# summator(1,2,3,4,show_steps=True )


def convert_to_pyton_case(text:str)->str:
    if len(text) ==0:
        return ""

    newtext: str = ""
    newtext += text[0].lower()

    for i in range(1,len(text)):
        if text[i].isupper():
            newtext += "_"

        newtext += text[i].lower()
    return newtext


text: str = "ThisIsCamelCased"
print(convert_to_pyton_case(text=text))



# def is_password_good(password:str)->bool:

#     flag_len: bool = False
#     flag_up: bool = False
#     flag_low: bool = False
#     flag_dig: bool = False
#     flag_pass: bool = False

#     if len(password) >=8:
#         flag_len = True

#     for i in range(len(password)):
#         if password[i].islower():
#             flag_low = True
#         elif password[i].isdigit():
#             flag_digit = True
#         elif password[i].isupper():
#             flag_up = True
#     if flag_len and flag_up and flag_digit and flag_low:
#         flag_pass = True
#     else:
#         flag_pass = False
#     return flag_pass
# print(is_password_good(password="Ahgg12qwer"))
