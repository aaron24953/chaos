class board:
  def __init__(self):
    self.spaces=["" for i in range(64)]
    self.turn=0
    self.kingPositions=[-1,-1]
  
  def move(self,start,move):
    end=start+move
    if not move:
      return False
    if end>=64 or end<0:
      return False
    if self.spaces[start]=="":
      print("thats a space")
      return False
    val=self.spaces[start].vMove(start,move,self)
    if val or val==-1:
      self.spaces[end]=self.spaces[start]
      self.spaces[start]=""
      if str(val)=="1":
        self.spaces[end-8]=""
      elif val==-1:
        self.spaces[end+8]=""
      self.turn+=1

  def loadFEN(self,FEN):
    FEN=FEN.split("/")
    for i in range(64):
      do=True
      if i%8==0:
        skip=0
        skiped=0
      try:
        FENL=FEN[i//8][i%8]
      except:
        do=False
      if do:
        try:
          num=int(FENL)
        except:
          num=False
        if num==False:
          if FENL==" ":
            pass
          elif FENL==FENL.upper():
            colour=1
          else:
            colour=0
          FENL=FENL.lower()
          if FENL=="p":self.spaces[i+skiped]=pawn(colour,i//8)
          elif FENL=="r":self.spaces[i]=rook(colour)
          elif FENL=="n":self.spaces[i]=knight(colour)
          elif FENL=="b":self.spaces[i]=bishop(colour)
          elif FENL=="q":self.spaces[i]=queen(colour)
          elif FENL=="k":self.spaces[i]=king(colour);self.kingPositions[colour]=i
        else:
          skip=num-1
          skiped+=skip

  def tDisplay(self):
    l=[]
    colour=0
    for i in range(64):
      if i%8==0:
        o=""
      try:
        letter=self.spaces[i].symbol
        colour=self.spaces[i].colour
      except:
        letter=" "
      if colour:
        letter=letter.upper()
      o+=letter
      if i%8==7:
        l.append(o)
      else:
        o+="|"
    for i in range(7,-1,-1):
      print(l[i])
  
  def startPos(self):
    self.loadFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w")

  def checkForCheck(self):
    kPos=self.kingPositions[self.turn%2]
    kCol=self.spaces[kPos].colour
    for pMove in [17,15,10,6,-17,-15,-10,-6]:
      if isinstance(self.spaces[kPos+pMove],knight):
        if self.spaces[kPos+pMove].colour!=kCol:
          if self.spaces[kPos-pMove].vMove(kPos-pMove,pMove,self):
            return True
    for i in range(1,8):
      for pMove in [-9,-8,-7,-1,1,7,8,9]:#horendously inneficient
        if 0<=kPos+pMove*i<64:
          if type(self.spaces[kPos+pMove*i])!=type("string"):
            if self.spaces[kPos+pMove*i].colour!=kCol:
              if self.spaces[kPos+pMove*i].vMove(kPos+pMove*i,-pMove*i,self):
                return True

class pawn:
  def __init__(self,colour,vPos):
    self.symbol="p"
    self.colour=colour
    self.jumped=-1
    if (vPos==1 and colour==0) or (vPos==6 and colour==1):
      self.jump=True
    else:
      self.jump=False
  
  def vMove(self,start,move,board):
    end=start+move
    if self.colour==0:
      if type(board.spaces[end])==type("string"):
        if  move==8 or (self.jump and move==16):
          if move==16:
            if type(board.spaces[end-8])!=type("string"):
              return False
          self.jumped=board.turn
          self.jump=False
          return True
      if end-8>=0:
        if isinstance(board.spaces[end-8],pawn):
          if board.spaces[end-8].jumped==board.turn-1:
            if ((move ==7 and start%8!=0) or (move==9 and start%8!=7)):
              return 1
      elif ((move ==7 and start%8!=0) or (move==9 and start%8!=7)) and type(board.spaces[end])!=type("string"):
        if board.spaces[end].colour!=self.colour:
          return True
        else:
          return False
    else:
      if type(board.spaces[end])==type("string"):
        if move==-8 or (self.jump and move==-16):
          if move==-16:
            if type(board.spaces[end+8])!=type("string"):
              return False
          self.jumped=board.turn
          self.jump=False
          return True
      if end+8<64:
        if isinstance(board.spaces[end+8],pawn):
          if board.spaces[end+8].jumped==board.turn-1:
            if ((move ==-7 and start%8!=7) or (move==-9 and start%8!=0)):
              return -1
      elif ((move ==-7 and start%8!=7) or (move==-9 and start%8!=0)) and type(board.spaces[end])!=type("string"):
        if board.spaces[end].colour!=self.colour:
          return True
        else:
          return False
  
  def pMoves(self,start,board):
    pMoves=[]
    if not self.colour:
      if type(board.spaces[start+8])==type("string"):
          pMoves.append(8)
      if type(board.spaces[start+16])==type("string"):
        if self.jump==True:
          pMoves.append(16)
      for move in [7,9]:
        if ((move ==7 and start%8!=0) or (move==9 and start%8!=7)):
          if type(board.spaces[start+move])!=type("string"):
            if board.spaces[start+move].colour:
              pMoves.append(move)
          if type(board.spaces[start+move])==type("string"):
            if type(board.spaces[start+move-8])!=type("string"):
              if board.spaces[start+move-8].jumped==board.turn:
                pMoves.append(move) 
    else:
      if type(board.spaces[start+8])==type("string"):
          pMoves.append(8)
      if type(board.spaces[start+16])==type("string"):
        if self.jump==True:
          pMoves.append(16)
      for move in [-7,-9]:
        if ((move ==-9 and start%8!=0) or (move==-7 and start%8!=7)):
          if type(board.spaces[start+move])!=type("string"):
            if not board.spaces[start+move].colour:
              pMoves.append(move)
          if type(board.spaces[start+move])==type("string"):
            if type(board.spaces[start+move+8])!=type("string"):
              if board.spaces[start+move+8].jumped==board.turn:
                pMoves.append(move) 

class knight:
  def __init__(self,colour):
    self.symbol="n"
    self.colour=colour
  
  def vMove(self,start,move,board):
    #17,15,10,6
    end=start+move
    if type(board.spaces[end])!=type("string"):
      if board.spaces[end].colour==self.colour:
        return False
    if abs(move) in [17,15,10,6]:
      if 1<start%8<6:
        return True
      elif move in [17,-15] and start%8<7:
        return True
      elif move in [-17,15] and start%8>0:
        return True

  def pMoves(self,start,board):#bad
    pMoves=[]
    for i in [17,15,10,6,-6,-10,-15,-17]:
      if self.vMove(start,i,board):
        pMoves.append(i)
    return pMoves
    
class bishop:
  def __init__(self,colour):
    self.symbol="b"
    self.colour=colour
  
  def vMove(self,start,move,board):
    end=start+move
    if type(board.spaces[end])!=type("string"):
      if board.spaces[end].colour==self.colour:
        return False
    if (move%9==0 and abs(move)==move) or (move%7==0 and abs(move)!=move):
      if end%8>start%8:
        for i in range(1,abs(move//8)):
          if move==9:
            if type(board.spaces[i*9+start])!=type("string"):
              return False
          else:
            if type(board.spaces[i*-7+start])!=type("string"):
              return False
        return True
    if (move%9==0 and abs(move)!=move) or (move%7==0 and abs(move)==move):
      if end%8<start%8:
        for i in range(1,abs(move//8+1)):
          if move==9:
            if type(board.spaces[i*-9+start])!=type("string"):
              return False
          else:
            if type(board.spaces[i*7+start])!=type("string"):
              return False
        return True
    def pMoves(self,start,board):
        pass

class rook:
  def __init__(self,colour):
    self.symbol="r"
    self.castle=True
    self.colour=colour
  
  def vMove(self,start,move,board):
    end=start+move
    if type(board.spaces[end])!=type("string"):
      if board.spaces[end].colour==self.colour:
        return False
    if move%8==0:
      for i in range(1,abs(move//8)):
        if move==abs(move):
          if type(board.spaces[start+8*i])!=type("string"):
            return False
        elif type(board.spaces[start-8*i])!=type("string"):
            return False
      return True
    if move<8:
      if move==abs(move):
        if move%8<end%8:
          for i in range(1,move):
            if type(board.spaces[start+i])!=type("string"):
              return False
          return True
      else:
        if move%8>end%8:
          for i in range(1,move):
            if type(board.spaces[start-i])!=type("string"):
              return False
          return True

class queen:
  def __init__(self,colour):
    self.colour=colour
    self.symbol="q"
    self.castle=False
  
  def vMove(self,start,move,board):
    return rook.vMove(self,start,move,board) or bishop.vMove(self,start,move,board)

class king:
  def __init__(self,colour):
    self.colour=colour
    self.symbol="k"
    self.castle=True
  
  def vMove(self,start,move,board):
    end=start+move
    if move not in [-9,-8,-7,-1,1,7,8,9]:
      return False
    if move in [-9,-1,7]:
      if end%8==start%8-1:
        return True
    elif move in [-7,1,9]:
      if end%8==start%8+1:
        return True
    else:
      return True


def tInput():
  start=int(input("start?"))
  move=int(input("move?"))
  return start,move

def main():
  gBoard=board()
  #gBoard.startPos()
  gBoard.loadFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w")
  while 1:
    gBoard.tDisplay()
    inp=tInput()
    gBoard.move(inp[0],inp[1])

if __name__=="__main__":
  main()