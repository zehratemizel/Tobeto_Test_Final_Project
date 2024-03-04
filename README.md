# 🌟 Tobeto UI Otomasyon Projesi 🌟

Bu repository, Tobeto web sitesinin UI otomasyonunu gerçekleştirmek için kullanılır. Selenium WebDriver ve Pytest kütüphaneleri kullanılarak test senaryoları yazılmıştır.

## 📁 Proje Yapısı

- **tests/**: Bu dizin, test senaryolarının Python dosyalarını içerir.
    - **test_calendar.py**: Takvimde eğitim filtrelemesi yaparak aradığımız eğitimin çıkan sonuçla eşleşmesini test eder.
    - **test_catalog.py**: Katalog kısmında arama işlemi yaparak çıkan sonucun arama sonucuyla eşleşmesini kontrol eder.
    - **test_login.py**: Kullanıcının başarılı ve başarısız girişlerini kontrol eden otomasyonunu yazdık.
    - **test_profile_creation.py**: Kullanıcının sosyal medya hesabı ekleme, profil oluşturma alanlarının otomasyonunu gerçekleştirir ve toast body kontrolü yapar.
    - **test_register.py**: Kullanıcının kayıt olmasını sağlayan otomasyon testini gerçekleştirir.
    - **test_tobeto_platform.py**: Platformun içeriklerine ve eğitimlerinin kontrollerini test eder.
- **README.md**: Proje hakkında genel bilgiler ve kurulum talimatları içeren dosya.
