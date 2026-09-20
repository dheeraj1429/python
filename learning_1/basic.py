from typing import Protocol
# from enum import Enum
# import requests
# from collections.abc import Callable
# import webbrowser
# import math
# from datetime import datetime
# from functools import reduce

# print("Hello, World!")
# user_input = input("What is your name... \n")
# print("The user enter:", user_input)

# Data types
# int
# float
# bool
# str
# list
# tuple
# set
# dict
# None

# int
# float
# print(type(2 + 2))
# print(type(2 / 1))

# num = 1
# num = "some string"
# print(num)

# print(3 // 1.7)
# print(3 // 2)
# print(2 / 4)
# print(2 // 4)

# math functions
# print(round(3.7))
# print(round(3.1))
# print(round(3.5))
# print(abs(-100))
# print(bin(5))

# a,b,c = 1,2,3
# print(a, b, c)

# some_val = 10
# some_val += 1
# print(some_val)

# This is not work in py
# some_val += 10
# some_val = 0
# print(some_val)

# print("This is the string")
# print('This is also the string')
# print("""
# This is also the string
# """)
# name = "Dheeraj"
# print(f"My name is: {name}")
# print("1" + 1)
# print(type(str(100)))

# some_string = "This"
# print(some_string[1])
# print(len(some_string))
# for char in some_string:
#   print(char)

some_string = "This is the string"
# print(some_string[0:10]) [start:end]
# print(some_string[0:10:2]) [start:end:step]
# print(some_string[1:len(some_string)])
# print(some_string[1:])
# print(some_string[:10])
# print(some_string[0:10])
# print(some_string[::2])
# print(some_string[:len(some_string):2])
# print(some_string.upper())
# print(some_string.lower())
# print(some_string.find("is"))
# print(some_string.replace("is", "IS"))
# print(some_string)

# def printStringItem(string, idx) -> None:
#   if idx == len(string):
#     return

#   print(string[idx])
#   printStringItem(string, idx + 1)

# printStringItem(some_string, 0)

# print(math.floor(5.3))
# print(math.floor(5.5))
# print(math.floor(5.6))

# def marge(nums: list[int], st: int, mid: int, end: int) -> None:
#   i,j=st,mid + 1
#   temp: list[int] = []
#   while i <= st and j <= end:
#     if(nums[i] < nums[j]):
#       temp.append(nums[i])
#       i+=1
#     else:
#       temp.append(nums[j])
#       j+=1

#   while i <= st:
#     temp.append(nums[i])
#     i+=1

#   while j <= end:
#     temp.append(nums[j])
#     j+=1

#   for i in temp:
#     nums[st+i] = temp[i]

# def partition(nums: list[int], st: int, end: int) -> None:
#   if(st < end):
#     mid = math.floor((st + end) / 2)
#     print(st, mid, end, nums[st:end])
#     partition(nums=nums, st=st, end=mid)
#     partition(nums=nums, st=mid+1, end=end)
#     marge(nums=nums, st=st, mid=mid, end=end)

# nums: list[int] = [10, 8, 2, 3, 19, 10]
# partition(nums=nums, st=0, end=len(nums) - 1)
# print(nums)

# birth_year = input("What is your birth year? \n")
# age = datetime.now().year - int(birth_year)
# print(age)

# user_name: str = input("Please enter your name \n")
# pass_word: str = input("Please enter your password \n")
# hash: str = ""
# for i in pass_word:
#   hash += "*"
# hash = "*" * len(pass_word)
# print(hash)

# arr = [1,2,3]
# print(arr[0])
# arr[0] = 10
# print(arr)

# arr = [10, 10, 100, 12, 13, 14, 15]
# arr.append(16)
# print(arr)

# arr.insert(0, 20)
# arr.clear()
# new_list = arr.copy()
# new_list.append(20)
# print(arr.count(10))
# print(arr.index(10))
# print(arr.index(15))
# print(arr.pop())
# arr.reverse()
# arr.sort(reverse=True)
# arr.extend([13,17])
# new_list = [x for x in arr if x % 2 == 0]
# new_list = []
# for x in arr:
#   if x % 2 == 0:
#     new_list.append(x)
# print(new_list)
# new_list = list(filter(lambda x: x % 2 == 0, arr))
# print(new_list)
# print(list(map(lambda x: x ** 2, arr)))
# print(reduce(lambda x, y: x + y, arr))
# print(arr.index(10, 1))
# print(10 in arr)
# print(arr)

