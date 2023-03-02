#Once I use SQLI more, I will add to this
import pyautogui
import time

def main():
    whatDo=int(input("What would you like to do?\n1)\tTest for SQLI\n"))
    
    if whatDo==1:
        time.sleep(3)
        pyautogui.typewrite("'or 1=1;")
        pyautogui.keyDown('enter')
        
        
        
main()