from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import argparse

def banner():
    print("==============================================")
    print("           ASSASIN DORK SCANNER")
    print("   Creator: fy9 / Eğitim amaçlı yapılmıştır.")
    print("==============================================\n")

if __name__ == "__main__":
    banner()


def captcha_var_mi(driver):
    page_source = driver.page_source.lower()
    return "captcha" in page_source or "verify you are not a robot" in page_source or "sorry" in page_source

def dork_tarayici_selenium(dork_listesi, cikti_dosyasi, toplam_sonuc_adedi):
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(options=options)

    with open(dork_listesi, 'r', encoding='utf-8') as dork_file, \
         open(cikti_dosyasi, 'w', encoding='utf-8') as cikti_file:

        dork_satirlari = [d.strip() for d in dork_file.read().splitlines() if d.strip()]
        dork_sayisi = len(dork_satirlari)

        if dork_sayisi == 0:
            print("Dork listesi boş.")
            return

        temel_sayi = toplam_sonuc_adedi // dork_sayisi
        kalan = toplam_sonuc_adedi % dork_sayisi

        sonuc_dagilimi = [temel_sayi + (1 if i < kalan else 0) for i in range(dork_sayisi)]

        for i, (dork, dork_sayisi) in enumerate(zip(dork_satirlari, sonuc_dagilimi)):
            print(f"[{i+1}/{len(dork_satirlari)}] Aranıyor: {dork} | Hedef: {dork_sayisi} link")

            driver.get(f"https://www.google.com/search?q={dork}")
            time.sleep(3)

            if captcha_var_mi(driver):
                print("CAPTCHA tespit edildi. Tarayıcıda çözün.")
                input("CAPTCHA'yı çözdüyseniz ENTER'a basın...")

            toplanan = 0
            while toplanan < dork_sayisi:
                results = driver.find_elements(By.CSS_SELECTOR, 'div.tF2Cxc')

                if not results:
                    print("-> Sonuç bulunamadı veya daha fazla yok.")
                    break

                for sonuc in results:
                    if toplanan >= dork_sayisi:
                        break
                    try:
                        link = sonuc.find_element(By.TAG_NAME, 'a').get_attribute('href')
                        cikti_file.write(f"{link}\n")
                        toplanan += 1
                    except:
                        continue

                print(f"-> {toplanan}/{dork_sayisi} link toplandı.")

                try:
                    next_button = driver.find_element(By.ID, "pnnext")
                    next_button.click()
                    time.sleep(3)

                    if captcha_var_mi(driver):
                        print("CAPTCHA tespit edildi.")
                        input("CAPTCHA'yı çözdüyseniz ENTER'a basın...")
                except:
                    print("-> Daha fazla sayfa yok.")
                    break

            print(f"{dork} için tamamlandı. Toplam: {toplanan} link.\n")

    driver.quit()
    print(f"\nTüm tarama tamamlandı. Sonuçlar: {cikti_dosyasi}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Google dork tarayıcı (toplam sonuç sayısına göre).')
    parser.add_argument('-d', '--dorkfile', type=str, required=True, help='Dork listesini içeren dosya')
    parser.add_argument('-s', '--savefile', type=str, required=True, help='Linkleri içeren çıktı dosyası')
    parser.add_argument('-v', '--results', type=int, required=True, help='Toplam alınacak sonuç sayısı (tüm dorklara bölüştürülür)')

    args = parser.parse_args()
    dork_tarayici_selenium(args.dorkfile, args.savefile, args.results)
