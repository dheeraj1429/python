import pytest
from enum import Enum

class Gender(Enum):
  MALE = 1
  FEMALE = 2

class User:
  def __init__(self, name: str, age: int, place: int, gender: Gender):
    self.name = name
    self.age = age
    self.place = place
    self.gender = gender

@pytest.fixture
def default_user():
  return User(name="Demo", age=10, place="Demo place", gender=Gender.MALE)

def test_user(default_user):
  assert default_user.name == "Demo"
  assert default_user.gender == Gender.MALE