from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify circle page has more than {number} links')
def verify_benefits_links(context, number):
    links = context.driver.find_elements(By.CSS_SELECTOR, "a[data-test*='@web/slingshot-components/CellsComponent/Link']" )
    print(links)

    assert len(links) > int(number), f'Expected {number} links, but got {len(links)}'


