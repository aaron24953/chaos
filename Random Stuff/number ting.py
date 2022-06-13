from random import randint
maxScore=0
got=False
while got!=True:
    score=0
    for i in range(5):
        rolla=randint(2,6)
        rollb=randint(2,6)
        score+=rolla
        score+=rollb
        if rolla == rollb:
            score+=randint(2,6)
        if (rolla+rollb)%2==0:
            score+=10
        else:
            score-=5
    if score>=maxScore:
        maxScore=score
        print(score)
        if score==140:
            got=True