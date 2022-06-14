numDigits=4
length=127-33
oa=[]
numI=length**numDigits
perN=0
perNP=3#2=%
counterD=10**perNP
for i in range(numI):
    o=""
    for j in range(numDigits):
        o+=chr((i//(length**j))%length+33)
    print(o,i,"/",numI,end="\r")
    """
    if i>=numI*perN/counterD:
        print(perN,"/",counterD,end="\r")
        perN+=10**(2-perNP)
        perN=round(perN,perNP-2)
    """
    #oa.append(o)
#print(oa)