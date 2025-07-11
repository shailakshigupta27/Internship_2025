from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('“Your cart is empty” message is shown')
def message(context):
    #expected_text = 'Your cart is empty'
    #actual_text = context.driver.find_element(By.XPATH,"//h1[contains(@class, 'styles_ndsHeading')]").text
    #assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'
    context.app.cart_page.empty_cart()

@then('Verify number of items in the cart is {count}')
def no_of_items(context, count):
    context.app.cart_page.no_of_items(count)
    #actual_text = context.driver.find_element(By.XPATH, '//span[@class="sc-46253dd2-2 ijhCkR"]').text
    #assert count in actual_text, f'Error, expected {count} not in actual {actual_text}'



@then('Verify Cart page opened')
def open_cart_page(context):
    context.app.cart_page.empty_cart()
