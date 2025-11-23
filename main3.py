# nums: list[int] = [1,2,3,4,"hello",3.14]
# tup: tuple=(1,2,3,4,5)
# natural: set={2,4,6,}

#print(nums[4])

#for i in nums:
#    print(i)

#for i in range(6):
#    print(nums[i])

#print(len(nums))
#for i in range(len(nums)):
 #   print(nums[i])
# for i in range(20, 10,-2):
#     print(i, end="")

# num: int=int(input("enterr number"))
# while num !=0:
#     num:

# m: int=int(input())
# n: int=int(input())
# #task 1
# for i in range(m,n+1):
#     print(i)


# m: int=int(input())
# n: int=int(input())

# for i in range(m,n-1,-1):
#    if i % 2==1:
#         print(i)

# num: str=input("enter number ")
# for i in range(1, len(num)+1):
#     print(num[-i], end="")

num: int=int(input("enter number "))
while num!=0:
    print(num %10, end="")
    num//=10
