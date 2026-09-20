from pathlib import Path
# data = {
#   "name": "demo data",
#   "age": 20
# }

# try:
#   print(data["place"])
# except KeyError as e:
#   print(f"Error {e}")


# def dont_know(data):
#   try:
#     print(f"Data: {data}")
#     if data == "unknown":
#       raise ValueError("Please provide the valid args")
#   except ValueError as e:
#     print(f"Error {e}")

#   else:
#     print(f"Data from the else block {data}")

#   finally:
#     print("Run completed..")

# dont_know("unknown")
# dont_know(10)

# def process_order(item, quantity):
#   try:
#     price = {"data", 20}[item]
#     cost = price * quantity
#     print(f"total cost is {cost}")
#   except TypeError as e:
#     print(f"Type error {e}")
#   except KeyError as e:
#     print(f"Key error {e}")

# process_order("data", 20)

# class MyCustomError(Exception):
#   pass

# def please_throw_error():
#   raise MyCustomError("Please don't use this code...")

# please_throw_error()

# def open_file(name: str):
#   try:
#     with open(name, 'r', encoding="utf-8") as file:
#       print(f"Open file: {file.read()}")
#   except FileNotFoundError as e:
#     print(f"File open error {e}")

# open_file("./a.txt")
# open_file("./b.txt")

# def read_file_content(p: str):
#   path = Path(p)
#   try:
#     content = path.read_text(encoding="utf-8")
#     print(f"Open file: {content}")
#   except FileNotFoundError as e:
#     print(f"File not found: {path.resolve()} and error: {e}")
#   except FileExistsError as e:
#     print(f"File not exist: {path.resolve()} and error: {e}")
#   except OSError as e:
#     print(f"Error reading file {path}: {e}")

# read_file_content("./a.txt")