from playsound import playsound
import time
import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def setAlarm(seconds):
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
            playsound("alarm.mp3")
            break

def main():
    input_minutes = int(input("Please enter the minutes: "))
    input_seconds = int(input("Please enter the seconds: "))
    total_seconds = input_seconds + (input_minutes * 60)
    setAlarm(total_seconds)
    

if __name__ == '__main__':
    main()