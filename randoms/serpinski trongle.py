import turtle as t
import math as m
import random as r
def dot():
    t.dot(2,"black")

width=1000
height=1000
offset=10
t.setworldcoordinates(0,0,width,height)
t.pu()
t.ht()
t.speed(0)
ax=offset
ay=offset
t.setpos(ax,ay)
dot()
bx=width-offset
by=offset
t.setpos(bx,by)
dot()
cx=width/2
cy=m.sqrt((width-offset*2)**2-((width-20)/2)**2)
t.setpos(cx,cy)
dot()
i=0
while True:
    i+=1
    pos=t.pos()
    genint=r.randint(0,3)
    if genint==0:
        t.setpos((pos[0]+ax)/2,(pos[1]+ay)/2)
        dot()
    elif genint==1:
        t.setpos((pos[0]+bx)/2,(pos[1]+by)/2)
        dot()
    elif genint==2:
        t.setpos((pos[0]+cx)/2,(pos[1]+cy)/2)
        dot()
    if i%1000==0:
        print(i)