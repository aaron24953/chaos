from linecache import getline
import instantNerdle as iN
import permutations as p
import cv2
from time import sleep
import pytesseract
from PIL import ImageGrab,Image
from numpy import asarray
from permutations import permute
import keyboard
outed=[]

def outIfValid(check,known,antiKnown):
    global q
    if iN.checkValidNerdle(check):
        notAns=False
        for i in range(len(check)):
            if (str(check[i])!=str(known[i]) and known[i]!=-1) or str(check[i])==str(antiKnown[i]):
                notAns=True
        if not notAns:
            if not "".join(check) in outed and len(q)==len(check):
                outed.append("".join(check))
                print("".join(check))
                return 1
    return 0

def getLine(lineNo):
    pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    #sleep(0.3)
    img=ImageGrab.grab(bbox=(458,165+55*lineNo,933,215+55*lineNo))
    img.save("temp.png")
    img=cv2.imread("temp.png")
    gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, gimg = cv2.threshold(gimg, 200, 255, cv2.THRESH_BINARY)
    cv2.imwrite("gimg.png",gimg)
    raw=pytesseract.image_to_string(gimg,config="--psm 7")
    raw=raw.split()
    line=[]
    for char in raw:
        if char=="7?":
            char="7"
        if char=="a":
            char="/"
        if char=="41":
            char="1"
        if char=="E)":
            char="9"
        line.append(char)
    lineInfo=[]
    img=Image.open("temp.png")
    img=img.load()
    for i in range(8):
        colour=img[27+60*i,5]
        if colour==(130,4,88):
            lineInfo.append(1)
        elif colour==(57,136,116):
            lineInfo.append(2)
        elif colour==(22,24,3):
            lineInfo.append(0)
    return line, lineInfo

def getStuff():
    known=[-1 for i in range(8)]
    antiKnown=[-1 for i in range(8)]
    valid=[str(i) for i  in range(10)]
    valid.append("*")
    valid.append("/")
    valid.append("-")
    valid.append("+")
    for i in range(6):
        line,info=getLine(i)
        print(line)
        if len(line)==8:
            lKnown=[]
            lAntiKnown=[]
            for j in range(8):
                if info[j]==1:
                    lAntiKnown.append(line[j])
                    lKnown.append(-1)
                elif info[j]==2:
                    lKnown.append(line[j])
                    lAntiKnown.append(-1)
                else:
                    if line[j] in valid:
                        valid.remove(line[j])
                    else:
                        print(line[j],"was not in valid")
                    lAntiKnown.append(-1)
                    lKnown.append(-1)
            for j in range(8):
                if lKnown[j]!=-1:
                    known[j]=lKnown[j]
                if lAntiKnown[j]!=-1:
                    antiKnown[j]=lAntiKnown[j]
    return known,antiKnown,valid

def getDigits(known,antiKnown):
    digits=[]
    for i in range(8):
        if known[i]!=-1:
            digits.append(known[i])
    for i in range(8):
        if antiKnown[i]!=-1 and antiKnown[i] not in digits:
            digits.append(antiKnown[i])
    for i in range(8-len(digits)):
        digits.append("x")
    return digits

def keyType(text):
    for char in text:
        keyboard.press_and_release(char)
        sleep(0.1)

#458,165,933,215,+60y for next line(55x55 squares+5 spacing)
def main():
    global q
    keyboard.press_and_release("alt+tab")
    sleep(0.1)
    keyType("48/6+1=9")
    sleep(0.1)
    keyboard.press_and_release("enter")
    keyType("2*5-7=03")
    sleep(0.1)
    keyboard.press_and_release("enter")
    sleep(0.1)
    complete=False
    while not complete:
        known,antiKnown,valid=getStuff()
        print(known,antiKnown,valid)
        if len(valid)>7:
            complete=True
            break
        counting=False
        lookingForAns=True
        foundValid=False
        #q=input("so far?")
        digits=getDigits(known,antiKnown)
        print(digits)
        q="".join(digits)
        #known=[-1 for i in range(8)]
        #antiKnown=[-1 for i in range(8)]
        #q="2*5-07=3"
        #q="48/6+1=9"
        perms=p.permute(q)
        #print(perms)
        print("perms genned")
        checked=0
        checkedpoint=0
        toCheck=len(perms)
        for stuff in perms:
            if stuff.count("x"):
                out=iterateRandoms("".join(stuff),valid)
                for check in out:
                        check = [digit for digit in check]
                        if outIfValid(check,known,antiKnown):
                            foundValid=True
                            keyType(check)
                            keyboard.press_and_release("enter")
            else:
                if outIfValid(stuff,known,antiKnown):
                    foundValid=True
                    keyType(stuff)
                    keyboard.press_and_release("enter")
            if foundValid and lookingForAns:
                break
            if counting:
                checked+=1
                if checked>checkedpoint:
                    print(round(checkedpoint//(toCheck//100)),"%")
                    checkedpoint+=toCheck/100

def iterateRandoms(toIterate,valid):
    values=[]
    bits=toIterate.split("x")
    for i in range(len(valid)**toIterate.count("x")):
        index=0
        used=0
        value=""
        for letter in toIterate:
            if letter =="x":
                value+=str(bits[used])
                value+=str(valid[(i//(len(valid)**(used)))%len(valid)])
                used+=1
            index+=1
        value+=str(bits[len(bits)-1])
        values.append(value)
    return values


if __name__=="__main__":
    main()