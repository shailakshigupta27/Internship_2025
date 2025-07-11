from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

search_results_txt =(By.CSS_SELECTOR, "[class*='h-text-bs h-display-flex h-flex-align']")


@then('Verify search worked for {search_word}')
def verify_found_results_text(context, search_word):
    #actual_text = context.driver.find_element(*search_results_txt).text
    #assert search_word in actual_text, f" Error, expected {search_word} not in actual {actual_text}"
    context.app.search_results_page.verify_search_results()
