* [Connect to Wi-Fi](#connect-to-wi-fi)
* [What to do at the start of each day](#what-to-do-at-the-start-of-each-day)
* [What to do at the end of each day](#what-to-do-at-the-end-of-each-day)
* [Other info](#other-info)

## What to do at the start of each day
1. Ensure all cables exept the power cables are plugged in. The mouse, the keyboard and the camera should all be plugged into the USB ports as shown in the picture. The display cable should be plugged into the port closest to the power port as shown in the picture.
![usb_ports](https://github.com/user-attachments/assets/48300acf-0d6c-475c-967b-cb4a5659cbab)
![power_display](https://github.com/user-attachments/assets/0b7293b9-4a4d-415d-ad3d-0887266e987d)
2. Power on the device by plugging in the power cable.
3. Ensure the Pi is connected to the right Wi-Fi network (ckeck [Connect to Wi-Fi](#connect-to-wi-fi)
5. Open the file `start.sh` on the Desktop by double clicking on it end pressing "Execute"
   
![20250515_21h50m07s_grim copy](https://github.com/user-attachments/assets/a06aba71-69e1-4e9d-b695-cefa2f1d3a4e)
![20250515_21h50m07s_grim](https://github.com/user-attachments/assets/ca45248f-8b1a-49da-a6d8-9dd0f843d9e1)

5. After the browser opens on the homepage of materialconnexions, accept the cookies (you will have to do this only once at startup)
6. Congrats! The camera will now automatically read the codes and cycle between the different web pages.

## Connect to Wi-Fi
Click on the Wi-Fi icon on the top right, then go to `Advanced Options`, then `Connect to Hidden Wireless Network`
![20250515_21h57m47s_grim](https://github.com/user-attachments/assets/062f0161-cf75-47ad-bff3-57a3f02bef2a)

Enter the name of the network and choose the appropriate `Wi-Fi Security` option (usually WPA3), then enter the password.
![20250515_21h58m30s_grim](https://github.com/user-attachments/assets/aa627325-554c-4573-ac98-51f09168904a)

## Change allowed URLs
By default, the code opens materialconnexion.com and only allows URLs with that domain to be opened. 
1) To change it, open scanner.py (Click: folder button in the left upper corner > qrscanner folder > scanner.py)
2) Overwrite the URL lines (underlined with red in the picture under) with the respective domain!
![modify-url](https://github.com/user-attachments/assets/f9267d3a-0033-43eb-8117-c26a330b28b9)


## What to do at the end of each day
1. Close the browser by moving the cursor to the top of the screen and pressing the X button.
2. Close the window that shows the view of the camera by pressing `q` while the window is in focus.
3. Close any other opened windows.
4. Select the berry button at the top left, then scroll down to `Shutdown...`, then select `Shutdown` from the menu that pops up.
![20250515_21h44m18s_grim](https://github.com/user-attachments/assets/6e6305a9-165c-45cc-9721-ed13c4a67440)
5. When the display turns off completely you can safely unplug the power cable.

## If something goes wrong
1. Try to close every window on screen and open the `start.sh` file again.
2. If this doesnt solve it:
   1. Open a new terminal window by clicking on the terminal icon at the top left ![20250515_21h50m25s_grim copy](https://github.com/user-attachments/assets/efa1b59e-a824-4bff-901a-939291604172)
   2. Write `cd qrscanner` and then press Enter ![20250515_21h50m25s_grim](https://github.com/user-attachments/assets/3e39949e-96d9-498a-bbc8-3ee713fb8807)
   3. Then write `bin/python3 ./scanner.py` and then press Enter ![20250515_21h51m27s_grim](https://github.com/user-attachments/assets/15a97203-462e-4544-a778-c9f142ae6857)
   4. You should now see Firefox and the camera window pop up.
   5. When Firefox is opened in full screen, accept the cookies.
   6. Congrats! The camera will now automatically read the codes and cycle between the different web pages.
## If something goes REALLY wrong (the Raspberry Pi doesn't load)
You need to reconfigure the SD card. Here is how you do it: 
1. (This is the biggest step) Follow the steps here **on you computer**: [Instructions to download and configure SD card](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system)
   1. Follow the steps of Install an operating system: Install using Imager.
   2. Then follow the in instruction of OS customisation, fill the data accordingly:
   [image]
   3. Then follow the instructions of Write
Now you have your SD card configured. Now you will insert it into the Rasberry Pi and fetch the dependencies:
2. Insert the SD card into the Rasberry Pi and start it like you do in the beginning of the day.
3. Once it has turned on, and you are connected to the WiFi, click in the browser symbol in the upper left corner of the screen.
4. In the browser, manually type https://github.com/I-O-I-O/qrcodescanner/.
5. Click on setup.sh > Download icon (Download raw file)
6. Open your File tree (Folder Icon in the upper left corner of the screen)
7. Move the setup.sh to Home
8. Click on the terminal icon in the upper left corner of the screen
9. In the terminal, write: sh setup.sh
10. Wait until in downloads everything (the last one will be geckodriver), then close the terminal
Now, that you have all the dependencies, time to fetch the code and start it:
11. In the browser on the site https://github.com/I-O-I-O/qrcodescanner/, click on start.sh
12. Click the download icon
13. Open your folder and by dragging and dropping, add start.sh to the Desktop
14. Now, that you have it there, right click > Properites > Permission tab > Select Execute drop down > Anyone > Now you can close it
15. Double click on the icon and click Execute

## Other info
**username:** ioio
**password:** materialautomation
