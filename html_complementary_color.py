'''
6 kyu
HTML Complementary Color
https://www.codewars.com/kata/56be4affc5dc03b84b001d2d
'''

# ---- SOLUTION ----

def get_reversed_color(hex_color):
  if type(hex_color) == str and len(hex_color) <= 6:
    return '#' + hex(16777215 - int(('000000' + hex_color)[-6:], 16)).replace('0x', '000000').upper()[-6:]
  else:
    raise ValueError('Invalid hex color')

# ---- TEST ----

def dotest(hex_color, expected):
  try:
    actual = get_reversed_color(hex_color)
  except:
    actual = 'invalid'
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Hex Color = "{hex_color}", expected = "{expected}", actual = "{actual}" -> {status}')

def main():
  dotest("", "#FFFFFF")
  dotest("0", "#FFFFFF")
  dotest("ff", "#FFFF00")
  dotest("123456", "#EDCBA9")
  dotest("abcdef", "#543210")
  dotest("1234567", "invalid")
  dotest("AA00ZZ", "invalid")
  dotest(0, "invalid")
  dotest([1, 2, 3], "invalid")
  dotest({"foo": "bar"}, "invalid")
  dotest(None, "invalid")
  dotest('f2e449', "#0D1BB6")
  dotest('fffffe', "#000001")

if __name__ == "__main__":
  main()
