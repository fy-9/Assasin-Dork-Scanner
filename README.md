# Assasin Dork Scanner

Assasin Dork Scanner, Google üzerinden özel dork sorguları ile hedef sistemler hakkında bilgi toplayan bir araçtır.

## ℹ️ Özellikler

Google dorklarını otomatik olarak arar

Sonuçları sadece link olarak çıktıya kaydeder

Toplam sonuç sayısı belirlenebilir (-v parametresi)

CAPTCHA çıkarsa kullanıcı çözebilir ve işlem kaldığı yerden devam eder

Selenium tabanlıdır

Headless (tarayıcıyı göstermeden çalışma) desteği vardır

## 🛠️ Kurulum

Python 3.8+ sürümü ve Google Chrome yüklü olmalıdır.

Sisteme uygun ChromeDriver indirilip çalıştığınız klasöre atılmalı veya PATH'e eklenmelidir.

`git clone https://github.com/fy-9/Assasin-Dork-Scanner`

`pip install -r requirements.txt`

## ▶️ Kullanım

**main.py** dosyasını bir klasöre çıkarın. Sonrasında **dorks.txt** ve **cikti.txt** dosyaları oluşturun.

dorks.txt dosyasının içine dorkları yazın.

Örnek kullanım: `python main.py -d dorks.txt -s cikti.txt -v 90`

-d: Dork listesini içeren dosya

-s: Çıktının kaydedileceği dosya

-v: Toplam kaç sonuç isteniyor (örneğin 90 sonuç, 3 dork varsa 30'ar sonuç şeklinde ayrılır)

## ⚠️ Yasal Uyarı
Bu araç yalnızca **eğitim**, **test**, **siber güvenlik araştırmaları** ve **bilgi amaçlı** geliştirilmiştir. Yetkisiz sistemlere erişim sağlamak, bu aracı kötüye kullanmak yasal olarak suçtur. Tüm sorumluluk kullanıcıya aittir.
