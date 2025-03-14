weight=float(input("please input your weight(kg):")) #get the person's weight
height=float(input("please input your height(m):")) #get the person's height
BMI=weight/(height**2) #calculate the value of BMI with the formula
if BMI<18.5: #decide which category the person's BMI is
    category="underweight"
if BMI>30:
    category="obese"
else:
    category="healthy"
print("The value of your BMI is:",BMI,",Your are",category) #output the result