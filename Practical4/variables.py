# 4.1
a=15 #walk to the bus stop
b=75 #bus journey
c=a+b #total 1
d=90 #drive
e=5 #parking
f=d+e #total 2
print("bus:",c,"minutes")
print("car:",f,"minutes")
#bus:90minutes car:95minutes 
compare = c < f #compare c with f
print("Is bus faster than car?", compare) #print the result

if compare: #make a conclusion
    print("Conclusion: Bus is faster")
else:
    print("Conclusion: Car is faster or equal")
#bus is faster
# 4.2
X=True
Y=False
for X in [True,False]:
    for Y in [True,False]:
        W=X and Y
        print("X =",X,"Y =",Y,"W =",W)
#X = True, Y = True, W = True
#X = True, Y = False, W = False
#X = False, Y = True, W = False
#X = False, Y = False, W = False