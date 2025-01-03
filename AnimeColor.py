import cv2
import numpy as np
import serial
import time
from typing import Dict

import mss
from PIL import Image
from screeninfo import get_monitors

print(f"Welcome to AnimeColor!")

curr_monitor = get_monitors()[0]
# Settings
s_width = curr_monitor.width
s_height = curr_monitor.height
print(f"Detected monitor size {s_width}x{s_height}")
scalingFactor = 0.1
print(f"Using scaling factor {scalingFactor}")
show = False
interval = 100 # milliseconds
print(f"Color check interval {interval}")

# begin
for serial_port_n in range(3, 20):
    serial_port = f"COM6"
    # print(f"Trying to connect to Arduino on port {serial_port}")
    try:
        arduino = serial.Serial(serial_port, 115200, timeout=0)
        print(f"Connected to Arduino on port {serial_port}")
        break
    except Exception:
        arduino = None
        # print("Connection error!")

if arduino is None:
    print("WARNING: Could not connect to Arduino!")

dictionary: Dict[int, str] = {
    0:"red",
    1:"blue",
    2:"green",
    3:"yellow",
    4:"cyan",
    5:"pink",
    6:"white",
    7:"orange",
    8:"watergreen",
    9:"violet",
    10:"black",
}
prev_blast = 999
i = 0

width = 0
height = 0

