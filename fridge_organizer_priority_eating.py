'''
7 kyu
Fridge Organizer: Priority Eating
https://www.codewars.com/kata/69971f385353edeaf428e1b0
'''

# ---- SOLUTION ----

def fridge_organizer(items):
  return [row.name for row in sorted(
    (row for row in items if row.expiry_days >= 0),
    key=lambda e: (not e.is_almost_empty, e.expiry_days, e.name)
  )]

# ---- TEST ----

class FoodItem:
  def __init__(self, n, ed, iae):
    self.name = n
    self.expiry_days = ed
    self.is_almost_empty = iae

  def tostring(self):
    return '[' + self.name + ', ' + str(self.expiry_days) + ', ' + str(self.is_almost_empty) + ']'

def dotest(items, expected):
  actual = fridge_organizer(items)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Items = {[items[row].tostring() for row in range(len(items))]}')
  print(f'expected = {expected}, actual = {actual} -> {status}\n')

def main():
  dotest(
    [FoodItem("Milk", 3, False),
     FoodItem("Jam", 3, True),
     FoodItem("Yogurt", 1, False),
     FoodItem("Old Meat", -1, True),
     FoodItem("Today's Tofu", 0, False)],
    ["Jam", "Today's Tofu", "Yogurt", "Milk"])
  dotest(
    [FoodItem("Zucchini", 5, False),
     FoodItem("Apples", 5, False)],
    ["Apples", "Zucchini"])

if __name__ == "__main__":
  main()
