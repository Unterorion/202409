m = 0
n = 0

while n < 1000:
    if n%3==0 or n%5==0:
        m += n
    n += 1

print(m)