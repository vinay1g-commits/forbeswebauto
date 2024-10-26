import logging

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import browser


class BasePage:
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def click(self,by,value):
        """Click on an element specified by its locator."""
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
            logging.info(f"clicked on {value}")
        except (TimeoutException,NoSuchElementException) as e:
            logging.error(f"clicking failed on {value}:{e}")


    def enter_text(self,by,value,text):
        """Enter text into an input field specified by its locator."""
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.clear()
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
            logging.info(f"entered text in {value}")
        except (TimeoutException,NoSuchElementException) as e:
            logging.error(f"error while entering text {value}:{e}")



    def scroll_to_element(self,by,value):
        """Scroll to an element specified by its locator and click it."""
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            logging.info(f"scrolled and clicked on {value}")
        except (TimeoutException,NoSuchElementException) as e:
            logging.error(f"error scrolling to {value}: {e}")

    def click_with_js(self,by,value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by,value)))
            self.driver.execute_script("arguments[0].click();",element)
        except Exception as e:
            print(f"error {e}")




