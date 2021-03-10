theboard={'topleft':' ','topmiddle':' ','topright':' ',
          'midleft':' ','midmiddle':' ','midright':' ',
          'lowleft':' ','lowmiddle':' ','lowright':' '}
def board():
    print(theboard['topleft']+"|"+theboard['topmiddle']+"|"+theboard['topright'])
    print("-+-+-")
    print(theboard['midleft']+"|"+theboard['midmiddle']+"|"+theboard['midright'])
    print("-+-+-")
    print(theboard['lowleft']+"|"+theboard['lowmiddle']+"|"+theboard['lowright'])
turn='X'    
for i in range(9):
    board()
    print("turn is "+turn+"Move on which space")
    move=input()
    if move in theboard.keys():
        theboard[move]=turn
    if turn=='X':
        turn='0'
    else:
        turn='X'
    print(board())    
    
    
    
    
    
