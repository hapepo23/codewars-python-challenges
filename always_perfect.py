'''
7 kyu
Always perfect
https://www.codewars.com/kata/55f3facb78a9fd5b26000036
'''

# ---- SOLUTION ----

import math

def check_root(strng):
  data = strng.split(',')
  if len(data) != 4:
    return "incorrect input"
  prod = 1
  for i, val in enumerate(data):
    try:
      data[i] = int(data[i])
    except ValueError:
      return "incorrect input"
    if i > 0 and int(data[i]) != int(data[i - 1]) + 1:
      return "not consecutive"
    prod *= int(data[i])
  return f'{prod + 1}, {math.isqrt(prod + 1)}'

# ---- TEST ----

def dotest(strng, expected):
  actual = check_root(strng)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'String = \"{strng}\", expected = \"{expected}\", actual = \"{actual}\" -> {status}')

def main():
  dotest('4,5,6,7', '841, 29')
  dotest('3,s,5,6', 'incorrect input')
  dotest('11,13,14,15', 'not consecutive')
  dotest('10,11,12,13,15', 'incorrect input')
  dotest('10,11,12,13', '17161, 131')
  dotest('ad,d,q,tt,v', 'incorrect input')
  dotest('//,;;,/,..,', 'incorrect input')
  dotest('1,2,3,4', '25, 5')
  dotest('1015,1016,1017,1018', '1067648959441, 1033271')
  dotest('555,777,444,111', 'not consecutive')
  dotest('20,21,22,24', 'not consecutive')
  dotest('9,10,10,11', 'not consecutive')
  dotest('11254,11255,11256,11258', 'not consecutive')
  dotest('25000,25001,25002,25003', '390718756875150001, 625075001')
  dotest('2000000,2000001,2000002,2000003', '16000048000044000012000001, 4000006000001')
  dotest('4,5,6,q', 'incorrect input')
  dotest('5,6,7', 'incorrect input')
  dotest('3,5,6,7', 'not consecutive')
  dotest('-4,-3,-2,-1', '25, 5')
  dotest('-1,0,1,2', '1, 1')

if __name__ == "__main__":
  main()
