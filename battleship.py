name = ['','']
board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
let = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letnum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
bkey = [{0:'· ',1:'O ',2:'X ',3:'· '},{0:'· ',1:'O ',2:'X ',3:'# '}]
pswap = {1:0,0:1}
key = [[],[]]
key2 = {0:0,1:0,2:0,3:0,4:0}
namekey = {0:'5',1:'4',2:'3',3:'3',4:'2'}
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
    hold = {}
    t = input()
    try:
      x = letnum[t[0]]
      y = int(t[1])
      d = t[2]
      if d == 'r':
        if 10 - length < x:
          1 / 0
        f = 0
        for z in range(length):
          if board[player][(y*10)+x+z] != 0:
            f = 1
        if f == 1:
          1 / 0
        for z in range(length):
          board[player][(y*10)+x+z] = 3
          hold[(y*10)+x+z] = 0
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
          hold[(y*10)+x+z] = 0
        i = 1
    except:
      print('Invalid input')
  key[player].append(hold)
print('Welcome to Battleship!')
for a in range(2): name[a] = input('Name for player '+str(a+1)+'?\n')
clear()
for x in range(2):
  print(name[x]+', it is your turn to set up your ships. Place ships by entering the top left cord in xyd format.')
  for k in [5,4,3,3,2]:
    bprint(x,1)
    print('Place your '+str(k)+' length ship')
    place(x,k)
    clear()
game = True
p = 1
while game == True:
  p = pswap[p]
  print(name[p]+'\'s turn!')
  input()
  clear()
  bprint(p,1)
  bprint(pswap[p],0)
  print(name[p]+', take your shot')
  i = 0
  while i == 0:
    try:
      t = input()
      x = letnum[t[0]]
      y = int(t[1])
      if board[pswap[p]][(y*10)+x] == 0:
        clear()
        board[pswap[p]][(y*10)+x] = 1
        bprint(p,1)
        bprint(pswap[p],0)
        print('Miss!')
        input()
        clear()
        i = 1
      elif board[pswap[p]][(y*10)+x] in [1,2]:
        print('You already shot there!')
      elif board[pswap[p]][(y*10)+x] == 3:
        clear()
        board[pswap[p]][(y*10)+x] = 2
        bprint(p,1)
        bprint(pswap[p],0)
        print('Hit!')
        for a in range(5):
          if ((y*10)+x) in key[pswap[p]][a]:
            key[pswap[p]][a][(y*10)+x] = 1
            l = 0
            for b in key[pswap[p]][a]:
              if key[pswap[p]][a][b] == 0:
                l = 1
                break
            if l == 0:
              print(name[pswap[p]]+'\'s '+namekey[a]+' length ship was destroyed!')
              key2[a] = 1
              l = 0
              for c in key2:
                if key2[c] == 0:
                  l = 1
                  break
              if l == 0:
                print(name[p]+' wins!')
                game = False
        if game == False:
          i = 1
        else:
          input()
          clear()
          i = 1
    except:
      print('Invalid input')
