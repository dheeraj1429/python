import threading
import time

def do_something():
  print(f"{threading.current_thread().name} started...")
  count = 0
  for _ in range(100_000_000):
    count += 1
  print(f"{threading.current_thread().name} ended...")

thread_1 = threading.Thread(target=do_something, name="Thread-1")
thread_2 = threading.Thread(target=do_something, name="Thread-2")

start = time.time()
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
end = time.time()

print(f"Total time taken: {end - start:.2f}ms")