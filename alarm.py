from playsound import playsound
import time
import os
import sys

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def setAlarm(seconds):
    current_dir = os.getcwd()
    file_path = current_dir + '/alarm.mp3'
    for i in range(0,seconds+1,1):
        time.sleep(1)
        time_left = seconds -i
        min_left = time_left//60
        sec_left = time_left % 60
        clear()
        print(f"The alarm rings in: {min_left:02d}:{sec_left:02d}")
        if time_left == 0:
            clear()
            print(f"The alarm rings in: {min_left:02d}:{sec_left:02d}")
            playsound(file_path)
            break

def main():

   # print(sys.argv[1] + " " + sys.argv[2])

    if len(sys.argv) == 1:
        input_minutes = int(input("Please enter the minutes: "))
        input_seconds = int(input("Please enter the seconds: "))
        total_seconds = input_seconds + (input_minutes * 60)
        setAlarm(total_seconds)
    elif len(sys.argv) > 1:
        if sys.argv[1] == "-t" or sys.argv[1] == "-h":
            if sys.argv[1] == "-t":
                try:
                    time = sys.argv[2].split(':')
                    if(time[0].isdigit() and time[1].isdigit()):
                        minutes = int(time[0])
                        seconds = int(time[1])
                        total_seconds = seconds + (minutes * 60)
                        setAlarm(total_seconds)
                    else:
                        print("Invalid Arguments. Call with alarm.py -t 10:22. Use -h for help!")
                except:
                    print("Enter a valid time XX:XX!")
            elif sys.argv[1] == "-h":
                print("Program options: \n \
                      -t: enter time to set the alarm i.e.: alarm.py -t 12:30 - sets an alarm for 12 min and 30 seconds. \n \
                      -h: displays helptext.")        
        else:
            print("Invalid arguments. Call alarm.py -h for help!")   
    
            
    else:
        print("not enough arguments")

if __name__ == '__main__':
    main()