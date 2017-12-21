# controller.py 
#
# Define the counter callback functions.
#

# NOTE:  This module - controller - acts as an interface between view and model.
# It contains callback functions that connect user (GUI) events to the 
# underlying - model - data and functionality.

import view, model
from gui import *
from random import *
from osc import *


# callback function to increase counter and update display 
# attached to mouse event - hence the (x, y) parameters
def add1(x, y):
   
   model.count += 1                           # increment counter in model
   view.display.setTitle( str(model.count) )  # update display counter in view - using counter in model

def drawCircle(message):
   x = randint(0, view.display.getWidth())
   y = randint(0, view.display.getHeight())
   z = randint(0, 100)
   circle1 = Circle(x, y, z)
   view.display.add(circle1)

def drawPolygon(message):
   x = randint(0, view.display.getWidth())
   y = randint(0, view.display.getHeight())
   z = randint(0, 100)
   polygon1 = Polygon(x, y)
   view.display.add(polygon1)



def callOSC(x,y):
   oscIn = OscIn(5380)
   #oscIn.onInput("/.*",drawCircle)
   oscIn.onInput( "/mrmr/pushbutton/0/Danzel-T-Caperss-iPhone", drawCircle )
   oscIn.onInput( "/mrmr/pushbutton/1/Danzel-T-Caperss-iPhone", drawCircle )
   oscIn.onInput( "/mrmr/pushbutton/2/Danzel-T-Caperss-iPhone", drawCircle )