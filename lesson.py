# Which number do you want to check?

# 🚨 Don't change the code above 👆


# Write your code below this line 👇
def is_even(num):
    if num % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")


def task_1():
    number = int(input())
    is_even(number)


def task_2():
    height = float(input())
    weight = int(input())
    bmi = weight / (height**2)
    bmi_if = ""
    if bmi >= 35:
        bmi_if = ", you are clinically obese."
    elif bmi >= 30 and bmi < 35:
        bmi_if = ", you are obese."
    elif bmi >= 25 and bmi < 30:
        bmi_if = ", you are slightly overweight."
    elif bmi > 18.5 and bmi < 25:
        bmi_if = ", you have a normal weight."
    else:
        bmi_if = ", you are underweight."
    print(f"Your BMI is {bmi}" + bmi_if)


def task_3():
    year = int(input())
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")


def task_4():
    size = input()  # What size pizza do you want? S, M, or L
    add_pepperoni = input()  # Do you want pepperoni? Y or N
    extra_cheese = input()  # Do you want extra cheese? Y or N
    bill = 0
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    
    if add_pepperoni=="Y":
        if size == "S":
            bill += 2
        elif size == "M" or size == "L":
            bill += 3
    if extra_cheese=="Y":
        bill+=1
    print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}.")

def task_5():
    print("The Love Calculator is calculating your score...")
    name1 = input() # What is your name?
    name2 = input() # What is their name?
    score_1=0
    score_2=0
    for char in name1+name2:
        if char=="T" or char=="R" or char=="U" or char=="E" or char=="t" or char=="r" or char=="u" or char=="e":
            score_1+=1
    for char in name1+name2:
        if char=="L" or char=="O" or char=="V" or char=="E" or char=="l" or char=="o" or char=="v" or char=="e":
            score_2+=1
    if score_1*10+score_2<10 or score_1*10+score_2>90:
        print(f"Your score is {score_1}{score_2}, you go together like coke and mentos.")
    elif score_1*10+score_2<50 and score_1*10+score_2>40:
        print(f"Your score is {score_1}{score_2}, you are alright together.")
    else:
        print(f"Your score is {score_1}{score_2}.")
    
task_5()
