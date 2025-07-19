from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
from features.steps.Cart_page_steps import message

class Header(Page):
    SEARCH_SUBMIT = (By.CSS_SELECTOR, "button[data-test*='@web/Search/SearchButton']")
    SEARCH_INPUT = (By.ID, 'search')
    CART_ICON = (By.CSS_SELECTOR, '[aria-label="cart 0 items"]')
    Account_Dropdown = (By.CSS_SELECTOR, '#account-sign-in')
    SETTING_BTN = (By.CSS_SELECTOR, "[class*='lucide lucide-settings']")
    # SETTING_BTN = (By.CSS_SELECTOR, "[href*='settings'] [class*='icon-menu w-embed']")


    def __init__(self, driver):
        super().__init__(driver)
        self.wait = None

    def search_product(self):
        self.input_text('Cup',*self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)
        sleep(10)

    def cart_icon(self):
        self.find_element(*self.CART_ICON).click()
        #self.wait.until(EC.presence_of_element_located(message))
        sleep(10)

    def account_dropdown(self):
        self.driver.find_element(*self.Account_Dropdown).click()
        sleep(3)

    def settings_option(self):
        self.driver.find_element(*self.SETTING_BTN).click()
        sleep(10)