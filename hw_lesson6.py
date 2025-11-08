a = int(input('enter first number: '))
b = int(input('enter second number: '))
array:list[int] = [sum( j for j in range(1, i+1) if i % j ==0) for i in range(a, b+1) ]
print(a+array.index(max(array)), max(array) )
