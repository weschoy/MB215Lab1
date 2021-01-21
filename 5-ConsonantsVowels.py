sInput=input("Enter any characters")
nVowels=0
nConsonants=0

for sVowels in sInput:
    if(sVowels=='a' or sVowels=='A' or sVowels=='e' or sVowels=='E' or sVowels=='i' or sVowels=="I" or sVowels=='o' or sVowels=='O' or sVowels=='u' or sVowels=='U'):
        nVowels=nVowels+1
    else:
        nConsonants=nConsonants+1
print("There are",nConsonants,"consonants and",nVowels,"vowels")

