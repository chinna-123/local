from constructor import Calculator


class ChildImp(Calculator):
    num1 = 20

    def __init__(self):
        Calculator.__init__(self, 3, 4)

    def getCompleteData(self):
        return self.num1 + self.num + self.getD()


obj = ChildImp()
print(obj.getCompleteData())