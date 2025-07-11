#amazon Logo
driver.find_element(By.CSS_SELECTOR, '[aria-label="Amazon"]')

#sign in or create account
#CSS
driver.find_element(By.CSS_SELECTOR,'h1.a-size-medium-plus a-spacing-small')
driver.find_element(By.CSS_SELECTOR,'.a-size-medium-plus a-spacing-small')

#Xpath
driver.find_element(By.XPATH,"//h1[@class='a-size-medium-plus a-spacing-small']")

#Enter mobile number or email
#CSS
driver.find_element(By.CSS_SELECTOR,'p.a-spacing-micro a-text-bold')
driver.find_element(By.CSS_SELECTOR,'.a-spacing-micro a-text-bold')
#Xpath
driver.find_element(By.XPATH, "//p[@class='a-spacing-micro a-text-bold']")

# Enter tab
driver.find_element(By.CSS_SELECTOR,'#ap_email_login')

#Continue button
driver.find_element(By.CSS_SELECTOR,'.a-button-input')

#Conditions and privacy notice
driver.find_element(By.CSS_SELECTOR,"[href*='ap_signin_notification_condition_of_use']")

#need help
driver.find_element(By.CSS_SELECTOR,'[role="button"]')

#buying for work
driver.find_element(By.CSS_SELECTOR,'span.a-text-bold')
