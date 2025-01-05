# Drawaria AutoPlayer

## Description

This repository contains a Python script that automates the process of playing the online drawing and guessing game [Drawaria](https://drawaria.online/). The script uses Selenium for browser automation, OpenCV for image processing, and PyAutoGUI for mouse and keyboard control to simulate a player interacting with the game.

The bot can:
1. Automatically start the game by entering a player name and clicking the play button.
2. Detect the word to be drawn using basic image processing techniques.
3. Draw predefined shapes (e.g., circle, square) or random lines based on the detected word.
4. Automatically guess words by typing and submitting them.

This project is intended for educational purposes and demonstrates how to integrate multiple Python libraries to create an automated bot for a web-based game.

## Features

- **Selenium WebDriver**: Automates browser interactions, such as navigating to the game URL, entering a player name, and clicking buttons.
- **OpenCV**: Captures and processes screenshots to detect the word to be drawn.
- **PyAutoGUI**: Simulates mouse movements and clicks to draw shapes on the canvas.
- **Pynput**: Simulates keyboard input to guess words.
- **Randomization**: Adds variability to the drawing process for a more natural appearance.

## Requirements

- Python 3.x
- Selenium
- OpenCV (`opencv-python`)
- PyAutoGUI
- Pynput
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/autodraw.git
   cd autodraw
   ```

2. Install the required Python packages:
   ```bash
   pip install selenium opencv-python pyautogui pynput
   ```

3. Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/) and place it in a directory. Update the `chrome_driver_path` variable in the script with the correct path.

4. Run the script:
   ```bash
   python autodraw.py
   ```

## Usage

1. Ensure the game URL (`https://drawaria.online/`) is accessible in your browser.
2. Run the script. The bot will automatically start the game, detect the word, and begin drawing and guessing.
3. Press the `Esc` key to stop the bot at any time.

## Customization

- **Drawing Logic**: Modify the `draw_automatically` function to add more shapes or improve drawing accuracy.
- **Word Detection**: Enhance the `detect_word` function with more advanced image processing or OCR techniques.
- **Guessing Logic**: Update the `guess_word` function to implement a more sophisticated word-guessing strategy.

## Disclaimer

This project is for educational purposes only. Please use it responsibly and avoid disrupting the experience of other players on the platform.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to the project by opening issues or submitting pull requests!