#choose your own adventure 
#by Olivia Tordoff
#9-17-15

hasDied = 0
hasHachet = 0
hasLolly = 0
inRoom="main" 
hasKey= 0 
opensecretdoor = 0 
hasEscaped= 0
hasSideGame= 0

while hasEscaped == 0 and hasDied == 0:
	if inRoom=="main":
	   print "you travel to a dark room."
	   print "there is a killer in the room, quick escape!"
	   print "1) move north"
	   print "2) move south"
	   print "3) move west"
	   print "4) move east"
		 
	   action=raw_input ("choose #1-4") 
	   action=int(action) 
	  
	   if action == 1:
		   inRoom = 'north'
	   if action == 2:
		   inRoom = 'south'
	   if action == 3:
		   inRoom = 'west'
	   if action == 4:
		   inRoom = 'east'
		   
	if inRoom=="west":
		print "you are in a haunted office building" 
		print "there is a small door in the far corner of the room"
		print "try to escape with out being seen by the demon and find a key."
		print "1) get key and move to main room" 
		print "2) move back to main room"
		print "3) open small door"
	   
	   
		action=raw_input ("choose #1-3") 
		action=int(action) 
		
		if action==1:
			inRoom="main"
			hasKey= 1
		if action==2:
			inRoom="main"
			hasKey= 0
			hasDied = 1
		if action==3:
			inRoom= "side"
			
	if inRoom== "side":
		print "there is a old grandma in the middle of the room."
		print "she is on her rocking chair" 
		print "she says 'whats brown and sticky'"
		print "1) poop"
		print "2) a stick"
		print "3) chocolate that has been in your pocket for 2 days"
		print "4) don't answer, go to main room"
		
		answer=raw_input ("choose #1-3")	
			
		if answer== 2:
			print "Correct"
			hasSideGame= 1
		if answer== 4:
			inRoom= "west"
		
	if inRoom=="north":
		print "you are in a old church with a blind murderer" 
		print "escape without bring heard by the blind man. Find a wepon."
		print "1) pick up a hatchet and move back to main room"
		print "2) grab a lolly pop and move back to main room"
					  
		action=raw_input ("choose #1-2") 
		action=int(action) 
			
		if action==1:
			inRoom="main"
			hasHachet = 1
		if action==2:
			inRoom="main"
			hasLolly=1
			hasDied = 1
	   
	if inRoom=="south":
		print "you are in a dark room that is soaked in blood." 
		print "try to find the lights."
		print "1) turn on lights, and move main room"
		print "2) move to main in the dark"
			
		action=raw_input ("choose #1-2") 
		action=int(action) 
			
		if action==1:
			inRoom="main"
		if action==2:
			hasDied = 1
	
	if inRoom=="east":
		print "you in an glass room, hannibal the cannibal wants you for lunch."
		print "open the locked door or kill him, but no matter what RUN!"
		print "1) you can kill hannibal if you picked up the hatchet from before."
		print "2) hide. "
		print "3) Unlock door." 

		action=raw_input ("choose #1-2") 
		action=int(action)
	
		if action==1: 
			inRoom="you killed hannibal and escape through the air vent."
			hasDied = 0 
			hasEscaped = 1
		if action==2:
			inRoom="hannibal found you, for dinner he is eating your liver, with some fava beans and a nice chianti"
			hasDied = 1
			hasEscaped = 0
		if action==3:
			inRoom="you unlock the door but hannibal is faster he catches you. For dinner he is eating your liver, with some fava beans and a nice chianti."
			hasDied = 1
			hasEscaped = 0
	 
if hasDied == 1:
	print "You lose"
if hasEscaped == 1:
	print "you win"	
	
	
