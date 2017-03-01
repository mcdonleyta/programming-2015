from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 500, 400                               # window size

def switch3D():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0,float(width)/float(height),1,1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()                                   # reset position

    glEnable(GL_DEPTH_TEST)                            

def switch2D():
    global width, height
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -10, 10)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()                                   # reset position

    glDisable(GL_DEPTH_TEST)                            #Disable so alpha blending works



def drawColor(r, g, b):
    drawColorA(r,g,b,1)

def drawColorA(r, g, b, a):
    glColor4f(r,g,b,a)
    
def drawRect(x, y, w, h):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x+w, y)
    glVertex2f(x+w, y+h)
    glVertex2f(x, y+h)
    glEnd()
    

def resize(w, h):
    global width, height
    
    glViewport(0, 0, w, h) 
    width = w
    height = h
        
def draw():                                            # ondraw is called all the time
    global xrot
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    
    #draw 2D stuff
    switch2D()

    #Squares
    glBegin(GL_QUADS)
    glColor4f(1,0,0,1)
    glVertex2f(0, 0)
    glVertex2f(50, 0)
    glVertex2f(50, 50)
    glVertex2f(0, 50)
    glEnd()

    #Points / Squares
    glPointSize(50)
    glBegin(GL_POINTS)
    glColor4f(0, 1, 0, 0.5)
    glVertex2f(50,50)
    glEnd()

    #Lines
    glLineWidth(10)
    glBegin(GL_LINES)
    glColor4f(0, 0, 1, 0.5)
    glVertex2f(0,0)
    glVertex2f(100,0)

    glVertex2f(100,0)
    glVertex2f(100,100)

    glVertex2f(100,100)    
    glVertex2f(0,0)
    glEnd()
    
    glutSwapBuffers()                                  # important for double buffering
    

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(100, 100)                           # set window position
window = glutCreateWindow(b'Basic Graphics')              # create window with title

glEnable(GL_DEPTH_TEST)

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)       #Enable 2D Alpha blending
glEnable(GL_BLEND)

glutReshapeFunc(resize)
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything
