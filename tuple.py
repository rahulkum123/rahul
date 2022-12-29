class student:
    def setdata(self):
        self.name= input("Enter name:")
        self.rollno =int(input("Enter roll no:"))
        self.per=float(input("percentage:"))
    def display(self):
        print("name:",self.name)
        print("roll no:",self.rollno)
        print("percentage:",self.per)

a=student()
a.setdata()
a.display()