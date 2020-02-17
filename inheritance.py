#Code to understand the concept of Inheritance
class Pappa():
    def feature1(self):
        print("Strict")

    def feature2(self):
        print("Loving")

class Beta(Pappa):
    def feature3(self):
        print("Naughty")

    def feature4(self):
        print("Loyal")



a1=Pappa()
b1=Beta()

b1.feature2()
b1.feature4()
