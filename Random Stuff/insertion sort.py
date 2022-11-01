# insertion sort

from random import randint


myArray = [randint(0 * i, 10) for i in range(10)]

print(myArray)

for i in range(1, len(myArray)):
    val = myArray[i]
    j=i-1
    while j>=0:
        if myArray[j]>val:
            myArray[j+1]=myArray[j]
            j-=1
        else:
            myArray[j+1]=val
            j=-10
        if j == -1:
            myArray[0]=val


    print(myArray)
