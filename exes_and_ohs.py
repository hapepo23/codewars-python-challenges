'''
7 kyu
Exes and Ohs
https://www.codewars.com/kata/55908aad6620c066bc00002a
'''

# ---- SOLUTION ----

def xo(s):
  s = s.lower()
  return s.count('x') == s.count('o')

# ---- TEST ----

def dotest(s, expected):
  actual = xo(s)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'String = \"{s}\", expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest("ooxx", True)
  dotest("xooxx", False)
  dotest("ooxXm", True)
  dotest("zpzpzpp", True)
  dotest("zzoo", False)
  dotest("oxOx", True)
  dotest("", True)

if __name__ == "__main__":
  main()
