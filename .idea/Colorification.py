import Reactions
import keyboard
import threading
import time
import cv2
import pyautogui
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def uploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def getPosition():
    ss = pyautogui.screenshot()
    time.sleep(3)
    thePosition = pyautogui.position()

    thePositionTemp = pyautogui.position()
    colorRGB = ss.getpixel(thePosition)

    hexColor = '#%02x%02x%02x' % colorRGB

    if (autoChecked.get() == 1):
        colorEntry.delete(0, END)
        colorEntry.insert(0, str(colorRGB))
        colorExample.config(bg = hexColor)

        cordinatesEntryX.delete(0, END)
        cordinatesEntryX.insert(0, thePosition[0])
        cordinatesEntryY.delete(0, END)
        cordinatesEntryY.insert(0, thePosition[1])


def threadStart():
    threading.Thread(target=start).start()

def threadStop():
    threading.Thread(target=stop).start()

def stop():
    Reactions.stop()
    status.set("STOPPED")

def start():
    # Gathers information for scan settings
    status.set("RUNNING")
    reaction = dropped.get()
    scanDelay = delay.get()
    wantedColor = color.get()
    x = int(cordinatesX.get())
    y = int(cordinatesEntryY.get())
    cordinates = (x , y)
    scanSettings = [reaction, scanDelay, wantedColor, cordinates]

    # Gathers information for etc
    reversed = reverseChecked.get()
    humanLike = humanChecked.get()
    infinite = stopChecked.get()
    alarm = alarmChecked.get()
    etcSettings = [reversed, humanLike, infinite, alarm]

    Reactions.start(scanSettings, etcSettings)
    status.set("STOPPED")

    # threading.Thread(target=Reactions.start(scanSettings, etcSettings)).start()


root = Tk()
menu = Menu(root)
root.config(menu=menu)
root.geometry("455x340")

#Scan Values
delay = IntVar()
color = StringVar()
visualColor = StringVar()
visualColor = ("pink")

cordinatesX = IntVar()
cordinatesY = IntVar()
autoChecked = IntVar()

#Reactions Values
dropped = StringVar()
custom = StringVar()

#Etc Values
reverseChecked = IntVar()
stopChecked = IntVar()
humanChecked = IntVar()
alarmChecked = IntVar()
shiftChecked = IntVar()
status = StringVar()
status.set("STOPPED")
Delay = 0

#Scan Window------------------------------------------------------------------------------------------------------------
scanWindow = LabelFrame(root, text="Scan Settings", width=1000, height = 1000)
scanTabs = ttk.Notebook(scanWindow)
scanTabs.pack()

colorTab = tkinter.Frame(scanTabs)
scanTabs.add(colorTab, text = "Color")

pictureTab = tkinter.Frame(scanTabs)
scanTabs.add(pictureTab, text = "Picture")

scanTabs.select(colorTab)
scanTabs.enable_traversal()

delayLabel = Label(colorTab, text = "Delay: ")
delayEntry = Entry(colorTab, textvariable = delay)

colorLabel = Label(colorTab, text = "Color: ")

colorEntry = Entry(colorTab, textvariable = color, width=14)
colorEntry.insert(0, str("(255, 192, 203)"))
colorExample = Frame(colorTab, width=40, height=19, bg=visualColor)

cordinatesLabel = Label(colorTab, text = "Cordinates: ")
cordinatesEntryX = Entry(colorTab, textvariable = cordinatesX, width=10)
cordinatesEntryX.delete(0, END)
cordinatesEntryX.insert(0, str("0"))
cordinatesEntryY = Entry(colorTab, textvariable = cordinatesY, width=9)
cordinatesEntryY.delete(0, END)
cordinatesEntryY.insert(0, str("0"))

autoCheck = Checkbutton(colorTab, text="Autofill", onvalue=1, offvalue=0, variable=autoChecked)
autoChecked.set(1)
positionButton = Button(colorTab, text="Get mouse position", command=getPosition)

pictureButton = Button(pictureTab,text="Upload...")

