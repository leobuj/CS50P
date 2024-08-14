# Basic studying of Python Conditionals

# Apparently good practice is to define your own main function:
def main():

    x = int(input("Give me a value for x: "))
    y = int(input("Give me a value for y: "))

    # Remember, indendation matters a lot. 
    if x > y:
        print(f"x is greater than y, with a difference of {x - y}.")
    elif x < y:
        print(f"y is greter than x, with a difference of {y - x}")
    else:
        print("x is the same number as y")

    print("Continuing conditional comparisons...")

    score = int(input("Please enter a student's score: "))

    # Python can do specific ranges in conditionals
    if 90 <= score <= 100:
        print ("Score is an A")
    elif 80 <= score < 90:
        print ("Score is a B")
    elif 70 <= score < 80:
        print ("Score is a C")
    else:
        print("Failure.")

    # Of course, we're being redundant here and checking a range.
    # Program efficiently by utilizing knowledge that the program learns.
    # If the current conditional contains a question already answered by
    # your current conditional, use that.
    if score >= 90:
        print ("Score is an A")
    elif score >= 80:
        print ("Score is a B")
    elif score >= 70:
        print("Score is a C")
    else:
        print("Failure.")

    


    # Determining even or odd is simple. % (modulo) operator is handy
    # X % Y results in the remainer after x has been divided by y
    print(f"10 % 4 is equal to {10%4}")

    # A number is only even is its remainder is zero after being divided by two.
    num = int(input("Please input a number to determine if its even or odd: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    # A function to determine even or oddness doesn't exist, let's make one.
    if is_evenV3(num):
        print("Even")
    else:
        print("Odd")



    # Match Keyword
    # Case by case basis essentially
    name = input("What is your name?: ")
    if(name == "Harry"):
        print("Gryffindor")
    elif(name == "Hermione"):
        print("Gryffindor")
    elif(name == "Ron"):
        print("Gryffindor")
    elif(name == "Draco"):
        print("Slytherin")
    else:
        print("Who?")

    # Improved with match
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")


# Very straightforward
def is_evenV1(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
# Pythonic expression method
def is_evenV2(num):
    return True if num % 2 == 0 else False

# Most succint method
def is_evenV3(num):
    return (num % 2 == 0)


main()