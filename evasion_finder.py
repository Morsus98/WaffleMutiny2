import cv2
import numpy as np
import pyautogui
import pytesseract

# Example icon image (replace this with your actual icon image)
icon_image = cv2.imread('icon.png', cv2.IMREAD_GRAYSCALE)

# Find the location of the icon using PyAutoGUI
icon_locations = []
# Define the starting point for searching the icon
start_x = 100
start_y = 100

for i in range(3):  # Assuming the icon can appear up to 3 times
    icon_location = pyautogui.locateOnScreen('evasion.png', confidence=0.8, region=(start_x, start_y, pyautogui.size().width - start_x, pyautogui.size().height - start_y))
    if icon_location:
        is_duplicate = False
        for existing_location in icon_locations:
            if abs(icon_location.left - existing_location.left) < 5 and abs(icon_location.top - existing_location.top) < 5:
                is_duplicate = True
                break
        if not is_duplicate:
            icon_locations.append(icon_location)
    else:
        break

# Convert the screenshot to OpenCV format
screenshot = pyautogui.screenshot()
screenshot_cv = np.array(screenshot)
screenshot_cv = cv2.cvtColor(screenshot_cv, cv2.COLOR_RGB2BGR)

# Define a region of interest (ROI) around each icon and sum the numbers
sum_of_numbers = 0
for icon_location in icon_locations:
    icon_center = (icon_location.left + icon_location.width // 2, icon_location.top + icon_location.height // 2)
    roi_top_left = (icon_center[0] + 1, icon_center[1] - 1)
    roi_bottom_right = (icon_center[0] + 10, icon_center[1] - 10)
    number_roi = screenshot_cv[roi_top_left[1]:roi_bottom_right[1], roi_top_left[0]:roi_bottom_right[0]]
    number_text = pytesseract.image_to_string(number_roi, config='--psm 8 digits')
    if number_text.isdigit():
        sum_of_numbers += int(number_text)

print("Sum of numbers associated with the icon:", sum_of_numbers)
