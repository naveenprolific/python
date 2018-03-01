import os

with open("mydata.txt",encoding = "utf-8") as myfile:
    linenum = 1
    while True :
        
        line = myfile.readline().split()
        if not line :
            break
        print("line ",linenum,":",line,"word count :",len(line))
        charcount =0
        for word in line :
            for char in word:
                charcount+=1
        avgc = charcount/len(line)
        print('average count = {:.2f} '.format(avgc))
        
        linenum += 1
        
    


