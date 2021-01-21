try:
    #input
    print("What is the distance in kilometre?")
    nKilometres=int(input())

    #processing
    nMiles=nKilometres*0.6214

    #output
    print("The distance in miles is",nMiles)

except:
    print("Please enter a number")

