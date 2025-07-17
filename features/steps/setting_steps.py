from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on the Change password option')
def changes_pwd(context):
    context.app.setting_page.changes_pwd()


@when('Verify the right page opens')
def verify_right_page(context):
    context.app.setting_page.verify_right_page()

@when('Add some test password to the input fields')
def add_test_password(context):
    context.app.setting_page.add_test_password()


@then('Verify the “Change password” button is available')
def change_password_btn(context):
    context.app.setting_page.change_password_btn()