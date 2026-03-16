'''
8 kyu
You only need one - Beginner
https://www.codewars.com/kata/57cc975ed542d3148f00015b
'''

# ---- SOLUTION ----

def check(seq, elem):
  return elem in seq

# ---- TEST ----

def dotest(expected, seq, elem):
  actual = check(seq, elem)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'seq = {seq}, elem = {elem}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest(True, [66, 101], 66)
  dotest(False, [78, 117, 110, 99, 104, 117, 107, 115], 8)
  dotest(True, [101, 45, 75, 105, 99, 107], 107)
  dotest(True, [80, 117, 115, 104, 45, 85, 112, 115], 45)
  dotest(True, ['t', 'e', 's', 't'], 'e')
  dotest(False, ["what", "a", "great", "kata"], "kat")
  dotest(True, [66, "codewars", 11, "alex loves pushups"], "alex loves pushups")
  dotest(False, ["come", "on", 110, "2500", 10, '!', 7, 15], "Come")
  dotest(True, ["when's", "the", "next", "Katathon?", 9, 7], "Katathon?")
  dotest(False, [8, 7, 5, "bored", "of", "writing", "tests", 115], 45)
  dotest(True, ["anyone", "want", "to", "hire", "me?"], "me?")

if __name__ == "__main__":
  main()
