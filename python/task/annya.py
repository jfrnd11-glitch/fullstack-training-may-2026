class student:

  def __init__(self,name,age,grade):
    self.name= name
    self.age=age
    self.grade=grade

  def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


student1 =  student("jayant kumar", 22 ,"A")
student2 =  student("sumit kumar", 32 ,"B")
student3 =  student("golu", 23 ,"C")

student1.display()
student2.display()
student3.display()


