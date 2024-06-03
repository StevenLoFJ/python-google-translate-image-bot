from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pyautogui

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled') #unmark controlled unit di chrome
dir = os.getcwd()
image_path = dir + "\\img-temp\\test.png"
browser = webdriver.Chrome(options=option)

browser.get('https://translate.google.com/?sl=id&tl=en&op=images')
time.sleep(1)

#image_path = "D:\\Work\\learn\\py\\upload-google-image-translate-bot\\test.png"

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
#ActionChains(browser).move_to_element(button).click(button).perform()
#browser.quit()