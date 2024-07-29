import pyautogui as mouse
import time
print("Welcome to autoclicker")
time.sleep(5)
print(mouse.position())
clickposx = int(input("X position of autoclicker:"))
clickposy = int(input("y position of autoclicker:"))
clickspeed = int(input("Autoclicker speed(CPS):"))
clickduration = int(input("Time autoclicker is active:"))

mouse.PAUSE = 1/clickspeed

itime = time.time()
mouse.click(clickposx, clickposy)
mouse.click(clickposx, clickposy)
while(time.time() <= itime + clickduration + 0.1):
    
    mouse.click(clickposx, clickposy)
