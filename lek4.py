#task1
# a: int=int(input("введи число а: "))
# b: int=int(input("введи число b: "))
# if a>b:
#     print('a больше b')
# elif a<b:
#     print("a меньше b")
# else:
#     print("a равно b")

#task2
# nums: str=input()
# nums_list=nums.split(",")
# print(nums_list)

# nums_list:list[str]=input().split()
# odd_sum:int=0
# even_sum:int=0
# for num in nums_list:
#     if int(num)%2==0:
#         odd_sum+=int(num)
#     else:
#         even_sum+=int(num)
# print("odd:", odd_sum)
# print("even:", even_sum)


# nums: list[int]=[90,2,3,4,5,6,90,7]
# max_elem:int=nums[0]
# max1_elem:int=nums[0]

# for num in nums:
#     if num>max_elem:
#         max_elem=num

# for num in nums:
#     if num>max1_elem and num<max_elem:
#         max1_elem=num

# print("predmax", max1_elem)
# print("max elem  ", max_elem)

# nums: list[int]=[90,2,3,4,5,6,90,7]
# nums.sort()
# nums=set(nums)
# nums=list(nums)
#  print(nums[-2])

num: int=int(input("vvedi chislo  "))
nums:list[int]=[]
for i in range(1,num+1):
    nums.append(i)

index:int=0

while index<len(nums):

    if nums [index]%3==0 or nums[index]%5==0:
        nums.pop(index)
    index+=1
# for num in nums:
#     print(num, end=" ")
print(nums)
