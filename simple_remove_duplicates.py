'''
7 kyu
Simple remove duplicates
https://www.codewars.com/kata/5ba38ba180824a86850000f7
'''

# ---- SOLUTION ----

def solve(arr):
  i = 0
  while i < len(arr):
    while arr.count(arr[i]) > 1:
      del arr[i]
    i += 1
  return arr

# ---- TEST ----

def dotest(arr, expected):
  print(f'arr = {arr}, ', end='')
  actual = solve(arr)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest([3, 4, 4, 3, 6, 3], [4, 6, 3])
  dotest([1, 2, 1, 2, 1, 2, 3], [1, 2, 3])
  dotest([1, 2, 3, 4], [1, 2, 3, 4])
  dotest([1, 1, 4, 5, 1, 2, 1], [4, 5, 2, 1])

if __name__ == "__main__":
  main()
