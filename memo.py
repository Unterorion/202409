import sys

option = sys.argv[1]

if option == 'a':
    content = sys.argv[2]
    f = open("C:\\Work\\202409\\memo.txt", 'a')
    f.write(content + "\n")
    f.close()
elif option == 'r':
    f = open("C:\\Work\\202409\\memo.txt", 'r')
    print(f.read())
    f.close()
elif option == 'i':
    f = open("C:\\Work\\202409\\memo.txt", 'w')
    f.close()
else:
    print("Type an appropriate option!")