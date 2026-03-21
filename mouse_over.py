'''
7 kyu
Mouse Over (x,y)
https://www.codewars.com/kata/68356baf60410813d358bb2c
'''

# ---- SOLUTION ----

class MouseOver:
  def __init__(self, rectangles):
    self.rectangles = []
    for rect in rectangles:
      (x, y, w, h) = rect
      self.rectangles.append((x, y, x + w, y + h))

  def find_rectangle(self, x, y):
    for rect in self.rectangles:
      x1, y1, x2, y2 = rect
      if x1 <= x <= x2 and y1 <= y <= y2:
        return (x1, y1, x2 - x1, y2 - y1)
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
