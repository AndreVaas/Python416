class Student:
    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()

    def show(self):
        print(f"{self.name} => {self.laptop.model}, {self.laptop.cpu}, {self.laptop.ram}")

    class Laptop:
        def __init__(self):
            self.model = "HP"
            self.cpu = "i7"
            self.ram = 16


student1 = Student("Roman")
student2 = Student("Vladimir")

student1.show()
student2.show()
