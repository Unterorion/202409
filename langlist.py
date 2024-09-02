lanlist = ['python', 'java', 'c']

#리스트 요소 순서대로
i = ''

for j in range(len(lanlist)):
    if j < len(lanlist)-1:
        i = i+lanlist[j]+", "
    else:
        i = i+lanlist[j]

print(i)

#리스트 요소 역순
k = ''

for l in range(len(lanlist)):
    if l<len(lanlist)-1:
        k = k+lanlist[-1-l]+", "
    else:
        k = k+lanlist[-1-l]

print(k)