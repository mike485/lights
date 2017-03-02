import Tkinter
import pyfirmata 
from pyfirmata import Arduino, INPUT, PWM
from time import sleep
import random


#  Associate the port and board with pyFirmata

port = "/dev/cu.usbmodem1471"
board = pyfirmata.Arduino(port)
sleep(5)

# intialize pin 13

pin = board.get_pin('d:13:o')



# intialize the main window with tile and size

top = Tkinter.Tk()
top.title("Button for Pin Action")
top.minsize(300, 30)


# create button

def onStartButtonPress():
    timePeriod = timePeriodEntry.get()
    timePeriod = float(timePeriod) 
    startButton.config(state=Tkinter.DISABLED)
    pin.write(1)
    #Led will be on for a specific amount of time listed below
    sleep(timePeriod)
    pin.write(0)
    startButton.config(state=Tkinter.ACTIVE)


timePeriodEntry = Tkinter.Entry(top, bd=5, width=25)
startButton = Tkinter.Button(top, text = "Start", command=onStartButtonPress)
# .pack() makes it available in the main window

timePeriodEntry.pack()
#can manually shift the focus of the graphical pointer to the timePeriodEntry widget
#using the focus_set method, it obtains the value from the timePeriodEntry object and convert
# it into a float value using using the float fuction() 
timePeriodEntry.focus_set() 
startButton.pack()

# define StartButtonPress fuction


    


# Label Widget

#hellolabel = Tkinter.Label(top, text = "Hello Label")

# the pack geometry manager organizes the widgets into rows and columns



#hellolabel.pack()

# Start and open the Window
# test update

top.mainloop()


