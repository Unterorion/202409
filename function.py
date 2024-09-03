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

#초기값
def intro(name, age, male=True):
    print("My name is %s."%name)
    print("I'm %d years old."%age)
    if male:
        print("I'm male.")
    else:
        print("I'm female.")

intro('kyj', 30)
intro('kyj', 30, True)
intro('jea', 27, False)

print("")

#리턴 개수
def add_mul(a,b):
    return a+b, a*b

result = add_mul(3,4)
print(result)

result1, result2 = add_mul(3,4)
print(result1)
print(result2)