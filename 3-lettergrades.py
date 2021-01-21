#input
print("Enter percentage as a number")
n=int(input())

if n in range(0,101):

    if n<50:
        print("You failed")
    elif n>=90:
        print("A+")
    elif n in range(50,60):
        if n<53:
            print("D-")
        elif n>56:
            print("D+")
        else:
            print("D")
    elif n in range(60,70):
        if n<63:
            print("C-")
        elif n>66:
            print("C+")
        else:
            print("C")
    elif n in range(70,80):
        if n<73:
            print("B-")
        elif n>76:
            print("B+")
        else:
            print("B")
    elif n in range(80,90):
        if n<=84:
            print("A-")
        else:
            print("A")
else:
    print("Not applicable")

