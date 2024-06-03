from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from helpers.common import randomStringGenerator
from helpers.image import getImageFromUrl
import os

#os.environ['DISPLAY'] = ':0'
import os,pyautogui,time,flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    imgUrl = flask.request.args.get('image_url','')
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled') #unmark controlled unit di chrome
   #option.add_argument("no-sandbox")
    #option.add_argument("headless")
    # option.add_argument("disable-gpu")
    driverPath=''
    #driverPath = "/usr/bin/chromedriver"
    fileName =randomStringGenerator()
    print(fileName)
    dir = os.getcwd()
    image_path = dir + "\\img-temp\\"+fileName+".png"
    getImageFromUrl(imgUrl ,image_path)
    browser = webdriver.Chrome(options=option)

    browser.get('https://translate.google.com/?sl=id&tl=en&op=images')
    time.sleep(3)

    #image_path = "D:\\Work\\learn\\py\\upload-google-image-translate-bot\\test.png"

    pyautogui.press('enter') #force open download file
    time.sleep(1) #force buffer sebelum popup launch

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
    app.run(debug=True)