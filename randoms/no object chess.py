from random import *
from pygame import *

def setup():
    global board, gameDone, mGone
    mGone=0
    gameDone = False
    print(
        "input moves as start and end grid coordionates eg 2223 to move a pawn at 2,2 to 2,3"
    )


def checkMate(cBoard):
    global vMoves, gameDone, mGone
    checkMate=True
    for i in range(len(vMoves)):
      if not checkForCheck(board,vMoves[i]):
        checkMate=False
    if checkMate:
      gameDone=True
      if checkForCheck(board,False):
        print(whoTurn,"is checkmated")
      else:
        print("stalemate lmao")
    elif mGone==50:
      gameDone=True
      print("stalemate lmao")


def loadFEN(FEN):
    global board, whoTurn
    FENBoard = [["  " for i in range(0, 8)] for x in range(0, 8)]
    FEN = FEN.split("/")
    for i in range(0, 8):
        skip = 0
        skiped = 0
        for x in range(0, 8):
            try:
                int(FEN[i][x])
                num = True
            except:
                num = False
            if num == False:
                try:
                    if FEN[i][x] == " ":
                        pass
                    elif FEN[i][x] == FEN[i][x].lower():
                        FENBoard[i][x + skiped] = "w" + FEN[i][x]
                    elif FEN[i][x] == FEN[i][x].upper():
                        FENBoard[i][x + skiped] = "b" + FEN[i][x].lower()
                except:
                    pass
            else:
                skip = int(FEN[i][x]) - 1
                skiped += skip
    if FEN[i].split(" ")[1] == "w":
        whoTurn = "w"
    elif FEN[i].split(" ")[1] == "b":
        whoTurn = "b"
    board = [[FENBoard[x][i] for x in range(0, 8)] for i in range(0, 8)]


def game(w,b):
    global whoTurn, gameDone, board
    take = False
    while not gameDone:
      if whoTurn=="w":
        p=w
      else:
        p=b
      if p=="h":
        move = input(whoTurn + " move?")
        if len(move) == 4:
            problem = False
            try:
                if board[int(move[2]) - 1][int(move[3]) - 1][0] == whoTurn:
                    print("cant move to yo own piece my guy")
                    problem = True
                elif board[int(move[2]) - 1][int(move[3]) - 1][0] == " ":
                    take = False
                    pass
                else:
                    take = True
                if board[int(move[0]) - 1][int(move[1]) - 1][0] == whoTurn:
                    pass
                elif board[int(move[0]) - 1][int(move[1]) - 1][0] == " ":
                    problem = True
                    print("no piece my guy")
                else:
                    problem = True
                    print("not yo piece at start")
            except:
                problem = True
                print("error wit yo input")
            if problem == False:
                tMove=""
                for i in range(0,4):
                  tMove+=str(int(move[i])-1)
                if tMove in vMoves:
                  if board[int(tMove[0])][int(tMove[1])]=="wp" and int(tMove[3])==7:
                    promote=True
                  elif board[int(tMove[0])][int(tMove[1])]=="bp" and int(tMove[3])==0:
                    promote=True
                  else:
                    promote=False
                  movePiece(move,take,promote)
        else:
            print("not 4 long")
      elif p=="r":
        tMove=vMoves[randint(0,len(vMoves)-1)]
        if board[int(tMove[0])][int(tMove[1])]=="wp" and int(tMove[3])==7:
            promote=True
        elif board[int(tMove[0])][int(tMove[1])]=="bp" and int(tMove[3])==0:
            promote=True
        else:
            promote=False
        if board[int(tMove[0])][int(tMove[1])][1]=="p":
          mGone=0
        move=""
        for i in range(0,4):
            move+=str(int(tMove[i])+1)
        movePiece(move,take,promote)


def movePiece(move, take, promote):
    global whoTurn, board, wPlayer, bPlayer, mGone
    tBoard = [[board[x][i] for i in range(0, 8)] for x in range(0, 8)]
    if promote == False:
        tBoard[int(move[2]) - 1][int(move[3]) - 1] = tBoard[int(move[0]) -
                                                            1][int(move[1]) -
                                                               1]
    while promote == True:
        if (whoTurn=="w" and wPlayer=="h") or (whoTurn=="b" and bPlayer=="h"):
          try:
              pPiece = input("promote?")
              if pPiece in ["r", "n", "b", "q"]:
                  tBoard[int(move[2]) - 1][int(move[3]) - 1] = whoTurn + pPiece
                  promote = False
          except:
              pass
        elif (whoTurn=="w" and wPlayer=="r") or (whoTurn=="b" and bPlayer=="r"):
          pPPieces=["q","r","n","b"]
          pPiece=pPPieces[randint(0,3)]
          tBoard[int(move[2]) - 1][int(move[3]) - 1] = whoTurn + pPiece
          promote = False
    tBoard[int(move[0]) - 1][int(move[1]) - 1] = "  "
    if checkForCheck(tBoard,False):
        print("you'd be in check lmao")
    else:
        board = tBoard
        if take or board[int(move[2])-1][int(move[3])-1][1]=="p":
          mGone=0
        else:
          mGone+=1
        if whoTurn == "w":
            whoTurn = "b"
        else:
            whoTurn = "w"
        showBoard()
        validMoves(board)
        checkMate(board)


