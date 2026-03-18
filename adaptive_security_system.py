'''
7 kyu
Adaptive Security System
https://www.codewars.com/kata/69b58aaee8f1deef7ece7d0e
'''

# ---- SOLUTION ----

def breach_attempts(hackers, security_level, increase):
  count = 0
  for hacker in hackers:
    if hacker > security_level:
      count += 1
    else:
      security_level += increase
  return count

# ---- TEST ----

def dotest(hackers, security_level, increase, expected):
  actual = breach_attempts(hackers, security_level, increase)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Hackers = {hackers}, security level = {security_level}, increase = {increase}')
  print(f'expected = {expected}, actual = {actual} -> {status}\n')

def main():
  cases = [
    ([7, 6, 8, 9], 6, 2, 1),
    ([10, 11, 12], 5, 3, 3),
    ([5, 5, 5], 5, 1, 0),
    ([], 4, 2, 0),
    ([2, 4, 6, 8, 10], 2, 1, 4)
  ]
  for hackers, security_level, increase, expected in cases:
    dotest(hackers, security_level, increase, expected)

if __name__ == "__main__":
  main()
