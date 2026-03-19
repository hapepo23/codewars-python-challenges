'''
8 kyu
Calculate BMI
https://www.codewars.com/kata/57a429e253ba3381850000fb
'''

# ---- SOLUTION ----

def bmi(weight, height):
  result = weight / (height * height)
  return "Underweight" if result <= 18.5 else (
    "Normal" if result <= 25 else (
      "Overweight" if result <= 30 else "Obese"))

# ---- TEST ----

def dotest(weight, height, expected):
  actual = bmi(weight, height)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Weight = {weight}, height = {height}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest(50, 1.80, "Underweight")
  dotest(80, 1.80, "Normal")
  dotest(90, 1.80, "Overweight")
  dotest(100, 1.80, "Obese")

if __name__ == "__main__":
  main()
