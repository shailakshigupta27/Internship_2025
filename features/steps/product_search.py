from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

SEARCH_SUBMIT = (By.CSS_SELECTOR, "button[data-test*='@web/Search/SearchButton']")
SEARCH_INPUT = (By.ID, 'search')


@when('Input {search_word} into search field')
def input_search(context,search_word):
    #search = context.driver.find_element(*SEARCH_INPUT)
    #search.clear()
    #search.send_keys(search_word)
    #sleep(4)
    context.app.header.search_product()


