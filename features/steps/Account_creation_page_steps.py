from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('"Enter your email or mobile number to continue" message is shown')
def account_creation_msg(context):
    context.app.account_creation_page.account_creation_msg()
    # expected_text = 'Enter your email or mobile number to continue'
    # actual_text = context.driver.find_element(By.XPATH, "//p[@class='h-margin-b-x6 h-text-md h-text-center']").text
    # assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'




