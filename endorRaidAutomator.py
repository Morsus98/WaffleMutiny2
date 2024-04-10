# Author: Morsus98
# This script is a simple brute force method that should result in a simplistic run of the Endor raid that
# leaves the player near the last wave of the raid. Manual play will be required for the last wave.

import pyautogui
import time
import numpy as np
import cv2

# The script follows a simple loop.
# The script has a maximum number of turns that it will run before it stops.
# To take a turn, it will grab a screenshot of the raid and check for one of the four possible moves.
# Moves are  stored as images in the same directory as the script.
# The moves have the following priority: Evasive Maneuvers, Hasty Repairs, Forest Friends, and Basic Attack.
# The script will not count a turn if it is unable to find a move to make.

maximum_turns = 50
i = 0
EM_stacks = 0
# Initializing the while loop for turn count
while i < maximum_turns:
    # Check for the available moves - note that evasive maneuvers may not exactly match the image
    basic_attack = pyautogui.locateOnScreen('basic_attack.png', confidence=0.85)
    forest_friends = pyautogui.locateOnScreen('forest_friends.png', confidence=0.85)
    hasty_repairs = pyautogui.locateOnScreen('hasty_repairs.png', confidence=0.85)
    evasive_maneuvers = pyautogui.locateOnScreen('evasive_maneuvers.png', confidence=0.85)
    if evasive_maneuvers is not None and EM_stacks < 65:
        print("Evasive Maneuvers found")
        pyautogui.click(evasive_maneuvers)
        EM_stacks += 4
        i += 1
    elif hasty_repairs is not None:
        print("Hasty Repairs found")
        pyautogui.click(hasty_repairs)
        #EM_stacks += 3
        i += 1
    elif forest_friends is not None:
        print("Forest Friends found")
        pyautogui.click(forest_friends)
        #EM_stacks += 2
        i += 1
    elif basic_attack is not None:
        print("Basic Attack found")
        pyautogui.click(basic_attack)
        i += 1
    else:
        print("No move found")
    # Wait 2 seconds for the next turn to finish loading
    time.sleep(1)

# I want a new function to restart if the run is not going well to minimize the time spent on a bad run.
def start_over():
    # First, we click the settings button
    settings = pyautogui.locateOnScreen('SettingsButton.png', confidence=0.85)
    pyautogui.click(settings)
    time.sleep(2)
    # Then we click the Retreat button
    retreat = pyautogui.locateOnScreen('RetreatButton.png', confidence=0.85)
    pyautogui.click(retreat)
    time.sleep(2)
    # We confirm the retreat
    confirm = pyautogui.locateOnScreen('YesButton.png', confidence=0.85)
    pyautogui.click(confirm)
    time.sleep(2)
    # Click the Battle (#)
    battle = pyautogui.locateOnScreen('BattleButton.png', confidence=0.85)
    pyautogui.click(battle)
    time.sleep(2)
    # Click the Leia icon to remove her button
    try:
        leia = pyautogui.locateOnScreen('LeiaIcon.png', confidence=0.85)
        pyautogui.click(leia)
        time.sleep(2)
    except:
        pass
    # Click the Battle 2 icon to start the raid
    battle2 = pyautogui.locateOnScreen('BattleIcon2.png', confidence=0.85)
    pyautogui.click(battle2)
    time.sleep(2)
    # Click the Ok 2 icon if it appears
    try:
        ok2 = pyautogui.locateOnScreen('Ok2Icon.png', confidence=0.85)
        pyautogui.click(ok2)
        time.sleep(2)
        # We'll need to click battle2 again
        battle2 = pyautogui.locateOnScreen('BattleIcon2.png', confidence=0.85)
    except:
        pass

