'''
5 kyu
Beeramid
https://www.codewars.com/kata/51e04f6b544cf3f6550000c1
'''

# ---- SOLUTION ----

def beeramid(bonus, price):
  result = 0
  total = 0
  if bonus <= 0 or price <= 0:
    return 0
  while total <= bonus:
    result += 1
    total += price * result * result
  return result - 1

# ---- TEST ----

def dotest(bonus, price, expected):
  actual = beeramid(bonus, price)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Bonus = {bonus}, price = {price}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest(9, 2, 1)
  dotest(10, 2, 2)
  dotest(11, 2, 2)
  dotest(21, 1.5, 3)
  dotest(454, 5, 5)
  dotest(455, 5, 6)
  dotest(4, 4, 1)
  dotest(3, 4, 0)
  dotest(0, 4, 0)
  dotest(-1, 4, 0)

if __name__ == "__main__":
  main()
