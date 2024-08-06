from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get('https://www.espn.com')

browser.current_url