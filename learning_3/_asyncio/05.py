import threading

stock = 0

def restock():
  global stock
  for _ in range(10000):
    stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()

print(f"Stock: {stock}")