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


    def search_nav_bar(self):
        try:
            print("Buscando el enlace de Fútbol en la barra de navegación")
            # Usa XPATH para seleccionar el enlace de fútbol
            football_link = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/futbol/') and .//span[contains(text(), 'Fútbol')]]"))
            )
            football_link.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error al intentar hacer clic en el enlace de Fútbol: {e}")

    def search_fantasy_link(self):
        try:
            print("Buscando el enlace de ESPN Fantasy Fútbol")
            fantasy_link = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-track-nav_item, 'espn fantasy fútbol')]"))
            )
            fantasy_link.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error al intentar hacer clic en el enlace de ESPN Fantasy Fútbol: {e}")

    def click_mock_draft_now(self):
        try:
            print("Buscando el enlace 'Mock Draft Now'")
            mock_draft_link = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='main-content layout-dbc one-feed']//section[@class='col-three']//div[@class='fantasySignup__footer']//a[contains(text(), 'Mock Draft Now')]"))
            )
            mock_draft_link.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error al intentar hacer clic en el enlace 'Mock Draft Now': {e}")

    def click_join_league(self):
        try:
            print("Buscando el enlace 'Join a League'")
            join_league_link = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='jsx-3009934533 mock-draft-lobby-container']//a[contains(text(), 'Join a League')]"))
            )
            join_league_link.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error al intentar hacer clic en el enlace 'Join a League': {e}")

    def click_join_public_league(self):
        try:
            print("Buscando el botón 'Join a Public League'")
            join_public_league_button = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='onboarding-actions-wrapper']//section[contains(@class, 'Onboarding-Action-Item')]//button[contains(text(), 'Join a Public League')]"))
            )
            join_public_league_button.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error al intentar hacer clic en el botón 'Join a Public League': {e}")

    def click_join_a_league(self):
        try:
            print("Buscando el botón 'Join a League'")
            join_a_league_button = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='Wrapper Card__Content KonaForm__Card__Content']//button[contains(text(), 'Join a League')]"))
            )
            join_a_league_button.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error al intentar hacer clic en el botón 'Join a League': {e}")

    def click_join_this_league(self):
        try:
            print("Buscando el botón 'Join This League'")
            join_this_league_button = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='jsx-693053285 waiting-room_container']//button[contains(text(), 'Join This League')]"))
            )
            join_this_league_button.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error al intentar hacer clic en el botón 'Join This League': {e}")

    def click_edit_pre_draft_rankings(self):
        try:
            print("Buscando el enlace 'Edit Pre-Draft Rankings'")
            edit_pre_draft_rankings_link = WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Edit Pre-Draft Rankings')]"))
            )
            edit_pre_draft_rankings_link.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error al intentar hacer clic en el enlace 'Edit Pre-Draft Rankings': {e}")

    def get_current_url(self) -> str:
        return self.browser.current_url
