MAX=100
numbers=[2,3,5,7,11,13,17]
words=["Fizz","Buzz","Bizz","Bozz","Boom","Fuzz","Fozz"]
if len(numbers)>len(words):
    print("you need more words")
elif len(numbers)<len(words):
    print("you need more numbers")
else:
    for x in range (1,MAX+1):
        output = ""
        for i in range(len(numbers)):
            if x%numbers[i]==0:
                output+=words[i]
        if output:
            print(output)
        else:
            print(x)