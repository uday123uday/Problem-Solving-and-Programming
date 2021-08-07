import math
def factorial(n):
  if n<2:
    return 1
  return n*factorial(n-1)

def sin(x, n):
  sine = 0
  for term in range(n):
    sign = (-1)**term
    y = x*(math.pi/180)
    sine += (((y**(2.0*term+1))/factorial(2*term+1))*sign)
  return sine

x=int(input("Enter the degree values: "))
n=int(input("How many terms? "))
print("The value of sine is :" ,sin(x,n))