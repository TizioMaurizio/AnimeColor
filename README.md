# Color-Based LED Control System

This project integrates several technologies to create a color-based LED control system. It uses Python with OpenCV to detect the most prominent color displayed on a computer screen. This color data is then sent via USB to an Arduino, which controls an LED lamp to emit the detected color using infrared signals. The system also features a Tkinter-based GUI that allows manual control of the LED colors through user input.

## Project Components

- **Color Detection**: Python script with OpenCV to detect the most present color on the computer screen.
- **Arduino Control**: Arduino script to receive the color data via USB and control the infrared LED to change the LED lamp color.
- **IR Reception**: Arduino setup with an IR sensor to receive signals and verify the transmitted color.
- **GUI Application**: A Tkinter GUI for manual control of the LED colors.

## Hardware Requirements

- Computer with Python 3.x installed.
- Arduino board (e.g., Uno, Mega).
- Infrared LED.
- IR sensor for Arduino.
- USB cable for connecting Arduino to the computer.
- LED color lamp capable of receiving IR signals.

## Software Requirements

- Python 3.x
- OpenCV Python library
- Arduino IDE
- PySerial Python library
- Tkinter Python library (usually included with Python)

## Installation

1. **Python and Libraries**: Ensure Python is installed, then install required libraries:
   ```bash
   pip install opencv-python pyserial

2. **IRremote library**: To flash Arduino you will need the proper version of the IRremote library, you can find it in folder IRremote_2_6_0
