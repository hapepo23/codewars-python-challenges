'''
8 kyu
Find the Slope
https://www.codewars.com/kata/55a75e2d0803fea18f00009d
'''

# ---- SOLUTION ----

def find_slope(points):
  deltax = points[2] - points[0]
  if deltax == 0:
    return 'undefined'
  else:
    slope = (points[3] - points[1]) / deltax
    return str(int(slope))

# ---- TEST ----

def dotest(points, expected):
  actual = find_slope(points)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Points = {points}, expected = {expected}, actual = {actual} -> {status}')

def main():
  dotest([19, 3, 20, 3], "0")
  dotest([-7, 2, -7, 4], "undefined")
  dotest([10, 50, 30, 150], "5")
  dotest([10, 20, 20, 80], "6")
  dotest([-10, 6, -10, 3], "undefined")

if __name__ == "__main__":
  main()
