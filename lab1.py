# task1
class Student:
   def __init__(self, name=None, course=None, gender=None):
      if name is not None and not isinstance(name, str):
            raise TypeError("Invalid type for 'name' field.")
      if course is not None:
            if not isinstance(course, int):
               raise TypeError("Invalid type for 'course' field.")
            if course <= 0:
               raise ValueError("Course must be a positive integer.")
      if gender is not None and not isinstance(gender, bool):
            raise TypeError("Invalid type for 'gender' field.")

      self.__name = name
      self.__course = course
      self.__gender = gender
      print(f"Constructor called for student {self.__name}")

   def __del__(self):
      print(f"Destructor called for student {self.__name}")

   def print_info(self):
      gender_str = 'M' if self.__gender is not None and self.__gender else 'W' if self.__gender is not None else 'Unknown'
      print(f"Name: {self.__name}, Course: {self.__course}, Gender: {gender_str}")

   def get_name(self):
      return self.__name

   def set_name(self, name):
      self.__name = name

   def get_course(self):
      return self.__course

   def set_course(self, course):
      self.__course = course

   def get_gender(self):
      return self.__gender

   def set_gender(self, gender):
      self.__gender = gender

student = Student()
student1 = Student("Masha")
student2 = Student("Alex", 3)
student3 = Student("Maria", 2, False)

student.print_info()
student1.print_info()
student2.print_info()
student3.print_info()

student.set_name("Alexandra")
student.set_course(4)
student.set_gender(False)

print(student.get_name())
print(student.get_course())
print(student.get_gender())

del student
del student1
del student2
del student3
