# 1.Simple Message: Assign a message to a variable, and then print that message.


assign="Albert Einstein once said, “A person who never made a mistake never tried anything new.”"
print(assign)


# Calculate Area of a Circle::

radius=float(input("Enter the radius of circle"))
area_of_circle=radius*3.143
print(f"Area of the circle having radius {radius} is" , area_of_circle)

# Check Number either positive, negative or zero::

value=int(input("Enter the value to check whether it is positive or negative or zero"))

if value < 0:
    print(f"Negative number Entered {value} ")
elif value >0:
    print(f"Positive number Entered {value}")
elif value == 0:
    print(f"zero Entered {value}")
else:
    print("Error in your mind :)")


# Vowel Tester Write a Python program to test whether a passed letter is a vowel or not

vowel=input("Enter variable to check either it is vowel or not ")
if(vowel == "a" or vowel=="A") or (vowel=="e" or vowel=="E") or (vowel=="i" or vowel=="I") or (vowel=="o" or vowel=="O") or (vowel=="u" or vowel=="U"):
    print(f"Letter {vowel} is a vowel")
else:
    print("Entered letter is not vowel")

# BMI Calculator

height=int(input("Enter height in cm"))
weight=int(input("Enter weight in KG"))

bmi=(weight/pow(height,2))*pow(100,2)
print(f"Your bmi is {bmi}")

# Store the names of a few of your friends in a list called names

# Print each person’s name by accessing each element in the list, one at a time.

list=["huzaifa", "mawahid" , "raza" , "furqan"]
for list1 in list:
    print(list1)


# Start with the list you used in Question 4, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

for lists in list :
    if lists == "huzaifa":
        print(f"Have a good day {lists}")
    elif lists == "mawahid":
        print(f"Have a Good day {lists}")
    elif lists == "raza":
        print(f"Have a Good day {lists}")
    elif lists == "furqan":
        print(f"Have a Good day {lists}")
    else:
        print("no name found")


# 10.Make a python program that conatains your nine favourite dishes in a list called foods. Print the message, The first three items in the list are:

# Then use a slice to print the first three items from that program’s list.

# Print the message, Three items from the middle of the list are:

# Use a slice to print three items from the middle of the list.

# Print the message, The last three items in the list are:

# Use a slice to print the last three items in the list.


foods = ["biryani" , "haleem" , "tiqqa" , "brosat" , "burger" , "pasta" ,"pizza" ,"mandi ", "nihari" ]
food1=[]
food2=[]
food3=[]
print("the first three items in the list are:" ,foods[0] + " " + foods[1] +" " + foods[2])
print(foods[:3])

print("the middle three items in the list are:" ,foods[3] + " " + foods[4] +" " + foods[5])
print(foods[3:6])

print("the last three items in the list are:" ,foods[6] + " " + foods[7] +" " + foods[8])
print(foods[6:9])



# Start with your program from your last Question8. Make a copy of the list of foods, and call it friend_foods. Then, do the following:
# Add a new dish to the original list.

# Add a different dish to the list friend_foods.

# Prove that you have two separate lists.

# Print the message, My favorite pizzas are: and then use a for loop to print the first list.

# Print the message,

# My friend’s favorite foods are:, and then use a for loop to print the second list.

# NOTE: Make sure each new dish is stored in the appropriate list.


friend_foods=foods.copy()
foods.append("zinger")
friend_foods.append("quorma")
print("This is original list" , foods)
print("This is coppied list" ,friend_foods )
