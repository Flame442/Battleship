name = ['','']
print('Welcome to Battleship!')
for a in range(2): name[a] = input('Name for player '+str(a+1)+'?\n')

board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
let = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
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
def bprint(player,bt):
  b = '  '
  for z in range(10): b += let[z]+' '
  print(b)
  for y in range(10):
    a = (str(y)+' ')
    for x in range(10): a += bkey[bt][board[player][(y*10)+x]]
    print(a)

print(name[0]+', it is your turn to set up your ships')
