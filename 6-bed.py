def decodeLetterFromNumber(nLetter):
    aAlphabet="abcdefghijklmnopqrstuvwxyz"
    return aAlphabet[nLetter-1]

sInput=input("Please enter a string of code")

sOutput=""
for sDigit in sInput.split(","):
    sOutput=sOutput+decodeLetterFromNumber(int(sDigit))
print(sOutput)
