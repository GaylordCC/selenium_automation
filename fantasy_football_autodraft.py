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
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_espn(self, InputIdentityFlowValue: str, password: str):
        self.click_button(by=By.ID, value='global-user-trigger')
        time.sleep(10)
        self.click_button(by=By.XPATH, value="//a[@data-affiliatename='espn' and contains(text(), 'Entrar')]")
        self.add_input(by=By.ID, value='InputIdentityFlowValue', text=InputIdentityFlowValue)
        # self.click_button(by=By.XPATH, value="//button[@type='submit']")
        # self.click_button(by=By.CLASS_NAME, value='d-grid gap-2')
        # self.add_input(by=By.ID, value='input-InputPassword form-control', text=password)
        # self.click_button(by=By.CLASS_NAME, value='btn btn-submit btn-primary')



if __name__ == '__main__':
    from espn_secret import EspnSecret

    browser = EspnBrowser()

    browser.open_page('https://www.espn.com.co')
    time.sleep(3)

    browser.login_espn(EspnSecret.email_espn, EspnSecret.password_espn)
    time.sleep(18)