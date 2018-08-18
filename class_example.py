class PythonClass:
    ' This is a Python class with two attributes and two methods.'
    x = 10
    y = 10
    def __init__(self):
        pass
    def method1(self, x,y):
        self.x = x
        self.y = y
myClass = PythonClass()
myClass.method1(5,4)
print(myClass.x)
print(myClass.y)
