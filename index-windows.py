# this file is used to test the code in windows environment
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

import pyautogui

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled') #unmark controlled unit di chrome
option.add_argument('--disable-popup-blocking') #unmark controlled unit di chrome

dir = os.getcwd()
image_path = dir + "\\result-temp\\BG4IFTWK0KRO.png"
browser = webdriver.Chrome(options=option)

browser.get('https://translate.google.com/?sl=id&tl=en&op=images')
time.sleep(1)

pyautogui.press('enter') #force open download file
time.sleep(1) #force buffer sebelum popup launch

pyautogui.typewrite(image_path) #force autoGUI input file url
time.sleep(1) #buffer buat pyautoGUI typing

pyautogui.press('enter') #buffer submit

# adding loop to check gradually
elements=[]
retryCounter=0
while len(elements) < 2 and retryCounter < 5:
    print(len(elements))
    elements = browser.find_elements(By.CLASS_NAME, "Jmlpdc")  # TODO: makesure IDnya ga dynamic
    retryCounter = retryCounter + 1
    time.sleep(1)
    
    
element= elements[1]
imageUrl = element.get_attribute('src')
print(imageUrl)
time.sleep(1)
pyautogui.press('enter') #force open download file
time.sleep(1) #force buffer sebelum popup launch

pyautogui.typewrite(image_path) #force autoGUI input file url


time.sleep(1) #buffer buat pyautoGUI typing

pyautogui.press('enter') #buffer submit
time.sleep(1)

element = browser.find_element(By.CLASS_NAME, "Jmlpdc")  # TODO: makesure IDnya ga dynamic
imageUrl = element.get_attribute('src')

new_tab_url = imageUrl
browser.execute_script(f"window.open('{new_tab_url}', '_blank');")
browser.switch_to.window(browser.window_handles[1])
imgElement = browser.find_element(By.TAG_NAME, "img") 
action = ActionChains(browser)
action.context_click(imgElement).perform()
time.sleep(1)
# pyautoGUI klik kanan & save as 
pyautogui.press('down', presses=2, interval=0.1) 
pyautogui.press('enter')
time.sleep(1)
resultPath = dir + "\\result-temp\\test.png"
pyautogui.write(resultPath)
pyautogui.press('enter')
time.sleep(4) #buffer buat download
browser.quit()