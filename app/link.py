from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
from typing import Literal
from .exceptions import KeyException, ExecutionException
import platform
from pyvirtualdisplay import Display
import os

class Link:
    """
    A instância da classe link será responsável por dar comandos ao navegador de clique, teclas e etc
    url: string do url que deseja abrir com o navegador
    sleep: o tempo de delay padrão entre um comando e outro
    driver: string que só aceita 'Chrome' ou 'Firefox' como valor para definir o navegador a ser usado
    """
    def __init__(self, url: str, sleep: int, driver: Literal['Chrome', 'Firefox'] = 'Chrome', headless: bool = False, log_path: str = '') -> None:

        self.url = url
        self.driver = driver
        self.sleep = sleep
        self.headless = headless
        self.display = Display(visible=0, size=(1960, 1080))


    # Função para implementação do delay padrão entre as execuções
    def _delay(self) -> None:
        if self.sleep > 0:
            time.sleep(self.sleep)


    def open_link(self) -> None:
        """
        Função inicial para abertura da url indicada
        irá definir as configurações padrão do navegador antes de abrir
        Redefine o driver para o navegador selecionado
        """
        try:
            if self.driver == "Chrome":
                options = webdriver.ChromeOptions()
                if self.headless:
                    prefs = {
                        "download.default_directory": '/home/ghf/Downloads',  
                        "download.prompt_for_download": False,       
                        "directory_upgrade": True,                   
                        "safebrowsing.enabled": True                 
                    }
                    
                    options.add_experimental_option("prefs", prefs)
                    options.add_argument('--headless')
                    options.add_argument('--no-sandbox')
                    options.add_argument('--disable-dev-shm-usage')
                    options.add_argument('--disable-gpu')
                    options.add_argument('--window-size=1960,1080')
                    options.add_argument('--start-maximized')
                    options.add_argument('--disable-features=VizDisplayCompositor')
                    options.add_argument('--ignore-certificate-errors')
                    options.add_argument('--allow-running-insecure-content')
                    options.add_argument('--disable-blink-features=AutomationControlled')
                    options.add_argument('--enable-automation')

                    self.display.start()
                    
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                self.driver = webdriver.Chrome(options=options)

            if self.driver == "Firefox":
                self.driver = webdriver.Firefox(options=Options())

            self.driver.get(url=self.url)
            self.actions = ActionChains(self.driver)
            time.sleep(self.sleep)
        except Exception as e:
            raise ExecutionException(str(e))

    def quit_site(self) -> None:
        """
        Método utilizado para fechar o navegador
        """
        try:
            self._delay()
            self.driver.quit()
            if self.headless:
                self.display.stop()
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
        
    def accept_alert(self) -> None:
        """
        Método utilizado para trocar o foco do script para o alerta do navegador
        """
        try:
            self._delay()
            new_driver = self.driver.switch_to.alert
            new_driver.accept()

        except Exception as e:
            raise ExecutionException(str(e))
    
    def move_to(self, element_xpath: str) -> None:
        """
        Método utilizado para mover o cursor para o elemento baseado em seu xpath
        """
        try:
            self._delay()
            self.actions.move_to_element(
                WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
            )
            self.actions.perform()
        except Exception as e:
            raise ExecutionException(str(e))

    def right_click(self, element_xpath: str) -> None:
        """
        Método utilizado para performar um clique direito em um elemento baseado em seu xpath
        """
        try:
            self._delay()
            self.actions.context_click(
                WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
            )
            self.actions.perform()
        except Exception as e:
            raise ExecutionException(str(e))

    def wait_element_clickable(self, element_xpath: str) -> bool:
        """
        Método utilizado para aguardar por 60 segundos um elemento se tornar clicável baseado no seu xpath, retorna True quando o elemento for clicável
        """
        try:
            self._delay()
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
            return True
        except Exception as e:
            raise ExecutionException(str(e))

    def click_element(self, element_xpath: str) -> None:
        """
        Método utilizado para para clicar em um elemento baseado no seu xpath
        """
        try:
            self._delay()
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, element_xpath))).click()
        except Exception as e:
            raise ExecutionException(str(e))

    def send_keys(self, element_xpath: str, text: str) -> None:
        """
        Método utilizado para digitar algo em um campo de texto baseado em seu xpath
        """
        try:
            self._delay()
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, element_xpath))).send_keys(text)
        except Exception as e:
            raise ExecutionException(str(e))

    def clear_field(self, element_xpath: str) -> None:
        """
        Método utilizado para limpar um campo de texto baseado em seu xpath
        """
        try:
            self._delay()
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, element_xpath))).clear()
        except Exception as e:
            raise ExecutionException(str(e))
    
    def press_key(self, key: str) -> bool:
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

    def clear_text(self, element_xpath: str) -> None:
        """
        Método utilizado para limpar um campo de texto 'manualmente' ou seja, usando o teclado
        É mais recomendado utilizar o método clearField ao invés desse
        Método tem suporte para MacOS, trocando o ctrl para command
        """
        try:
            self._delay()
            self.driver.find_element(By.XPATH, element_xpath).click()

            system_map = {
                'Darwin': self.actions.key_down(keys.Keys.COMMAND).send_keys('a').key_up(keys.Keys.COMMAND).perform(),
                'Windows': self.actions.key_down(keys.Keys.CONTROL).send_keys('a').key_up(keys.Keys.CONTROL).perform(),
                'Linux': self.actions.key_down(keys.Keys.CONTROL).send_keys('a').key_up(keys.Keys.CONTROL).perform(),
            }

            system_map[platform.system()]

            self.driver.find_element(By.XPATH, element_xpath).send_keys(keys.Keys.BACKSPACE)
        except Exception as e:
            raise ExecutionException(str(e))

    def send_keys_by_name(self, element_name: str, text: str) -> None:
        """
        Método utilizado para digitar algo em um campo de texto baseado no seu name
        """
        try:
            self._delay()
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.NAME, element_name))).send_keys(text)
        except Exception as e:
            raise ExecutionException(str(e))

    def switch_window(self, index:int) -> None:
        """
        Método utilizado para alterar a aba de navegação baseado no index (primeira aba = index 0, segunda aba = index 1, etc...)
        """
        try:
            self._delay()
            self.driver.switch_to.window(self.driver.window_handles[index])
        except Exception as e:
            raise ExecutionException(str(e))

    def switch_to_frame(self, xpath: str) -> None:
        """
        Método utilizado para trocar o script para um iframe baseado em seu xpath
        """
        try:
            self._delay()
            self.driver.switch_to.frame(
                WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            )
        except Exception as e:
            raise ExecutionException(str(e))

    def element_exists(self, xpath: str) -> bool:
        """
        Método utilizado para saber se um elemento existe (retorna True ou False)
        """
        try:
            self._delay()
            self.driver.find_element(By.XPATH, xpath)
            return True
        except Exception as e:
            raise ExecutionException(str(e))
        
    def take_screenshot(self, path: str) -> None:
        """
        Método utilizado para tirar screenshot da tela do navegador, é salvo no caminho do path
        """
        try:
            self.driver.save_screenshot(path)
        except Exception as e:
            raise ExecutionException(str(e))

    def element_text(self, xpath: str) -> str:
        """
        Método utilizado para extrair o valor em string dentro da tag HTML baseado no xpath
        """
        try:
            self._delay()
            return WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, xpath))).text
        except Exception as e:
            raise ExecutionException(str(e))
        
    def click_query(self, query: str) -> None:
        """
        Método utilizado para enviar clique com base em uma query do elemento
        """
        try:
            self._delay()
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, query))).click()
        except Exception as e:
            raise ExecutionException(str(e))
        
    def refresh(self) -> None:
        """
        Método utilizado para dar refresh na página
        """
        try:
            self.driver.refresh()
        except Exception as e:
            raise ExecutionException(str(e))
        
    def execute_script(self, script: str) -> None:
        """
        Método para executar javascript na instância
        """
        try:
            self._delay()
            self.driver.execute_script(script)
        except Exception as e:
            raise ExecutionException(str(e))
