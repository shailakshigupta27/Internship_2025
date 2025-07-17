from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
from features.steps.Cart_page_steps import message

class LoginPage(Page):
   email =  (By.CSS_SELECTOR, "[id*='email-2']")
   password = (By.CSS_SELECTOR, "[id*='field']")
   continue_button = (By.CSS_SELECTOR, "[class*='login-button w-button']")

   username = 'gupta.shailakshi27@gmail.com'
   Password = 'Shailu@27'

   def input_username(self):
       self.input_text(self.username, *self.email)

   def input_password(self):
       self.input_text(self.Password, *self.password)

   def click_continue(self):
       self.click(*self.continue_button)
       sleep(10)



