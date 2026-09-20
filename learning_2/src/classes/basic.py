# class Game:
#   action = "right"

# a1 = Game()
# a1.action = "left"
# a1.move = "running"
# print(f"Object property action: {a1.action} and move: {a1.move}")
# print(f"Class attribute action: {Game.action}")

# del a1.action
# del a1.move
# print(f"Object property action: {a1.action}")
# print(f"Class attribute action: {Game.action}")

# class User:
#   def __init__(self, age: int):
#     self._age = age

#   @property
#   def age(self):
#     print("Age property method called...")
#     return self._age + 10

#   @age.setter
#   def age(self, age):
#     if age <= 5:
#       print("Invalid age")
#     else:
#       self._age = age

# u = User(10)
# print(u.age)
# u.age = 1
# u.age = 20
# print(u.age)