import unittest
import main

class TestMain(unittest.TestCase):
  def test_main_fun(self):
    num1 = 10
    num2 = 20
    res = main.demo(num1=num1, num2=num2)
    self.assertEqual(res, 30, "10 + 20 should be 30")

  def test_main_fun2(self):
      num1 = 10
      res = main.demo(num1=num1, num2="abc")
      self.assertTrue(isinstance(res, TypeError))

  def test_main_fun3(self):
    num1 = None
    res = main.demo(num1=num1, num2="abc")
    self.assertEqual(res, "Please enter the number")

if __name__ == "__main__":
  unittest.main()