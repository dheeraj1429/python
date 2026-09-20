import asyncio
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def func_1():
  with lock_a:
    print("Task 1 with acquiring lock a")
    with lock_b:
      print("Task 1 with acquiring lock b")

def func_2():
  with lock_b:
    print("Task 2 with acquiring lock b")
    with lock_a:
      print("Task 2 with acquiring lock a")

t1 = threading.Thread(target=func_1)
t2 = threading.Thread(target=func_2)

t1.start()
t2.start()

t1.join()
t2.join()