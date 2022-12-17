def collatz(number):
  if number%2==0:
    print(number // 2)
    return number // 2
  else:
    print(3 * number + 1)
    return 3 * number + 1


while True:
  print("Type in an integer :")
  inp = input()
  try:
    if collatz(int(inp)) == 1:
      break
  except ValueError:
    print("Please add appropriate input")