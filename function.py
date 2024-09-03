#매개변수
def sub(a,b):
    return a-b
print(sub(a=2, b=5))
print(sub(2,5))
print(sub(b=5, a=2))

print("")

#복수의 매개변수
def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(sum(1,2,3))

print("")

#키워드 매개변수
def print_dict(**kwarg):
    print(kwarg)

print_dict(a=1, b='python')

print("")