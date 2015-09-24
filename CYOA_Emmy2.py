inRoom="main"
hasKey=0
haskilledslaughters= 0
hasknife= 0 
hasdied=0

while haskilledslaughters < 6 and hasdied==0:
    if inRoom == "west":
        print "you travle to a dark, musky, humid, room, contaning two slaughters"
        print "there is a knife on the ground"
    
        print
        print "1) move into main room" 
        print "2) pick up knife" 
        print "3) attack slaughters" 
        print
        
        action=raw_input("choose #1-2:")
        action=int(action)
        
        if action== 1:
            inRoom= "main"
        if action== 2:
            hasknife = 1
        if action == 3:
            if hasknife == 1:
                print "attack slaughters and sucsesfully kill them"
                haskilledslaughters = haskilledslaughters + 1
            if hasknife == 0:
				print "attack slaughters and get killed"
				hasdied = 1
                
    if inRoom=="east": 
        print "you are in the east room and are faced with one slaughter" 
       
        print
        print "1) move into main room"  
        print "2) attack slaughter" 
        print
        
        action=raw_input("choose #1-2:")
        action=int(action)
        
        if action== 1:
            inRoom= "main"
        if action == 2:
            if hasknife == 1:
                print "attack slaughters and sucsesfully kill them"
                haskilledslaughters = haskilledslaughters + 1
            if hasknife == 0:
				print "attack slaughters and get killed"
				hasdied = 1
				
    if inRoom == "north" :
        print "you move from the main room to the north room"
        print "there is one slaughter in the middle of the room carying a ax"
        print "he is one foot taller than you and has hands the size of your face"
        
        print
        print "1) move into main room"  
        print "2) attack slaughter" 
        print
        
        action=raw_input("choose #1-2:")
        action=int(action)
        
        if action== 1:
            inRoom= "main"
        if action == 2:
            if hasknife == 1:
                print "attack slaughters and sucsesfully kill them"
                haskilledslaughters = haskilledslaughters + 1
            if hasknife == 0:
				print "attack slaughters and get killed"
				hasdied = 1
				
    if inRoom == "south":
        print "there is one slaughter in the back right coner of the room"
        print "you start walking toward it and another slaughter comes up behind you"
        print "now you are in between two slaughters, the only thing you are thinking is don't die"
        
        print
        print "1) move into main room"  
        print "2) attack slaughters" 
        print
        
        action=raw_input("choose #1-2:")
        action=int(action)
        
        if action== 1:
            inRoom= "main"
        if action == 2:
            if hasknife == 1:
                print "attack slaughters and sucsesfully kill them"
                haskilledslaughters = haskilledslaughters + 1
            if hasknife == 0:
				print "attack slaughters and get killed"
				hasdied = 1

    if inRoom=="main":
        print "you are lost in a warehouse with slaughters. try to kill all of them and not to die"
    
        print
        print "1) move north"
        print "2) move south"
        print "3) move east"
        print "4) move west"
        print
        
        action=raw_input("choose #1-4:")
        action=int(action)
        
        if action== 1:
            inRoom= "north"
        if action== 2:
            inRoom= "south"
        if action== 3:
            inRoom= "east"
        if action== 4:
            inRoom= "west"

if haskilledslaughters >= 6: 
	print "You killed all the slaughteres"
	print "you win"
if hasdied == 1 :
	print "you lose"
