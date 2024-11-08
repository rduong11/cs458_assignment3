#user inputs
x = int(input("Enter base x: "))
y = int(input("Enter exponent y: "))
z = int(input("Enter modulus n: "))

#function to convert any number to binary 
#logic is as follows: 
#mod number by two, then divide the number by two and repeat until the number is eventually 0
def convertBinary(y):
  binary = ""
  flag = y
  while flag != 0:
    integer = flag % 2
    binary = str(integer) + binary
    flag = flag // 2

  return binary

#turn user exponential to binary
binary = convertBinary(y)

#function for square and multiply algorithm
#for every digit in the binary string, 
#square the number and mod it by the user modulus
#if the binary digit is 1, multiply the previous result by the initial value(user base) modded by user modulus. otherwise keep looping thru the binary digits. 
def square_and_multiply():
  result = 1 
  initial = x 
  for digit in binary: 
    result = (result ** 2) % z
    if digit == "1":
      result = (result * initial) % z
      
  return result


print(square_and_multiply())