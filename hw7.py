from typing import Any
students: list[list[Any]] = []# таблица=список с именами и оценками, каждый элемент=список списков
names: str
marks: list[int] = []# список оценок
stud_aver: list[list[str | float]] = []
stud_grade: list[list[str]] = []
num: int = int(input("введи количество студентов "))
#ввод данных
for i in range (num):
    names = input(f"введи имя {i+1}  студента ")
    marks_input = input("введи список оценок через пробел ")
    marks = [int(x) for x in marks_input.split()]
    students.append([names, marks])
print()

#печать введенного материала
for student in students:
    print(student)
print()

#функция поиска среднего без sum /len
def aver(mark:list[float])-> float:
    total, count = 0, 0
    for i in mark:
        total += i
        count +=1
    return round(total/count, 1)

#функция градации
def grade(x: float)->str:
    if x >=4.5:
        mark = "отлично"
    elif 3.5 <= x < 4.5:
        mark = "хорошо"
    elif 2.5 <= x < 3.5:
        mark = "удовлетворительно"
    else:
        mark = "неуд"
    return mark

#печать студентов и средних оценок + создание новых списков со средними оценками и градациями
print(f"{"имя":<15} {"средний балл":<3}")
for n, marks in students:
    print(f"{n:<15} {aver(marks):<3}")
    stud_aver.append([n, aver(marks)])
    stud_grade.append([n, grade(aver(marks))])
print()

#вывод на печать списка со средними оценками
print("вывод как списка сосредними баллами как массив")
for student in stud_aver:
        print(student)
print()

#вывод на печать списка с градациями
print("вывод как градация")
print(f"{"имя":<15} {"статус":<15}")
for n, grade in stud_grade:
    print(f"{n:<15} {grade:<15}")
print()

#поиск максимальной оценки по группе
max_name: str = ""
max_score: float = 0
for name, score in stud_aver:
    if score > max_score:
        max_score = score
        max_name = name
print(f"{"лучший студент"} {max_name}  {max_score}")
print()

#поиск минимальной оценки по группе
min_name: str = ""
min_score: float = 6
for name, score in stud_aver:
    if score < min_score:
        min_score = score
        min_name = name
print(f"{"худший студент"} {min_name}  {min_score}")
print()

#поиск средней оценки по группе
print("вывод среднего")
a: list[float] = []
for n, marks in stud_aver:
    a.append(marks)
print (f"{"средний балл по группе"} {aver(a)}")
print()

#поиск список имён студентов, у которых средний балл >= 4.5
print("список студентов,у которыхсредний балл > 4.5: ", *([n for n, marks in stud_aver if marks>=4.5]))
