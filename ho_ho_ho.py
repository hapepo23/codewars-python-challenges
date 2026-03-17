'''
6 kyu
Ho Ho Ho with Functions!
https://www.codewars.com/kata/52af1f150fcae8d33d0009bc
'''

# ---- SOLUTION ----

def ho(x=None):
  if x is None:
    return 'Ho!'
  return x[:-1] + ' Ho!'

# ---- TEST ----

def dotest(call, actual, expected):
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Call = {call}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest('ho()', ho(), 'Ho!')
  dotest('ho(ho())', ho(ho()), "Ho Ho!")
  dotest('ho(ho(ho()))', ho(ho(ho())), "Ho Ho Ho!")

if __name__ == "__main__":
  main()
