'''
4 kyu
Sum by Factors
https://www.codewars.com/kata/54d496788776e49e6b00052f
'''

# ---- SOLUTION ----

def unique_prime_factors(n):
  factors = set()
  i = 2
  while i * i <= n:
    while n % i == 0:
      factors.add(i)
      n //= i
    i += 1
  if n > 1:
    factors.add(n)
  return factors

def sum_for_list(lst):
  prime_sums = {}
  for n in lst:
    for p in unique_prime_factors(abs(n)):
      prime_sums[p] = prime_sums.get(p, 0) + n
  return sorted([[p, s] for p, s in prime_sums.items()])

# ---- TEST ----

def dotest(lst, expected):
  actual = sum_for_list(lst)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'List = {lst},\nexpected = {expected},\nactual = {actual}\n-> {status}\n')

def main():
  dotest([12, 15], [[2, 12], [3, 27], [5, 15]])
  dotest([15, 21, 24, 30, 45], [[2, 54], [3, 135], [5, 90], [7, 21]])
  dotest([15, 21, 24, 30, -45], [[2, 54], [3, 45], [5, 0], [7, 21]])
  dotest([107, 158, 204, 100, 118, 123, 126, 110, 116, 100], [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158],
       [107, 107]])
  dotest([-29804, -4209, -28265, -72769, -31744], [[2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], [53, -72769], [61, -4209], [1373, -72769],
       [5653, -28265], [7451, -29804]])

if __name__ == "__main__":
  main()
