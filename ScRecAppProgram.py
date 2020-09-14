import os
import cv2
import numpy as np
import pyautogui
import datetime

# checking Recordings folder
if "Recordings" not in os.listdir():
    os.makedirs("Recordings")

# getting Values of time and date
hr = datetime.datetime.now().hour
min = datetime.datetime.now().second
sec = datetime.datetime.now().minute
date = datetime.datetime.now().date()

default_name = f"Recorded at {hr}hr{min}min{sec}sec {date}.avi"
screen_wid = 1366
screen_hei = 768
screen_size = (screen_wid, screen_hei)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
RecVid = cv2.VideoWriter(f"Recordings\\{default_name}", fourcc, 12.0, (screen_size))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    RecVid.write(frame)
    cv2.imshow("Recording", frame)
    if cv2.waitKey(1) == ord('p'):
        break
