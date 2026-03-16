'''
7 kyu
Minimum Perimeter of a Rectangle
https://www.codewars.com/kata/5826f54cc60c7e5266000baf
'''

# ---- SOLUTION ----

import math

def minimum_perimeter(area):
  side_a = int(math.isqrt(area))
  while area % side_a != 0:
    side_a -= 1
  side_b = area // side_a
  return 2 * (side_a + side_b)

# ---- TEST ----

def dotest(area, expected):
  actual = minimum_perimeter(area)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Area = {area}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest(45, 28)
  dotest(30, 22)
  dotest(81, 36)
  dotest(89, 180)
  dotest(676, 104)
  dotest(3315685185,230436)
  dotest(3846442491,260616)

if __name__ == "__main__":
  main()
