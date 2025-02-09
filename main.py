# Prints greeting message  to the console
print("Hello! My name is SoftwareChoreographer, and welcome to my Python basics")

# Today's Date: February 5, 2025
# Topic: Learning Variables in Python
# In this section, we will explore how to;
# 1. Assign and store values to variables
name = "SoftwareChoreographer"
age = 21

# 2. Print variable values
print("My name is " + name + " and I'm" , age ,"years old!")

# 3. How to assign a new value to an already existing variable
age = age + 1
print("Age:" , age)

# Task 1: Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time.
# Your task is to:
# 1. Create the variables: john, mary, and adam;
# 2. Assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
John = 3
Mary = 5
Adam = 6

# 3. Print the variables on one line, and separate each of them with a comma;
print("\nTask 1 Results: ")
print(John, Mary, Adam, sep=",")

# 4. Now create a new variable named total_apples equal to the addition of the three previous variables;
total_apples = John + Mary + Adam

# 5. Print the value stored in total_apples to the console;
print("Total Apples: ", total_apples)

# Task 2: Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:
# 1. miles to kilometers;
# 2. kilometers to miles.
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print("\nTask 2 Results: ")
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Task 3: Your task is to complete the code in order to evaluate the following expression:
# 3x3 - 2x2 + 3x - 1

x = -1 # Hardcode your test data here.
x = float(x)
# Write your code here.
y = 3 * (x ** 2) - 2 * (x ** 2) + 3 * x - 1

print("\nTask 3 Results: ")
print("y =", y)

# -------------------------------------------------------------------------------------------------------------
# Switching from Variables to User Input
# -------------------------------------------------------------------------------------------------------------
# Now that we've covered the basics of variables, let's learn how to read from the console using the input() function
print("\nLet's try the input() function!")

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# The input() function can do something else: it can prompt the user without any help from print().
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

# Type casting (type conversions)
print("\nUsing Input() to get numerical data: ")
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

#----------------------------------------------------------------------------------------------------
#END OF LESSON ONE
#----------------------------------------------------------------------------------------------------

# Today's Date: February 7, 2025
# Topic: String operators
# The + (plus) sign, when applied to two strings, becomes a concatenation operator:
print("\nConcatenation Example: ")
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# The * (asterisk) sign, when applied to a string and number (or a number and string, as it remains commutative in this position) becomes a replication operator:
print("\nReplication Example: ")
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# Task 1: Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
print("\nTask 1...")

# input a float value for variable b here
a = float(input("Enter a value: "))
# input a float value for variable b here
b = float(input("Enter a value: "))
# output the result of addition here
print("Addition: ", str(a+b))
# output the result of subtraction here
print("Subtraction: ", str(a-b))
# output the result of multiplication here
print("Muliplication:", str(a*b))
# output the result of division here
print("Division:", str(a/b))

print("\nThat's all, folks!")

# Task 2: Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
print("Task 2 Results: ")
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
# find a total of all minutes
mins = mins + dura
# find a number of hours hidden in minutes and update the hour
hour = hour + mins // 60
# correct minutes to fall in the (0..59) range
mins = mins % 60
# correct hours to fall in the (0..23) range
hour = hour % 24
print(hour, ":", mins, sep='')

