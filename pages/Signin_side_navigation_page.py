from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
from features.steps.Cart_page_steps import message

class SigninSideNavigation(Page):
   side_signin =  (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')


   def create_account(self):
        self.driver.find_element(*self.side_signin).click()
        sleep(10)


