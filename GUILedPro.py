import Tkinter
import pyfirmata 
from pyfirmata import Arduino, INPUT, PWM
from time import sleep
import random


#  Associate the port and board with pyFirmata
# created data to commit change

port = "/dev/cu.usbmodem1471"
board = pyfirmata.Arduino(port)
sleep(5)

# intialize pin 11
# Three pin modes supportted o = output, i=input, p=PMW

greenPin = board.get_pin('d:10:p')
redPin = board.get_pin('d:11:p')
#pin = board.get_pin('d:11:p')



# intialize the main window with tile and size

#Tkinter.Label(top, text="Time (seconds)").grid(column=2, row=1)
top = Tkinter.Tk()
top.title("Button for Pin Action")
top.minsize(300, 30)
redVar = Tkinter.IntVar()
greenVar = Tkinter.IntVar()



# create button

def onStartButtonPress():
    #timePeriod = timePeriodEntry.get()
    #timePeriod = float(timePeriod)
    #ledBrigtness = brightnessScale.get()
    #ledBrightness = float()
    startButton.config(state=Tkinter.DISABLED)
    #pin.write(ledBrightness/100.0)
    #pin.write(1)
    #Led will be on for a specific amount of time listed below
    #sleep(timePeriod)
    #pin.write(0)
    startButton.config(state=Tkinter.ACTIVE)
    redPin.write(redVar.get())
    greenPin.write(greenVar.get())

def onStopButtonPress():
    redPin.write(0)
    greenPin.write(0)
                                
#timePeriodEntry = Tkinter.Entry(top, bd=5, width=25)
#brightnessScale = Tkinter.Scale(top, from_=0, to=100, orient=Tkinter.HORIZONTAL)                                
startButton = Tkinter.Button(top, text = "Start", command=onStartButtonPress)
stopButton = Tkinter.Button(top, text = "Stop", command=onStopButtonPress)
exitButton = Tkinter.Button(top, text = "Exit", command=quit)
redCheckBox = Tkinter.Checkbutton(top, text = "Red LED", variable=redVar)
greenCheckBox = Tkinter.Checkbutton(top, text = "Green light", variable=greenVar)
                        
                                
# .pack() makes it available in the main window

#timePeriodEntry.grid(column=1,row=1)                                
#timePeriodEntry.pack()
#brightnessScale.grid(column=1, row=2)
#brightnessScale.pack() 

#can manually shift the focus of the graphical pointer to the timePeriodEntry widget
#using the focus_set method, it obtains the value from the timePeriodEntry object and convert
# it into a float value using using the float fuction()

#timePeriodEntry.focus_set()
#Tkinter.Label(top, text="Time (seconds)").grid(column=2, row=1)
#Tkinter.Label(top, text="Brightness (%)").grid(column=2, row=2)
startButton.grid(column=1, row=3)
stopButton.grid(column=3, row=3)
redCheckBox.grid(column=1, row=1)
greenCheckBox.grid(column=2, row=1)
exitButton.grid(column=2, row=3)

#startButton.pack()
# define StartButtonPress fuction
# Label Widget
#hellolabel = Tkinter.Label(top, text = "Hello Label")
# the pack geometry manager organizes the widgets into rows and columns
#hellolabel.pack()
# Start and open the Window


top.mainloop()