def showBoard():
    global board
    for x in range(0, 8):
        a = str(8 - x) + "|"
        for i in range(0, 8):
            a += board[i][7 - x] + "|"
        print(a[0:len(a) - 1])
    a = ""
    for i in range(0, 8):
        a += " |" + str(i + 1)
    print(a)

    
def checkForCheck(cBoard,move):
    global whoTurn
    check = False
    tBoard = [[cBoard[x][i] for i in range(0, 8)] for x in range(0, 8)]
    if move:
      tBoard[int(move[2])][int(move[3])]=tBoard[int(move[0])][int(move[1])]
      tBoard[int(move[0])][int(move[1])]="  "
    cBoard=tBoard
    posOfKnight = ""
    if whoTurn == "b":
        oppo = "w"
    else:
        oppo = "b"
    for i in range(0, 8):
        for x in range(0, 8):
            if cBoard[i][x] == whoTurn + "k":
                posOfKing = str(i) + str(x)
            if cBoard[i][x] == oppo + "n":
                posOfKnight += str(i) + str(x)
    #knights
    for i in range(0, len(posOfKnight) // 2):
        hDif = abs(int(posOfKnight[2 * i]) - int(posOfKing[0]))
        vDif = abs(int(posOfKnight[2 * i + 1]) - int(posOfKing[1]))
        if hDif == 2 and vDif == 1:
            check = True
        elif hDif == 1 and vDif == 2:
            check = True
    #straights
    for i in range(1, int(posOfKing[0])+1):
        tPiece = cBoard[int(posOfKing[0])-i][int(posOfKing[1])]
        if tPiece == oppo + "r" or tPiece == oppo + "q" or (tPiece == oppo + "k" and i == 1):
            check = True
        elif tPiece != "  ":
            break
    for i in range(int(posOfKing[0]) + 1, 8):
        tPiece = cBoard[i][int(posOfKing[1])]
        if tPiece == oppo + "r" or tPiece == oppo + "q" or (tPiece == oppo + "k" and i-int(posOfKing[0]) == 1):
            check = True
        elif tPiece != "  ":
            break
    for i in range(1, int(posOfKing[1])+1):
        tPiece = cBoard[int(posOfKing[0])][int(posOfKing[1]) - i]
        if tPiece == oppo + "r" or tPiece == oppo + "q" or (tPiece == oppo + "k" and i == 1):
            check = True
        elif tPiece != "  ":
            break
    for i in range(int(posOfKing[1]) + 1, 8):
        tPiece = cBoard[int(posOfKing[0])][i]
        if tPiece == oppo + "r" or tPiece == oppo + "q" or (tPiece == oppo + "k" and i-int(posOfKing[1]) == 1):
            check = True
        elif tPiece != "  ":
            break
    #diags
    for i in range(1, 8):
        if 7 >= int(posOfKing[0]) + i >= 0 and 7 >= int(
                posOfKing[1]) + i >= 0 and cBoard[int(posOfKing[0]) + i][
                    int(posOfKing[1]) + i] != whoTurn + "k":
            tPiece = cBoard[int(posOfKing[0]) + i][int(posOfKing[1]) + i]
            if tPiece == oppo + "b" or tPiece == oppo + "q" or (
                    tPiece == oppo + "k"
                    and i == 1) or ("bp" == tPiece == oppo + "p" and i == 1):
                check = True
            elif tPiece != "  ":
                break
    for i in range(1, 8):
        if 7 >= int(posOfKing[0]) + i >= 0 and 7 >= int(
                posOfKing[1]) - i >= 0 and cBoard[int(posOfKing[0]) + i][
                    int(posOfKing[1]) - i] != whoTurn + "k":
            tPiece = cBoard[int(posOfKing[0]) + i][int(posOfKing[1]) - i]
            if tPiece == oppo + "b" or tPiece == oppo + "q" or (
                    tPiece == oppo + "k"
                    and i == 1) or ("wp" == tPiece == oppo + "p" and i == 1):
                check = True
            elif tPiece != "  ":
                break
    for i in range(1, 8):
        if 7 >= int(posOfKing[0]) - i >= 0 and 7 >= int(
                posOfKing[1]) + i >= 0 and cBoard[int(posOfKing[0]) - i][
                    int(posOfKing[1]) + i] != whoTurn + "k":
            tPiece = cBoard[int(posOfKing[0]) - i][int(posOfKing[1]) + i]
            if tPiece == oppo + "b" or tPiece == oppo + "q" or (
                    tPiece == oppo + "k"
                    and i == 1) or ("bp" == tPiece == oppo + "p" and i == 1):
                check = True
            elif tPiece != "  ":
                break
    for i in range(1, 8):
        if 7 >= int(posOfKing[0]) - i >= 0 and 7 >= int(
                posOfKing[1]) - i >= 0 and cBoard[int(posOfKing[0]) - i][
                    int(posOfKing[1]) - i] != whoTurn + "k":
            tPiece = cBoard[int(posOfKing[0]) - i][int(posOfKing[1]) - i]
            if tPiece == oppo + "b" or tPiece == oppo + "q" or (
                    tPiece == oppo + "k"
                    and i == 1) or ("wp" == tPiece == oppo + "p" and i == 1):
                check = True
            elif tPiece != "  ":
                break

    if check == True:
        return True
    else:
        return False


def pPawnMoves(board, x, y): # no peasnt
    global vMoves
    for a in range(0, 8):
        for b in range(0, 8):
            canMove = False
            take = False
            if board[a][b][0] != whoTurn:
                if whoTurn == "w":
                    if board[a][b][0] == "b":
                        take = True
                    if a != x:
                        if take and abs(x - a) == 1 and y - b == -1:
                            canMove = True
                    elif (not take) and b - y == 1:
                        canMove = True
                    elif (not take) and y == 1 and b - y == 2:
                        canMove = True
                else:
                  if board[a][b][0] == "w":
                      take = True
                  if a != x:
                      if take and abs(x - a) == 1 and y - b == 1:
                          canMove = True
                  elif (not take) and b - y == -1:
                      canMove = True
                  elif (not take) and y == 6 and b - y == -2:
                      canMove = True
            if canMove and not checkForCheck(board,str(x) + str(y) + str(a) + str(b)):
                vMoves.append(str(x) + str(y) + str(a) + str(b))


def pKnightMoves(board,x,y):
    global vMoves
    for a in range(0, 8):
        for b in range(0, 8):
            canMove = False
            if board[a][b][0] != whoTurn:
              if abs(x-a)==2 and abs(y-b)==1:
                canMove=True
              elif abs(x-a)==1 and abs(y-b)==2:
                canMove=True
            if canMove and not checkForCheck(board,str(x) + str(y) + str(a) + str(b)):
                vMoves.append(str(x) + str(y) + str(a) + str(b))


def pRookMoves(board,x,y):
    global vMoves
    for a in range(0, 8):
        for b in range(0, 8):
            canMove = True
            if board[a][b][0] != whoTurn:
              if x==a:
                if y<b:
                  for i in range(y+1,b):
                    if board[x][i]!="  ":
                      canMove=False
                else:
                  for i in range(b+1,y):
                    if board[x][i]!="  ":
                      canMove=False
              elif y==b:
                if x<a:
                  for i in range(x+1,a):
                    if board[i][y]!="  ":
                      canMove=False
                else:
                  for i in range(a+1,x):
                    if board[i][y]!="  ":
                      canMove=False
              else:
                canMove=False
            else:
              canMove=False
            if canMove and not checkForCheck(board,str(x) + str(y) + str(a) + str(b)):
                vMoves.append(str(x) + str(y) + str(a) + str(b))
            

def pBishopMoves(board,x,y):
    global vMoves
    for a in range(0, 8):
        for b in range(0, 8):
            canMove = True
            if board[a][b][0] != whoTurn:
              if abs(x-a)==abs(y-b):
                if x>a:
                  if y>b:
                      go=x-a  
                      for i in range(1,go):
                        if board[a+i][b+i]!="  ":
                          canMove=False
                  else:
                    go=x-a
                    for i in range(1,go):
                      if board[a+i][b-i]!="  ":
                        canMove=False
                else:
                  if y>b:
                      go=a-x
                      for i in range(1,go):
                        if board[a-i][b+i]!="  ":
                          canMove=False
                  else:
                    go=a-x
                    for i in range(1,go):
                      if board[a-i][b-i]!="  ":
                        canMove=False
              else:
                canMove=False
            else:
                canMove=False
            if canMove and not checkForCheck(board,str(x) + str(y) + str(a) + str(b)):
              vMoves.append(str(x) + str(y) + str(a) + str(b))


def pKingMoves(board,x,y):
    global vMoves
    for a in range(0, 8):
        for b in range(0, 8):
            canMove = False
            if board[a][b][0] != whoTurn:
              if abs(x-a)<=1 and abs(y-b)<=1:
                canMove=True
            if canMove and not checkForCheck(board,str(x) + str(y) + str(a) + str(b)):
              vMoves.append(str(x) + str(y) + str(a) + str(b))



def validMoves(board):
    global whoTurn, vMoves
    vMoves=[]
    for i in range(0, 8):
        for x in range(0, 8):
            piece = board[i][x]
            if piece[0] == whoTurn:
                if piece[1] == "p":
                    pPawnMoves(board, i, x)
                elif piece[1] == "n":
                    pKnightMoves(board, i, x)
                elif piece[1]=="r":
                  pRookMoves(board,i,x)
                elif piece[1]=="b":
                  pBishopMoves(board,i,x)
                elif piece[1]=="q":
                  pBishopMoves(board,i,x)
                  pRookMoves(board,i,x)
                elif piece[1]=="k":
                  pKingMoves(board,i,x)


setup()
loadFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w")  #starting position
#loadFEN("K7/7r/8/8/8/8/7k/5r2 w")
showBoard()
validMoves(board)
wPlayer=input("w?(h/r)")
bPlayer=input("b?(h/r)")
game(wPlayer,bPlayer)