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
cap = cv2.VideoCapture(0)

# QR code detection Method
detector = cv2.QRCodeDetector()

while True:
	# Returns a boolean value and the image
	_, img = cap.read()
	
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

