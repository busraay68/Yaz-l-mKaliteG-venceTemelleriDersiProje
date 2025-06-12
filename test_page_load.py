from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="logo"]'))
    )
    print("✅ Page loaded successfully.")

except:
    print("❌ Page failed to load or took too long.")

driver.quit()
