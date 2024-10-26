import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import random

@pytest.fixture(scope="function", params=["desktop", "mobile"])
def browser(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("detach", True)  # Keep the browser open

    # Set a custom user agent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")

    # Disable WebDriver flag
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # Use incognito mode
    #chrome_options.add_argument("--incognito")

    # Disable extensions
    chrome_options.add_argument("--disable-extensions")

    if request.param == "mobile":
        mobile_emulation = {"deviceName": "Nexus 5"}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    else:
        chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


"""

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import random
import time

@pytest.fixture(scope="function", params=["desktop", "mobile"])
def browser(request):
    chrome_options = Options()

    if request.param == "mobile":
        # Set a custom User-Agent for mobile
        mobile_user_agent = "Mozilla/5.0 (Linux; Android 5.0; Nexus 5 Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36"
        mobile_emulation = {"deviceName": "Nexus 5"}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_argument(f"user-agent={mobile_user_agent}")
    else:
        # Set a custom User-Agent for desktop
        desktop_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
        chrome_options.add_argument(f"user-agent={desktop_user_agent}")


    # Disable WebDriver flag
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()

def wait_random_time(min_seconds=1, max_seconds=3):
    
    time.sleep(random.uniform(min_seconds, max_seconds))
"""