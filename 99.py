#구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print("")

print("")

for i in range(2,10):
    result = []
    for j in range(1,10):
        result.append(i*j)
    print(result)

print("")

#3의 배수
result = 0
i = 1
while i <= 1000:
    if i%3 == 0:
        result += i
    i += 1
print(result)

print("")

result = []
i = 1
while i <= 100:
    if i%3 == 0:
        result.append(i*2)
    i += 1
print(result)

print("")

#별 표시
i = 0
while True:
    i += 1
    if i>5: break
    print("*"*i)

print("")

# 1부터 100까지 표시
for i in range(1,101):
    print(i)

print("")
for i in range(1,101):
    print(i, end=" ")

print("\n")

#평균
scores = [34, 98, 39, 85, 20, 38, 94, 92, 72, 52]
total = 0
for score in scores:
    total += score
average = total/len(scores)
print(average)

print("")

#list comprehension
nums = [1,2,3,4,5]
result = [num*2 for num in nums if num%2==1]
print(result)
print("")
result = [i*2 for i in range(1,100) if i%3==0]
print(result)