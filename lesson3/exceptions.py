# Ocasionally, you will face syntax errors
# These are must fixes, the code will not compile otherwise.
# e.g., print("hello world"
# will give an "error: unterminated string literal"

# But there can also be run-time errors that can occur from faulty or bad input
# e.g., 
# x = int(input("What is x?: "))
# print(f"x is {x})
# If a user inputs a number, nothing is wrong. But what happens if a user doesn't input it?
# "error: ValueErrorL invalid lietral for int() with base 10: 'cat'"

# Write some code with some error handling!

def main():


    # We try something, anything in this chunk of code.
    try:
        x = int(input("What is X?: "))
        # Make sure to print only if x gets defined. If the error gets caught, x is not defined and will print error.
        print(f"x is {x}")
    except ValueError:
    # Here, we catch any errors that we expect and prevent code from crashing out.
        print("x is not an integer!!")

    
    # But lets be more friendly.
    # Give the user a chance to fix their mistake.
    # Loop!

    while True:
        try:
            x = int(input("What is X? "))
        except ValueError:
            print("X isn't an integer!")
        else:
            # Excape the loop with break!
            break           
    print(f"x is {x}")


    # Be more efficient, no need to have an else statement.
    while True:
        try:
            x = int(input("What is X? "))
            break
        except ValueError:
            print("X isn't an integer!")

    print(f"x is {x}")

    # Now let's use the function we wrote to be efficient about it
    # Abstraction !

    get_intv1()

    get_intv2("What is x?")


def get_intv1():

    while True:
        try:
            x = int(input("What is X? "))
        except ValueError:
            print("X isn't an integer!")
        else:
            # Excape the loop with break!
            break           
    return x

# improved version 
def get_intv2(prompt):

    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            pass


main()