from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=Python+Tutorial")
time.sleep(3)

first_video = driver.find_element(By.ID, "video-title")
first_video.click()
time.sleep(5)

try:
    play_button = driver.find_element(By.CLASS_NAME, "ytp-play-button")
    play_button.click()
except:
    pass

time.sleep(3)

current_time = driver.find_element(By.CLASS_NAME, "ytp-time-current").text
assert current_time != "0:00", "Video baslamadi!"
print("✅ Video oynatildi ve sure ilerliyor.")

driver.quit()
