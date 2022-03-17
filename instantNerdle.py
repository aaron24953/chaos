import cv2
from time import sleep
import pytesseract
from PIL import ImageGrab,Image
from numpy import asarray
from permutations import permute
import keyboard

def calc(toCheck,operand,i):
    temp=toCheck
    a=int(toCheck[i-1])
    try:
        if i-2>=0:
            a+=10*int(toCheck[i-2])
        try:
            if i-3>=0:
                a+=100*int(toCheck[i-3])
            try:
                if i-4>=0:
                    a+=1000*int(toCheck[i-4])
            except:
                pass
        except:
            pass
    except:
        pass
    b=int(toCheck[i+1])
    try:
        b=10*int(toCheck[i+1])
        b+=int(toCheck[i+2])
        try:
            b=100*int(toCheck[i+1])
            b+=10*int(toCheck[i+2])
            b+=int(toCheck[i+3])
            try:
                b=1000*int(toCheck[i+1])
                b+=100*int(toCheck[i+2])
                b+=10*int(toCheck[i+3])
                b+=1*int(toCheck[i+3])
            except:
                b=100*int(toCheck[i+1])
                b+=10*int(toCheck[i+2])
                b+=int(toCheck[i+3])
        except:
            b=10*int(toCheck[i+1])
            b+=int(toCheck[i+2])    
    except:
        b=int(toCheck[i+1])
    #print(a,toCheck,b)
    if operand=="*":
        value=a*b
    elif operand=="/":
        try:
            value=a//b
        except:
            return "False"
    elif operand=="+":
        value=a+b
    else:
        if a-b>0:
            value=a-b
        else:
            value=99999999
    toCheck="".join([temp[j] for j in range(0,i-len(str(a)))])
    toCheck+=str(value)
    toCheck+="".join([temp[j] for j in range(i+len(str(b))+1,len(temp))])
    return toCheck

def checkCalc(toCheck):
    bothSides=toCheck.split("=")
    toCheck=bothSides[0]
    for i in range(len(toCheck)):
        if toCheck[i] == "/":
            toCheck=calc(toCheck,toCheck[i],i)
            break
    for i in range(len(toCheck)):
        if toCheck[i] == "*":
            toCheck=calc(toCheck,toCheck[i],i)
            break
    for i in range(len(toCheck)):
        if toCheck[i] == "-":
            toCheck=calc(toCheck,toCheck[i],i)
            break
    for i in range(len(toCheck)):
        if toCheck[i] == "+":
            toCheck=calc(toCheck,toCheck[i],i)
            break
    if toCheck==bothSides[1]:
        return True
    return False

def checkValidNerdle(toCheck):
    #print(toCheck)
    eq=0
    for i in toCheck:
        if i!="=":
            eq+=1
        else:
            break
    if eq<len(toCheck)-4 or eq==len(toCheck)-1:
        return False
    symbol=0
    symbols=[]
    for i in toCheck:
        if i not in ["+","-","*","/","="]:
            symbol+=1
        else:
            symbols.append(symbol)
            symbol+=1
    pp=-1
    for point in symbols:
        if point-1==pp or point==len(toCheck)-1:
            return False
        pp=point
    return checkCalc("".join(toCheck))
                
def getNerdle():
    pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    #sleep(0.3)
    img=ImageGrab.grab(bbox=(90,330,1300,470))
    img.save("temp.png")
    img=cv2.imread("temp.png")
    gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, gimg = cv2.threshold(gimg, 200, 255, cv2.THRESH_BINARY)
    #cv2.imwrite("gimg.png",gimg)
    raw=pytesseract.image_to_string(gimg,config="--psm 7")
    raw=raw.split()
    print(raw)
    nerdle=""
    for char in raw:
        if char=="|":
            char="1"
        if char=="r4":
            char="2"
        nerdle+=char
    print(nerdle)
    return nerdle

def checkKnown(index):
    img=Image.open("temp.png")
    img=img.load()
    colour=img[70+150*index,120]
    if colour==(130,4,88):
        return False
    else:
        return True

def getKnown(nerdle):
    known=[]
    antiKnown=[]
    for i in range(8):
        if checkKnown(i):
            known.append(nerdle[i])
            antiKnown.append(-1)
        else:
            antiKnown.append(nerdle[i])
            known.append(-1)
    return known,antiKnown

def main():
    keyboard.press_and_release("alt+tab")
    sleep(0.1)
    question=getNerdle()
    known,antiKnown=getKnown(question)
    print(known,antiKnown)
    question=[i for i in question]
    perms=permute(question)
    ans="no ans"
    for i in perms:
        if checkValidNerdle(i):
            pAns="".join(i)
            isAns=True
            for j in range(len(pAns)):
                if (pAns[j]!=str(known[j]) and known[j]!=-1) or pAns[j]==str(antiKnown[j]):
                    isAns=False
            if isAns:
                ans=pAns
            print(pAns)
    print(ans,"is ans")
    for digit in ans:
        keyboard.press_and_release(digit)
        #sleep(0.1)
    keyboard.press_and_release("\n")
    keyboard.press_and_release("\n")
        
if __name__ == "__main__":
    main()
