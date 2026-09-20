import threading
import time

def take_order():
  for i in range(1, 4):
    print(f"Taking order 1 for #{i}")
    time.sleep(2)

def take_order_2():
  for i in range(1, 4):
    print(f"Taking order 2 for #{i}")
    time.sleep(3)

# take_order()
# take_order_2()

# Creating threads
order_thread_1 = threading.Thread(target=take_order)
order_thread_2 = threading.Thread(target=take_order_2)

order_thread_1.start()
order_thread_2.start()

# Wait for the results of the threads
order_thread_1.join()
order_thread_2.join()
print("All work completed")