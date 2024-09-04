from random import *

data = []
for i in range(45):
    data.append(i+1)

'''lotto = []
for j in range(6):
    idx = randint(1, 45-j)
    lotto.append(data[idx-1])
    data.pop(idx-1)'''

lotto = []
while len(lotto) < 6:
    idx = randint(1,len(data))
    lotto.append(data.pop(idx))

lotto.sort()
print(lotto)
print(len(data))