from functools import wraps

# def response_to_user():
#   yield 10
#   yield 20
#   yield 30

# response = response_to_user()
# for item in response:
#   print("Items: ",item)

# print(response)
# print(next(response))
# print(next(response))
# print(next(response))

# def infinite_refill():
#   count = 1

#   while True:
#     yield f"Refill {count}"
#     count+=1

# c = infinite_refill()
# c2 = infinite_refill()

# for _ in range(3):
#   print(next(c))

# for _ in range(3):
#   print(next(c2))

# def some_data():
#   print("Welcome!")
#   data = yield

#   while True:
#     print(f"Data: {data}")
#     data = yield

# s = some_data()
# next(s)
# s.send("First data")
# s.send("Second data")

# def first_fuc():
#   yield 1
#   yield 2

# def second_fun():
#   yield 3
#   yield 4

# def fun():
#   yield from first_fuc()
#   yield from second_fun()

# for n in fun():
#   print(n)

# n = fun()
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))

# def my_decorator(func):
#   @wraps(func)
#   def wrapper():
#     print("Before function run")
#     func()
#     print("After function run")
#   return wrapper

# @my_decorator
# def sum_func():
#   print("Basic function called....")

# sum_func()
# print(sum_func.__name__)

# def log_activity(func):
#   @wraps(func)
#   def wrapper(*args, **kwargs):
#     print("Before function run")
#     result = func(*args, **kwargs)
#     print("After function run")
#     return result

#   return wrapper

# @log_activity
# def example_function():
#   print("Example function is running...")

# example_function()

# @log_activity
# def sum_of_two_numbers(a: int, b: int):
#   return a + b

# total = sum_of_two_numbers(10, 20)
# print(total)

# Auth decorator
# def has_admin_role(func):
#   @wraps(func)
#   def wrapper(role: str):
#     if role != "admin":
#       print("Access denied..")
#       return None
#     else:
#       return func(role)

#   return wrapper

# @has_admin_role
# def admin(role: str):
#   print(f"Run logic with role: {role}")

# admin("user")
# admin("admin")