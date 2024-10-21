class Calculator:

    num = 10

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('hello world')

    def getD(self):
        return self.a + self.b + Calculator.num


obj = Calculator(2, 3)
print(obj.getD())
print(obj.num)

obj1 = Calculator(4, 5)
print(obj1.getD())
print(obj1.num)