'''
6 kyu
City walking tour
https://www.codewars.com/kata/6904bf406a5bf8ce9fa046df
'''

# ---- SOLUTION ----

import math

def mins(time_string):
  hm = time_string.split(':')
  return int(hm[0]) * 60 + int(hm[1])

def distance(x1, y1, x2, y2):
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_possible_to_visit_all(attractions, hotel_coords, start_time_str, close_time_str):
  t = mins(start_time_str)
  x = hotel_coords.x
  y = hotel_coords.y
  for a in attractions:
    d = distance(x, y, a.x, a.y)
    t += d * 12 + a.v  # 12 min/km
    x = a.x
    y = a.y
  d = distance(x, y, hotel_coords.x, hotel_coords.y)
  t += d * 12
  return t <= mins(close_time_str)

# ---- TEST ----

class Attraction:
  def __init__(self, x, y, v):
    self.x = x
    self.y = y
    self.v = v

  def __str__(self):
    return '[Attraction: x=' + str(self.x) + ', y=' + str(self.y) + ', view_mins=' + str(self.v) + ']'

class Hotel:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return '[Hotel: x=' + str(self.x) + ', y=' + str(self.y) + ']'

def dotest(attractions, hotel_coords, start_time_str, close_time_str, expected):
  actual = is_possible_to_visit_all(attractions, hotel_coords, start_time_str, close_time_str)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Attractions = {[str(row) for row in attractions]}')
  print(f'Hotel = {str(hotel_coords)}')
  print(f'Time from = {start_time_str}, to = {close_time_str}')
  print(f'expected = {expected}, actual = {actual} -> {status}\n')

def main():
  attractions = [
    Attraction(100, 100, 30),
    Attraction(200, 200, 40),
    Attraction(300, 300, 50)
  ]
  hotel_coords = Hotel(50, 50)
  start_time = "10:00"
  close_time = "17:00"
  dotest(attractions, hotel_coords, start_time, close_time, False)
  attractions = [
    Attraction(100, 100, 30),
    Attraction(110, 110, 40),
    Attraction(120, 120, 50)
  ]
  hotel_coords = Hotel(90, 90)
  start_time = "03:00"
  close_time = "23:00"
  dotest(attractions, hotel_coords, start_time, close_time, True)
  attractions = [
    Attraction(13, 21, 30),
    Attraction(-10, 5, 30),
    Attraction(0, 50, 30),
    Attraction(0, 60, 30),
    Attraction(0, 70, 30),
    Attraction(0, 80, 30)
  ]
  hotel_coords = Hotel(0, 0)
  start_time = "08:20"
  close_time = "20:50"
  dotest(attractions, hotel_coords, start_time, close_time, False)

if __name__ == "__main__":
  main()
