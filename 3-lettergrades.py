#input
print("Enter percentage as a number")
n=int(input())

if n in range(0,101):

    if n<50:
        print("You failed")
    elif n>=90:
        print("A+")

else:
    print("Not applicable")

