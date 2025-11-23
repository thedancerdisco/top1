# import random
# figures: list[str]=['kamen', 'nozn','paper']
# u_c:str=input('vvedi figuru:')
# c_c: str=random.choice(['kamen', 'nozn','paper'])
# print('vibor pc ', c_c)
# while thue:
#     u_c:str=input('vvedi figuru:')
#     c_c: str=random.choice(['kamen', 'nozn','paper'])
#     print('vibor pc ', c_c)
# if u_c=='kamen' and c_c=='nozn'\
#     or u_c=='nozn' and c_c=='paper'\
#     or u_c=='paper' and c_c=='kamen':
#     print('win!!')
# elif u_c==c_c:
#     print('nichya')
# elif u_c not in ['kamen', 'nozn','paper']:
#     print('figura ne naidena')
# else:
#     print('loose')

# userbrake:str=input('do u wanna continue? y/n', end='')
# if  userbrake=='n':
#     break
# elif userbrake not in ['y', 'n']:
#     print('i dont understand')

# arr:list[int]=[i**2 for i in range(1,6)]

# print(arr)

# arr:list[int]=[i for i in range(1,22) if i%3==0]

# print(arr)


# name: str='marat'
# age: str='37'
# print(f"hello, {name} . your age {age} ")


# import random

# matrix: list[list[int]]=[]

# n:int=10
# m:int =7
# for i in range(n):
#     row: list[int]=[]
#     for j in range(m):
#         row.append(random.randint(1,100))
#     matrix.append(row)
# for row in matrix:
#     print(row)
# row_sums: list[int]=[sum(row) for row in matrix]
# print(row_sums)


# cols:int=len(matrix[0])
# cols_sums: list[int]=[]

# for j in range(cols):
#     col_sum: int=0
#     for i in range(len(matrix)):
#         col_sum+=matrix[i][j]
#     cols_sums.append(col_sum)
# print()
# print(cols_sums)

# import random
# matrix: list[list[int]]=[]

# for i in range(5):
#     row: list[int]=[]
#     for j in range(5):
#         row.append(i*5+j+1)
#     matrix.append(row)

# for  row in matrix:
#     print(row)


# import random
# matrix: list[list[int]]=[]

# for i in range(5):
#     row: list[int]=[]
#     for j in range(5):
#         row.append(i*5+j+1)
#     matrix.append(row)

# for  row in matrix:
#     print(row)
# diasum:int=0
# for i in range (len(matrix)):
#     diasum+=matrix[i][i]
# print(diasum)



# import random
# matrix: list[list[int]]=[]

# for i in range(5):
#     row: list[int]=[]
#     for j in range(5):
#         row.append(i*5+j+1)
#     matrix.append(row)

# for  row in matrix:
#     print(row)
# diasum:int=0
# for i in range (len(matrix)):
#     diasum+=matrix[i][i]
# print(diasum)

# diasum_list: int=sum([matrix[i][i] for i in range(len(matrix))])
# print(diasum)

# print()

#ручной максимум
# max: int = matrix[0][0]
# indexes: list[int]=[0,0]
# for i, row in enumerate( matrix):
#     for j, item in enumerate(row):
#         if item>max:
#             max=item
#             indexes[0], indexes[1]=i, j
# print(max, indexes)

# max_el: int=matrix[0][0]
# for row in matrix:
#     maxinrow: int =max(row)
#     if maxinrow>max:
#         max_el=maxinrow
# print(max_el)



#даны 2 матрицы.посчитать их поэлементнуюумму - сформировать новуюматрицу
# matrix1: list[list[int]]=[[1,2,3],[4,5,6]]
# matrix2: list[list[int]]=[[8,9,10], [11,12,13]]
# matrix3: list[list[int]]=[]

# for i in range(len(matrix1)):
#     row: list[int]=[]
#     for j in range(len(matrix1[i])):
#         row.append(matrix1[i][j] +matrix2[i][j])
#     matrix3.append(row)
# for row in matrix3:
#     print(row)

matrix: list[list[int]]=[
    [1,2,3,4],
    [2,1,5,6],
    [3,5,1,8],
    [1,1,1,1]
    ]

sim_flag:bool=True
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]!=matrix[j][i]:
            sim_flag=False
            break
if sim_flag==True:
    print('yes')
else:
    print('n')
