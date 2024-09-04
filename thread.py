import time
import threading

def task_5s():
    for i in range(5):
        time.sleep(1)
        print("Working: %s\n" % (i+1))

print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target = task_5s) #t는 task_5s 함수를 수행하는 thread이다
    threads.append(t)

for t in threads:
    t.start() #t를 시작한다

for t in threads:
    t.join() #t가 끝날 때까지 대기

print("End")