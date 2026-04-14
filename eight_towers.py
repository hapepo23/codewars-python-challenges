'''
7 kyu
8 towers
https://www.codewars.com/kata/535bea76cdbf50281a00004c
'''

# ---- SOLUTION ----

import math

def tower_combination(n):
  return math.factorial(n)

# ---- TEST ----

def dotest(n, expected):
  actual = tower_combination(n)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'n = {n}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest(2, 2)
  dotest(3, 6)
  dotest(32, 263130836933693530167218012160000000)

if __name__ == "__main__":
  main()
