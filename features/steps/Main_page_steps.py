from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@given('Open target.com')
def open_target(context):
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()



@given('Open target circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')


@when ('Click on Add to Cart')
def add_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-focusid*='82242697_product_card'] [id*='addToCartButtonOrTextId']").click()
    #context.driver.wait.until(EC.visibility_of_element_located(again_add_to_cart))
    sleep(4)


@when ('Again Click on Add to Cart in side navigation')
def again_add_to_cart(context):
    context.app.cart_page.again_add_to_cart()
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test*='content-wrapper'] button[id*='addToCartButtonOrTextId']").click()

@when('Click view cart')
def view_cart(context):
    context.app.cart_page.view_cart()
    #context.driver.find_element(By.CSS_SELECTOR, "a[class*='fullWidth__3XX6f styles_ndsButtonSecondary']").click()
