print("BMI CALCULATOR \n\n")

name = input("What is your name?  ")
print("\n")
print("Hello " + name + " Welcome to your personal BMI Calculator! \n\n")
age = input("How old are you, " + name + "? \n")

weight = input("What is your current weight in lb?\n")

height = input("How tall are you in inches?\n")



confirm = input("So you are " + age + " , weigh " + weight + " lbs " + ", and are " + height + " inches tall?:  Type 'yes' or 'no'\n")

height_sq = float(height)* float(height)
results = (float(weight) / float(height_sq)) * float(703)
if "yes":
    print("Here is your BMI")
    print(results)
