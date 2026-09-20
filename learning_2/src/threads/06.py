import requests
from multiprocessing import Process
import time

def download_image(url: str, name: str):
  print(f"Downloading started... with: {url}")
  response = requests.get(url=url)
  response.raise_for_status()
  with open(f"{name}.jpg", "wb") as f:
    f.write(response.content)
  print(f"Downloading completed... with: {url}")

if __name__ == "__main__":
  start = time.time()
  task1 = Process(target=download_image, args=("https://httpbin.org/image/jpeg", "image_1"))
  task2 = Process(target=download_image, args=("https://httpbin.org/image/png", "image_2"))
  task1.start()
  task2.start()
  task1.join()
  task2.join()
  end = time.time()

  print(f"Task completed... with time {end - start:.2f}ms")