
# Experiment No: 06
# Program to Demonstrate Polymorphism and Encapsulation

# Polymorphism

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Encapsulation

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks!")


# Main Program

print("Demonstration of Polymorphism")

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.sound()

print("\nDemonstration of Encapsulation")

student = Student("Jariab", 85)

print("Student Name:", student.name)
print("Original Marks:", student.get_marks())

student.set_marks(95)

print("Updated Marks:", student.get_marks())
