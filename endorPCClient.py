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

# attempt_the_raid will take the number of rebels as an argument. The default is 1.
def attempt_the_raid(number_of_rebels=1):
    maximum_EM = 16 / number_of_rebels + (number_of_rebels - 1) * 2
    i = 0
    EM_stacks = 0
    EM_Uses = 0
    # Initializing the while loop for turn count
    while EM_Uses < maximum_EM:
        # Check for the available moves - note that evasive maneuvers may not exactly match the image
        basic_attack = pyautogui.locateOnScreen(r'Endor_PC_Client\BasicAttack.png', confidence=0.85)
        forest_friends = pyautogui.locateOnScreen(r'Endor_PC_Client\ForestFriends.png', confidence=0.85)
        hasty_repairs = pyautogui.locateOnScreen(r'Endor_PC_Client\HastyRepairs.png', confidence=0.85)
        evasive_maneuvers = pyautogui.locateOnScreen(r'Endor_PC_Client\EvasiveManeuvers.png', confidence=0.85)
        if evasive_maneuvers is not None:
            print("Evasive Maneuvers found")
            pyautogui.click(evasive_maneuvers)
            EM_stacks += 4 * number_of_rebels
            EM_Uses += 1
            i += 1
        elif hasty_repairs is not None:
            print("Hasty Repairs found")
            pyautogui.click(hasty_repairs)
            EM_stacks += 3 * number_of_rebels
            i += 1
        elif forest_friends is not None:
            print("Forest Friends found")
            pyautogui.click(forest_friends)
            EM_stacks += 2 * number_of_rebels
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
    settings = pyautogui.locateOnScreen(r'Endor_PC_Client\SettingsButton.png', confidence=0.85)
    pyautogui.click(settings)
    time.sleep(2)
    # Then we click the Retreat button
    retreat = pyautogui.locateOnScreen(r'Endor_PC_Client\RetreatButton.png', confidence=0.85)
    pyautogui.click(retreat)
    time.sleep(2)
    # We confirm the retreat
    confirm = pyautogui.locateOnScreen(r'Endor_PC_Client\YesButton.png', confidence=0.85)
    pyautogui.click(confirm)
    time.sleep(10)
    # Click the Battle (#)
    battle = pyautogui.locateOnScreen(r'Endor_PC_Client\BattleButton.png', confidence=0.85)
    pyautogui.click(battle)
    time.sleep(5)
    # Click the Leia icon to remove her button - here confidence is lower since she's in motion
    try:
        leia = pyautogui.locateOnScreen(r'Endor_PC_Client\LeiaOrganaName.png', confidence=0.60)
        pyautogui.click(leia)
        time.sleep(2)
    except:
        pass
    # Click the Battle 2 icon
    battle2 = pyautogui.locateOnScreen(r'Endor_PC_Client\BattleIcon2.png', confidence=0.85)
    pyautogui.click(battle2)
    time.sleep(2)
    # Click the Ok 2 icon if it appears
    try:
        ok2 = pyautogui.locateOnScreen(r'Endor_PC_Client\Ok2Icon.png', confidence=0.85)
        pyautogui.click(ok2)
        time.sleep(2)
        # We'll need to click battle2 again
        battle2 = pyautogui.locateOnScreen(r'Endor_PC_Client\BattleIcon2.png', confidence=0.85)
        pyautogui.click(battle2)
    except:
        pass

def check_for_minimum_evasion():
    # As a statistics tracking, we'll take a screenshot and save it as timestamp.png
    # This will allow us to track the number of EM stacks we have at the end of the run for the paper
    #timestamp = time.time()
    #pyautogui.screenshot(f'{timestamp}.png')
    # If we have not met the minimum EM stacks, we will restart the run
    # We'll check by looking for the EM icon, which has a number in the top right corner
    # We'll only need the first digit of the number to determine if we have the minimum stacks
    # The icons to check for are saved as FiftyEvasion.png, FortyEvasion.png, ThirtyEvasion.png
    # If either of these icons are found, we will restart the run - we'll want high confidence for this check
    # Because the icon is small and the number is small, we'll need to be sure we're looking at the right thing, so we'll check multiple times
    for _ in range(3):
        time.sleep(1) # Give the icon time to appear
        fifty_evasion = pyautogui.locateOnScreen(r'Endor_PC_Client\FiftyEvasion.png', confidence=0.90)
        forty_evasion = pyautogui.locateOnScreen(r'Endor_PC_Client\FortyEvasion.png', confidence=0.90)
        thirty_evasion = pyautogui.locateOnScreen(r'Endor_PC_Client\ThirtyEvasion.png', confidence=0.90)
        twenty_evasion = pyautogui.locateOnScreen(r'Endor_PC_Client\TwentyEvasion.png', confidence=0.90)
        if fifty_evasion is not None or forty_evasion is not None or thirty_evasion is not None or twenty_evasion is not None:
            print("Restarting the run")
            return False
    
    #fifty_evasion = pyautogui.locateOnScreen('FiftyEvasion.png', confidence=0.875)
    #forty_evasion = pyautogui.locateOnScreen('FortyEvasion.png', confidence=0.875)
    #thirty_evasion = pyautogui.locateOnScreen('ThirtyEvasion.png', confidence=0.875)
    #twenty_evasion = pyautogui.locateOnScreen('TwentyEvasion.png', confidence=0.875)
    #if fifty_evasion is not None or forty_evasion is not None or thirty_evasion is not None or twenty_evasion is not None:
    #    print("Restarting the run")
    #    return False
    #else:
    #    print("EM stacks are good, returning control to the player")
    #    return True
    print("EM stacks are good, returning control to the player")
    return True
    
def auto_basic():
    # This will only use basic attacks until the end of the run
    number_of_no_moves = 0
    # We'll go until we have 10 turns with no moves, then we'll stop
    while number_of_no_moves < 10:
        basic_attack = pyautogui.locateOnScreen(r'Endor_PC_Client\BasicAttack.png', confidence=0.85)
        if basic_attack is not None:
            print("Basic Attack found")
            pyautogui.click(basic_attack)
            number_of_no_moves = 0
        else:
            print("No move found")
            number_of_no_moves += 1
            print(f"Number of no moves: {number_of_no_moves}")
        time.sleep(1)

ready_for_manual_play = False
em_holders = 1
while not ready_for_manual_play:
    attempt_the_raid(number_of_rebels=em_holders)
    ready_for_manual_play = check_for_minimum_evasion()
    if not ready_for_manual_play:
        start_over()
    else:
        print("Ready for manual play")
        #auto_basic()
        break
