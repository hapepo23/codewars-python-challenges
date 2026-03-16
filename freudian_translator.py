'''
8 kyu
Freudian translator
https://www.codewars.com/kata/5713bc89c82eff33c60009f7
'''

# ---- SOLUTION ----

def to_freud(sentence):
  return ('sex ' * sentence.count(' ')) + ('sex' if len(sentence) > 0 else '')

# ---- TEST ----

def dotest(sentence, expected):
  actual = to_freud(sentence)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Sentence = {sentence}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest("", "")
  dotest("test", "sex")
  dotest("sexy sex", "sex sex")
  dotest("This is a test", "sex sex sex sex")
  dotest("This is a longer test", "sex sex sex sex sex")
  dotest("You're becoming a true freudian expert", "sex sex sex sex sex sex")

if __name__ == "__main__":
  main()
