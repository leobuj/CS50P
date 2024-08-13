def goodbye():
    print("This is the conclusion of the program. Lesson 0 has been finished.")


# function with parameter "num" that returns its square, with a default value of 10
def square(num=10):
    return num * num


##################################
##################################
####### Strings and Inputs ####### 

# Ask user for name
name = input("What's your name? ")

# Removes any excess leading and trailing whitespace and capitilizes all names
name = name.strip().title()

# Say hello to user
print("Hello,", name)
# Different way of formatting
print(f"Hello, {name}!")



##################################
##################################
##### Floats and Formatting ###### 

# Asks user to input a number. Then converts the input to a float number.
x = float(input("What is the value of x: "))
y = float(input("What is the value of y: "))

# Adds x and y, and rounds it to the third decimal place
z = round(x+y, 3)

# Different styles of formatting
print("x + y = ", z)
print(f"x + y  = {z}")
print(f"x + y = {(x+y):.3f}")


# Calling a function you created
num = int(input("Please input a number to be squared: "))
print(square(num))

# Calling the function with no parameter passed, it uses its default value
print(square())

goodbye()