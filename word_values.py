'''
7 kyu
Word values
https://www.codewars.com/kata/598d91785d4ce3ec4f000018
'''

# ---- SOLUTION ----

def name_value(my_list):
  result = []
  base = ord('a') - 1
  for i, s in enumerate(my_list):
    result.append((i + 1) * sum(ord(c) - base for c in s if c.isalpha()))
  return result

# ---- SECOND SOLUTION ----
'''
def name_value(my_list):
  base = ord('a') - 1
  return [
    (i + 1) * sum(ord(c) - base for c in s if c.isalpha())
    for i, s in enumerate(my_list)
  ]
'''

# ---- TEST ----

def dotest(my_list, expected):
  actual = name_value(my_list)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'List = {my_list}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest(["codewars", "abc", "xyz"], [88, 12, 225])
  dotest(["abc abc", "abc abc", "abc", "abc"], [12, 24, 18, 24])

if __name__ == "__main__":
  main()
