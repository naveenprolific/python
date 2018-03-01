string = input("enter a string in uppercase :")
secstring = ""

for i in string:
     secstring += str(ord(i))
print(secstring)
string = ""
for i in range(0,len(secstring)-1,2):
    charcode  = secstring[i]+secstring[i+1]

    string += chr(int(charcode)+32)
print(string)


