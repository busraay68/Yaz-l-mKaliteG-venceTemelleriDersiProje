from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=python+tutorial")

time.sleep(2)

first_video = driver.find_element(By.ID, "video-title")
first_video.click()

time.sleep(5)  

try:
    skip_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "ytp-ad-skip-button"))
    )
    skip_button.click()
    print("✅ Ad was skipped successfully.")

except:
    print("⚠️ Skip Ads button not found. No skippable ad or ad not shown.")

driver.quit()
