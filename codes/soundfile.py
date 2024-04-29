from pydub import AudioSegment
from pydub.generators import Sine

# List of note names and their corresponding frequencies (C4 to C5)
notes = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88,
    "C5": 523.25
}

duration = 2000  # Duration of each note in milliseconds

def generate_sound_files(notes):
    for note, freq in notes.items():
        # Generate a sine wave sound at the given frequency
        sound = Sine(freq).to_audio_segment(duration=duration)
        
        # Reduce volume to -20 dB
        sound = sound - 20
        
        # Export the sound to a WAV file named after the note
        filename = f"{note}.wav"
        sound.export(filename, format="wav")
        print(f"Generated {filename}")

if __name__ == "__main__":
    generate_sound_files(notes)

