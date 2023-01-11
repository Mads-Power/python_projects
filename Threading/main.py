import threading
import time

def func():
    print('ran ')
    time.sleep(1)
    print('done')

# create new thread
x1 = threading.Thread(target=func, args=())
x1.start()



def count(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.01)
for _ in range(2):
    x = threading.Thread(target=count, args=(10,))
    x.start()

print("active count", threading.activeCount())
print('Done')