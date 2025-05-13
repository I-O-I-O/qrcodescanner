# Origial code from 'Tim' at Core Electronics: https://core-electronics.com.au/guides/raspberry-pi/QR-codes-raspberry-pi/#Soft
# Edited by: Eszter Kovacs and Filippo De Togni, IOIO Lab, Malmö University, 2025

import cv2
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()

#options.add_argument('--kiosk')  # Or '--headless' if no display
service = Service(executable_path='/usr/local/bin/geckodriver') 

selenium = webdriver.Firefox(service=service, options=options)

default_url = "https://materialconnexion.com"
selenium.get(default_url)
selenium.fullscreen_window()

lastData = default_url
pattern = r"^https://([a-zA-Z0-9-]+\.)*materialconnexion\.com(/.*)?$"

# Set VideoCapture to 1 while testing on a laptop to use the external camera
# TODO: Change to 0 when using the camera on the Raspberry Pi

def find_camera():
    for index in range(2):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print(f"Camera found at index {index}")
            return cap
        cap.release()
    return None

cap = find_camera()

# QR code detection Method
detector = cv2.QRCodeDetector()

while True:
	# Returns a boolean value and the image
	ret, img = cap.read()
	if not ret or img is None:
		print("Failed to capture image from camera.")
		continue
	data, bbox, _ = detector.detectAndDecode(img)
	if data:
		if re.match(pattern, data):
			print("data found: ", data)
			print("previous detection: ", lastData)
			if not data == lastData:
				selenium.get(data)
				selenium.fullscreen_window()
			lastData = data
	cv2.imshow("code detector", img)
	if(cv2.waitKey(1) == ord("q")):
		break

cap.release()
cv2.destroyAllWindows()
selenium.quit() 

