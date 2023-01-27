import sys
import os

n = len(sys.argv)

def raiseIssue():
    if n == 1:
        print("This is a program to simplify changing the color of your terminal.")
        print("To use this program, add arguments to the command prompt. ")
        print("The options are:\n1)\tBlack\t\t2)\tBlue\t\t3)\tGreen\t\t4)\tRed\n5)\tPurple\t\t6)\tYellow\t\t7)\tWhite\t\t8)\tGrey")
        print("You first select the background, and then the foreground")
    
    
def colorToColor():
    backgroundarg = str(sys.argv[1])
    foregroundarg = str(sys.argv[2])
    background=''
    foreground=''
    if backgroundarg == 'black':
        background = 0
    elif backgroundarg == 'blue':
        background = 1
    elif backgroundarg == 'green':
        background = 2
    elif backgroundarg == 'red':
        background = 4
    elif backgroundarg == 'purple':
        background = 5
    elif backgroundarg == 'yellow':
        background = 6
    elif backgroundarg == 'white':
        background = 7
    elif backgroundarg == 'grey':
        background = 8
    else:
        print("Invalid color, please try again")
        
    if foregroundarg == 'black':
        foreground = 0
    elif foregroundarg == 'blue':
        foreground = 1
    elif foregroundarg == 'green':
        foreground = 2
    elif foregroundarg == 'red':
        foreground = 4
    elif foregroundarg == 'purple':
        foreground = 5
    elif foregroundarg == 'yellow':
        foreground = 6
    elif foregroundarg == 'white':
        foreground = 7
    elif foregroundarg == 'grey':
        foreground = 8
    else:
        print("Invalid color, please try again")
        
    print("Now that is a change of color")
    os.system('cmd /k "color '+ str(background) + str(foreground) +'"')
    


def main():
    raiseIssue()
    colorToColor()

main()

