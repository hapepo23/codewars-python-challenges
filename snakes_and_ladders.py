'''
5 kyu
Snakes and Ladders
https://www.codewars.com/kata/587136ba2eefcb92a9000027
'''

# ---- SOLUTION ----

class SnakesLadders():
  jumps = (
    (2, 38), (7, 14), (8, 31), (15, 26), (21, 42), (28, 84), (36, 44),
    (51, 67), (71, 91), (78, 98), (87, 94), (16, 6), (46, 25), (49, 11),
    (62, 19), (64, 60), (74, 53), (89, 68), (92, 88), (95, 75), (99, 80)
  )

  def __init__(self):
    self.pos = [0, 0]
    self.next_player = 0

  def play(self, die1, die2):
    notfin = True
    message = ''
    if self.pos[0] == 100 or self.pos[1] == 100:
      message = 'Game over!'
    else:
      self.pos[self.next_player] += die1 + die2
      if self.pos[self.next_player] == 100:
        message = f'Player {self.next_player + 1} Wins!'
        notfin = False
      elif self.pos[self.next_player] > 100:
        self.pos[self.next_player] = 200 - self.pos[self.next_player]
      if notfin:
        for j in SnakesLadders.jumps:
          if self.pos[self.next_player] == j[0]:
            self.pos[self.next_player] = j[1]
            break
    if message == '':
      message = f'Player {self.next_player + 1} is on square {self.pos[self.next_player]}'
    if not (notfin and die1 == die2):
      self.next_player = (self.next_player + 1) % 2
    return message

# ---- TEST ----

def dotest(game, die1, die2, expected):
  actual = game.play(die1, die2)
  status = 'OK' if expected == actual else 'FAIL'
  print(f'Dies: {die1} and {die2}, expected: {expected}, actual: {actual} -> {status}')

def main():
  game = SnakesLadders()
  dotest(game, 1, 1, "Player 1 is on square 38")
  dotest(game, 1, 5, "Player 1 is on square 44")
  dotest(game, 6, 2, "Player 2 is on square 31")
  dotest(game, 1, 1, "Player 1 is on square 25")
  dotest(game, 1, 2, "Player 1 is on square 84")
  dotest(game, 1, 2, "Player 2 is on square 34")
  dotest(game, 2, 1, "Player 1 is on square 94")
  dotest(game, 1, 2, "Player 2 is on square 37")
  dotest(game, 6, 2, "Player 1 is on square 98")
  dotest(game, 4, 6, "Player 2 is on square 47")
  dotest(game, 1, 1, "Player 1 Wins!")
  dotest(game, 6, 6, "Game over!")
  dotest(game, 6, 6, "Game over!")

if __name__ == "__main__":
  main()
