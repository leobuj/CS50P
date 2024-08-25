def main():
    hello("world")
    goodbye("world")


def hello(name):
    print("hello,", name)

def goodbye(name):
    print("goodbye,", name)


# Prevents main from running if it isn't directly from this file. 
if __name__ == "__main__":
    main()