from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
from features.steps.Cart_page_steps import message

class SigninSideNavigation(Page):
   side_signin =  (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
   sign_in_reelly = (By.CSS_SELECTOR, "[class*='sing-in-text']")

   def create_account(self):
        self.driver.find_element(*self.side_signin).click()
        sleep(10)


   def sign_in(self):
       self.driver.find_element(*self.sign_in_reelly).click()
       sleep(10)


