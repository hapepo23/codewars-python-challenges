'''
7 kyu
Reverse words
https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
'''

# ---- SOLUTION ----

def reverse_words(text):
  result = ''
  while text != '':
    lblank = len(text) - len(text.lstrip())
    if lblank > 0:
      result += text[:lblank]
      text = text.lstrip()
    lword = text.find(' ')
    if lword == -1:
      lword = len(text)
    word = text[:lword]
    result += word[lword::-1]
    text = text[lword::]
  return result

# ---- SECOND SOLUTION ----
'''
def reverse_words(text):
  return ' '.join(word[::-1] for word in text.split(' '))
'''

# ---- TEST ----

def dotest(text, expected):
  actual = reverse_words(text)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Text = "{text}", expected = "{expected}", actual = "{actual}" -> {status}')

def main():
  dotest('The quick brown fox jumps over the lazy dog.', 'ehT kciuq nworb xof spmuj revo eht yzal .god')
  dotest('apple', 'elppa')
  dotest('a b c d', 'a b c d')
  dotest('  double  spaced  words  ', '  elbuod  decaps  sdrow  ')
  dotest('  ', '  ')
  dotest('  du', '  ud')
  dotest('du  ', 'ud  ')
  dotest('', '')

if __name__ == "__main__":
  main()
