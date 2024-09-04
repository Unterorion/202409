try:
    age = int(input('Your age: '))
except:
    print('Input a correct age.')
else:
    if age <= 18:
        print("Adults only")
    else:
        print("Welcome")