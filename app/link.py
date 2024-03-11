from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
import time
from typing import Literal
from .exceptions import KeyException, ExecutionException, DriverDownloadException
import platform
import os
import requests
import zipfile

class Link:
    """
    A instância da classe link será responsável por dar comandos ao navegador de clique, teclas e etc
    url: string do url que deseja abrir com o navegador
    sleep: o tempo de delay padrão entre um comando e outro
    driver: string que só aceita 'Chrome' ou 'Firefox' como valor para definir o navegador a ser usado
    """
    def __init__(self, url: str, sleep: int, driver_path: str = None, browser: Literal['Chrome', 'Firefox'] = 'Chrome') -> None:

        self.url = url
        self.browser = browser
        self.sleep = sleep
        self.driver_path = driver_path


    # Função para testar o funcionamento do driver
    @staticmethod
    def _test() -> bool:
        try:
            _test_instance = Link(url='https://www.google.com/', driver='Chrome', sleep=1)
            _test_instance.open()
            _test_instance.quit()
            return True
        except WebDriverException:
            return False
        
    def _download_driver_last_version(self, index: int) -> None:
        try:
            execution_dir = os.path.dirname(os.path.realpath(__file__))
            url = 'https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json'

            request = requests.get(url)

            data = request.json()

            x = dict(data)

            version = x.get('versions')[index]['version']

            system = platform.system()

            system_map = {
                'Darwin': 'mac-x64',
                'Windows': 'win64',
                'Linux': 'linux64',
            }

            driver_url = f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{version}/{system_map[system]}/chromedriver-{system_map[system]}.zip'

            download_request = requests.get(driver_url)

            if download_request.status_code == 200:
                file_name = 'chromedriver.zip'
                if not os.path.exists(os.path.join(execution_dir, 'driver')):
                    os.mkdir(os.path.join(execution_dir, 'driver'))

                file_name = os.path.join(os.path.join(execution_dir, 'driver'), file_name)

                with open(file_name, 'wb') as file:
                    file.write(download_request.content)

                with zipfile.ZipFile(file_name, 'r') as zip_ref:
                    zip_ref.extractall(os.path.join(execution_dir, 'driver'))

                extracted_dir = os.path.join(os.path.join(execution_dir, 'driver'), f'chromedriver-{system_map[system]}')
                for file in os.listdir(extracted_dir):
                    if 'LICENSE' not in file:
                        os.rename(os.path.join(extracted_dir, file), os.path.join(execution_dir, file))

                self.driver_path = os.path.join(execution_dir, file)
                
        except Exception as e:
            raise DriverDownloadException(str(e))

    # Função para implementação do delay padrão entre as execuções
    def _delay(self) -> None:
        if self.sleep > 0:
            time.sleep(self.sleep)

    def open(self) -> None:
        """
        Função inicial para abertura da url indicada
        irá definir as configurações padrão do navegador antes de abrir
        Redefine o driver para o navegador selecionado
        """
        try:
            if self.browser == "Chrome":
                options = webdriver.ChromeOptions()
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                self.browser = webdriver.Chrome(options=options)

            if self.browser == "Firefox":
                self.browser = webdriver.Firefox(options=Options())

            self.browser.get(url=self.url)
            self.actions = ActionChains(self.browser)
            time.sleep(self.sleep)
        except WebDriverException as e:
            raise WebDriverException(str(e))
        except Exception as e:
            raise ExecutionException(str(e))

    def quit(self) -> None:
        """
        Método utilizado para fechar o navegador
        """
        try:
            self._delay()
            self.browser.quit()
        except Exception as e:
            raise ExecutionException(str(e))
    
    def maximize(self) -> None:
        """
        Método utilizado para maximizar o navegador
        """
        try:
            self._delay()
            self.browser.maximize_window()
        except Exception as e:
            raise ExecutionException(str(e))
        
    def accept_alert(self) -> None:
        """
        Método utilizado para trocar o foco do script para o alerta do navegador
        """
        try:
            self._delay()
            new_driver = self.browser.switch_to.alert
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
                WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
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
                WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
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
            WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
            return True
        except Exception as e:
            raise ExecutionException(str(e))

    def click_element(self, element_xpath: str) -> None:
        """
        Método utilizado para para clicar em um elemento baseado no seu xpath
        """
        try:
            self._delay()
            WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, element_xpath))).click()
        except Exception as e:
            raise ExecutionException(str(e))
        
    def click_query(self, query: str) -> None:
        """
        Método utilizado para enviar clique com base em uma query do elemento
        """
        try:
            self._delay()
            WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, query))).click()
        except Exception as e:
            raise ExecutionException(str(e))

    def send_keys(self, element_xpath: str, text: str) -> None:
        """
        Método utilizado para digitar algo em um campo de texto baseado em seu xpath
        """
        try:
            self._delay()
            WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.XPATH, element_xpath))).send_keys(text)
        except Exception as e:
            raise ExecutionException(str(e))

    def clear_field(self, element_xpath: str) -> None:
        """
        Método utilizado para limpar um campo de texto baseado em seu xpath
        """
        try:
            self._delay()
            WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.XPATH, element_xpath))).clear()
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
            self.browser.find_element(By.XPATH, element_xpath).click()

            system_map = {
                'Darwin': self.actions.key_down(keys.Keys.COMMAND).send_keys('a').key_up(keys.Keys.COMMAND).perform(),
                'Windows': self.actions.key_down(keys.Keys.CONTROL).send_keys('a').key_up(keys.Keys.CONTROL).perform(),
                'Linux': self.actions.key_down(keys.Keys.CONTROL).send_keys('a').key_up(keys.Keys.CONTROL).perform(),
            }

            system_map[platform.system()]

            self.browser.find_element(By.XPATH, element_xpath).send_keys(keys.Keys.BACKSPACE)
        except Exception as e:
            raise ExecutionException(str(e))

    def send_keys_by_name(self, element_name: str, text: str) -> None:
        """
        Método utilizado para digitar algo em um campo de texto baseado no seu name
        """
        try:
            self._delay()
            WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.NAME, element_name))).send_keys(text)
        except Exception as e:
            raise ExecutionException(str(e))

    def switch_window(self, index:int) -> None:
        """
        Método utilizado para alterar a aba de navegação baseado no index (primeira aba = index 0, segunda aba = index 1, etc...)
        """
        try:
            self._delay()
            self.browser.switch_to.window(self.browser.window_handles[index])
        except Exception as e:
            raise ExecutionException(str(e))

    def switch_to_frame(self, xpath: str) -> None:
        """
        Método utilizado para trocar o script para um iframe baseado em seu xpath
        """
        try:
            self._delay()
            self.browser.switch_to.frame(
                WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            )
        except Exception as e:
            raise ExecutionException(str(e))

    def element_exists(self, xpath: str) -> bool:
        """
        Método utilizado para saber se um elemento existe (retorna True ou False)
        """
        try:
            self._delay()
            self.browser.find_element(By.XPATH, xpath)
            return True
        except Exception as e:
            raise ExecutionException(str(e))
        
    def take_screenshot(self, path: str) -> None:
        """
        Método utilizado para tirar screenshot da tela do navegador, é salvo no caminho do path
        """
        try:
            self.browser.save_screenshot(path)
        except Exception as e:
            raise ExecutionException(str(e))        