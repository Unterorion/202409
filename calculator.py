class FourCal():
    def __init__(self, input1, input2):
        self.first = input1
        self.second = input2

    def sum(self):
        return self.first + self.second
    
    def sub(self):
        return self.first - self.second
    
    def prod(self):
        return self.first * self.second
    
    def div(self):
        return self.first / self.second

a = FourCal(4.5, 2.8)
print(a.sum())
print(a.sub())
print(a.prod())
print(a.div())

#상속
class PwrCal(FourCal):
    def pwr(self):
        return self.first**self.second
    
a = PwrCal(4.5, 2.8)
print(a.pwr())

#method overide
class SafeCal(PwrCal):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first / self.second
        
a = SafeCal(4.5, 2.8)
b = SafeCal(4.5, 0)
print(a.div())
print(b.div())

c = FourCal(4.5, 0)
print(c.div())