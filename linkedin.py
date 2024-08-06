from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class Browser:
    browser, service = None, None

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        options.add_experimental_option("detach", True)
        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service, options=options)

    def open_page(self, url: str):
        self.browser.get(url)

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

    def login_linkedin(self, username: str, password: str):
        self.add_input(by=By.ID, value='username', text=username)
        self.add_input(by=By.ID, value='password', text=password)
        self.click_button(by=By.CLASS_NAME, value='login__form_action_container ')


if __name__ == '__main__':
    from secret import Secret

    browser = Browser()

    browser.open_page('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')
    time.sleep(3)

    browser.login_linkedin(Secret.email, Secret.password)
    time.sleep(18)


    # browser.close_browser()
