'''
7 kyu
KISS - Keep It Simple Stupid
https://www.codewars.com/kata/57eeb8cc5f79f6465a0015c1
'''

# ---- SOLUTION ----

def is_kiss(words):
  w = words.split()
  return 'Good work Joe!' if all(len(word) <= len(w) for word in w) else 'Keep It Simple Stupid'

# ---- TEST ----

def dotest(words, expected):
  actual = is_kiss(words)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Words = {words}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest('Joe had a bad day', "Good work Joe!")
  dotest('Joe had some bad days', "Good work Joe!")
  dotest('Joe is having no fun', "Keep It Simple Stupid")
  dotest('Sometimes joe cries for hours', "Keep It Simple Stupid")
  dotest('Joe is having lots of fun', "Good work Joe!")
  dotest('Joe is working hard a lot', "Keep It Simple Stupid")
  dotest('Joe listened to the noise and it was an onamonapia', "Good work Joe!")
  dotest('Joe listened to the noises and there were some onamonapias', "Keep It Simple Stupid")

if __name__ == "__main__":
  main()
