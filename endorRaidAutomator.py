# Author: Morsus98
# This script is a simple brute force method that should result in a simplistic run of the Endor raid that
# leaves the player near the last wave of the raid. Manual play will be required for the last wave.

import pyautogui
import time

# The script follows a simple loop.
# The script has a maximum number of turns that it will run before it stops.
# To take a turn, it will grab a screenshot of the raid and check for one of the four possible moves.
# Moves are  stored as images in the same directory as the script.
# The moves have the following priority: Evasive Maneuvers, Hasty Repairs, Forest Friends, and Basic Attack.
# The script will not count a turn if it is unable to find a move to make.

maximum_turns = 50
i = 0
# Initializing the while loop for turn count
while i < maximum_turns:
    # Take a screenshot of the raid, which is found in the Bluestacks window
    # raid_screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    # Check for the move Evasive Maneuvers - note that evasive maneuvers may not exactly match the image
    evasive_maneuvers = pyautogui.locateOnScreen('evasive_maneuvers.png', confidence=0.9)
    # If Evasive Maneuvers is found, click on it
    if evasive_maneuvers is not None:
        pyautogui.click(evasive_maneuvers)
        print("Using Evasive Maneuvers")
    # If Evasive Maneuvers is not found, check for Hasty Repairs
    if evasive_maneuvers is None:
        hasty_repairs = pyautogui.locateOnScreen('hasty_repairs.png', confidence=0.9)
    # If Hasty Repairs is found, click on it
    if hasty_repairs is not None:
        pyautogui.click(hasty_repairs)
        print("Using Hasty Repairs")
    # If Hasty Repairs is not found, check for Forest Friends
    if hasty_repairs is None:
        forest_friends = pyautogui.locateOnScreen('forest_friends.png', confidence=0.9)
    # If Forest Friends is found, click on it
    if forest_friends is not None:
        pyautogui.click(forest_friends)
        print("Using Forest Friends")
    # If Forest Friends is not found, click on Basic Attack
    if forest_friends is None:
        basic_attack = pyautogui.locateOnScreen('basic_attack.png', confidence=0.9)
    # If Basic Attack is found, click on it
    if basic_attack is not None:
        pyautogui.click(basic_attack)
        print("Using Basic Attack")
    # If no move is found, do not count the turn
    if basic_attack is None:
        i -= 1
        print("No move found, waiting for opponent to take their turn")
    i += 1
    # Wait 0.5 seconds for the next turn
    time.sleep(0.5)