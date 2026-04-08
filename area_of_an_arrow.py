'''
7 kyu
Area of an arrow
https://www.codewars.com/kata/589478160c0f8a40870000bc
'''

# ---- SOLUTION ----

def arrow_area(a, b):
  return 0.25 * a * b

# ---- TEST ----

def dotest(a, b, expected):
  actual = arrow_area(a, b)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'a = {a}, b = {b}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest(4, 2, 2)
  dotest(7, 6, 10.5)
  dotest(25, 25, 156.25)

if __name__ == "__main__":
  main()
