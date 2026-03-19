'''
6 kyu
Find the odd int
https://www.codewars.com/kata/54da5a58ea159efa38000836
'''

# ---- SOLUTION ----

def solve(arr):
  i = 0;
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
