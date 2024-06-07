from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from helpers.common import randomStringGenerator
from helpers.aws import uploadToS3
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
dir = os.getcwd()
@app.route('/')
def index():
    imgUrl = flask.request.args.get('image_url','')
    option = Options()
    
    option.add_argument('--disable-blink-features=AutomationControlled') #unmark controlled unit di chrome
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")  
    
    driverPath = "/usr/bin/chromedriver"
    service = Service(driverPath)
    fileName =randomStringGenerator()
    image_path = dir + "/img-temp/"+fileName+".png"
    getImageFromUrl(imgUrl ,image_path)
    browser = webdriver.Chrome(service=service,options=option)

    browser.get('https://translate.google.com/?sl=id&tl=en&op=images')
    time.sleep(3)

    pyautogui.press('enter') #force open download file
    time.sleep(1) #force buffer sebelum popup launch

    pyautogui.typewrite(image_path) #force autoGUI input file url
    time.sleep(1) #buffer buat pyautoGUI typing

    pyautogui.press('enter') #buffer submit
  
    # adding loop to check gradually
    elements=[]
    retryCounter=0
    while len(elements) < 2 and retryCounter < 5:  # max buffer 5 detik, lebih dianggap gagal
        elements = browser.find_elements(By.CLASS_NAME, "Jmlpdc")  # TODO: makesure IDnya ga dynamic
        retryCounter = retryCounter + 1
        print('loop',elements)
        time.sleep(1)
        
    element= elements[1]
    imageUrl = element.get_attribute('src')

    browser.execute_script(f"window.open('{imageUrl}', '_blank');")
    browser.switch_to.window(browser.window_handles[1])
    imgElement = browser.find_element(By.TAG_NAME, "img") 
    action = ActionChains(browser)
    action.context_click(imgElement).perform()
    time.sleep(1)
    
    # pyautoGUI klik kanan & save as 
    pyautogui.press('down', presses=2, interval=0.1) 
    pyautogui.press('enter')
    time.sleep(1)
    

    resultPath = dir + "/result-temp/"+fileName
    pyautogui.write(resultPath)
    pyautogui.press('enter')
    time.sleep(2) #buffer buat download
    uploadDir = dir + "/result-temp/"
    s3Url = uploadToS3(uploadDir,'itemku-upload-alpha',f'{fileName}.png')
    browser.quit()
    return s3Url

if __name__ == '__main__':
    app.run(port=80)