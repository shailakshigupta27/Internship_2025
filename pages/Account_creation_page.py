from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
from features.steps.Cart_page_steps import message

class AccountCreation(Page):
   Account_Creation =  (By.XPATH, "//p[@class='h-margin-b-x6 h-text-md h-text-center']")

   def account_creation_msg(self):
        expected_text = 'Enter your email or mobile number to continue'
        actual_text = self.driver.find_element(*self.Account_Creation).text
        assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'


