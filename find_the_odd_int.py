'''
6 kyu
Find the odd int
https://www.codewars.com/kata/54da5a58ea159efa38000836
'''

# ---- SOLUTION ----

def find_it(seq):
  counts = {}
  for num in seq:
    counts[num] = counts.get(num, 0) + 1
  for k, v in counts.items():
    if v % 2 == 1:
      return k
  return 0  # should not happen

# ---- SECOND SOLUTION ----
'''
# XOR has useful properties: a ^ a = 0 and a ^ 0 = a
# So all paired numbers cancel out: a ^ a ^ b ^ b ^ c = c

def find_it(seq):
  result = 0
  for num in seq:
    result ^= num
  return result
'''

# ---- THIRD SOLUTION ----
'''
# Even shorter using functools.reduce

from functools import reduce
from operator import xor

def find_it(seq):
  return reduce(xor, seq)
'''

# ---- TEST ----

def dotest(seq, expected):
  actual = find_it(seq)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'seq = {seq}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5)
  dotest([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5], -1)
  dotest([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5], 5)
  dotest([10], 10)
  dotest([10, 10, 10], 10)
  dotest([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1], 10)
  dotest([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10], 1)

if __name__ == "__main__":
  main()
