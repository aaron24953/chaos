import instantNerdle as iN
import permutations as p
outed=[]

def outIfValid(check,known):
    global q
    if iN.checkValidNerdle(check):
        notAns=False
        for i in range(len(check)):
            if str(check[i])!=str(known[i]) and known[i]!=-1:
                notAns=True
        if not notAns:
            if not "".join(check) in outed and len(q)==len(check):
                outed.append("".join(check))
                print("".join(check))
                return 1
    return 0

def main():
    global q
    counting=True
    lookingForAns=True
    foundValid=False
    #q=input("so far?")
    q="4*1=826/"
    #0,1,2,3,4,5,6,7,8,9,
    valid=[1,2,4,6,8,9,"/","*","+"]
    known=[-1 for i in range(8)]
    known[1]="*"
    known[4]=1
    #known[5]="="
    #known[6]=5
    #known[7]=7
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
                    if outIfValid(check,known):
                        foundValid=True
        else:
            if outIfValid(stuff,known):
                foundValid=True
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