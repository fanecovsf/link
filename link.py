from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import os

class Link:
    def __init__(self, link, driver, sleep=0, headless=bool):

        self.headless = headless
        self.link = link
        self.sleep = sleep
        self.driver = driver
        


    @staticmethod
    def wait(action):
        def wrapper(self, *args, **kwargs):
            x = 0
            while x == 0:
                try:
                    action(self, *args, **kwargs)
                    x += 1

                except Exception as e:
                    print(e)
        
        return wrapper


    def openLink(self):

        match self.driver:
            case "Chrome":
                if self.headless == True:
                    options = webdriver.ChromeOptions()
                    options.add_argument("--headless")
                    options.add_argument('--ignore-certificate-errors')
                    options.add_argument('--allow-running-insecure-content')
                    options.add_argument('--window-size=1920,1080')
                    self.driver = webdriver.Chrome(options=options)
                    self.driver.implicitly_wait(5)

                elif self.headless == False:
                    current_path = os.path.abspath(__file__)
                    current_path = os.path.dirname(current_path)
                    driver_path = os.path.join(current_path, 'chromedriver.exe')
                    
                    if os.path.exists(driver_path):
                        service = Service(driver_path)
                        self.driver = webdriver.Chrome(options=Options(), service=service)

                    else:
                        self.driver = webdriver.Chrome(options=Options())

            case "Firefox":
                self.driver = webdriver.Firefox(options=Options())

        self.driver.get(url=self.link)
        self.actions = ActionChains(self.driver)
        time.sleep(5)

    def quitSite(self):
        self.driver.quit()
    
    def maximize(self):
        self.driver.maximize_window()

    def waitElementClickable(self, elementXpath):
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, elementXpath)))
            return True
        
        except:
            return False
            
    @wait
    def clickElement(self, elementXpath):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, elementXpath))).click()

    @wait
    def sendKeys(self, elementXpath, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, elementXpath))).send_keys(text)

    @wait
    def clearField(self, elementXpath):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_selected((By.XPATH, elementXpath))).clear()

    @wait
    def getValue(self, elementXpath):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, elementXpath)))
        return element.get_attribute('value')
    
    def pressEnter(self):
        self.actions.send_keys(keys.Keys.ENTER)
        self.actions.perform()

    def pressTab(self):
        self.actions.send_keys(keys.Keys.TAB)
        self.actions.perform()

    def pressDown(self):
        self.actions.send_keys(keys.Keys.DOWN)
        self.actions.perform()

    def pressUp(self):
        self.actions.send_keys(keys.Keys.UP)
        self.actions.perform()

    @wait
    def clearText(self, elementXpath):
        self.driver.find_element(By.XPATH, elementXpath).click()
        self.actions.key_down(keys.Keys.CONTROL).send_keys('a').key_up(keys.Keys.CONTROL).perform()
        self.driver.find_element(By.XPATH, elementXpath).send_keys(keys.Keys.BACKSPACE)

    @wait
    def sendKeysName(self, elementName, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, elementName))).send_keys(text)

    def switchWindow(self, index:int):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @wait
    def switchSelector(self, cssSelector):
        frame = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, cssSelector)))
        self.driver.switch_to.frame(frame)

    @wait
    def switchFrameXpath(self, xpath):
        frame = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        self.driver.switch_to.frame(frame)

    def elementExist(self, xpath):
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except:
            return False