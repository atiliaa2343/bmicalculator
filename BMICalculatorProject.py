print("Welcome to the BMI calculator") 
height = float(input("enter your height in m: ")) 
weight = float(input('enter your weight in kg: '))

bmi = round(weight /height ** 2) 

if bmi < 18.5: 
    print("Your bmi is {0}, and you are underweight.".format(bmi))
elif bmi < 25: 
    print("Your bmi is {0}, and you have a normal weight.".format(bmi)) 
elif bmi < 30: 
    print("Your bmi is {0}, and you are overweight.".format(bmi)) 
elif bmi < 35: 
    print("Your bmi is {0}, and you are overweight.".format(bmi)) 
else: 
    print("Your bmi is {0}, and you are clinically obese".format(bmi))