def demo(num1: int, num2: int):
  try:
    if num1:
      return num1 + num2
    else:
      return "Please enter the number"
  except Exception as error:
    return error