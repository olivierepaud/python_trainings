#loops definition

def main():
    print("\ntest of a \"while\" loop")
    x= 0
    while (x < 5):
        print(x)
        x= x+1

    print("\ntest of a \"for\" loop with range 5 to 10")
    for x in range(5,10):
        print(x)

    print("\ntest of a \"for\" loop with range only one digit 4")
    for x in range(4):
        print(x)

    print("\ntest of a loop on a collection")
    days=["Mon","Tue","Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    print("\ntest of the break statement in a loop")
    for y in range(5,10):
        if (y == 7): break
        print(y)


    print("\ntest of the continue statement in a loop")
    for y in range(5,10):
        if (y % 2 == 0): continue
        print(y)

    print("\nusing the enumerate() function")
    days=["Mon","Tue","Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):
        print(i,d)


#execution
if __name__ == "__main__":
    main()
