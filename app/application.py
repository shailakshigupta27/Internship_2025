from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from pages.cart_page import Cart
from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.search_results_page import SearchResultsPage
from pages.setting_page import SETTING
from pages.target_app_page import TargetAppPage
from pages.terms_cond_page import TermsCondPage
from pages.Signin_side_navigation_page import SigninSideNavigation
from pages.Account_creation_page import AccountCreation



class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.header = Header(driver)
        self.cart_page = Cart(driver)
        self.wait = WebDriverWait(driver, timeout=10)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.terms_cond_page = TermsCondPage(driver)
        self.signin_side_navigation_page = SigninSideNavigation(driver)
        self.account_creation_page = AccountCreation(driver)
        self.login_page = LoginPage(driver)
        self.setting_page = SETTING(driver)







