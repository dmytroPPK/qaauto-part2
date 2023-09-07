import pytest
from src import user_db
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture
def test_db():
    db = user_db.UserDb("tests/artifacts/pytest_test.db")
    yield db
    db.execute("delete from users")
    db.close()





@pytest.fixture(scope="module")
def driver():
    
    chrome_service = ChromeService(executable_path="/usr/local/bin/chromedriver")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    yield driver

    driver.quit()

@pytest.fixture
def base_url():
    return 'https://reqres.in'