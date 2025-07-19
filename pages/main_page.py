from pages.base_page import Page
from time import sleep

class MainPage(Page):
    def open_main_page(self):
        self.driver.get('https://www.target.com/')


    def open_relly_page(self):
        self.driver.get('https://soft.reelly.io/sign-in')
        sleep(15)