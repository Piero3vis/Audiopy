# Color Sound Effects

This project generates sound based on the RGB values of an image's pixels as you hover over them. 

## How It Works
- The program loads an image, displays it, and uses the mouse position to detect the RGB values of each hovered pixel.
- It generates and plays a sound with a frequency based on the RGB values.

## Installation
1. Clone this repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the main script:
    ```bash
    python main.py
    ```

## Project Structure
- **main.py**: The main program that displays the image and plays sounds.
- **sound_generator.py**: Sound generation based on RGB values.
- **assets/**: Directory for images and sounds.
