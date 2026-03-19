'''
7 kyu
List Filtering
https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
'''

# ---- SOLUTION ----

def filter_list(l):
  return [item for item in l if type(item) != str]

# ---- TEST ----

def dotest(l, expected):
  actual = filter_list(l)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'List = {l}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest([1, 2, 'a', 'b'], [1, 2])
  dotest([1, 'a', 'b', 0, 15], [1, 0, 15])
  dotest([1, 2, 'aasf', '1', '123', 123], [1, 2, 123])

if __name__ == "__main__":
  main()
