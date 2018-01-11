class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employees", Employee.empCount

    def displayName(self):
        print "Name : ", self.name, ", Salary : ", self.salary

class Parent:
    parentAttr = 100

    def __init__(self):
        print "Calling parent's constructor"

    def parentMethod(self):
        print "Calling parent's method"

    def setAttr(self, attr):
        Parent.parentAttr = attr;

    def getAttr(self):
        print "Parent Attribute : ", Parent.parentAttr


class Check:
    def __init__(self):
        print "Check Method"

class Child(Parent, Check):
    def __init__(self):
        print "Calling child Constructor"
        # super(Child, self).__init__()

    def childMethod(self):
        print "Calling Child Method"


c = Child()
c.childMethod()
c.parentMethod()
# c.setAttr(2100)
# c.getAttr()

print isinstance(c, Parent)
print isinstance(Child, Parent)



#
# print "Employee.__doc__ : ", Employee.__doc__
# print "Employee.__name__:", Employee.__name__
# print "Employee.__module__:", Employee.__module__
# print "Employee.__bases__:", Employee.__bases__
# print "Employee.__dict__:", Employee.__dict__
#
# e1 = Employee("Satish", 5000)
# e2 = Employee("Prashanth", 6000)
#
# e1.displayCount()
# e2.displayName()