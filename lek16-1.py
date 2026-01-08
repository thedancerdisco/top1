class Student:
    # имя фамилия отчество возраст класс
    def __init__(
            self,
            name:str,
            surname:str,
            age:int,
            lastname: str,
            grade:str
    ) ->None:
        self.name = name
        self.surname=surname
        self.lastname = lastname
        self.age = age
        self.grade = grade
    def show_info(self):
        print(f"FIO:  {self.surname}, {self.name}, {self.lastname}")
        print(f"Age : {self.age}")
        print(f"class: {self.grade}")

class Journal:
    def __init__(self)->None:
        self.__students: list[Student] =[]

    def show_students(self)->None:
        row_index:int = 1
        for st in self.__students:
            print(f"{row_index}. {st.surname} {st.name} {st.lastname}")
            row_index +=1

    def add_student(self, st:student)->None:
        self.__student.append(st)

    def del_student(self, name:str, surname:str, lastname:str)->None:
        pass

    def show_student(self, st:student)->None:
        for st in self.__students:
            if st.name == name and st.surname == surname and st.lastname == lastname:
                st.showinfo()
                break
journal = Journal()

s_1 = Student(
    name = "Ivan",
    surname = "ivanov",
    age = 12,
    lastname = "ivanovich",
    grade = "6 A"
)

s_2 = Student(
    name = "petr",
    surname = "petrov",
    age = 18,
    lastname = "petrovich",
    grade = "11 C"
)

journal.add_student(s_1)
journal.add_student(s_2)
journal.add_student(s_3)
print()

journal.show_students()
print()

journal.show_student(name = "ivan", surname = "ivanov", lastname = "ivanovich")
for student in [s_1, s_2]:
    student.show_info()
    print()
