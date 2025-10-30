n: int = int(input('vvedi kol-vo strok '))
m:int = int(input('vvedi kol-vo stolbov '))
matrix1: list[list[int]] = []
matrixt: list[list[int]] = []
# for i in range(n):
#     print('vvedi строку через пробел ',  i+1)
#     str1: list[str] = input().split()
#     row = []
#     for j in str1:
#         row.append(int(j))

#     matrix1.append(row)



matrix1=[[int(x) for x in input(f'введи {i+1}-ю строку через пробел ').split()] for i in range(n)]
print("исходная матрица ", matrix1)
matrixt = [[matrix1[i][j] for i in range(n)] for j in range(m)]
# for i in range(n):
#     t=[]
#     for j in range(m):
#         t.append(matrix1[j][i])
#     matrixt.append(t)
print('транспонированная матрица')
for i in range(m):
    for j in range(n):
        print(matrixt[i][j],  end="  ")
    print()
