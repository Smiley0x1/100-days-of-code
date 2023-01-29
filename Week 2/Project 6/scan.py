import subprocess
import datetime
import os

def main():
    if os.path.exists('Results/') == False:
        os.mkdir("Results")
    
    print("Hello World!\nThis tool is used to tell you the network latency in ms between you and a speciific IP\nA log will be created for each scan that you do\nHappy Scanning!\n")
    
    target = str(input("What is the IP that you are trying to reach?:\n"))
    
    print("Please be patient, this may take a minute")
    subprocess.run(
        ["tracert",target,">","results/" + str(datetime.date.today()) +".txt"],
        shell=True
    )
    
    print("Successful, a log has been created and your summary is:")
    
    textfile = open("results/" + str(datetime.date.today()) +".txt",'r')
    lines =[]
    n = 0
    for i in textfile:
        n+=1
        lines.append(i)
        
    sum = str(lines[n-3][7:12])
    print("It took",sum,"to reach",target)
        
