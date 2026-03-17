'''
7 kyu
2D Vector Mapping
https://www.codewars.com/kata/5da995d583326300293ce4cb
'''

# ---- SOLUTION ----

import math

def map_vector(vector, circle1, circle2):
  x1 = vector[0] - circle1[0]
  y1 = vector[1] - circle1[1]
  r1 = math.sqrt(x1 * x1 + y1 * y1)
  a = math.atan2(y1, x1)
  r2 = r1 * circle2[2] / circle1[2]
  x2 = r2 * math.cos(a) + circle2[0]
  y2 = r2 * math.sin(a) + circle2[1]
  return [x2, y2]

# ---- SECOND SOLUTION ----
'''
def map_vector(vector, circle1, circle2):
  return [circle2[0] + circle2[2] / circle1[2] * (vector[0] - circle1[0]),
          circle2[1] + circle2[2] / circle1[2] * (vector[1] - circle1[1])]
'''

# ---- TEST ----

def dotest(vector, circle1, circle2, expected):
  actual = map_vector(vector, circle1, circle2)
  actual[0] = round(actual[0], 2)
  actual[1] = round(actual[1], 2)
  status = 'OK' if expected == actual else 'FAIL'
  print(
    f'Vector = {vector}, circle1 = {circle1}, circle2 = {circle2}\nexpected = {expected}, actual = {actual} -> {status}\n')

def main():
  dotest([46, 58], [0, 0, 100], [0, 0, 100], [46, 58])
  dotest([50, 88], [-25, 128, 100], [50, 50, 100], [125, 10])
  dotest([120, 58], [100, 76, 36], [120, -62, 50], [147.78, -87.0])
  dotest([5, 5], [10, 20, 42], [-100, -42, 60], [-107.14, -63.43])
  dotest([5, 5], [10, 20, 42], [-100, -42, 69], [-108.21, -66.64])

if __name__ == "__main__":
  main()
