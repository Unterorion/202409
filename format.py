#왼쪽 정렬
print("%-10s" % 'hi')
print("{0:<10}".format('hi'))
print(f'{"hi":<10}')
print("{0:=<10}".format('hi'))
print(f'{"hi":=<10}')

print("\n")
#오른쪽 정렬
print("%10s" % 'hi')
print("{0:>10}".format('hi'))
print(f'{"hi":>10}')
print("{0:=>10}".format('hi'))
print(f'{"hi":=>10}')

print("\n")
#가운데 정렬
print("{0:^10}".format('hi'))
print(f'{"hi":^10}')
print("{0:=^10}".format('hi'))
print(f'{"hi":=^10}')

print("\n")
#소수점
pi = 3.1415926535
print("%0.4f"%pi)
print("{0:0.4f}".format(pi))
print(f'{pi:0.4f}')

print("\n")
#소수점 왼쪽 정렬
print("%-10.4f"%pi)
print("{0:<10.4f}".format(pi))
print(f'{pi:<10.4f}')
print("{0:=<10.4f}".format(pi))
print(f'{pi:=<10.4f}')

print("\n")
#소수점 오른쪽 정렬
print("%10.4f"%pi)
print("{0:>10.4f}".format(pi))
print(f'{pi:>10.4f}')
print("{0:=>10.4f}".format(pi))
print(f'{pi:=>10.4f}')