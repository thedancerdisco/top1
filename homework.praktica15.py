#task15
# spisok: list[str] = max(input('vvedi spisok slov ').split(' '), key=len)
# print(f' самая длинное слово ',spisok)

#task14
# nums: list[int] = [5, 2, 3, 2, 5, 2]
# nums = [i for i in nums if i != 2]
# print(nums)

#task13

# j = 0
# nums = [int(x) for x in input("Введите числа через пробел: ").split()]
# for i in range(1, len(nums)):
#     if nums[i]>nums[i-1]:
#         j+=1
# print("Количество элементов, больше предыдущего: ", j)

#task12
# n: int = int(input("Введите числo: "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(f"{i}*{j}={j*j}", end=" ")
#     print()

#task11
# words: list[str] = ["apple", "banana", "cherry", "date"]
# big_words = []
# for l in words:
#     big_words.append(l.upper())
# print(big_words)

#task10
# nums = [int(x) for x in input("Введите числа через пробел: ").split()]
# avg=sum(nums)/len(nums)
# print("среднее  будет  ", avg)
# nums1 = [x for x in nums if x > avg]
# print(nums1)

#task9
# n: int = int(input('vvedi chislo n '))
# fact = 1
# for i in range(1, n+1):
#     fact*=i
# print(fact)

#task8
# n: int = int(input('vvedi chislo n '))
# for i in range(1, n+1):
#     if i % 3 ==0:
#         continue
#     else:
#         print(i)

#task7№1
# names:list[str] = ["Анна", "Борис", "Катя", "Дима"]
# for i in range(len(names)):
#     if names[i][0] == 'К':
#         print(names[i])

# #task7№2
# names:list[str]  = ["Анна", "Борис", "Катя", "Дима"]
# for name in names:
# if name.startswith("К"):
# print(name)

#task6
# nums = [int(x) for x in input("Введите числа через пробел: ").split()]
# print(sum(nums))


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
# nums = [int(x) for x in input("Введите числа через пробел: ").split()]
# odd_sum:int=0
# even_sum:int=0
# for num in nums:
#     if num %2 == 0:
#         odd_sum += int(num)
#     else:
#         even_sum += int(num)
# print("odd:", odd_sum)
# print("even:", even_sum)

#task3
# nums: list[int]=[5,3,8,6,2,8,3]
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

#task4
# num: int=int(input("vvedi chislo  "))
# nums:list[int]=[]
# for i in range(1,num+1):
#     nums.append(i)

# index:int=0

# while index<len(nums):

#     if nums [index]%3==0 or nums[index]%5==0:
#         nums.pop(index)
#     index+=1

# print(nums)

#task5

nums: list[int]=[5,3,8,6,2, 100,8,3]

print(max(nums))
