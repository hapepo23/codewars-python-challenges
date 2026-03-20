'''
6 kyu
Validate Credit Card Number
https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2
'''

# ---- SOLUTION ----

def validate(n):
  digits = list(map(int, str(n)))
  for i in range(len(digits) % 2, len(digits), 2):
    digits[i] = 2 * digits[i] - 9 if digits[i] > 4 else 2 * digits[i]
  return sum(digits) % 10 == 0

# ---- TEST ----

def dotest(n, expected):
  actual = validate(n)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'n = {n}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest(1714, False)
  dotest(12345, False)
  dotest(891, False)
  dotest(123, False)
  dotest(1, False)
  dotest(2121, True)
  dotest(1230, True)

if __name__ == "__main__":
  main()
