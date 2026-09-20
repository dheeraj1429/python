from multiprocessing import Process
import time

def do_something():
  print("Process started...")
  count = 0
  for _ in range(100_000_000):
    count += 1
  print("Process ended...")


if __name__ == "__main__":
  process_1 = Process(target=do_something, name="Process_1")
  process_2 = Process(target=do_something, name="Process_2")

  start = time.time()
  process_1.start()
  process_2.start()
  process_1.join()
  process_2.join()
  end = time.time()

  print(f"Total time multiprocess taken: {end - start:.2f}ms")