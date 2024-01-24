from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
from typing import Literal
from .exceptions import KeyException, ExecutionException

class Link:
    """
    A instância da classe link será responsável por dar comandos ao navegador de clique, teclas e etc
    url: string do url que deseja abrir com o navegador
    sleep: o tempo de delay padrão entre um comando e outro
    driver: string que só aceita 'Chrome' ou 'Firefox' como valor para definir o navegador a ser usado
    """
    def __init__(self, url: str, sleep: int,  driver: Literal['Chrome', 'Firefox'] = 'Chrome') -> None:

        self.url = url
        self.driver = driver
        self.sleep = sleep


    # Função para implementação do delay padrão entre as execuções
    def _delay(self) -> None:
        if self.sleep > 0:
            time.sleep(self.sleep)


    def openLink(self) -> None:
        """
        Função inicial para abertura da url indicada
        irá definir as configurações padrão do navegador antes de abrir
        Redefine o driver para o navegador selecionado
        """
        try:
            if self.driver == "Chrome":
                options = webdriver.ChromeOptions()
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                self.driver = webdriver.Chrome(options=options)

            if self.driver == "Firefox":
                self.driver = webdriver.Firefox(options=Options())

            self.driver.get(url=self.url)
            self.actions = ActionChains(self.driver)
            time.sleep(self.sleep)
        except Exception as e:
            raise ExecutionException(str(e))

    def quitSite(self) -> None:
        """
        Método utilizado para fechar o navegador
        """
        try:
            self._delay()
            self.driver.quit()
        except Exception as e:
            raise ExecutionException(str(e))
    
    def maximize(self) -> None:
        """
        Método utilizado para maximizar o navegador
        """
        try:
            self._delay()
            self.driver.maximize_window()
        except Exception as e:
            raise ExecutionException(str(e))
        
    def switchToAlert(self) -> Alert:
        """
        Método utilizado para trocar o foco do script para o alerta do navegador
        """
        try:
            self._delay()
            new_driver = self.driver.switch_to.alert
            return new_driver
        except Exception as e:
            raise ExecutionException(str(e))
    
    def moveTo(self, elementXpath: str) -> None:
        """
        Método utilizado para mover o cursor para o elemento baseado em seu xpath
        """
        try:
            self._delay()
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, elementXpath)))
            self.actions.move_to_element(element)
            self.actions.perform()
        except Exception as e:
            raise ExecutionException(str(e))

    def rightClick(self, elementXpath: str) -> None:
        """
        Método utilizado para performar um clique direito em um elemento baseado em seu xpath
        """
        try:
            self._delay()
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, elementXpath)))
            self.actions.context_click(element)
            self.actions.perform()
        except Exception as e:
            raise ExecutionException(str(e))

    def waitElementClickable(self, elementXpath: str) -> bool:
        """
        Método utilizado para aguardar por 60 segundos um elemento se tornar clicável baseado no seu xpath, retorna True quando o elemento for clicável
        """
        try:
            self.delay()
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, elementXpath)))
            return True
        except Exception as e:
            raise ExecutionException(str(e))

    def clickElement(self, elementXpath: str) -> None:
        """
        Método utilizado para para clicar em um elemento baseado no seu xpath
        """
        try:
            self._delay()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, elementXpath))).click()
        except Exception as e:
            raise ExecutionException(str(e))

    def sendKeys(self, elementXpath: str, text: str) -> None:
        """
        Método utilizado para digitar algo em um campo de texto baseado em seu xpath
        """
        try:
            self._delay()
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, elementXpath))).send_keys(text)
        except Exception as e:
            raise ExecutionException(str(e))

    def clearField(self, elementXpath: str):
        """
        Método utilizado para limpar um campo de texto baseado em seu xpath
        """
        try:
            self._delay()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_selected((By.XPATH, elementXpath))).clear()
        except Exception as e:
            raise ExecutionException(str(e))
    
    def pressKey(self, key: str) -> bool:
        """
        Método utilizado para pressionar a tecla baseado na string passada
        """
        key_map = {
            'enter': keys.Keys.ENTER,
            'f11': keys.Keys.F11,
            'tab': keys.Keys.TAB,
            'down': keys.Keys.DOWN,
            'up': keys.Keys.UP,
            'right': keys.Keys.RIGHT,
            'left': keys.Keys.LEFT
        }

        if key.lower() in key_map:
            try:
                self._delay()
                self.actions.send_keys(key_map[key.lower()])
                self.actions.perform()
                return True
            except Exception as e:
                raise ExecutionException(str(e))
        
        raise KeyException(key, key_map)

    def clearText(self, elementXpath: str) -> None:
        """
        Método utilizado para limpar um campo de texto 'manualmente' ou seja, usando o teclado
        É mais recomendado utilizar o método clearField ao invés desse
        """
        try:
            self._delay()
            self.driver.find_element(By.XPATH, elementXpath).click()
            self.actions.key_down(keys.Keys.CONTROL).send_keys('a').key_up(keys.Keys.CONTROL).perform()
            self.driver.find_element(By.XPATH, elementXpath).send_keys(keys.Keys.BACKSPACE)
        except Exception as e:
            raise ExecutionException(str(e))

    def sendKeysName(self, elementName: str, text: str) -> None:
        """
        Método utilizado para digitar algo em um campo de texto baseado no seu name
        """
        try:
            self._delay()
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, elementName))).send_keys(text)
        except Exception as e:
            raise ExecutionException(str(e))

    def switchWindow(self, index:int) -> None:
        """
        Método utilizado para alterar a aba de navegação baseado no index (primeira aba = index 0, segunda aba = index 1, etc...)
        """
        try:
            self._delay()
            self.driver.switch_to.window(self.driver.window_handles[index])
        except Exception as e:
            raise ExecutionException(str(e))

    def switchFrameXpath(self, xpath: str) -> None:
        """
        Método utilizado para trocar o script para um iframe baseado em seu xpath
        """
        try:
            self._delay()
            frame = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.switch_to.frame(frame)
        except Exception as e:
            raise ExecutionException(str(e))

    def elementExists(self, xpath: str) -> bool:
        """
        Método utilizado para saber se um elemento existe (retorna True ou False)
        """
        try:
            self._delay()
            self.driver.find_element(By.XPATH, xpath)
            return True
        except Exception as e:
            raise ExecutionException(str(e))
        
    def takeScreenshot(self, path: str) -> None:
        """
        Método utilizado para tirar screenshot da tela do navegador, é salvo no caminho do path
        """
        try:
            self.driver.save_screenshot(path)
        except Exception as e:
            raise ExecutionException(str(e))        