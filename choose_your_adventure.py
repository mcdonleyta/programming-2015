inRoom = "main" 
useToilet = "use toilet"
hasEscaped = 0 
hasKnife = 0
westZombieAlive = 1
 
while hasEscaped == 0: 
	if inRoom == "west": 
		print "You have traveled to an old dining room." 
		if westZombieAlive == 1:
			print "There is a zombie in the corner coming towards you." 
		  
		print "1) Main Room"
		if westZombieAlive == 1: 
			print "2) Attack zombie" 
		  
		action = raw_input("choose #: ") 
		action = int(action) 
		  
		if action == 1: 
			inRoom = "main" 
		if action == 2 and westZombieAlive == 1: 
			if hasKnife == 1:
				print "You have killed the zombie."
				westZombieAlive = 0
			else:
				print "You need a knife to kill the zombie. You have a bad cut on the side of your face."
	 
	if inRoom == "east":
		print "You have entered a dusty bathroom with an old toilet." 
		  
		print "1) Main Room"
		print "2) Sit on toilet."
		  
		action = raw_input("choose #1-2: ") 
		action = int(action) 
		  
		if action == 1: 
			inRoom = "main" 
		if action == 2:
			useToilet = "use toilet"
	 
	if inRoom == "north": 
		print "It looks like this used to be a kitchen." 
		print "There is a knife on the ground."

		print "1) Main Room" 
		print "2) Pick up knife"
		  
		action = raw_input("choose #1-2: ") 
		action = int(action) 
		  
		if action == 1: 
			inRoom = "main" 
		if action == 2:
			hasKnife = 1
			print "You now have a knife."
			
	if inRoom == "south": 
		print "There is a huge zombie guarding a door here." 
		  
		print "1) Main Room" 
		print "2) Open door" 
		print "3) Attack zombie"
		  
		action = raw_input("choose #1-3: ") 
		action = int(action) 
		  
		if action == 1: 
			inRoom = "main" 
		if action == 2:  
			print "You have to kill the zombie first!" 
			print "You have been attacked and now have a gash in your gut" 
		if action == 3:
			print "You have killed the zombie. You can now get to the door."
	  
			print "1) Main Room"
			print "2) Open door"
			
			action = raw_input("choose #1-2: ")
			action = int(action)
			
			if action == 1:
				inRoom = "main"
			if action == 2:
				print "You have successfully escaped!"
				print "You win!"
				hasEscaped = 1
	  
	if inRoom == "main": 
		print "You are in a scary warehouse." 
		print "Try to escape if you can!" 
		  
		print "1) Move North" 
		print "2) Move South" 
		print "3) Move West" 
		print "4) Move East" 
		  
		action = raw_input("choose #1-4: ") 
		action = int(action) 
		  
		if action == 1: 
			inRoom = "north" 
		if action == 2: 
			inRoom = "south" 
		if action == 3: 
			inRoom = "west" 
		if action == 4: 
			inRoom = "east" 