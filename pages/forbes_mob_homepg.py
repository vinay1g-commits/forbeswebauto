#This file is not required


from selenium.webdriver.common.by import By



from pages.base_page import BasePage


class MobPg(BasePage):
    SEARCH_BTN = (By.XPATH, "//a[@aria-label='Search']")
    SEARCH_TEXT_BOX = (By.XPATH, "//input[@class='SearchField_input__K6yMG']")
    VIEW_MORE_BTN = (By.XPATH, "//button[text()='View More']")

    def search_for_news(self):
        self.click(*self.SEARCH_BTN)
        self.click(*self.SEARCH_TEXT_BOX)
        self.enter_text(*self.SEARCH_TEXT_BOX,"news")
        self.scroll_to_element(*self.VIEW_MORE_BTN)




