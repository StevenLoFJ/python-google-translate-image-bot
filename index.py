from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from helpers.common import randomStringGenerator
from helpers.image import getImageFromUrl
import Xlib.display
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display
import time,flask
display = Display(visible=0, size=(1920, 1080))
display.start()
import pyautogui

pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])


app = flask.Flask(__name__)

@app.route('/')
def index():

    #imgUrl = flask.request.args.get('image_url','')
    imgUrl= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkjvtQ8VnKYCd_F65p0d6HtTy6woyi8ZhKew'
    option = Options()

    option.add_argument('--disable-blink-features=AutomationControlled') #unmark controlled unit di chrome
  
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")  
    #driverPath=''
    driverPath = "/usr/bin/chromedriver"
    service = Service(driverPath)
    fileName =randomStringGenerator()
    dir = os.getcwd()
    image_path = dir + "\\img-temp\\"+fileName+".png"
    getImageFromUrl(imgUrl ,image_path)
    browser = webdriver.Chrome(service=service,options=option)

    #browser.get('https://translate.google.com/?sl=id&tl=en&op=images')
    browser.get('https://www.speedtypingonline.com/typing-test')
    time.sleep(3)

    #image_path = "D:\\Work\\learn\\py\\upload-google-image-translate-bot\\test.png"
    pyautogui.typewrite('testngetik') #force open download file
    time.sleep(1) #force buffer sebelum popup launch
    screenshot_path = 'screenshot.png'
    browser.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
    return screenshot_path
    pyautogui.typewrite(image_path) #force autoGUI input file url
    time.sleep(1) #buffer buat pyautoGUI typing

    pyautogui.press('enter') #buffer submit
    time.sleep(1)
  
    elements = browser.find_elements(By.CLASS_NAME, "Jmlpdc")  # TODO: makesure IDnya ga dynamic
    element= elements[1]
    imageUrl = element.get_attribute('src')

    new_tab_url = imageUrl
    print(imageUrl)
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
    resultPath = dir + "\\result-temp\\"+fileName+".png"
    pyautogui.write(resultPath)
    pyautogui.press('enter')
    time.sleep(2) #buffer buat download
    browser.quit()
    return resultPath

if __name__ == '__main__':
    app.run(port=80)