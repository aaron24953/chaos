from permutations import permute

def calc(toCheck,operand,i):
    temp=toCheck
    a=int(toCheck[i-1])
    try:
        if i-2>=0:
            a+=10*int(toCheck[i-2])
    except:
        pass
    b=int(toCheck[i+1])
    try:
        b=10*int(toCheck[i+1])
        b+=int(toCheck[i+2])
    except:
        b=int(toCheck[i+1])
    #print(a,toCheck,b)
    if operand=="*":
        value=a*b
    elif operand=="/":
        value=a//b
    elif operand=="+":
        value=a+b
    else:
        value=a-b
    toCheck="".join([temp[j] for j in range(0,i-len(str(a)))])
    toCheck+=str(value)
    toCheck+="".join([temp[j] for j in range(i+len(str(b))+1,len(temp))])
    return toCheck

def checkCalc(toCheck):
    bothSides=toCheck.split("=")
    toCheck=bothSides[0]
    for i in range(len(toCheck)):
        if toCheck[i] == "*":
            toCheck=calc(toCheck,toCheck[i],i)
            break
    for i in range(len(toCheck)):
        if toCheck[i] == "/":
            toCheck=calc(toCheck,toCheck[i],i)
            break
    for i in range(len(toCheck)):
        if toCheck[i] == "+":
            toCheck=calc(toCheck,toCheck[i],i)
            break
    for i in range(len(toCheck)):
        if toCheck[i] == "-":
            toCheck=calc(toCheck,toCheck[i],i)
            break
    if toCheck==bothSides[1]:
        return True
    return False

def checkValidNerdle(toCheck):
    eq=0
    for i in toCheck:
        if i!="=":
            eq+=1
        else:
            break
    if eq<len(toCheck)-3 or eq==len(toCheck)-1:
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
                
def main():
    stuff="75*=34-8"
    stuff=[i for i in stuff]
    perms=permute(stuff)
    for i in perms:
        if checkValidNerdle(i):
            print("".join(i))
        
if __name__ == "__main__":
    main()
