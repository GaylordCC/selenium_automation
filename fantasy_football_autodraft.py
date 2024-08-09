from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EspnBrowser:
    browser, service = None, None

    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        options.add_experimental_option("detach", True)
        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service, options=options)

    def open_page(self, url: str):
        self.browser.get(url)
        self.browser.maximize_window()

    def close_browser(self):
        self.browser.quit()

    def switch_to_iframe_by_id(self, iframe_id: str):
        try:
            print(f"Cambiando al iframe con ID = {iframe_id}")
            iframe = WebDriverWait(self.browser, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, iframe_id))
            )
        except Exception as e:
            print(f"Error al cambiar al iframe: {e}")

    def switch_to_default_content(self):
        self.browser.switch_to.default_content()

    def add_input(self, by: By, value: str, text: str):
        try:
            print(f"Buscando el campo con {by} = {value}")
            field = WebDriverWait(self.browser, 20).until(
                EC.visibility_of_element_located((by, value))
            )
            print("Elemento encontrado: ", field.get_attribute('outerHTML'))
            field.clear()
            field.send_keys(text)
            time.sleep(1)
        except Exception as e:
            print(f"Error al intentar escribir en el campo: {e}")

    def click_button(self, by: By, value: str):
        try:
            print(f"Buscando el botón con {by} = {value}")
            button = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((by, value))
            )
            button.click()
            time.sleep(1)
        except Exception as e:
            print(f"Error al intentar hacer clic en el botón: {e}")

    def login_espn(self, InputIdentityFlowValue: str, InputPassword: str):
        self.click_button(by=By.ID, value='global-user-trigger')
        time.sleep(10)
        self.click_button(by=By.XPATH, value="//a[@data-affiliatename='espn' and contains(text(), 'Entrar')]")
        time.sleep(5)
        self.switch_to_iframe_by_id('oneid-iframe')
        self.add_input(by=By.ID, value='InputIdentityFlowValue', text=InputIdentityFlowValue)
        self.click_button(by=By.ID, value='BtnSubmit')
        self.add_input(by=By.ID, value='InputPassword', text=InputPassword)
        self.click_button(by=By.ID, value='BtnSubmit')
        self.switch_to_default_content()


if __name__ == '__main__':
    from espn_secret import EspnSecret

    browser = EspnBrowser()

    browser.open_page('https://www.espn.com.co')
    time.sleep(3)

    browser.login_espn(EspnSecret.email_espn, EspnSecret.password_espn)
    print(EspnSecret.email_espn)
    time.sleep(18)