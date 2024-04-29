import pygame
import Adafruit_BBIO.GPIO as GPIO
import time

# Initialize Pygame Mixer
pygame.mixer.init()

# Define a dictionary of notes and their corresponding GPIO pins and sound files
notes = {
    'C': {'pin': 'P8_10', 'file': 'sounds/piano-c_C_major.wav'},
    'D': {'pin': 'P8_12', 'file': 'sounds/piano-d_D_major.wav'},
    'E': {'pin': 'P8_14', 'file': 'sounds/piano-e_E_major.wav'},
    'F': {'pin': 'P8_16', 'file': 'sounds/piano-f_F_major.wav'},
    'G': {'pin': 'P8_18', 'file': 'sounds/piano-g_G_major.wav'},
    'A': {'pin': 'P8_15', 'file': 'sounds/piano-a_A_major.wav'},
    'B': {'pin': 'P8_17', 'file': 'sounds/piano-b_B_major.wav'}
}

# Load sounds and configure GPIOs
for note in notes.values():
    note['sound'] = pygame.mixer.Sound(note['file'])
    GPIO.setup(note['pin'], GPIO.IN)
    GPIO.add_event_detect(note['pin'], GPIO.RISING, callback=lambda channel, n=note['sound']: n.play(), bouncetime=300)

# Setup recording button
recording_pin = 'P8_11'
GPIO.setup(recording_pin, GPIO.IN)
last_press_time = None
recording = False
events = []

def record_event(channel):
    global last_press_time, recording, events
    current_time = time.time()
    if not recording:
        recording = True
        events = []  # Clear previous events
        print("Recording started.")
    else:
        recording = False
        print("Recording stopped.")
        print("Recorded events:", events)
    last_press_time = current_time

GPIO.add_event_detect(recording_pin, GPIO.BOTH, callback=record_event, bouncetime=200)

try:
    while True:
        # Check each note pin if it's pressed and record the event if recording is active
        if recording:
            for note_name, note_info in notes.items():
                if GPIO.input(note_info['pin']):
                    event_time = time.time() - last_press_time
                    events.append((note_name, event_time))
                    last_press_time = time.time()
        time.sleep(0.1)  # Check every 100ms
except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    GPIO.cleanup()  # Clean up GPIO settings before exiting
