import tkinter as tk
from tkinter import messagebox
import serial
import serial.tools.list_ports

# Check if the desired port is available
def check_port(port):
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if p.device == port:
            return True
    return False

# Establish connection to the serial port
def connect_to_serial(port):
    try:
        ser = serial.Serial(port, 9600, timeout=1)
        return ser
    except serial.SerialException:
        messagebox.showerror("Connection Error", f"Failed to connect on {port}")
        return None

# Send data to the serial port
def send_data(ser, data):
    if ser:
        ser.write(data.encode())

# Button command function
def on_button_click(ser, color_code):
    send_data(ser, str(color_code))
    print(f"Sent '{dictionary[color_code]}' to {serial_port}")

# Define color dictionary with valid color names or RGB values
dictionary = {
    0: "red",
    1: "blue",
    2: "green",
    3: "yellow",
    4: "cyan",
    5: "pink",
    6: "white",
    7: "orange",
    8: "#3CB371",  # Using RGB for a shade similar to watergreen (MediumSeaGreen)
    9: "violet",
    'a': "off",  # Special code to turn off the LED
    'b': "on",  # Special code to turn on the LED
    'd': "down",  # Special code to decrease brightness
    'u': "up",  # Special code to increase brightness
}

# Serial port configuration
serial_port = "COM6"
if check_port(serial_port):
    ser = connect_to_serial(serial_port)
else:
    ser = None
    messagebox.showinfo("Port Info", "COM6 is not available.")

# Create the main window
root = tk.Tk()
root.title("Color Control Panel")

i = 0
# Create buttons for each color
for idx, color in dictionary.items():
    try:
        btn = tk.Button(root, text=color, bg=color, width=35, height=7,
                        command=lambda idx=idx: on_button_click(ser, idx))
    except tk.TclError:
        # If the color is an RGB value, use a white background
        btn = tk.Button(root, text=color, bg="white", width=35, height=7,
                        command=lambda idx=idx: on_button_click(ser, idx))
    try:
        btn.grid(row=idx // 2, column=idx % 2)  # Adjust layout to your preference
    except TypeError as e:
        btn.grid(row=6 + int(i/2), column=(i % 2))
        i += 1

root.mainloop()

# Close the serial connection on exit
if ser:
    ser.close()
