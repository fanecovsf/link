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
    def __init__(self, link, sleep:int,  driver="Chrome", headless=False, delay_notifications=False, driver_path=None):

        self.headless = headless
        self.link = link
        self.driver = driver
        self.sleep = sleep
        self.delay_notification = delay_notifications
        self.driver_path = driver_path


    def _delay(self):
        if self.sleep > 0:
            if self.delay_notification:
                print(f'Waiting {self.sleep} seconds...')
            time.sleep(self.sleep)



    def openLink(self):

        match self.driver:
            case "Chrome":
                options = webdriver.ChromeOptions()
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
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
                    
                    if os.path.exists(self.driver_path):
                        service = Service(self.driver_path)
                        self.driver = webdriver.Chrome(options=options, service=service)

                    else:
                        self.driver = webdriver.Chrome(options=options)

                elif self.headless == False:
                    if self.driver_path:
                        if os.path.exists(self.driver_path):
                            service = Service(self.driver_path)
                            self.driver = webdriver.Chrome(options=options, service=service)

                    else:
                        self.driver = webdriver.Chrome(options=options)

            case "Firefox":
                self.driver = webdriver.Firefox(options=Options())

        self.driver.get(url=self.link)
        self.actions = ActionChains(self.driver)
        time.sleep(5)

    def quitSite(self):
        self._delay()
        self.driver.quit()
    
    def maximize(self):
        self._delay()
        self.driver.maximize_window()
        
    def switchToAlert(self):
        self._delay()
        new_driver = self.driver.switch_to.alert
        return new_driver
    
    def moveTo(self, elementXpath):
        self._delay()
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, elementXpath)))
        self.actions.move_to_element(element)
        self.actions.perform()

    def rightClick(self, elementXpath):
        self._delay()
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, elementXpath)))
        self.actions.context_click(element)
        self.actions.perform()

    def waitElementClickable(self, elementXpath):
        self._delay()
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, elementXpath)))
            return True
        
        except:
            return False

    def clickElement(self, elementXpath):
        self._delay()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, elementXpath))).click()

    def sendKeys(self, elementXpath, text):
        self._delay()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, elementXpath))).send_keys(text)

    def clearField(self, elementXpath):
        self._delay()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_selected((By.XPATH, elementXpath))).clear()

    def getValue(self, elementXpath):
        self._delay()
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, elementXpath)))
        return element.get_attribute('value')
    
    def pressEnter(self):
        self._delay()
        self.actions.send_keys(keys.Keys.ENTER)
        self.actions.perform()

    def pressTab(self):
        self._delay()
        self.actions.send_keys(keys.Keys.TAB)
        self.actions.perform()

    def pressDown(self):
        self._delay()
        self.actions.send_keys(keys.Keys.DOWN)
        self.actions.perform()

    def pressUp(self):
        self._delay()
        self.actions.send_keys(keys.Keys.UP)
        self.actions.perform()

    def clearText(self, elementXpath):
        self._delay()
        self.driver.find_element(By.XPATH, elementXpath).click()
        self.actions.key_down(keys.Keys.CONTROL).send_keys('a').key_up(keys.Keys.CONTROL).perform()
        self.driver.find_element(By.XPATH, elementXpath).send_keys(keys.Keys.BACKSPACE)

    def sendKeysName(self, elementName, text):
        self._delay()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, elementName))).send_keys(text)

    def switchWindow(self, index:int):
        self._delay()
        self.driver.switch_to.window(self.driver.window_handles[index])

    def switchSelector(self, cssSelector):
        self._delay()
        frame = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, cssSelector)))
        self.driver.switch_to.frame(frame)

    def switchFrameXpath(self, xpath):
        self._delay()
        frame = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        self.driver.switch_to.frame(frame)

    def elementExist(self, xpath):
        self._delay()
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except:
            return False
        
    def takeScreenshot(self, path):
        self.driver.save_screenshot(path)
        