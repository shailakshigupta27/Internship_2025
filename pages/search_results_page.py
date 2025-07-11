from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    search_results_txt = (By.CSS_SELECTOR, "[class*='h-text-bs h-display-flex h-flex-align']")

    def verify_search_results(self):
        self.verify_partial_text('Car', *self.search_results_txt)
        #actual_text = self.find_element(*self.search_results_txt).text
        #assert 'Car' in actual_text, f" Error, expected {'Car'} not in actual {actual_text}"
