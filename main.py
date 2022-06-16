error = False
try:
    import os
    os.system("title " + "Auto Typer,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
try:
    import pynput.keyboard
except:
    error = True
if error == True:
    print("Missing Modules, Press Enter To Start Repair Process (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install pynput")
        print("Error May Be Fixed Now, Restart The Program")
        input("")
        exit()
    except:
        print("Failed To Fix")
        input("")
        exit()
import time
def valid():
    print("Enter A Valid Choice")
print("Auto Typer (Works With Discord)")
msg = input("Enter What To Auto Type: ")
while True:
    autoenter = input("Want To Auto Press Enter At End (y/n): ")
    if autoenter == "y" or autoenter == "n":
        break
    else:
        valid()
while True:
    try:
        sleep = input("Enter Delay (0=None, 1 Recomended, If 0 Can Crash PC): ")
        sleep = float(sleep)
        break
    except:
        valid()
while True:
    try:
        sleepletter = input("Delay Between Each Letter (0=None): ")
        sleepletter = float(sleepletter)
        break
    except:
        valid()
keyboard = pynput.keyboard.Controller()
def start(l):
    print("Starting In " + str(l))
    time.sleep(1)
start(3)
start(2)
start(1)
done = 0
while True:
    done = int(done) + 1
    for letter in msg:
        keyboard.press(letter) 
    if autoenter == "y":
        keyboard.press(pynput.keyboard.Key.enter)
        keyboard.release
    print("["+str(done)+"]"+" Typed")
    time.sleep(float(sleep))
