# import threading
# import time
# from functools import wraps

# event = threading.Event()

# def task():
#   print("Task started...")
#   time.sleep(3)
#   event.set()

# def end():
#   event.wait()
#   if event.is_set():
#     print("Task end..")

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=end)

# t1.start()
# t2.start()

# def custom_exception_handler(args):
#   print(args)

# threading.excepthook = custom_exception_handler

# def do_something():
#   print("Do something with error")
#   raise ValueError("This is the error function.")

# def do_something_2():
#   print("Do something 2")

# tasks = [threading.Thread(target=do_something), threading.Thread(target=do_something_2)]
# for i in tasks:
#   try:
#     i.start()
#     i.join()
#   except ValueError as e:
#     print(f"Error {e}")
# print("Work completed")

# lock = threading.Semaphore(3)

# def display(name: str):
#   lock.acquire()
#   for i in range(0, 3):
#     print(f"Name {name} with i #{i}")
#     time.sleep(2)
#   lock.release()

# task1 = threading.Thread(target=display, args=("task1",))
# task2 = threading.Thread(target=display, args=("task2",))
# task3 = threading.Thread(target=display, args=("task3",))
# task4 = threading.Thread(target=display, args=("task4",))
# task4 = threading.Thread(target=display, args=("task4",))
# task5 = threading.Thread(target=display, args=("task5",))

# task1.start()
# task2.start()
# task3.start()
# task4.start()
# task5.start()

# print([1,2,3,4][::-1])

# list = [1,2,3,4]
# print([i + 10 for i in list])

# print(type(6/ 3))
# print(6/3)

# def my_decorator(func):
#   @wraps(func)
#   def wrapper(*args, **kwargs):
#     print("run...")
#     func(*args, **kwargs)

#   return wrapper

# @my_decorator
# def timer():
#   print("10")

# timer()

# class Account:
#   def __init__(self):
#     self.amount = 0
#     # self.lock = threading.Lock()
#     self.lock = threading.RLock()

#   def deposit(self, amount: int, sleep: int):
#     self.lock.acquire()
#     # self.lock.acquire()
#     print(self.lock)
#     print(f"Current thread {threading.current_thread()}")
#     time.sleep(sleep)
#     self.amount += amount
#     print(f"Amount {amount} total amount is {self.amount}")
#     self.lock.release()
#     # self.lock.release()

# a = Account()
# task1 = threading.Thread(target=a.deposit, args=(1,2))
# task2 = threading.Thread(target=a.deposit, args=(2,0))

# task1.start()
# task2.start()

# def do_something1():
#   print("Started do_something1")
#   for _ in range(0,100):
#     pass
#   print("Completed do_something1")

# def do_something2():
#   print("Started do_something2")
#   for _ in range(0,100):
#     pass
#   print("Completed do_something2")

# task1 = threading.Thread(target=do_something1)
# task2 = threading.Thread(target=do_something2)

# task2.start()
# task2.join()
# task1.start()

# print("Completed task..")

# def do_something():
#   print("Do something....")

# task1 = threading.Thread(target=do_something)
# task2 = threading.Thread(target=do_something)
# task1.start()
# task2.start()
# print(threading.enumerate())

# task = threading.Thread(target=do_something, name="do_something")
# print(threading.main_thread(), threading.active_count())
# task.start()
# print(threading.main_thread(), threading.active_count())
# task.join()
# print("Completed the work..")
# print(threading.main_thread(), threading.active_count())

# class ExampleStartClass(Thread):
#   def run(self):
#     print("Run the thread..")
#     # return super().run()
#     task = Thread(target=do_something, name="ExampleStartClass")
#     task.start()
#     task.join()
#     return None

# def do_something():
#   print(f"Started do something with {current_thread()}")
#   for _ in range(1, 20):
#     pass
#   print("Task completed...")

# task = ExampleStartClass(target=do_something, name="do_something")
# task.start()
# task.join()
# print("Task completed last statement..")

# class User:
#   def do_something(self):
#     for _ in range(1, 10):
#       pass
#     print(f"Task completed from the do something function... with {current_thread()}")

#   @classmethod
#   def do_something2(cls):
#       for _ in range(1, 10):
#         pass
#       print(f"Task completed from the do something function... with {current_thread()}")

#   @staticmethod
#   def do_something3():
#     for _ in range(1, 10):
#       pass
#     print(f"Task completed from the do something function... with {current_thread()}")

# u = User()
# task1 = Thread(target=u.do_something, name="do_something")
# task1 = Thread(target=User.do_something2, name="do_something")
# task1 = Thread(target=User.do_something3, name="do_something")
# task1.start()
# task1.join()
# print("Task completed last statement..")

# def do_something():
#   print(f"Started do something with {current_thread()}")
#   for _ in range(1, 20):
#     pass
#   print("Task completed...")

# task1 = Thread(target=do_something, name="do_something_thread")
# print(f"Before stated-> {task1.is_alive()}")
# task1.start()
# print(f"After start-> {task1.is_alive()}")
# task1.join()
# print("Task completed last statement..")

# do_something()