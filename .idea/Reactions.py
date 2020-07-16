import pyautogui
import time

ReverseScan = False
reactionDelay = 0
Infinite = False
Alarm = False
running = False

def stop():
    global running
    running = False

def Nothing():
    print("nothing happened")


def PermitOpen(values):
    scanpic = pyautogui.screenshot()
    print(values[3])
    print(values[4])
    foundColor = scanpic.getpixel((values[3], values[4]))


    print("This is Permit open")

def MushieOpen():
    print("This is mushie open")

def PermitSetUp():
    pyautogui.press('enter')
    pyautogui.click(x=47, y=50)
    pyautogui.click(x=21, y=84)
    pyautogui.click(x=572, y=389)
    pyautogui.press('tab')
    pyautogui.write('696420696')
    pyautogui.press('enter')
    time.sleep(0.14)
    pyautogui.click(x=593, y=270)


def MushieSetUp():
    print("This is mushie setup")

def CallTop():
    print("This is call top")

def CallMid():
    print("This is callmid")

def CallADC():
    print("This is call adc")

def CallSup():
    print("This is call sup")

def Custom():
    print("This is custom")

def Upload():
    print("This is upload")


def start(scanning, etc):
    global running
    switcher = {
        'Nothing':  Nothing,
        "Permit open": PermitOpen,
        "Mushie open": MushieOpen,
        "Permit setup": PermitSetUp,
        "Mushie setup": MushieSetUp,
        "Call top": CallTop,
        "Call mid": CallMid,
        "Call adc": CallADC,
        "Call sup": CallSup,
        "Custom key": Custom,
        "Upload custom": Upload
    }
    myReaction = switcher.get(scanning[0], lambda: "Error")
    running = True
    scanpic = pyautogui.screenshot()
    foundColor = scanpic.getpixel(scanning[3])

    print("color changed")

    # scanSettings = [reaction, scanDelay, wantedColor, x, y]
    # etcSettings = [reversed, humanLike, infinite, alarm]

    #check for reactionDelay
    if (etc[1] != 0):
        reactionDelay = 100
    else:
        reactionDelay = 0

    #checks for alarm
    if (etc[3] != 0):
        return 0


    # check for Reverse Scan
    if (etc[0] == 0):
        while running == True:
            time.sleep(scanning[1])
            scanpic = pyautogui.screenshot()
            foundColor = scanpic.getpixel(scanning[3])
            if (str(foundColor)) != (str(scanning[2])):
                myReaction()
                if (etc[2] != 1):
                    running = False

    else:
        while running == True:
            time.sleep(scanning[1])
            scanpic = pyautogui.screenshot()
            foundColor = scanpic.getpixel(scanning[3])
            if (str(foundColor)) == (str(scanning[2])):
                myReaction()
                if (etc[2] != 1):
                    running = False


