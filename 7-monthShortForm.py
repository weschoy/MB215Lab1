dictMonths={"January":"Jan","February":"Feb","March":"Mar","April":"Apr","May":"May","June":"Jun","August":"Aug","September":"Sept","October":"Oct","November":"Nov","December":"Dec"}
def getAbbreviations(sMonthAbbrev):
    global dictMonths
    return dictMonths[sMonthAbbrev]

try:
    sMonth=input("Please enter a month. First letter is capitalized:")
    sAbbreviation=getAbbreviations(sMonth)
    print("The abbreviation of",sMonth,"is",sAbbreviation)

except:
    print("Please enter a proper month with a capitlized first letter")