import os
import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from dotenv import load_dotenv

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True)
def browser_settings(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "120.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')
    url = os.getenv('SELENOID_URL')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{url}",
        options=options)

    browser.config.driver = driver

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
