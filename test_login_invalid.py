from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin")

time.sleep(2)

email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys("invalid_email@test.com")
email_input.send_keys(Keys.RETURN)

time.sleep(3)

# Check for the presence of the error message container
error_message = driver.find_element(By.CSS_SELECTOR, 'div[jsname="B34EJ"]')
assert error_message.is_displayed()

print("✅ Invalid login test passed.")

driver.quit()
