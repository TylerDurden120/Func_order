from pynput.mouse import Controller
import threading
import time
import pyautogui

# Initialize mouse controller
mouse = Controller()

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Define top and bottom boundaries
TOP_BOUNDARY = 50
BOTTOM_BOUNDARY = screen_height - 5

# Function to restrict mouse movement
def restrict_cursor():
    while True:
        x, y = mouse.position
        # Prevent cursor from going above the top boundary
        if y < TOP_BOUNDARY:
            mouse.position = (x, TOP_BOUNDARY)
        # Prevent cursor from going below the bottom boundary
        elif y > BOTTOM_BOUNDARY:
            mouse.position = (x, BOTTOM_BOUNDARY)
        time.sleep(0.01)  # Reduce CPU usage

# Start a thread to restrict the cursor
restrict_thread = threading.Thread(target=restrict_cursor, daemon=True)
restrict_thread.start()

# Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Script terminated.")
