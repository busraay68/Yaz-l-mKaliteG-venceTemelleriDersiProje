# YouTube API ve UI Testleri

## Proje Açıklaması

Bu proje, YouTube Data API v3 ve Selenium WebDriver kullanılarak API ve kullanıcı arayüzü (UI) testleri gerçekleştirmek amacıyla geliştirilmiştir. Projenin hedefi, YouTube platformu üzerinde API uç noktalarının doğruluğunu ve UI etkileşimlerini analiz etmek için otomatik test senaryoları oluşturmaktır.

---

## API Testleri

### Kullanılan Uç Noktalar

API testleri, Postman kullanılarak aşağıdaki uç noktalar üzerinde gerçekleştirilmiştir:

* **Search Endpoint**: Video arama sonuçlarını doğrulama
* **Videos Endpoint**: Belirli bir videonun bilgilerini alma
* **Channels Endpoint**: Kanal aboneliklerini ve istatistikleri kontrol etme
* **Playlists Endpoint**: Oynatma listesi yönetimi
* **PlaylistItems Endpoint**: Oynatma listesine video ekleme ve silme
* **LiveBroadcasts Endpoint**: Canlı yayın bilgilerini getirme
* **Captions Endpoint**: Video altyazılarını doğrulama

### Test Senaryoları

* **Olumlu Senaryolar**: Uç noktaların doğru veri döndürdüğü durumlar test edilmiştir.
* **Hatalı Senaryolar**: Eksik API anahtarı, yetkilendirme hataları (403 Forbidden), yanlış parametre kullanımı (400 Bad Request) gibi durumlar test edilmiştir.
* **Performans Testleri**: Yanıt süreleri ölçülerek API’nin hız ve güvenilirliği analiz edilmiştir.

---

## UI Testleri (Selenium)

### Gerçekleştirilen Testler

1. **Arama Kutusu Testi (Search Box):**

   * "Python Tutorial" arama sorgusu gerçekleştirilir.
   * Sonuçların başarıyla yüklendiği doğrulanır.
   * **Sonuç:** ✅ Başarılı

2. **Video Oynatma Testi (Video Play):**

   * Bir video açılır ve "Play" düğmesine tıklanır.
   * Videonun süre çubuğu gözlemlenir.
   * **Sonuç:** ✅ Başarılı

3. **Abone Ol Butonu Testi (Subscribe):**

   * "Subscribe" butonuna tıklanır.
   * Kullanıcı login olmadığı için giriş ekranına yönlendirilir.
   * **Sonuç:** ✅ Başarılı

4. **Geçersiz Giriş Testi (Invalid Login):**

   * Yanlış kullanıcı adı ve şifre ile giriş yapılmaya çalışılır.
   * Hata mesajı görüntülenir.
   * **Sonuç:** ⚠️ Kısmen Başarılı

5. **Altyazı ve Kalite Ayarları (Subtitles & Quality):**

   * Altyazılar açılır ve kalite 1080p olarak değiştirilir.
   * **Sonuç:** ✅ Başarılı

6. **Sayfa Yüklenme Testi (Page Load):**

   * Ana sayfanın yüklendiği doğrulanır.
   * **Sonuç:** ✅ Başarılı

7. **Reklam Atla Butonu Testi (Skip Ads):**

   * Reklam "Skip Ads" düğmesi test edilir.
   * Atlanabilir reklam olmadığı için pas geçildi.
   * **Sonuç:** 🔹 Pas Geçildi

---

## Kullanılan Teknolojiler

* **Postman:** API testleri
* **Selenium WebDriver:** UI test otomasyonu
* **Python:** Test scriptleri
* **WebDriverWait:** Sayfa yüklenmesini beklemek için
* **XPath & CSS Selectors:** UI elementlerini seçmek için

---

## Nasıl Çalıştırılır?

### API Testleri

1. Postman koleksiyonunu içe aktarın.
2. API anahtarını (`{{API_KEY}}`) güncelleyin.
3. Testleri çalıştırın.

### UI Testleri

1. Python ve Selenium WebDriver’ı yükleyin.
2. ChromeDriver’ı sisteminize kurun.
3. Test scriptlerini çalıştırın:

```bash
python selenium_tests.py
```


