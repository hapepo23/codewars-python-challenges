'''
5 kyu
What's a Perfect Power anyway?
https://www.codewars.com/kata/54d4c8b08776e4ad92000835
'''

# ---- SOLUTION ----

import math

def isPP(n):
  if n < 2:
    return None
  max_b = int(math.log2(n)) + 1
  for b in range(2, max_b + 1):
    a = int(round(n ** (1 / b)))
    if a > 1 and a ** b == n:
      return [a, b]
  return None

# ---- TEST ----

def dotest(n, expected):
  actual = isPP(n)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'n = {n}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest(4, [2, 2])
  dotest(9, [3, 2])
  dotest(5, None)
  dotest(961, [31, 2])
  dotest(4096, [64, 2])

if __name__ == "__main__":
  main()
