# view.py
# 
# Create the click-counter GUI and associate callback functions
# with user (GUI) events.
#

# NOTE:  This module - view - creates all the GUI objects needed by the application.
# It uses callback functions defined in controller, and may access model data (as needed).

from gui import *
from osc import *

import model, controller                 # import other application modules

display = Display("", 800, 600)          # create application display
display.setTitle( str(model.count) )     # initialize title (notice use of model data here)

#display.onMouseClick( controller.drawCircle )  # when display is mouse-clicked, call this function

display.onMouseClick( controller.callOSC )
#display.onMouseClick( controller.getInfo )