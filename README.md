# Epic Seven Auto Buyer
This script is a tool for automatically purchasing bookmarks in the game Epic Seven using image recognition.

# Dependencies
pynput
pyautogui
mouse

#Usage
To run the script, use the following command:

python main.py
The script will continuously search for bookmarks on the screen, and if it finds them, it will attempt to purchase them. It will also refresh the page and scroll through the listings to search for more bookmarks.

# Configuration
The script can be configured by modifying the search() function to look for different bookmarks on the screen, and adjusting the confidence parameter in the pyautogui.locateOnScreen() function to fine-tune the accuracy of the image detection. The buy() function can also be modified to fit the specific purchase process for bookmarks in Epic Seven.

# Note
Use caution when running this script, as it may accidentally purchase bookmarks that you did not intend to buy. It is recommended to carefully test the script and adjust the confidence parameter before using it in the game.

# Additional Information
The search() function searches for two specific images on the screen, mystic_banner.png and covenant_banner.png. These images are used to represent bookmarks in the game. If either of these images are found on the screen, the script will click on the image and then run the buy() function.

The scroll() function uses the mouse controller to scroll the page by a fixed amount.

The refresh() function clicks on specific coordinates on the screen twice to refresh the page.

The buy() function clicks on a specific coordinate on the screen, simulating a mouse click to initiate the purchase of a bookmark
