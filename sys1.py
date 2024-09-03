import sys
args = sys.argv[1:] #이 프로그램(파일) 실행할때 받는 인수를 args라고 한다는 뜻
for i in args:
    print(i, end=" ") #end 기본값은 \n
