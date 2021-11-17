#Conditions

def main():
    x,y=10,100
    if (x<y):
        st="x is less than y"
    elif (x==y):
        st="x and y are equal"
    else:
        st="x is greater than y"
    print(st)

    st2="x is less than y" if (x<y) else "x is greater or equal to y" 
    print(st2)


#execution
if __name__ == "__main__":
    main()
