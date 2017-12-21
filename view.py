from gui import *
from model import *
from controller import *



frontPage.setColor(Color.BLACK)
#syncButton = Button("Sync with phone",callOSC)
#frontPage.add(syncButton, 450,500)

frontPage.add(logo, 50, 0)
textlabel.setFont( Font("Serif", Font.PLAIN, 40) )
frontPage.add(textlabel, 400, 400)

menu = Menu("Menu")
menu.addItem("Sync with phone",callOSC(textlabel))

frontPage.addMenu(menu)

