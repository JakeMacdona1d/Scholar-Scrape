# https://answers.microsoft.com/en-us/windows/forum/all/how-to-enable-a-fake-second-display-in-windows-10/3c02e2ee-cade-4916-be46-390e59ea2a04
# Python program to take
# screenshots

import numpy as np
import cv2
import pyautogui
import tkinter
import os
import time


root = tkinter.Tk()
width = root.winfo_screenwidth() / 2
height = root.winfo_screenheight()
# time.sleep(3)
# take screenshot using pyautogui
# os.system('start "" /max "input.pdf"')

image = pyautogui.screenshot()

# since the pyautogui takes as a
# PIL(pillow) and in RGB we need to
# convert it to numpy array and BGR
# so we can write it to the disk
image = cv2.cvtColor(np.array(image),
					cv2.COLOR_RGB2BGR)

# writing it to the disk using opencv
cv2.imwrite("image1.jpg", image)

path = "image1.jpg"

image = cv2.imread(path)
  
# Naming a window
cv2.namedWindow("Resize", cv2.WINDOW_NORMAL)
  
  
# Using resizeWindow()
cv2.resizeWindow("Resize", width, height)
  
# Displaying the image
cv2.imshow("Resize", image)
cv2.waitKey(0)

