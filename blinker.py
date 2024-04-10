from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware ##
ledBlue = LED(14)
ledRed = LED(23)
ledGreen = LED(25)

## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

### EVENT FUNCTIONS ###
def ledBlueToggle():
	if ledBlue.is_lit: 
		ledBlue.off()
		ledBlueButton["text"] = "Turn BLUE LED on"
	else:
		ledBlue.on()
		ledBlueButton["text"] = "Turn BLUE LED off"
		
def ledRedToggle():
	if ledRed.is_lit:
		ledRed.off()
		ledRedButton["text"] = "Turn RED LED on"
	else:
		ledRed.on()
		ledRedButton["text"] = "Turn RED LED off"
		
def ledGreenToggle():
	if ledGreen.is_lit:
		ledGreen.off()
		ledGreenButton["text"] = "Turn GREEN LED on"
	else:
		ledGreen.on()
		ledGreenButton["text"] = "Turn GREEN LED off"
		
def exitToggle():
	RPi.GPIO.cleanup()
	win.destroy()

### WIDGETS ###
ledBlueButton = Button(win, text = 'Turn BLUE LED on', font = myFont, command = ledBlueToggle, bg = 'bisque2', height = 1, width = 24)
ledBlueButton.grid(row = 0, column = 1)
ledRedButton = Button(win, text = 'Turn RED LED on', font = myFont, command = ledRedToggle, bg = 'bisque2', height = 1, width = 24)
ledRedButton.grid(row = 1, column = 1)
ledGreenButton = Button(win, text = 'Turn GREEN LED on', font = myFont, command = ledGreenToggle, bg = 'bisque2', height = 1, width = 24)
ledGreenButton.grid(row = 2, column = 1)

## EXIT BUTTON ##
exitButton = Button(win, text = 'EXIT', font = myFont, command = exitToggle, bg = 'bisque2', height = 1, width = 24)
exitButton.grid(row = 3, column = 1)

win.mainloop()
