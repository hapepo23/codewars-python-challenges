'''
8 kyu
Draw stairs
https://www.codewars.com/kata/5b4e779c578c6a898e0005c5
'''

# ---- SOLUTION ----

def draw_stairs(n):
  result = ''
  for i in range(n):
    result += ('\n' if i > 0 else '') + (' ' * i) + 'I'
  return result

# ---- TEST ----

def dotest(n, expected):
  actual = draw_stairs(n)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'n = {n}')
  print('Expected = ')
  print(expected)
  print('actual = ')
  print(actual)
  print(f'status = {status}\n')

def main():
  dotest(3, 'I\n I\n  I')
  dotest(5, 'I\n I\n  I\n   I\n    I')

if __name__ == "__main__":
  main()
