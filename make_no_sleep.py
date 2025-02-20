import pyautogui
import time

try:
    print("Preventing sleep... Press Ctrl+C to stop.")
    while True:
        pyautogui.moveRel(0, 1)  # Move cursor slightly
        pyautogui.moveRel(0, -1)
        time.sleep(30)  # Adjust interval as needed
except KeyboardInterrupt:
    print("\nSleep prevention stopped.")
