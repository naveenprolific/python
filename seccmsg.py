   
msg = input("enter the message :")
key = int(input("enter the characters to shift (1 to 26):"))
secmsg = ""
for i in msg:
    if i.isalpha():
        charcode = ord(i)
        charcode += key
        if i.isupper():
            if charcode> ord('Z') :
                charcode -=26

            if charcode< ord('A') :
                charcode +=26
            
        else :
            if charcode> ord('z') :
                charcode -=26

            if charcode< ord('a') :
                charcode +=26
        secmsg += chr(charcode)
    else:
        secmsg += i

print("encrypted ====>",secmsg)
key = -key
orgmsg = ""
for i in secmsg:
    if i.isalpha():
        charcode = ord(i)
        charcode += key
        if i.isupper():
            if charcode> ord('Z') :
                charcode -=26

            if charcode< ord('A') :
                charcode +=26
            
        else :
            if charcode> ord('z') :
                charcode -=26

            if charcode< ord('a') :
                charcode +=26
        orgmsg += chr(charcode)
    else:
         orgmsg += i

        
print("decrypted ====>",orgmsg)
    

    
    


          
