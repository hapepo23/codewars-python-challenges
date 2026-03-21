'''
4 kyu
Mouse Over (x,y) (Performance Version)
https://www.codewars.com/kata/68358ebb8a04e38c1f278e56
'''

# ---- SOLUTION ----

from collections import defaultdict

class MouseOver:
  def __init__(self, rectangles):
    self.cell_size = 1000  # x,y in the 100000 ranges
    self.rectangles = rectangles
    self.grid = defaultdict(list)
    for i, (x, y, w, h) in enumerate(rectangles):
      x1, y1 = x, y
      x2, y2 = x + w, y + h
      gx1, gy1 = int(x1 // self.cell_size), int(y1 // self.cell_size)
      gx2, gy2 = int(x2 // self.cell_size), int(y2 // self.cell_size)
      for gx in range(gx1, gx2 + 1):
        for gy in range(gy1, gy2 + 1):
          self.grid[(gx, gy)].append(i)

  def find_rectangle(self, px, py):
    gx, gy = int(px // self.cell_size), int(py // self.cell_size)
    for i in self.grid.get((gx, gy), []):
      x, y, w, h = self.rectangles[i]
      if x <= px <= x + w and y <= py <= y + h:
        return self.rectangles[i]
    return None

# ---- TEST ----

def dotest(mouse_over, x, y, expected):
  actual = mouse_over.find_rectangle(x, y)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'x,y: [{x}, {y}], expected: {expected}, actual: {actual} -> {status}')

def main():
  rectangles = [(9, 8, 9, 3), (6, 4, 15, 3), (9, 16, 9, 3), (6, 20, 15, 3), (5, 9, 3, 9), (1, 6, 3, 15), (19, 9, 3, 9),
                (23, 6, 3, 15), (15, 15, 10, 10)]
  mouse_over = MouseOver(rectangles)
  dotest(mouse_over, 3, 18, (1, 6, 3, 15))
  dotest(mouse_over, 6, 15, (5, 9, 3, 9))
  dotest(mouse_over, 10, 11, (9, 8, 9, 3))
  dotest(mouse_over, 15, 13, None)
  dotest(mouse_over, 18, 21, (6, 20, 15, 3))

if __name__ == "__main__":
  main()
