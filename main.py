import time
import pygame

def set_alarm(alarm_time, sound_file):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up samurai!")   #change the text to your choice
            pygame.mixer.init()
            try:
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)  # Add a delay to keep the audio playing
            except pygame.error as e:
                print("Pygame error:", e)
            break
        time.sleep(1)

def main():
    print("Welcome to the Alarm Clock App")
    alarm_time = input("Set the alarm time (HH:MM:SS): ")
    sound_file = input("Enter the path to the alarm sound file: ")

    try:
        valid_time = time.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS format.")
        return

    try:
        with open(sound_file):
            pass
    except FileNotFoundError:
        print("Sound file not found. Please provide a valid file path.")
        return

    set_alarm(alarm_time, sound_file)

if __name__ == "__main__":
    main()
