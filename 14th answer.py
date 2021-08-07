import math
def factorial(n):
  if n<2:
    return 1
  return n*factorial(n-1)
def cos(x, n):
  cosine = 0
  for term in range(n):
    sign = (-1)**term  
    y = x*( math.pi/180)
  cosine += (((y**(2.0*term))/factorial(2*term))*sign)
  return cosine

x=int(input("Enter the degree values: "))
n=int(input("How many terms? "))
print("The value of cosine is :" ,cos(x,n))