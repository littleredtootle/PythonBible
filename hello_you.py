#Ask the user their name

name = input("Hi, what is your name?: ")

#Ask the user their age

age = input("What is your age?: ")

#Ask the user for city

city = input("What city do you live in?: ")

#Ask user what they enjoy

love = input("What do you love to do as a hobby?: ")

#Create output text

string = "Your name is {} and you are {} years old. You live in {} and you love {}."

output = string.format(name, age, city, love)

#Print output to screen

print(output)
