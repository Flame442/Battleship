name = ['','']
board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
let = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letnum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
bkey = [{0:'· ',1:'O ',2:'X ',3:'· '},{0:'· ',1:'O ',2:'X ',3:'# '}]
pswap = {1:0,0:1}
#   KEY FOR BOARD # TO SYMBOL:
#      ENEMY(0) FRIENDLY(1)
#   ·: Unknown | Nothing
#   O: Nothing | Enemy Miss
#   X: Hit     | Hit Friendly
#   #: N/A     | Unhit Friendly
#   ---------------------------
#   0: Blank Spot
#   1: Miss Spot
#   2: Hit Spot
#   3: Unchecked Ship Spot
def clear(): 
  for c in range(50): print()
def bprint(player,bt):
  b = '  '
  for z in range(10): b += let[z]+' '
  print(b)
  for y in range(10):
    a = (str(y)+' ')
    for x in range(10): a += bkey[bt][board[player][(y*10)+x]]
    print(a)
def place(player,length):
  i = 0
  while i == 0:
    t = input()
    try:
      x = letnum[t[0]]
      y = int(t[1])
      d = t[2]
      if d == 'r': #stop people from right looping----------------------------------------------
        f = 0
        for z in range(length):
          if board[player][(y*10)+x+z] != 0:
            f = 1
        if f == 1:
          1 / 0
        for z in range(length):
          board[player][(y*10)+x+z] = 3
        i = 1
      elif d == 'd':
        f = 0
        for z in range(length):
          if board[player][((y+z)*10)+x] != 0:
            f = 1
        if f == 1:
          1 / 0
        for z in range(length):
          board[player][((y+z)*10)+x] = 3
        i = 1
    except:
      print('Invalid input')

print('Welcome to Battleship!')
for a in range(2): name[a] = input('Name for player '+str(a+1)+'?\n')
clear()
print(name[0]+', it is your turn to set up your ships. Place ships by entering the top left cord in xyd format.')
bprint(0,1)
print('Place your 5 length ship')
place(0,5)
bprint(0,1)
print('Place your 4 length ship')
place(0,4)
bprint(0,1)
print('Place your first 3 length ship')
place(0,3)
bprint(0,1)
print('Place your second 3 length ship')
place(0,3)
bprint(0,1)
print('Place your 2 length ship')
place(0,2)
clear()
print(name[1]+', it is your turn to set up your ships. Place ships by entering the top left cord in xyd format.')
bprint(1,1)
print('Place your 5 length ship')
place(1,5)
bprint(1,1)
print('Place your 4 length ship')
place(1,4)
bprint(1,1)
print('Place your first 3 length ship')
place(1,3)
bprint(1,1)
print('Place your second 3 length ship')
place(1,3)
bprint(1,1)
print('Place your 2 length ship')
place(1,2)
bprint(1,1)
