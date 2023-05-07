import math

# Requests user input for weight and height
user_weight = float(input("Please enter your weight in kg!:"))
user_height = float(input("Please enter your height in metres!: "))

_bmi = (user_weight) / ((user_height * user_height))  #Calculation for bmi = (weight/(height x height))
print(" ")
print(f"Your BMI is ", (round(_bmi , 2))) # Print bmi of user, rounded to 2 decimal places
print(" ")
if _bmi >= 30: # If bmi is equal to or greater than 30, print text
    print("You are obese, we recommend that you visit a dietician")
elif _bmi >= 25:  #If bmi is equal to or greater than 25, print text
    print("You are overweight")
elif _bmi >= 18.5:  #If bmi is greater than or equal to 18.5, print text
    print("You are within the normal range for BMI")
elif _bmi < 18.5:  #If bmi is less than 18.5, print text
    print("You are underweight, we recommend that you visit a dietician")

