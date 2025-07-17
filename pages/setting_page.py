from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
from features.steps.Cart_page_steps import message

class SETTING(Page):
   change_pwds =  (By.CSS_SELECTOR, "[href*='/set-new-password']")
   change_pwd_page = (By.CSS_SELECTOR, "[class*='change-password-text']")
   new_pwd = (By.CSS_SELECTOR, "[name*='Enter-new-password']")
   change_pwd_button = (By.CSS_SELECTOR, "[class*='submit-button-2 w-button']")

   new_password = '12345678'

   def changes_pwd(self):
       self.driver.find_element(*self.change_pwds).click()

   def verify_right_page(self):
       self.driver.find_element(*self.change_pwd_page)

   def add_test_password(self):
       self.input_text(self.new_password, *self.new_pwd)

   def change_password_btn(self):
       self.driver.find_element(*self.change_pwd_button)
