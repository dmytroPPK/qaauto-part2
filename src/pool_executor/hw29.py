from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os
from urllib.parse import urlparse


def make_site_screenshot(url: str, browser: str, img_dir='screenshots'):

    img_name = urlparse(url).netloc.replace(".", "_") + f"_{browser}.png"
    img_path = os.path.join(os.getcwd(), img_dir, img_name)

    img_dir_path = os.path.dirname(img_path)
    if not os.path.exists(img_dir_path):
        os.makedirs(img_dir_path)

    if browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        raise ValueError("Wrong browser type. Use firefox or chrome browser")

    driver.set_window_size(1920, 1080)
    driver.get(url)
    driver.save_screenshot(img_path)
    driver.quit()
