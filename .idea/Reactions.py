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
    global running
    pyautogui.press('enter')
    time.sleep(0.14)

    scanpic = pyautogui.screenshot()
    checkColor = scanpic.getpixel((715,409))
    if (str(checkColor)) != ("(68, 136, 187)"):
        pyautogui.click(x=47, y=57)
        pyautogui.click(x=30, y=86)
        pyautogui.click(x=507, y=409)
        pyautogui.press('tab')
        pyautogui.write('666666666')
        pyautogui.press('enter')
        time.sleep(0.18)
        pyautogui.click(x=594, y=275)
        running = False

    else:
        pyautogui.press('enter')
        pyautogui.click(x=26, y=84)
        pyautogui.click()
        time.sleep(1)
        pyautogui.write('S>RPOT')

def MushieSetUp():
    global running
    pyautogui.doubleClick(x=16, y=90)                       #clicks the mushie in your inventory
    time.sleep(0.18)
    scanpic = pyautogui.screenshot()
    checkColor = scanpic.getpixel((664, 451))

    if (str(checkColor)) == ("(255, 255, 255)"):             #checks if the "you can't open the shop window is there"

        pyautogui.write('8')                           #types the name of the shop
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.click(x=47, y=57)                         #clicks on the use tab
        pyautogui.click(x=30, y=86)                         #clicks first item in use tab
        pyautogui.click(x=507, y=409)                       #places the item in your shop
        pyautogui.press('tab')                              #presses tab so that you only put in 1 item
        pyautogui.write('666666666')                        #inputs the price
        pyautogui.press('enter')                            #confirms item into shop
        time.sleep(0.28)                                    #delay to prevent hang
        pyautogui.click(x=594, y=275)                       #clicks open
        running = False                                     #turns off program (not sure if this works)

    else:
        pyautogui.press('enter')                            #closes shop can't open window

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


    else:
        while running == True:
            time.sleep(scanning[1])
            scanpic = pyautogui.screenshot()
            foundColor = scanpic.getpixel(scanning[3])
            if (str(foundColor)) == (str(scanning[2])):
                myReaction()
                if (etc[2] != 1):
                    running = False