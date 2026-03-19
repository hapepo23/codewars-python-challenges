'''
6 kyu
Convert string to camel case
https://www.codewars.com/kata/517abf86da9663f1d2000003
'''

# ---- SOLUTION ----

def to_camel_case(text):
  return text[:1] + text.replace('_', ' ').replace('-', ' ').title().replace(' ', '')[1:]

# ---- TEST ----

def dotest(text, expected):
  actual = to_camel_case(text)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'String = \"{text}\", expected = \"{expected}\", actual = \"{actual}\" -> {status}')

def main():
  dotest("", "")
  dotest("the_stealth_warrior", "theStealthWarrior")
  dotest("The-Stealth-Warrior", "TheStealthWarrior")
  dotest("A-B-C", "ABC")

if __name__ == "__main__":
  main()
