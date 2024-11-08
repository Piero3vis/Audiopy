import numpy as np
import pygame

# Initialize mixer for sound
pygame.mixer.init()

def generate_sound(r, g, b):
    # Define sound properties based on dominant color
    if r > g and r > b:
        # Red-dominant color: low-pitched sine wave
        frequency = 200 + r  # Low frequency for red tones
        amplitude = 4096
    elif g > r and g > b:
        # Green-dominant color: mid-pitched square wave
        frequency = 400 + g  # Mid frequency for green tones
        amplitude = 3072
        return generate_square_wave(frequency, amplitude)
    elif b > r and b > g:
        # Blue-dominant color: high-pitched sawtooth wave
        frequency = 600 + b  # High frequency for blue tones
        amplitude = 2048
        return generate_sawtooth_wave(frequency, amplitude)
    else:
        # Mixed color: soft white noise
        return generate_white_noise()
    
    # Generate and play a sine wave as default
    duration = 0.2  # seconds
    play_wave(generate_sine_wave(frequency, amplitude, duration))


def generate_sine_wave(frequency, amplitude, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    wave = wave.astype(np.int16)
    return np.column_stack((wave, wave))  # Stereo


def generate_square_wave(frequency, amplitude, duration=0.2, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
    wave = wave.astype(np.int16)
    return np.column_stack((wave, wave))  # Stereo


def generate_sawtooth_wave(frequency, amplitude, duration=0.2, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * (2 * (t * frequency - np.floor(0.5 + t * frequency)))
    wave = wave.astype(np.int16)
    return np.column_stack((wave, wave))  # Stereo


def generate_white_noise(duration=0.2, sample_rate=44100):
    wave = np.random.normal(0, 4096, int(sample_rate * duration))
    wave = wave.astype(np.int16)
    return np.column_stack((wave, wave))  # Stereo


def play_wave(wave):
    sound = pygame.sndarray.make_sound(wave)
    sound.play()
