one = [ "", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen" ,"eighteen ", "nineteen "]
ten = [ "", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety ",]
def num_words(n, s):
  str = ""
  if(n > 19):
    str += ten[n // 10] + one[n % 10]
  else:
    str += one[n]
  if (n):
    str += s
  return str

def convert_words(n):
  out = ""  #empty string
  out += num_words((n // 10000000),"crore ")
  out += num_words((n // 100000) % 100 ,"lakh ")
  out += num_words((n // 1000) % 100 ,"thousand ")
  out += num_words((n // 100) % 100 ,"hundered ")
  if (n > 100 and n % 100):
      out += "and "
  out += num_words((n % 100), "")
  return out

n=int(input("Enter the number"))
print(convert_words(n))