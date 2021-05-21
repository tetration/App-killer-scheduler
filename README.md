# App Killer Scheduler
Set a timer to termina a process at a specified date
------------


### Features
- Python 3 script that sets a timer for when you want applications to be terminated
- Works on Windows and Unix OSes
- Pick how many minutes you'd like to let a program run

### Future Planned Features
- Set hours, days, months and years that an app can run
- Set dates to kill an app
- Set dates to also start apps
# How to use it

                    
```seq
Input->Timer: 1: User types the name of the app to be killed
Input->Timer: 2:  User types how long the app can run(in minutes)
Input->>Timer: 3: When the timer runs out the app is terminated
```

## Invoking the program with arguments
You can also use argument parsers to run this script and schedule an app to be killed by it. 
In order to do that all you have to invoke this python script in the commandline the following way: python appKillerScheduler.py [NameofTheProgram] [HowManyMinutesYouWantToLetItRun]

example:

```bash
    python appKillerScheduler.py mspaint 2
```

This example schedules my script to terminate mspaint.exe in 2 minutes.


###End
