# controller.py
#
# Author:     Danzel Capers, Raquel Jones
# Email:      capersdt@g.cofc.edu, jonesra1@g.cofc.edu
# Class:      CSCI 380
# Assignment: Final Project
# Due Date:   12/11/2015
#
# Purpose: Setup functions
#
# Input:   Variables from model.py and gui images from view.py
#
# Output:  Displays from view.py 

import view, model
from gui import *
from random import *
from osc import *

   
#Draws a Circle with random specs
def drawCircle(message):
   model.Play.midi(model.note1)
   model.x = randint(0, view.display.getWidth())
   model.y = randint(0, view.display.getHeight())
   model.z = randint(0, 100)
   circle1 = Circle(model.x, model.y, model.z)
   view.display.add(circle1)
   

#Draws a Rectangle with random specs
def drawRectangle(message):
   model.Play.midi(model.note2)
   model.x1 = randint(0, view.display.getWidth())
   model.y1 = randint(0, view.display.getHeight())
   model.x2 = randint(0, view.display.getWidth())
   model.y2 = randint(0, view.display.getHeight())
   rectangle1 = Rectangle(model.x1, model.y1, model.x2, model.y2)
   view.display.add(rectangle1)
   

#Draws a Arc with random specs and plays a single note
def drawArc(message):
   model.Play.midi(model.note3)
   model.x1 = randint(0, view.display.getWidth())
   model.y1 = randint(0, view.display.getHeight())
   model.x2 = randint(0, view.display.getWidth())
   model.y2 = randint(0, view.display.getHeight())
   model.angle1 = randint(0, 180)
   model.angle2 = randint(0, 180)
   arc1 = Arc(model.x1, model.y1, model.x2, model.y2,model.angle1,model.angle2)
   view.display.add(arc1)
   

def removeAll(message):
   view.display.removeAll()
   
def removeALL():
   view.display.removeAll()
   
def callNothing():
   view.label1 = view.Label("Will be a furture feature, please try again")
   view.display.add(view.label1, 50, 50)

def callOSC():
   view.display.remove(view.label1)
   oscIn = OscIn(5380)
   #oscIn.onInput("/.*",drawCircle)
   oscIn.onInput( "/mrmr/pushbutton/0/Danzel-T-Caperss-iPhone", drawCircle )
   oscIn.onInput( "/mrmr/pushbutton/1/Danzel-T-Caperss-iPhone", drawRectangle )
   oscIn.onInput( "/mrmr/pushbutton/2/Danzel-T-Caperss-iPhone", drawArc )
   oscIn.onInput( "/mrmr/pushbutton/6/Danzel-T-Caperss-iPhone", removeAll )