from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Cart(Page):
    Empty_cart_msg = (By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]")
    expected_text = 'Your cart is empty'
    Side_Cart_Button = (By.CSS_SELECTOR, "[data-test*='content-wrapper'] button[id*='addToCartButtonOrTextId']")
    View_cart = (By.CSS_SELECTOR, "a[class*='fullWidth__3XX6f styles_ndsButtonSecondary']")
    Cart_Item_Count = (By.XPATH, '//span[@class="sc-46253dd2-2 ijhCkR"]')


    def empty_cart(self):

        #actual_text = self.find_element(*self.Empty_cart_msg).text
        #sleep(5)
        #assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'
        self.verify_text(self.expected_text,  *self.Empty_cart_msg)


    def open_cart_page(self):
        self.verify_url('https://www.target.com/cart')

    def again_add_to_cart(self):
        self.click(*self.Side_Cart_Button)

    def view_cart(self):
        self.driver.find_element(*self.View_cart)
        self.click(*self.View_cart)

    def no_of_items(self, count):
        actual_text = self.driver.find_element(*self.Cart_Item_Count).text
        assert count in actual_text, f'Error, expected {count} not in actual {actual_text}'
