from permutations import permute

def calc(toCheck,operand,i):
    temp=toCheck
    a=int(toCheck[i-1])
    try:
        if i-2>=0:
            a+=10*int(toCheck[i-2])
        try:
            if i-3>=0:
                a+=100*int(toCheck[i-3])
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
            b=10*int(toCheck[i+2])
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
            if a//b==a/b:
                value=a//b
            else:
                return "False"
        except:
            return "False"
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
    #print(toCheck)
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
    known=[-1 for i in range(8)]
    question="62=+9/71"
    known[0]=6
    question=[i for i in question]
    perms=permute(question)
    ans="no ans"
    for i in perms:
        if checkValidNerdle(i):
            pAns="".join(i)
            isAns=True
            for j in range(len(pAns)):
                if pAns[j]!=str(known[j]) and known[j]!=-1:
                    isAns=False
            if isAns:
                ans=pAns
            print(pAns)
    print(ans,"is ans")
        
if __name__ == "__main__":
    main()
