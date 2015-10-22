from easyGl import *
x=0
y=0

def draw():
	global x,y
	
	setColor(0, .5, .5)
	drawRect(x, y, 10, 10)
	x=x+1
	y=y+1
	
	
	
	
run (800,600, "bouncing ball", draw)