prevTime = int(round(time.time() * 1000))
# CAMERA uncomment for general camera input
# cap = cv2.VideoCapture(1)    
frame: np.ndarray
with mss.mss() as sct:
    while(True):

        currentTime = int(round(time.time() * 1000))
        if(currentTime - prevTime >= interval):
            # CAMERA uncomment for general camera input
            # ret, frame = cap.read()

            # The screen part to capture
            monitor = {"top": 0, "left": 0, "width": s_width, "height": s_height}
            sct_img = sct.grab(monitor)
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "RGBX")
            frame = np.array(img)
            
            frameOriginal = frame
            width = int(s_width * scalingFactor)
            height = int(s_height * scalingFactor)
            frame = cv2.resize(frame,(width,height))
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Red color
            imagered = np.zeros((height, width, 3), np.uint8)
            imagered[:] = (0, 0, 255)
            low_red = np.array([0, 80, 80])
            high_red = np.array([10, 255, 255])
            red_mask = cv2.inRange(hsv_frame, low_red, high_red)
            red = cv2.bitwise_and(imagered, imagered, mask=red_mask)
            
            # Yellow color
            imageyellow = np.zeros((height, width, 3), np.uint8)
            imageyellow[:] = (0, 255, 255)
            low_yellow = np.array([20, 80, 80]) #hue 20
            high_yellow = np.array([35, 255, 255])
            yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
            yellow = cv2.bitwise_and(imageyellow, imageyellow, mask=yellow_mask)

            # Orange color
            imageorange = np.zeros((height, width, 3), np.uint8)
            imageorange[:] = (0, 128, 255)
            low_orange = np.array([10, 80, 80]) #hue 20
            high_orange = np.array([20, 255, 255])
            orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
            orange = cv2.bitwise_and(imageorange, imageorange, mask=orange_mask)

            # Green color
            imagegreen = np.zeros((height, width, 3), np.uint8)
            imagegreen[:] = (0, 255, 0)
            low_green = np.array([35, 80, 80])
            high_green = np.array([70, 255, 255])
            green_mask = cv2.inRange(hsv_frame, low_green, high_green)
            green = cv2.bitwise_and(imagegreen, imagegreen, mask=green_mask)

            # Cyan color
            imagecyan = np.zeros((height, width, 3), np.uint8)
            imagecyan[:] = (255, 255, 0)
            low_cyan = np.array([80, 80, 80])
            high_cyan = np.array([100, 255, 255])
            cyan_mask = cv2.inRange(hsv_frame, low_cyan, high_cyan)
            cyan = cv2.bitwise_and(imagecyan, imagecyan, mask=cyan_mask)

            # Waterwatergreen color
            imagewatergreen = np.zeros((height, width, 3), np.uint8)
            imagewatergreen[:] = (128, 255, 0)
            low_watergreen = np.array([60, 80, 80])
            high_watergreen = np.array([80, 255, 255])
            watergreen_mask = cv2.inRange(hsv_frame, low_watergreen, high_watergreen)
            watergreen = cv2.bitwise_and(imagewatergreen, imagewatergreen, mask=watergreen_mask)

            # Blue color
            imageblue = np.zeros((height, width, 3), np.uint8)
            imageblue[:] = (255, 0, 0)
            low_blue = np.array([100, 80, 80])
            high_blue = np.array([140, 255, 255])
            blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
            blue = cv2.bitwise_and(imageblue, imageblue, mask=blue_mask)

            # Pink color
            imagepink = np.zeros((height, width, 3), np.uint8)
            imagepink[:] = (255, 0, 255)
            low_pink = np.array([150, 80, 80])
            high_pink = np.array([170, 255, 255]) #hue 160
            pink_mask = cv2.inRange(hsv_frame, low_pink, high_pink)
            pink = cv2.bitwise_and(imagepink, imagepink, mask=pink_mask)

            # Violet color
            imageviolet = np.zeros((height, width, 3), np.uint8)
            imageviolet[:] = (255, 0, 128)
            low_violet = np.array([130, 80, 80])
            high_violet = np.array([150, 255, 255])
            violet_mask = cv2.inRange(hsv_frame, low_violet, high_violet)
            violet = cv2.bitwise_and(imageviolet, imageviolet, mask=violet_mask)

            # White color
            imagewhite = np.zeros((height, width, 3), np.uint8)
            imagewhite[:] = (255, 255, 255)
            low_white = np.array([0, 0, 80])
            high_white = np.array([255, 80, 255])
            white_mask = cv2.inRange(hsv_frame, low_white, high_white)
            white = cv2.bitwise_and(imagewhite, imagewhite, mask=white_mask)

            imagesum = cv2.add(red, blue)
            imagesum = cv2.add(imagesum, green)
            imagesum = cv2.add(imagesum, yellow)
            imagesum = cv2.add(imagesum, cyan)
            imagesum = cv2.add(imagesum, pink)
            imagesum = cv2.add(imagesum, white)
            imagesum = cv2.add(imagesum, watergreen)
            imagesum = cv2.add(imagesum, orange)
            imagesum = cv2.add(imagesum, violet)

            #0 red, 1 blue, 2 green, 3 yellow, 4 cyan, 5 pink, 6 white, 7 off   (+1)
            # Work out what we are looking for
            # Find all pixels where the 3 RGB values match "sought", and count
            results = []
            #          B G R
            sought = [0,0,255]
            results.append(np.count_nonzero(np.all(imagesum==sought,axis=2)))
            sought = [255,0,0]
            results.append(np.count_nonzero(np.all(imagesum==sought,axis=2)))
            sought = [0,255,0]
            results.append(np.count_nonzero(np.all(imagesum==sought,axis=2)))
            sought = [0,255,255]
            results.append(np.count_nonzero(np.all(imagesum==sought,axis=2)))
            sought = [255,255,0]
            results.append(np.count_nonzero(np.all(imagesum==sought,axis=2)))
            sought = [255,0,255]
            results.append(np.count_nonzero(np.all(imagesum==sought,axis=2)))
            sought = [255,255,255]  
            results.append(np.count_nonzero(np.all(imagesum==sought,axis=2))*0.1)
            sought = [0,128,255]
            results.append(np.count_nonzero(np.all(imagesum==sought,axis=2)))
            sought = [128,255,0]
            results.append(np.count_nonzero(np.all(imagesum==sought,axis=2)))
            sought = [255,0,128]
            results.append(np.count_nonzero(np.all(imagesum==sought,axis=2)))
            max_res = max(results)
            if max_res == 0:
                blast = 10
            else:
                blast = results.index(max_res)
            if blast != 10 and blast != prev_blast:
                if arduino:
                    arduino.write(chr(blast+48).encode())
                prev_blast = blast
                cname: str = dictionary.get(blast, "invalid")
                print(f"[Frame {i}: {currentTime-prevTime-100}ms] Firing {cname}")
                #read serial
                #if arduino:
                #    while arduino.in_waiting:
                #        print(arduino.readline().decode())
            if(show):
                cv2.imshow("frame", frame)
                cv2.imshow("imagesum", imagesum)
            i += 1
            if(cv2.waitKey(1) & 0xFF == ord('q')):
                break
            prevTime = currentTime
        time.sleep(interval/1000)

if arduino:
    print(arduino.name)
    arduino.close()

# cap.release()