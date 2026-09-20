import time
from multiprocessing import Process

def order_tracker(order_id: int):
  print(f"Start order tracking with order ID: #{order_id}")
  time.sleep(3)
  print(f"Start order tracking with order ID: #{order_id}")

if __name__ == "__main__":
  all_orders = [
    Process(target=order_tracker, args=(i + 1,))
    for i in range(1, 4)
  ]

  # Start the processes
  for i in all_orders:
    i.start()

  # Wait for all the complete
  for i in all_orders:
    i.join()

  print("All process completed...")