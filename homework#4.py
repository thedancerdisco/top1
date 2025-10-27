# #task 1
# m: int=int(input('vvedi m  '))
# n: int= int(input('vvedi n '))

# for i in range(m,n+1):
#     if i % 17==0 or (i %3==0 and i%5==0) or i%10==9:
#         print(i)


#task 2 sposob1

# n: int=int(input('vvedi chislo   '))

# for i in range(1,n+1):
#     if i<5:
#         print(i)
#     if 9<i<17:
#         print(i)
#     if 37<i<78:
#         print(i)
#     if  i>87:
#         print(i)

#task 2 sposob 2
# n: int=int(input('vvedi chislo   '))
# for i in range(1,n+1):
#       if 5<=i<=9 or 17<=i<=37 or 78<=i<=87:
#             continue
#       print(i)

#task 2 sposob 3
# n: int=int(input('vvedi chislo   '))
# i=0
# while i<=n-1:
#     i+=1
#     if 5<=i<=9 or 17<=i<=37 or 78<=i<=87:
#         continue
#     print(i)

#task 3 sposob 1
# n: int=int(input('vvedi chislo   '))
# j=0
# while  j<=n-1:
#     j+=1
#     for i in range(1,4):
#         print(n, end=" ")
#     print()

#task 3 sposob 2

# n = int(input())

# for i in range(n):
#     print(n, n, n)