# a,b,c = [1,2,3]
# print(a, b, c)

# a,b,*c = [1,2,3,4,5,6,7]
# print(a, b, c)

# data = {
#   "name": "Demo User Name",
#   "place": "New place",
#   1: 10,
# }
# print(data[1])

# data = {
#   "data": [1,2,3],
#   "age": 10
# }
# print(data.get("data"))
# print(data.get("non"))
# print(data.get("non", 10))
# data["data"] = False
# data.update({"data": False})
# print(data)
# new_data = data.items()
# for x in new_data:
#   print(x[0], x[1])

# my_set = {1,2,3,3,4,5}
# my_set.add(10)
# my_set.add(100)
# my_set.add(1)
# print(my_set.copy())
# print(my_set.clear())
# print(my_set)

# my_set = {1,2,6,7,3,4,5}
# my_set = {1,2,7}
# your_set = {3,4,5,6}
# print(my_set.intersection(your_set))
# print(my_set.union(your_set))
# print(my_set.difference(your_set))
# my_set.discard(6)
# print(my_set.isdisjoint(your_set))
# print(my_set)


# Ternary Operator
# is_active = False
# is_active = True if 10 % 2 == 0 else False
# print(is_active)

# is_friend = True
# can_message = True if is_friend == True else False
# print(can_message)

# arr = [1,2,3,4,5]
# for i,value in enumerate(arr):
#   print(i, value)

# i = 0
# while i < 10:
#   i += 1
#   break
# else:
#   print("Complete")

# def find_duplicates(arr):
#   map = {}
#   res = []
#   for item in arr:
#     if not map.get(item):
#       map[item] = 1
#     else:
#       res.append(item)
#   print(res)

# find_duplicates(["a", "b", "c", "b", "d", "m", "n", "n"])

# def do_something(*args, **kwargs):
#   print(args, kwargs)

# do_something(1,2,3,4,5, name="Demo", age=25)

# string = "Hello"

# if (i := len(string)) > 5:
#   print(f"This string is to long with {i} elements")

# while (n := (len(string) - 1)) >= 0:
#   print(string[n])
#   string = string[:-1]

# counter = 10
# def updateCounter():
#   global counter
#   counter += 20
#   print("Inside the local scope", counter)

# updateCounter()
# print(counter)

# counter = 10

# def updateCounter(counter: int):
#   counter += 20
#   return counter

# counter = updateCounter(counter=counter)
# print(counter)

# x = "Global"

# def outer():
#   x = "local"
#   def inner():
#     nonlocal x
#     x = "nonlocal"
#     print("Inner: ", x)

#   inner()
#   print("Outer: ", x)

# outer()

# webbrowser.open("http://google.com")
# search = input("What you want to search?\n")
# webbrowser.open(f"https://search.brave.com/search?q={search}&source=desktop")

# class PlayerCharacter:
#   def __init__(self, name: str):
#     self.name = name

# player1 = PlayerCharacter("Demo player")
# print(player1)

# class object attribute
# class Counter:
#   counter: int = 0

#   def __init__(self):
#     Counter.counter += 1

# c1 = Counter()
# print(c1.counter)
# c2 = Counter()
# print(c2.counter)
# c3 = Counter()
# print(c3.counter)

# class Player:
#   def __init__(self, age=20):
#     self.age = age

# p1 = Player(age=10)
# print(p1.age)

# LinkedList
# class ListNode:
#   def __init__(self, val, next = None):
#     self.val = val
#     self.next = next

# node3 = ListNode(30)
# node2 = ListNode(20, node3)
# node1 = ListNode(10, node2)

# class LinkedList:
#   def __init__(self):
#     self.head = None
#     self.size = 0

#   def append(self, val: int):
#     self.head = ListNode(val, self.head)
#     self.size += 1

#   def pop(self):
#     if self.head:
#       self.head = self.head.next
#       self.size -= 1

# linkedList = LinkedList()
# linkedList.append(10)
# linkedList.append(20)
# linkedList.append(30)
# linkedList.append(40)
# print(linkedList.size)
# print(linkedList.head.val)
# print(linkedList.head.next.val)
# linkedList.pop()
# print(linkedList.head.val)

# class Person:
#   # Class attribute
#   instance: int = 0
#   def __init__(self):
#     self.instance +=1

