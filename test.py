original_dict = {"banana": 3, "apple": 1, "cherry": 2}
print("До sorted():", original_dict)
print()
result =sorted(original_dict)
print(" после Sorted", result)
print()
result =sorted(original_dict.items())
print(" после Sorted.items", result)
