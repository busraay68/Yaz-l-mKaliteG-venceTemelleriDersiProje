from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Tarayıcıyı başlat
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=Python+Tutorial")
time.sleep(3)

# İlk videoyu tıkla
first_video = driver.find_element(By.ID, "video-title")
first_video.click()
time.sleep(7)  # video yüklensin

# Tüm butonları bul ve içinde "Subscribe" geçen varsa tıkla
buttons = driver.find_elements(By.TAG_NAME, "button")
found = False

for btn in buttons:
    try:
        if "Subscribe" in btn.text:
            print(f"🟡 Bulundu: {btn.text}")
            btn.click()
            found = True
            break
    except:
        continue

if found:
    print("✅ Subscribe butonuna tıklandı.")
else:
    print("❌ Subscribe butonu bulunamadı.")

# Tarayıcıyı kapat
driver.quit()
