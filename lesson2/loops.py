def main():

    # Loops allow us to be more scalable. This method isn't very scalable.
    print("meow")
    print("meow")
    print("meow")

    # Instead, we can do this.
    for i in range(3):
        print("meow")   

    # Also, let's introduce Lists
    mylist = [0, 1, 2,]
    # Lists are indexed by zero, and are simply a list of "things"

    # It can also allow us to dynamically choose it. We can choose how many times it should meow.
    # We can also have a sort of index counter      
    meowTimes = int(input("How many times should we meow?: "))
    for i in range(meowTimes):
        print(i,"meow")

    # Notice that range(x) returns a list [0,..,x]

    # Simple "pythonic" solution, if you do not intend to use the 'i', you
    # can simply just use an underscore.
    for _ in range(meowTimes):
        print("meow")



    # Loops are also real handy in ensuring you get the correct input from a user.
    while True:
        num = int(input("Please input a number greater than 0: "))
        if num <= 0:
            continue
        else:
            break
    # We will only escape this loop in the condition is met. 'Break' completely escapes it.
    # More efficient
    while True:
        n = int(input("Please input a number greater than 0: "))
        if n > 0:
            break

    
    # Let's make a function for meowing
    funct_num = get_num()
    meow(funct_num)



    # Lets handle some lists
    students = ["hermione", "harry", "ron"]
    # How do we specify which student to print? indexing.
    print(students[0])   # hermione
    print(students[1])   # harry
    print(students[2])   # ron 
    # Let's be more efficient
    for student in students:
        print(student)
    # We could also do it with some numbers instead.
    for i in range(len(students)):
        print(i+1, students[i])


    
    # Dictionaries.
    # Data structure that allows us to associate a value with another value
    # Key-value pairs.
    students_v2 = ["hermione", "harry", "ron", "draco"]
    houses = ["gryffindor", "gryffindor", "gryffindor", "slytherin"]
    # Maintaining this association is NOT scalable and not ideal, so we use a dict.

    students_dict = {
        "Hermione":"Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin",
    }
    # Dicts allow you to look into them via their keys
    print(students_dict["Hermione"])

    # Loop through efficiently..
    for student in students_dict:
        print(student, students_dict[student])


    # But what if we want to add more to these students? Like a patronus
    # More sophisticated solution
    students_v3 = [
        {
            "name": "hermione",
            "house": "gryffindor",
            "patronus": "otter",
        },
        {
            "name": "harry",
            "house": "gryffindor",
            "patronus": "stag",
        },
        {
            "name": "ron",
            "house": "gryffindor",
            "patronus": "jack russel terrier",
        },
        {
            "name": "draco",
            "house": "slytherin",
            "patronus": None
        }
    
    ]
    # students_v3 is a list of dictionaries

    for student in students_v3:
        print(student["name"], student["house"], student["patronus"])



    # Let's mess a little bit with some nested loops.
    # Build a square.

    print_square(3)




def meow(n):
    for _ in range(n):
        print("meow")

def get_num():
    while True:
        n = int(input("How many times should we meow: "))
        if n > 0:
            return n
        
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()