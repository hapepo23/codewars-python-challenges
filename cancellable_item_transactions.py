'''
6 kyu
Cancellable Item Transactions
https://www.codewars.com/kata/69bf57993a0061ef6d03c095
'''

# ---- SOLUTION ----

import re
from collections import defaultdict

def calculate(price_dict, transaction):
  result = 0
  stacks = defaultdict(list)
  matches = re.finditer("[-]{0,1}[0-9]*[A-Z]{1}", transaction)
  for match in matches:
    letter = match.group()[-1]
    num = match.group()[:-1]
    if num == '':
      if stacks[letter]:
        result -= stacks[letter].pop()
    else:
      count = int(num) * price_dict[letter]
      result += count
      stacks[letter].append(count)
  return result

# ---- TEST ----

def dotest(price_dict, transaction, expected):
  actual = calculate(price_dict, transaction)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Prices = {price_dict},\nTransaction = {transaction},\nexpected = {expected}, actual = {actual} -> {status}\n')

def main():
  dotest({"X": 0, "Y": 0, "Z": 0}, '5X6Y20Z1X6Y', 0)
  dotest({"R": 1, "Q": 2, "E": 3, "X": 4}, "4R1Q4X2E1R2X", 37)
  dotest({"T": 12, "F": 6}, "2F5T1T", 84)
  dotest({"G": 1, "M": 1, "F": 1, "H": 1, "J": 1}, "5J2F7M1H9G6M1H", 31)
  dotest({"E": 67}, "1E", 67)
  dotest({"X": 3, "Y": 3, "Z": 3}, "2X-1Y7X2Z-1Z9Y5X-3Y", 60)
  dotest({"W": 12}, "9W6W-2W8W5W-4W1W", 276)
  dotest({"X": 1, "Y": 2, "Z": 5}, "10X22Y12Z2X", 116)
  dotest({"K": 0, "P": 2, "B": 6, "M": 4}, "50K10P42B521M4K125B", 3106)
  dotest({"A": 3, "B": 1, "C": 4}, "3C2B1AC", 5)
  dotest({"D": 6, "B": 10, "G": 2}, "5D4GG6B2D1GBD", 32)
  dotest({"A": 4, "B": 3, "C": 2, "D": 1}, "6D1A3B5A2C3AAAA", 19)
  dotest({"S": 12, "I": 56, "G": 2, "M": 1, "A": 8}, "5G1S7M2I9A6SMISGAS", 0)
  dotest({"T": 1, "V": 5}, "6TVTT2V", 10)
  dotest({"L": 2, "M": 4, "N": 6, "O": 8}, "12LO3MLL5L1O4N", 54)
  dotest({"W": 2, "D": 4}, "DWDWDWWD", 0)

if __name__ == "__main__":
  main()
