'''
7 kyu
Maximum Length Difference
https://www.codewars.com/kata/5663f5305102699bad000056
'''

# ---- SOLUTION ----

def mxdiflg(a1, a2):
  return -1 if not a1 or not a2 else max(
    max(map(len, a1)) - min(map(len, a2)),
    max(map(len, a2)) - min(map(len, a1))
  )

# ---- TEST ----

def dotest(a1, a2, expected):
  actual = mxdiflg(a1, a2)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'a1 = {a1}, a2 = {a2}, expected = {expected}, actual = {actual} -> {status}')

def main():
  s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
  s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
  dotest(s1, s2, 13)
  s1 = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
  s2 = ["bbbaaayddqbbrrrv"]
  dotest(s1, s2, 10)
  s2 = []
  s1 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
  dotest(s1, s2, -1)

if __name__ == "__main__":
  main()
