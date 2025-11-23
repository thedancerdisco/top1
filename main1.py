num: int=int(input("введи число: "))
if (1000<=num<10000) and (num % 7==0 and num % 17==0):
    print("yes")
else:
    print("no")
