'''
7 kyu
Number encrypting: cypher
https://www.codewars.com/kata/57aa3927e298a757820000a8
'''

# ---- SOLUTION ----

def cypher(s):
  translationtable = str.maketrans('lzeasbtgoIREASGTBO', '123456790123456780')
  return s.translate(translationtable)

# ---- TEST ----

def dotest(s, expected):
  actual = cypher(s)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'String = {s}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest("Hello World", "H3110 W0r1d")
  dotest("I am your father", "1 4m y0ur f47h3r")
  dotest("I do not know what else I can test. Be cool. Good luck",
         "1 d0 n07 kn0w wh47 3153 1 c4n 7357. 83 c001. 600d 1uck")
  dotest("IlRzEeAaSsGbTtBgOo", "112233445566778900")
  dotest("", "")

if __name__ == "__main__":
  main()
