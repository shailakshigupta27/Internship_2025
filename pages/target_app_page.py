from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetAppPage(Page):
    PP_LINK = (By.CSS_SELECTOR, "a[aria-label*='privacy policy']")
    TC_link = (By.CSS_SELECTOR, "a[aria-label*='terms & conditions']")

    def open_target_app(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_privacy_link(self):
        self.click(*self.PP_LINK)

    def click_tc_link(self):
        self.click(*self.TC_link)