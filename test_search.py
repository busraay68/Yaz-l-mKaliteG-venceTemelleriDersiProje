from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Tarayıcıyı başlat
driver = webdriver.Chrome()

# YouTube'a git
driver.get("https://www.youtube.com/")
time.sleep(2)

# Arama kutusunu bul ve anahtar kelime yaz
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Python Tutorial")
search_box.send_keys(Keys.RETURN)

# Sayfanın yüklenmesini bekle
time.sleep(3)

# Arama sonuçlarında "Python" kelimesi geçti mi?
assert "Python" in driver.page_source
print("✅ Test başarıyla tamamlandı!")

# Tarayıcıyı kapat
driver.quit()
