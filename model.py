from gui import *
from controller import *
# model.py
#
# Creates the counter data structure - for this applications, this is minimal - just an int.
#

# NOTE:  This module - model - contains application data structure, i.e., variables, 
# functions, and classes that pertain to the data side of the application.
# Therefore, no need to import view or controller - this code not even "knows" they exist.
# This is done for better modularization and information hiding.

# holds current count
count = 0    # initialize

frontPage = Display("Fractaural", 1200, 800)
logo = Icon("logo.png")
lwidth = logo.getWidth()
lheight = logo.getHeight()

text = "Click menu to sync your phone."
textlabel = Label(text, CENTER, Color.WHITE, Color.BLACK)

