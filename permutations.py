from factorial import factorial as fact
def permute(array):
    print(array)
    leng=len(array)
    facts=[fact(i) for i in range(leng)]
    perms=[]
    print(leng**leng)
    for i in range(leng**leng):
        pPerm=[]
        valid=True
        indexes=[]
        for j in range(leng):
            index=i//(leng**j)%leng
            add=array[index]
            if not index in indexes:
                indexes.append(index)
                pPerm.append(add)
            else:
                valid=False
                break
        if valid:
            perms.append(pPerm)
    return perms
