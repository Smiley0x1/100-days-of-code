import subprocess
import datetime
import os

def main(target):
    if os.path.exists('Results/') == False:
        os.mkdir("Results")
        
    subprocess.run(
        ["tracert",target,">","results/" + str(datetime.date.today()) +".txt"],
        shell=True
    )
        
    textfile = open("results/" + str(datetime.date.today()) +".txt",'r')
    lines =[]
    n = 0
    for i in textfile:
        n+=1
        lines.append(i)
        
    sum = str(lines[n-3][7:12])
    return sum
