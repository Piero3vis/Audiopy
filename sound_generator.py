import numpy as np
import pygame

# Initialize mixer for sound
pygame.mixer.init()

def generate_sound(r, g, b):
    # Generate frequency based on RGB values
    frequency = 100 + (r + g + b) // 3  # Scale frequency based on RGB values
    duration = 0.2  # seconds
    sample_rate = 44100
    amplitude = 4096

    # Generate a sine wave
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    wave = wave.astype(np.int16)

    # Convert 1D wave array to 2D for stereo (left and right channels)
    stereo_wave = np.column_stack((wave, wave))

    # Play the sound
    sound = pygame.sndarray.make_sound(stereo_wave)
    sound.play()
