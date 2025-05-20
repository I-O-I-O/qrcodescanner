# Original code from 'Tim' at Core Electronics: https://core-electronics.com.au/guides/raspberry-pi/QR-codes-raspberry-pi/#Soft
# Edited by: Eszter Kovacs and Filippo De Togni, IOIO Lab, Malmö University, 2025
# Updated for robustness with pyzbar and try/except by ChatGPT, 2025

import cv2
import re
from pyzbar.pyzbar import decode
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# Configure Selenium WebDriver
options = Options()
# options.add_argument('--kiosk')  # Uncomment for fullscreen kiosk mode
# options.add_argument('--headless')  # Uncomment for headless mode (no display)
service = Service(executable_path='/usr/local/bin/geckodriver')
selenium = webdriver.Firefox(service=service, options=options)

# Default page and matching pattern
default_url = "https://materialconnexion.com"
selenium.get(default_url)
selenium.fullscreen_window()

lastData = default_url
pattern = r"^https://([a-zA-Z0-9-]+\.)*materialconnexion\.[a-zA-Z]{2,}(/.*)?$"

# Function to find an available camera
def find_camera():
    for index in range(2):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print(f"Camera found at index {index}")
            return cap
        cap.release()
    return None

cap = find_camera()

if not cap:
    print("No camera found. Exiting.")
    selenium.quit()
    exit()

# Main loop
try:
    while True:
        ret, img = cap.read()
        if not ret or img is None:
            continue

        try:
            codes = decode(img)
            for code in codes:
                data = code.data.decode('utf-8')
                if re.match(pattern, data):
                    print("data found: ", data)
                    print("previous detection: ", lastData)
                    if data != lastData:
                        selenium.get(data)
                        selenium.fullscreen_window()
                    lastData = data
        except Exception as e:
            print("Error decoding QR code:", e)

        cv2.imshow("code detector", img)
        if cv2.waitKey(1) == ord("q"):
            break

except KeyboardInterrupt:
    print("Interrupted by user.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    selenium.quit()
