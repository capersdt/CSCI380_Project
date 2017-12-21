from osc import *
from gui import *
from model import *
from music import *        # import music library
from timer import *

pitch = A4            # pitch of note to be played

def callOSC(newelement):
   newelement.setForegroundColor(Color.BLACK)
   OscIn(5357)
   
   
def playOSC(): 
   oscIn.onInput( "/mrmr/pushbutton/1/Danzel-T-Caperss-iPhone", startNote )
   oscIn.onInput( "/mrmr/pushbutton/0/Danzel-T-Caperss-iPhone", startNote )
   oscIn.onInput( "/mrmr/pushbutton/2/Danzel-T-Caperss-iPhone", startNote )

def playLeft():pass

def playMiddle():pass
def playRight():pass

def drawCircle():
   circle1 = Circle(255, 300, 20)
   frontpage.add(circle1)

def startNote():   # function to start the note
   frontPage.add(circle1)
   #global pitch        # we use this global variable
   #Play.noteOn(pitch)  # start the note
   
   

