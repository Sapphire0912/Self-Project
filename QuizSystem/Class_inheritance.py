class Info(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHi(self):
        print(self.name + " 說你好")


class Student(Info):
    def __init__(self, name, age, major, grade):
        super(Student, self).__init__(name, age)
        self.major = major
        self.grade = grade

    def study(self):
        print(self.name + " 正在努力讀 " + self.major)


lily = Student("Lily", 18, "English", "A+")
print(lily.name, lily.age, lily.major, lily.grade)
lily.sayHi()
lily.study()
