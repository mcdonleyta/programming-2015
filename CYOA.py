inRoom = "Main"
hasSword = 0
hasEscaped = 0

while hasEscaped == 0:
	if inRoom == "Main":
		print "You are in a scary warehouse." 
		print "Try to escape!"
		
		print "1.) Move North"
		print "2.) Move South"
		print "3.) Move West"
		print "4.) Move East"
		
		action = raw_input("choose #1-4")
		action = int(action)
		
		if action == 1:
			inRoom = "North"
		if action == 2:
			inRoom = "South"
		if action == 3:
			inRoom = "West"
		if action == 4:
			inRoom = "East"
			
	if inRoom == "East":
		print "There is a door to your right, try to open it."
		print "Its locked, you need something powerful to blow it open."
		
		print "1.) Move North"
		print "2.) Move South"
		print "3.) Move West"
		print "4.) Move Main"
		
		action = raw_input("choose #1-4")
		action = int(action)
		
		if action == 1:
			inRoom = "North"
		if action == 2:
			inRoom = "South"
		if action == 3:
			inRoom = "West"
		if action == 4:
			inRoom = "Main"
			
	if inRoom == "South":
		print "There is a magic sword to your right."
		print "There is also a locked door to your right."
		
		print "1.) pick up sword"
		print "2.) move to the main room"
		
		action = raw_input("choose #1-2")
		action = int(action)
		
		if action == 1:
			has_sword = "1"
		if action == 2:
			inRoom = "Main"
			
	if inRoom == "Main":
		print "1.) move North"
		print "2.) move West"
		
		action = raw_input("choose #1-2")
		action = int(action)
		
		if action == 1:
			inRoom = "West"
		if action == 2:
			inRoom = "North"
			
	if inRoom == "West":
		print "There is nothing in this room, just dust and spiderwebs."
		
		print "1.) move to the main room"
		
		action = raw_input("choose #1")
		action = int(action)
		
		if action == 1:
			inRoom = "Main"
	
	if inRoom == "Main":
		print "Try your sword on the door."
		print "The door is still not opening."
		
		print "1.) go back to main and search for enchantment"
		print "2.) keep trying"
		
		action= raw_input("choose #1-2")
		action = int(action)
		
		if action == 1:
			inRoom = "Main"
		if action == 2:
			inRoom = "North"
		
	if inRoom == "Main":
		print "See that, there is a sparkling piece of metal to your left."
		print "Go see what it is."
		
		print "1.) go check out the piece of metal"
		print "2.) keep looking"
		
		action = raw_input("choose #1-2")
		action = int(action)
		
		if action == 1:
			print "There is an enchatment in this secret hatch, hmm.. convenient."
		if action == 2:
			inRoom = "Main"
			
	if inRoom == "Main":
		print "You now have an enchanted magic sword, go check and see if you can unlock the door."
		
		print "1.) move North"
		
		action = raw_input("choose #1")
		action = int(action)
		
		if action == 1:
			inRoom = "North"
			
	if inRoom == "North":
		print "See if your sword is powerful enough to open the door."
		
		print"1.) open the door"
		
		action = raw_input("choose #1")
		action = int(action)
		
		if action == 1:
			print "you have opened the door" 
			print "you win!"
			hasEscaped = 1
