import Adafruit_BBIO.GPIO as GPIO
import pygame
import time

pygame.init()
pygame.mixer.init()

keys = {
    "P8_10": "C4.wav",
    "P8_12": "D4.wav",
    "P8_14": "E4.wav",
    "P8_16": "F4.wav",
    "P8_18": "G4.wav",
    "P8_20": "A4.wav",
    "P8_15": "B4.wav",
    "P8_17": "C5.wav"
}

for pin in keys:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Assuming active-high buttons with pull-down resistors


def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def is_button_pressed(pin):
    current_state = GPIO.input(pin)
    if current_state:
        time.sleep(0.05)  # Debounce delay
        current_state = GPIO.input(pin)  # Check the pin state again after the delay
    return current_state

try:
    while True:
        for pin, sound in keys.items():
            if is_button_pressed(pin):
                play_sound(sound)
                # Wait for the button to be released with additional debouncing
                while is_button_pressed(pin):
                    time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting program")


GPIO.cleanup()
