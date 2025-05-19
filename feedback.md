The feedback I received was for Practical4, variables.py.
The feedback was that while the times are compared for c and f, it is done manuallly rather that using a boolean funciton.
So I added a boolean function to compare the two variables. 
compare = c < f #compare c with f
print("Is bus faster than car?", compare) #print the result

if compare: #make a conclusion
    print("Conclusion: Bus is faster")
else:
    print("Conclusion: Car is faster or equal")
#bus is faster