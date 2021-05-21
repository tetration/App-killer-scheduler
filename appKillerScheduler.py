import time, os, signal
import datetime
import argparse

#You can also use argument parsers to schedule app termination
#In order to do that all you have to invoke this python script in the commandline the following way: python appKillerScheduler.py [NameofTheProgram] [HowManyMinutesYouWantToLetItRun]
#example: python discord 


parser = argparse.ArgumentParser()
parser.add_argument("name", help="Type the name of the program you wish to terminate here")
parser.add_argument("timeleft", help="Type how many minutes you'd like to let it run here")
args = parser.parse_args()

def GetDateNowAndAfter(mins):
    #Gets current time and calculates what time and date the timer will end
    now = datetime.datetime.now()
    after= now + datetime.timedelta(minutes = mins)
    array=[now,after]
    return array


def SetTimer(name):
    #Allows the user to pick how many minutes he wants the timer to last
    if args.timeleft==None:
        minutesAllowed = int(input("Type how many minutes you'd like to let the program "+name+" run before the script kills it: \n "))
    else:
        minutesAllowed = int(args.timeleft)

    mins = 0
    nowAndAfter= GetDateNowAndAfter(minutesAllowed)
    print("The timer started at:\n", nowAndAfter[0],"\n The timer will end at:\n",nowAndAfter[1])
    # Loop until we reach minutesAllowed minutes running
    while mins != minutesAllowed:
        timeleft=minutesAllowed-mins
        print("It's been {}".format(mins),"minutes since the timer has started")
        print("The app",name, "will be killed in about",timeleft,"minutes")
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1



def check_Os():
    #Detects the OS in which the script is running
    userOs=""
    from sys import platform
    userOs=platform
    print("Script is runnning in:",userOs)
    return userOs

def killProcess_linux(name):
    # kills the process or processes on Linux
    # iterating through each instance of the proess
    for line in os.popen("ps ax | grep " + name + " | grep -v grep"): 
        fields = line.split()
              
        # extracting Process ID from the output
        pid = fields[0] 
              
        # terminating process 
        os.kill(int(pid), signal.SIGKILL)

def killProcess_Win32(name): 
        #kills the process or processes in windows
        os.system("TASKKILL /F /IM "+name+".exe")

def main():

    # Ask user for the name of process he/she wishes to terminate
    if args.name==None:
        name = input("Enter process Name: ")
    else:
        name=args.name
    try:
        currentOs=check_Os()
        SetTimer(name)
        if currentOs=="win32":
            killProcess_Win32(name)
        else:
            killProcess_linux(name)     
             
        print("Process",name,"has been successfully terminated")
        
    except Exception as e:
        print("An Error has ocurred while running the script:",e)
   
main()



