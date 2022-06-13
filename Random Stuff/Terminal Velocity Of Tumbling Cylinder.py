import math
PI=3.14159265358979323846
g=9.807
Sd=1102
e=1.225
L=float(input("Length?"))
D=float(input("Diameter?"))
A=((L*D)+(PI*(D/2)*(D/2)))/2
m=Sd*PI*(D/2)*(D/2)*L
Cd=2*(1+(PI*PI*(L+D))/(6*(4*L+PI*D))*(D/2))
V=math.sqrt((2*m*g)/(Cd*e*A))
print(V)