#Reaction Window--------------------------------------------------------------------------------------------------------
reactionWindow = LabelFrame(root, text="Reactions", width=225, height = 135)

reactionLabel = Label(reactionWindow,text = "Reaction: ")
reactionDrop = OptionMenu(reactionWindow, dropped,
                          "Nothing",
                          "Permit open",
                          "Mushie open",
                          "Permit setup",
                          "Mushie setup",
                          "Call top",
                          "Call mid",
                          "Call adc",
                          "Call sup",
                          "Custom key",
                          "Upload custom",)
reactionDrop.config(width=12)
dropped.set('Nothing')

customLabel = Label(reactionWindow, text = "Custom key: ")
customEntry = Entry(reactionWindow, textvariable = custom)

uploadLabel = Label(reactionWindow, text = "Upload custom: ")
upLoadButton = Button(reactionWindow, text='Upload...', command=uploadAction)

#Etc Window-------------------------------------------------------------------------------------------------------------
etcWindow = LabelFrame(root, text="Etc", width=437, height = 100)

reverseCheck = Checkbutton(etcWindow, text="Reverse Scan", onvalue=1, offvalue=0, variable=reverseChecked)
stopCheck = Checkbutton(etcWindow, text="Continue when color found", onvalue=1, offvalue=0, variable=stopChecked)
humanCheck = Checkbutton(etcWindow, text="Human reactions", onvalue=1, offvalue=0, variable=humanChecked)
alarmCheck = Checkbutton(etcWindow, text="Activate Alarm", onvalue=1, offvalue=0, variable=alarmChecked)
shiftCheck = Checkbutton(etcWindow, text="Scan color shift", onvalue=1, offvalue=0, variable=shiftChecked)

#Start/Stop-------------------------------------------------------------------------------------------------------------
stopButton = Button(root, text="Stop", width=20, height=3, command = threadStop)
startButton = Button(root, text="Start!", width=20, height=3, command = threadStart)
runningStatus = Label(root, text = "Stopped", textvariable=status)
#Scan grid--------------------------------------------------------------------------------------------------------------
scanWindow.grid(row=0, column=0, padx=(10,10), sticky="E")
delayLabel.grid(row=1, column=0)
delayEntry.grid(row=1, column=1, columnspan=2)

colorLabel.grid(row=2)
colorEntry.grid(row=2, column=1, columnspan=2, sticky="W")
colorExample.grid(row=2, column=2, sticky="W", padx=(18,0))

cordinatesLabel.grid(row=3)
cordinatesEntryX.grid(row=3, column=1, sticky="W")
cordinatesEntryY.grid(row=3, column=2, sticky="W")

autoCheck.grid(row=4, column=0)
positionButton.grid(row=4, column=1, columnspan=2)


#Reaction grid----------------------------------------------------------------------------------------------------------
reactionWindow.grid(row=0, column = 1)
reactionWindow.grid_propagate(0)
reactionLabel.grid(row=1,column=0, pady=(10,0))
reactionDrop.grid(row=1, column=1, pady=(10,0))
reactionDrop.grid_propagate(0)

customLabel.grid(row=2, column=0)
customEntry.grid(row=2, column=1)

uploadLabel.grid(row=3, column=0)
upLoadButton.grid(row=3, column=1)

pictureButton.grid(row=0, column=1,padx=(68), pady=(35))


#Etc grid----------------------------------------------------------------------------------------------------------
etcWindow.grid(row=1, column = 0, columnspan=2, padx=(10,0))
etcWindow.grid_propagate(0)
reverseCheck.grid(row=1, column=0, sticky=W, padx=(50))
stopCheck.grid(row=1, column=1, sticky=W)
humanCheck.grid(row=2, column=0, sticky=W, padx=(50))
alarmCheck.grid(row=2, column=1, sticky=W)
shiftCheck.grid(row=3, column=0, sticky=W, padx=(50))


#Start/Stop grid--------------------------------------------------------------------------------------------------------
stopButton.grid(row=2, column = 0, pady=(15))
startButton.grid(row=2, column = 1)
runningStatus.grid(row=3, columnspan = 2, padx=(45))

root.mainloop()
