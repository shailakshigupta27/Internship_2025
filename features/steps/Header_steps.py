from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from features.steps.Cart_page_steps import message
from selenium.webdriver.common.by import By
from pages.base_page import Page



@when('Click on cart icon')
def cart(context):
    #context.driver.find_element(By.CSS_SELECTOR, '[aria-label="cart 0 items"]').click()
    #sleep(3)
    #context.driver.wait.until(EC.presence_of_element_located(message))
     context.app.header.cart_icon()

@when('Click account drop-down')
def account_dropdown(context):
    #context.driver.find_element(By.CSS_SELECTOR, '#account-sign-in').click()
    #sleep(3)
    context.app.header.account_dropdown()

