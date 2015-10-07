inRoom = "Main"
hasSword = 0
hasEscaped = 0
hasSecretRoom = 0

while hasEscaped == 0:
	if inRoom == "Main":
		print "you are in a scary warehouse." 
		print "try to escape"
		
		print "1.) Move North"
		print "2.) Move South"
		print "3.) Move West"
		print "4.) Move East"
		print "5.) Move Secret"
		
		action = raw_input("choose #1-5")
		action = int(action)

		if action == 1:
			inRoom = "North"
		if action == 2:
			inRoom = "South"
		if action == 3:
			inRoom = "West"
		if action == 4:
			inRoom = "East"
		if action == 5: 
			inRoom = "Secret"
		
	if inRoom == "Secret": 
		print "What occurs once in a minute, twice in a moment, and never in one thousand years?"
		
		print "1.) an eclipse"
		print "2.) M"
		print "3.) the apocalypse"
		print "4.) move to main room"
		
		action = raw_input("choose #1-4")
		action = int(action)
		
		if action == 1:
			print "incorrect"
		if action == 2:
			print "correct"
			hasSecretRoom == 1
		if action == 3:
			print "incorrect"
		if action == 4:
			inRoom = "Main"
		
	if inRoom == "East":
		print "there is a door to your right, try to open it"
		print "its locked, you need something powerful to blow it open"
		
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
		print "there is a magic sword to your right"
		print "there is also a locked door to your right"
		
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
		print "there is nothing in this room, just dust and spiderwebs."
		
		print "1.) move to the main room"
		
		action = raw_input("choose #1")
		action = int(action)
		
		if action == 1:
			inRoom = "Main"
	
	if inRoom == "Main":
		print "try your sword on the door"
		print "the door is still not opening"
		
		print "1.) go back to main and search for enchantment"
		print "2.) keep trying"
		
		action= raw_input("choose #1-2")
		action = int(action)
		
		if action == 1:
			inRoom = "Main"
		if action == 2:
			inRoom = "North"
		
	if inRoom == "Main":
		print "see that, there is a sparkling piece of metal to your left"
		print "go see what it is"
		
		print "1.) go check out the piece of metal"
		print "2.) keep looking"
		
		action = raw_input("choose #1-2")
		action = int(action)
		
		if action == 1:
			print "there is an enchatment in this secret hatch, hmm.. convenient"
		if action == 2:
			inRoom = "Main"
			
	if inRoom == "Main":
		print "you now have an enchanted magic sword, go check and see if you can unlock the door"
		
		print "1.) move North"
		
		action = raw_input("choose #1")
		action = int(action)
		
		if action == 1:
			inRoom = "North"
			
	if inRoom == "North":
		print " see if your sword is powerful enough to open the door"
		
		print"1.) open the door"
		
		action = raw_input("choose #1")
		action = int(action)
		
		if action == 1:
			print "you have opened the door" 
			print "you win!"

hasEscaped = 1


if hasSecretRoom == 1:
	print ":)"
	
