# view.py
#
# Author:     Danzel Capers, Raquel Jones
# Email:      capersdt@g.cofc.edu, jonesra1@g.cofc.edu
# Class:      CSCI 380
# Assignment: Final Project
# Due Date:   12/11/2015
#
# Purpose: Displays windows for user to interact with
#
# Input:   None
#
# Output:  Displays 

from gui import *
from osc import *


import model, controller                 # import other application modules

display = Display("Fractaural", 800, 600)          # create application display
label1 = Label("Click 'Menu' button followed be 'Sync with phone' to begin")
display.add(label1, 50, 50)

#Creates Menu menu
menu = Menu("Menu")
menu.addItem("Sync with phone", controller.callOSC)
menu.addItem("RemoveAll", controller.removeALL)
menu.addItem("New", controller.callNothing) #Furture feature
menu.addItem("Save", controller.callNothing) #Furture feature
display.addMenu(menu)

#Creates Share menu
share = Menu("share")
share.addItem("Facebook", controller.callNothing) #Furture feature
share.addItem("Twitter", controller.callNothing) #Furture feature
share.addItem("Instagram", controller.callNothing) #Furture feature
share.addItem("MySpace", controller.callNothing) #Furture feature
display.addMenu(share)
