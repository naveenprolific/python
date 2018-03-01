
for i in range(int(input())):
	s= input()
	c1,c2=0,0
	last_symbol = None
	num_dots = 0
	for char in s:
		if char == '.':
			num_dots += 1
		else:
			if char == 'A':
				c1+=1
				if char == last_symbol:
					c1 += num_dots
			else:
				c2 += 1
				if char == last_symbol:
					c2 += num_dots
			last_symbol = char
			num_dots = 0
	print(c1, c2)
 


                    
                       
                
                    
                    
                        
                
                
        

