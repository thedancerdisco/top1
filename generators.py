# nums = (i for i in range (10))
# # print(nums)
# # print(next(nums))
# # print(next(nums))
# # print(next(nums))
# for n in nums:
#     print(n)


# for n in nums:
#     print(n)
# del nums
# print(nums)

from typing  import Generator
def nums_generator(counter: int) -> Generator:
    for i in range(counter):
        yield i*i


nums = nums_generator(5)
print(nums)
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# for n in nums:
#     print(n)
