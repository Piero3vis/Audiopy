import numpy as np
import pygame

# Initialize the Pygame mixer for sound playback
pygame.mixer.init()

def generate_sound(r, g, b):
    """
    Generate a sound based on the RGB color values of a pixel.
    Different dominant colors produce unique sounds:
        - Red-dominant: Low-pitched sine wave
        - Green-dominant: Mid-pitched square wave
        - Blue-dominant: High-pitched sawtooth wave
        - Mixed/other colors: White noise
    Parameters:
        r (int): Red channel value (0-255)
        g (int): Green channel value (0-255)
        b (int): Blue channel value (0-255)
    """
    
    # Determine the dominant color and select the corresponding sound type
    if r > g and r > b:
        # Red-dominant: Low-pitched sine wave
        frequency = 200 + r  # Set frequency proportional to red value
        amplitude = 4096
        wave = generate_sine_wave(frequency, amplitude)

    elif g > r and g > b:
        # Green-dominant: Mid-pitched square wave
        frequency = 400 + g  # Set frequency proportional to green value
        amplitude = 3072
        wave = generate_square_wave(frequency, amplitude)

    elif b > r and b > g:
        # Blue-dominant: High-pitched sawtooth wave
        frequency = 600 + b  # Set frequency proportional to blue value
        amplitude = 2048
        wave = generate_sawtooth_wave(frequency, amplitude)

    else:
        # Mixed color: Play a soft white noise
        wave = generate_white_noise()

    # Play the generated wave
    play_wave(wave)


def generate_sine_wave(frequency, amplitude, duration=0.2, sample_rate=44100):
    """
    Generate a sine wave sound array.
    Parameters:
        frequency (float): Frequency of the sine wave in Hz
        amplitude (int): Amplitude of the wave (volume)
        duration (float): Duration of the sound in seconds
        sample_rate (int): Sample rate in Hz (default: 44100)
    Returns:
        np.ndarray: Stereo sine wave sound array
    """
    # Generate time values for the wave
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # Calculate the sine wave
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    wave = wave.astype(np.int16)
    # Convert to stereo by duplicating the wave data into two channels
    return np.column_stack((wave, wave))


def generate_square_wave(frequency, amplitude, duration=0.2, sample_rate=44100):
    """
    Generate a square wave sound array.
    Parameters:
        frequency (float): Frequency of the square wave in Hz
        amplitude (int): Amplitude of the wave (volume)
        duration (float): Duration of the sound in seconds
        sample_rate (int): Sample rate in Hz (default: 44100)
    Returns:
        np.ndarray: Stereo square wave sound array
    """
    # Generate time values for the wave
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # Calculate the square wave by taking the sign of a sine wave
    wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
    wave = wave.astype(np.int16)
    # Convert to stereo by duplicating the wave data into two channels
    return np.column_stack((wave, wave))


def generate_sawtooth_wave(frequency, amplitude, duration=0.2, sample_rate=44100):
    """
    Generate a sawtooth wave sound array.
    Parameters:
        frequency (float): Frequency of the sawtooth wave in Hz
        amplitude (int): Amplitude of the wave (volume)
        duration (float): Duration of the sound in seconds
        sample_rate (int): Sample rate in Hz (default: 44100)
    Returns:
        np.ndarray: Stereo sawtooth wave sound array
    """
    # Generate time values for the wave
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # Calculate the sawtooth wave with a linear ramp within each period
    wave = amplitude * (2 * (t * frequency - np.floor(0.5 + t * frequency)))
    wave = wave.astype(np.int16)
    # Convert to stereo by duplicating the wave data into two channels
    return np.column_stack((wave, wave))


def generate_white_noise(duration=0.2, sample_rate=44100):
    """
    Generate white noise sound array.
    Parameters:
        duration (float): Duration of the noise in seconds
        sample_rate (int): Sample rate in Hz (default: 44100)
    Returns:
        np.ndarray: Stereo white noise sound array
    """
    # Generate random samples from a normal distribution for white noise
    wave = np.random.normal(0, 4096, int(sample_rate * duration))
    wave = wave.astype(np.int16)
    # Convert to stereo by duplicating the wave data into two channels
    return np.column_stack((wave, wave))


def play_wave(wave):
    """
    Play a wave array using pygame's sound system.
    Parameters:
        wave (np.ndarray): Stereo sound array to play
    """
    # Create a sound object from the wave array and play it
    sound = pygame.sndarray.make_sound(wave)
    sound.play()
