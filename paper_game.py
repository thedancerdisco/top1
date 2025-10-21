user_fig: str=str(input("старт игры камень-ножницы-бумага \n веди фигуру: "))
PC_fig:str=str("камень")
if  user_fig== "бумага"and PC_fig=="камень" or user_fig== "ножницы"and PC_fig=="бумага" or user_fig== "камень"and PC_fig=="ножницы":
    print("user wins")
elif user_fig==PC_fig:
    print("ничья")
else:
    print("PC wins")
