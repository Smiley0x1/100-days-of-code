import os,subprocess
import network
import scan


def main():
    if os.path.exists('Results/') == False:
        os.mkdir("Results")
        
    subprocess.Popen(
        ['ipconfig',"|","findstr","Default Gateway",">",'results/Logging.txt'],
        shell=True
    )
    
    textfile = open("results/Logging.txt",'r')
    
    for i in textfile:
        gateway = i[39:50]
        
    print("Successful, a log has been created and your default gateway is ",gateway)
            
    textfile.close()
            
    sum = scan.main(gateway)
    print("It took",sum,"to reach your default gateway\nNow scanning for open ports")
    
    print("Please be patient, this will take a while(~10 minutes)")
    
    openPorts = network.main(gateway)
    print("Your open ports are",end=" ")
    for i in openPorts:
        print(i,end=', ')
    

main()