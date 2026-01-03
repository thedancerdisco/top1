students = [
{"name": "Анна", "score": 88},
{"name": "Павел", "score": 95},
{"name": "Игорь", "score": 72},
{"name": "Марина", "score": 91},
]
stud = list(filter(lambda x: x["score"]>85, sorted(students, key = lambda x: x["score"] )))
print(list(map(lambda x: x["name"].upper(), stud)))
