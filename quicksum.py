'''
7 kyu
Quicksum
https://www.codewars.com/kata/569924899aa8541eb200003f
'''

# ---- SOLUTION ----

def quicksum(packet):
  if any(not (c == ' ' or 'A' <= c <= 'Z') for c in packet):
    return 0
  return sum((i + 1) * (ord(c) - ord('A') + 1) for i, c in enumerate(packet) if c != ' ')

# ---- TEST ----

def dotest(packet, expected):
  actual = quicksum(packet)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Packet = {packet}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest("ACM", 46)
  dotest("MID CENTRAL", 650)
  dotest("BBC", 15)
  dotest("???", 0)
  dotest("axg ", 0)
  dotest("234 234 WEF ASDF AAA 554211 ???? ", 0)
  dotest("A C M", 75)
  dotest("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 6201)
  dotest("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z", 12051)
  dotest(
    "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
    848640)
  dotest("Z     A", 33)
  dotest("12312 123 123 asd asd 123 $$$$/()=", 0)
  dotest("As ", 0)
  dotest("         ", 0)

if __name__ == "__main__":
  main()