# p = Person()
# p = Person()
# p = Person()
# p = Person()
# p = Person()
# print(p.instance)

# class PlayerCharacter:
#   def __init__(self, name: str, score: int):
#     self.name = name
#     self.score = score

#   @classmethod # <- This is the same as static method but we can access the class in first param
#   def add(cls, num1: int, num2: int):
#     return cls("Creating-instance", num1 + num2)

#   @staticmethod
#   def add2(num1: int, num2: int) -> int:
#     return num1 + num2

# print(PlayerCharacter.add(10, 20).name)
# print(PlayerCharacter.add2(20, 30))

# p = PlayerCharacter()
# print(p.add(20, 20))

# class Counter:
#   def __init__(self):
#     self._counter = 0

#   def update(self, count: int):
#     self._counter += count
#     return self

#   def getCounter(self) -> int:
#     return self._counter

# c = Counter()
# c.update(10).update(20).update(30).update(40)
# print(c.getCounter())


# url = "https://jsonplaceholder.typicode.com/todos/1"

# response = requests.get(url=url)

# if response.status_code == 200:
#   data = response.json()
#   print(data)
# else:
#   print(f"Error {response.status_code}")

# class Person:
#   def getName(self) -> str:
#     return "This is the person method"

# class User(Person):
#   pass

# u = User()
# print(u.getName())


# class MainClass:
#   def __init__(self, name: str):
#     self.name = name
#     self.age = 20

#   def calculate(self, num1: int, num2: int):
#     return num1 + num2

#   def getAge(self):
#     return 20

# class MainClassSecond:
#   def __init__(self, age: int):
#     self.age = age

#   def getAge(self):
#     return self.age

# class SubClass(MainClassSecond, MainClass):
#   def __init__(self, name):
#     MainClass.__init__(self,name)
#     MainClassSecond.__init__(self, 100)

  # def getAge(self):
  #   print("Hello")

# class SubClass(MainClass, MainClassSecond):
#   def __init__(self, name, age):
#     MainClass.__init__(self, name)
#     MainClassSecond.__init__(self, age)

# s = SubClass("Demo name")
# print(SubClass.mro())
# print(s.getAge())
# print(s.age)
# print(s.calculate(10, 20))
# print(s.getAge())
# print(isinstance(s, MainClass))
# print(isinstance(s, SubClass))
# print(isinstance(s, MainClassSecond))

# class DemoClass:
#   def __init__(self, name):
#     self.name = name

#   def run(self):
#     print("First")

#   def run(self, age):
#     print(age)

# c = DemoClass("Deo")
# c.run(10)

# class SecondClass:
#   def __init__(self, name: str):
#     self.name = name

#   def getName(self) -> str:
#     return self.name

# class DiClass:
#   def __init__(self, cls: SecondClass):
#     self.cls = cls

# d = DiClass(SecondClass("Demo"))
# print(d.cls.getName())
# print(dir(d))
# print(dir(d.cls))

# my_list = [1,2,3]
# def map_fn(item: int):
#   return item * 2
# new_list = list(map(map_fn,my_list))
# new_list = list(map(lambda x: x * 2,my_list))
# print(new_list)
# new_list = list(filter(lambda x: x % 2 != 0, my_list))
# print(new_list)

# def make_request(callback: Callable[str, None]):
#   try:
#     url: str = "https://jsonplaceholder.typicode.co/todos/1"
#     response = requests.get(url=url)

#     if response.status_code == 200:
#         print(response.json())
#         callback("Done")
#     else:
#         print("Request failed!")
#         callable("Error")

#   except requests.exceptions.ConnectionError:
#     callable("Error")
#     raise
  
#   except Exception as e:
#     callable("Error")
#     raise

# def callback_fn(response: str):
#   print("Hi i am callback fn and here is the response", response)

# make_request(callback_fn)

# class Color(Enum):
#   RED = 1
#   GREEN = 2
#   BLUE = 3

# print(Color.RED.value)
# print(Color.GREEN)
# print(Color.BLUE)

# class DrawProtocol(Protocol):
#   def draw(self, condition: list[int]) -> None: ...

# class Circle(DrawProtocol):
#   def draw(self, condition):
#     print(condition)

# c = Circle()
# c.draw([100, 20])

# my_list = [1,2,3]
# your_list = [10,20,30]
# print(list(zip(my_list, your_list)))