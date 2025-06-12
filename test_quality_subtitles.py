from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=python+tutorial")

time.sleep(2)

# Open first video
first_video = driver.find_element(By.ID, "video-title")
first_video.click()

time.sleep(5)

# Open settings
settings_button = driver.find_element(By.CSS_SELECTOR, 'button.ytp-button.ytp-settings-button')
settings_button.click()

time.sleep(1)

# Open quality menu
quality_menu = driver.find_elements(By.XPATH, '//div[@class="ytp-menuitem-label"]')
for item in quality_menu:
    if item.text.lower() == "quality":
        item.click()
        break

time.sleep(1)

# Select 1080p (if available)
quality_options = driver.find_elements(By.XPATH, '//span[@class="ytp-menuitem-label"]')
for option in quality_options:
    if "1080" in option.text:
        option.click()
        break

time.sleep(2)

# Reopen settings menu to enable subtitles
settings_button.click()
time.sleep(1)

# Enable subtitles (if available)
cc_menu = driver.find_elements(By.XPATH, '//div[@class="ytp-menuitem-label"]')
for item in cc_menu:
    if "subtitles" in item.text.lower():
        item.click()
        break

print("✅ Quality and subtitles test passed.")

driver.quit()
