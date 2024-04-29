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

try:
    while True:
        # Main loop doing nothing, just waiting for button events
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    GPIO.cleanup()  # Clean up GPIO settings before exiting


