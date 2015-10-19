from easyGL import *
    
def draw(): 
  setColor(1, 1, 0)                          
  drawRect(10, 10, 10, 10)
  setColor(1, 1, 0)                          
  drawRect(20, 20, 40, 20)
  setColor(1, 1, 0)                          
  drawRect(60, 10, 10, 10)
  setColor (1, 1, 0)
  drawRect (45,30,20,25)
  setColor (0,0,1)
  drawRect (60,23,3,3)
  setColorA (0,.5,.5,.3)
  drawRect (60,10, 300,300)
  
run(800, 600, "Mr McDonley's Awesome Example", draw)
