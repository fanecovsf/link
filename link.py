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
    def __init__(self, link, driver, sleep=0, headless=False, sleep_notifications=True):

        self.headless = headless
        self.link = link
        self.sleep = sleep
        self.driver = driver
        self.sleep_notifications = sleep_notifications



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
    
    @staticmethod
    def sleep_wait(action):
        def wrapper(self, *args, **kwargs):
            if self.sleep_notifications:
                print(f'Waiting {self.sleep} seconds...')
            time.sleep(self.sleep)
            action(self, *args, **kwargs)
        
        return wrapper


    def openLink(self):

        match self.driver:
            case "Chrome":
                if self.headless == True:
                    print('Headless mode is not implemented yet, turning to false automatically...')
                    self.headless = False
                    '''
                    options = webdriver.ChromeOptions()
                    options.add_argument("--headless")
                    options.add_argument('--ignore-certificate-errors')
                    options.add_argument('--allow-running-insecure-content')
                    options.add_argument('--window-size=1920,1080')
                    self.driver = webdriver.Chrome(options=options)
                    self.driver.implicitly_wait(5)
                    '''
                    current_path = os.path.abspath(__file__)
                    current_path = os.path.dirname(current_path)
                    driver_path = os.path.join(current_path, 'chromedriver.exe')
                    
                    if os.path.exists(driver_path):
                        service = Service(driver_path)
                        self.driver = webdriver.Chrome(options=Options(), service=service)

                    else:
                        self.driver = webdriver.Chrome(options=Options())

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

    @sleep_wait
    def quitSite(self):
        self.driver.quit()
    
    @sleep_wait
    def maximize(self):
        self.driver.maximize_window()

    @sleep_wait
    def switchToAlert(self):
        new_driver = self.driver.switch_to.alert

        return new_driver

    @sleep_wait
    def waitElementClickable(self, elementXpath):
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, elementXpath)))
            return True
        
        except:
            return False

    @sleep_wait         
    @wait
    def clickElement(self, elementXpath):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, elementXpath))).click()

    @sleep_wait
    @wait
    def sendKeys(self, elementXpath, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, elementXpath))).send_keys(text)

    @sleep_wait
    @wait
    def clearField(self, elementXpath):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_selected((By.XPATH, elementXpath))).clear()

    @sleep_wait
    @wait
    def getValue(self, elementXpath):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, elementXpath)))
        return element.get_attribute('value')
    
    @sleep_wait
    def pressEnter(self):
        self.actions.send_keys(keys.Keys.ENTER)
        self.actions.perform()

    @sleep_wait
    def pressTab(self):
        self.actions.send_keys(keys.Keys.TAB)
        self.actions.perform()

    @sleep_wait
    def pressDown(self):
        self.actions.send_keys(keys.Keys.DOWN)
        self.actions.perform()

    @sleep_wait
    def pressUp(self):
        self.actions.send_keys(keys.Keys.UP)
        self.actions.perform()

    @sleep_wait
    @wait
    def clearText(self, elementXpath):
        self.driver.find_element(By.XPATH, elementXpath).click()
        self.actions.key_down(keys.Keys.CONTROL).send_keys('a').key_up(keys.Keys.CONTROL).perform()
        self.driver.find_element(By.XPATH, elementXpath).send_keys(keys.Keys.BACKSPACE)

    @sleep_wait
    @wait
    def sendKeysName(self, elementName, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, elementName))).send_keys(text)

    @sleep_wait
    def switchWindow(self, index:int):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @sleep_wait
    @wait
    def switchSelector(self, cssSelector):
        frame = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, cssSelector)))
        self.driver.switch_to.frame(frame)

    @sleep_wait
    @wait
    def switchFrameXpath(self, xpath):
        frame = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        self.driver.switch_to.frame(frame)

    @sleep_wait
    def elementExist(self, xpath):
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except:
            return False
        