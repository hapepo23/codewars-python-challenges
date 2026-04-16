'''
7 kyu
Is Sator Square?
https://www.codewars.com/kata/5cb7baa989b1c50014a53333
'''

# ---- SOLUTION ----

def is_sator_square(tablet):
  n = len(tablet)
  if any(len(row) != n for row in tablet):
    return False
  for i in range(n):
    for j in range(n):
      if tablet[i][j] != tablet[j][i]:
        return False
      if tablet[i][j] != tablet[n - 1 - i][n - 1 - j]:
        return False
  return True

# ---- TEST ----

def dotest(tablet, expected):
  actual = is_sator_square(tablet)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Tablet = {tablet}, expected = {expected}, actual = {actual} -> {status}')

def main():
  tests = [
    [
      [['T', 'E', 'N'],
       ['E', 'Y', 'E'],
       ['N', 'E', 'T']],
      True
    ],
    [
      [['N', 'O', 'T'],
       ['O', 'V', 'O'],
       ['N', 'O', 'T']],
      False
    ],
    [
      [['B', 'A', 'T', 'S'],
       ['A', 'B', 'U', 'T'],
       ['T', 'U', 'B', 'A'],
       ['S', 'T', 'A', 'B']],
      True
    ],
    [
      [['P', 'A', 'R', 'T'],
       ['A', 'G', 'A', 'R'],
       ['R', 'A', 'G', 'A'],
       ['T', 'R', 'A', 'M']],
      False
    ],
    [
      [['B', 'A', 'T', 'S'],
       ['U', 'B', 'U', 'T'],
       ['T', 'U', 'B', 'U'],
       ['S', 'T', 'A', 'B']],
      False
    ],
    [
      [['S', 'A', 'T', 'O', 'R'],
       ['A', 'R', 'E', 'P', 'O'],
       ['T', 'E', 'N', 'E', 'T'],
       ['O', 'P', 'E', 'R', 'A'],
       ['R', 'O', 'T', 'A', 'S']],
      True
    ],
    [
      [['S', 'A', 'L', 'A', 'S'],
       ['A', 'R', 'E', 'N', 'A'],
       ['L', 'E', 'V', 'E', 'L'],
       ['A', 'R', 'E', 'N', 'A'],
       ['S', 'A', 'L', 'A', 'S']],
      False
    ]
  ]
  for tablet, expected in tests:
    dotest(tablet, expected)

if __name__ == "__main__":
  main()
