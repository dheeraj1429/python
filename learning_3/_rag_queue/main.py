from client.rq_client import queue
from queues.worker import process_query

if __name__ == "__main__":
  user_input = input("Ask something....")
  job = queue.enqueue(process_query, user_input)
  print(f"Job: {job}")