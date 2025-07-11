from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# 3 As: Arrange / Act / Assert

# #Question 1
# # Practice with locators.
# # Create locators + search strategy for these page elements of Amazon Sign in page:
# # # Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
# #
# # # Email field
driver.find_element(By.XPATH, "//input[@type='email']")
# #
# # # Continue button
driver.find_element(By.XPATH, "//input[@class='a-button-input']")
# #
# # # Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href,'signin_notification_condition_of_use')]")
# #
# # # Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href,'signin_notification_privacy_notice')]")
# #
# # # Need help link
driver.find_element(By.XPATH, "//a[@class='a-size-base a-link-normal']")
#
# # # Forgot your password link
driver.find_element(By.ID, "//a[@id='auth-fpp-link-bottom']")
#
# # # Other issues with Sign-In link
driver.find_element(By.XPATH,"//a[@id='ap-other-signin-issues-link']")
#
# # # Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='register_accordion_header']")
#
#
# # #Question 2
# # 2. Create a test case for the SignIn page using python & selenium script.
# # (Make sure to use Incognito browser mode when searching for locators)
# #
# # Test Case: Users can navigate to SignIn page
# # 1. Open https://www.target.com/
# # 2. Click Account button
# # 3. Click SignIn btn from side navigation
# # 4. Verify SignIn page opened:
# # “Sign in or create account” text is shown,
# # SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
#
# # open the url

driver.get('https://www.target.com/')
driver.find_element(By.ID,'account-sign-in').click()
sleep(5)
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(5)
expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH,"//h1[contains(@class,'styles_ndsHeading__HcGpD')]").text
assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'
print('Test case passed')
driver.quit()

# #Question 3
#[Optional] Build a test case yourself from scratch to search for a product on Target (same as shown in the class),
# make sure it works and you remember selenium commands.

driver.get('https://www.target.com/')
driver.find_element(By.ID,'search').send_keys('Flowers')
sleep(5)
driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)
expected_text = 'Flower'
actual_text = driver.find_element(By.XPATH,"//div[@title='LEGO Botanicals Petite Sunny Bouquet Flower Building Set 10347']").text

assert expected_text in actual_text, f'Error: {expected_text} not in  {actual_text}'
print('Test Case Passed')
driver.quit()