import threading
import asyncio
import time

def background_task():
  while True:
    print(f"Logging..")
    time.sleep(1)

threading.Thread(target=background_task, daemon=True).start()

print("Task completed..")