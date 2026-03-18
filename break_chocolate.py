'''
7 kyu
Breaking chocolate problem
https://www.codewars.com/kata/534ea96ebb17181947000ada
'''

# ---- SOLUTION ----

def break_chocolate(n, m):
  return (n * m - 1) if n > 0 and m > 0 else 0

# ---- TEST ----

def dotest(n, m, expected):
  actual = break_chocolate(n, m)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'n = {n}, m = {m}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest(5, 5, 24)
  dotest(7, 4, 27)
  dotest(1, 1, 0)
  dotest(0, 0, 0)
  dotest(1, 0, 0)
  dotest(0, 1, 0)
  dotest(6, 1, 5)

if __name__ == "__main__":
  main()
