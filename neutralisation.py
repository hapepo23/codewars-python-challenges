'''
8 kyu
Neutralisation
https://www.codewars.com/kata/65128732b5aff40032a3d8f0
'''

# ---- SOLUTION ----

def neutralise(s1, s2):
  r = ''
  for i in range(0, len(s1)):
    if s1[i] != s2[i]:
      r += '0'
    else:
      r += s1[i]
  return r

# ---- SECOND SOLUTION ----
'''
def neutralise(s1, s2):
  r = ''
  for i, c in enumerate(s1):
    r += '0' if c != s2[i] else c
  return r
'''

# ---- THIRD SOLUTION ----
'''
def neutralise(s1, s2):
  r = ''
  for a, b in zip(s1, s2):
    r += '0' if a != b else a
  return r
'''

# ---- TEST ----

def dotest(s1, s2, expected):
  actual = neutralise(s1, s2)
  status = 'OK' if expected == actual else 'FAIL'
  print(f's1 = {s1}, s2 = {s2}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest("--++--", "++--++", "000000")
  dotest("-+-+-+", "-+-+-+", "-+-+-+")
  dotest("-++-", "-+-+", "-+00")
  dotest("--++", "++++", "00++")
  dotest("+++--+---", "++----++-", "++0--000-")
  dotest("-----", "-----", "-----")
  dotest("-+", "++", "0+")
  dotest("--", "-+", "-0")
  dotest("-++", "+--", "000")
  dotest("++-++--++-", "-+++-++-++", "0+0+0000+0")
  dotest("-++-+-++-", "+-++++---", "00+0+000-")
  dotest("---++-+--", "-+++--++-", "-00+0-+0-")
  dotest("+-----+++-", "--+-+-++--", "0-0-0-++0-")
  dotest("+-----+-", "---++-++", "0--00-+0")
  dotest("-+--+-+---", "-+--+-+-+-", "-+--+-+-0-")
  dotest("+-+", "-++", "00+")
  dotest("-++", "-+-", "-+0")
  dotest("---+", "-+++", "-00+")
  dotest("+--", "+--", "+--")
  dotest("--+++-+-", "+++++---", "00+++-0-")

if __name__ == "__main__":
  main()
