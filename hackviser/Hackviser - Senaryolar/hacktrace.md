# [HackTrace]([https://app.hackviser.com/scenarios/anchor](https://app.hackviser.com/scenarios/hacktrace))

- CTF GÖRSELİ
<img width="1400" height="700" alt="image" src="https://github.com/user-attachments/assets/d284bd90-77fd-4cb3-80cc-3c76a882a616" />
<br>

Her ctf'de elimize bir makine verip ona sızmamız istenir fakat bu makinede tam tersi sızmış bir makineye bize verip bazı veriler elde etmemizi istiyorlar sorular şöyle

1. Websitesine saldıran saldırganın IP adresi nedir?
2. Saldırgan, dizin taraması için hangi aracı kullanmıştır?
3. Dosya yükleme zafiyeti yazılımdaki hangi fonksiyondan kaynaklanmıştır?
4. Saldırgan, sistemden hangi önemli dosyayı zipleyerek çalmış?
5. Saldırgan, eriştiği verileri hangi domain'e yüklemiştir?

İlk sorumuz için her apache2 veya wordpress kısacası bütün web yazılımların kalbine ineceğiz evet /var/log nasıl bildiniz 😲

```
cd /var/log/apache2
```

<img width="923" height="297" alt="image" src="https://github.com/user-attachments/assets/90a0b61f-fc63-4e11-821b-230d92a329f1" />

Resimdede görüldüğü üzere "access.log" diye bir dosyamız bulunmakta cat ile dosyamızı inceleyeceğizde gerçekten çok uzun onun için bunu bir .txt dosyasına kaydedelim

```
cat access.log > loglar.txt
```

Bu txt dosyasını metin editörümle açıyorum ki daha rahat görebileyim

Açtığımda beni /gobuster'lı bir IP karşılıyor bilirsinizki ağı bir fuzz aracıdır yani 1.sorumuzla beraber 2.sorumuzun cevabınıda gobuster ile öğrenmiş oluyoruz

<img width="1540" height="831" alt="image" src="https://github.com/user-attachments/assets/d4d31373-37ec-4973-b988-e31af330c761" />

### 1.Sorumuzun ve 2.Sorumuzun cevabıyla beraber 3.sorumuzun cevabı için girişi sağladıktan sonraki aşamaya bakmamız gerek

<hr>

<img width="1900" height="345" alt="image" src="https://github.com/user-attachments/assets/79e351b2-9b84-4c86-905f-36d14a634455" />

### Seçili ve satır sonrasıda olduğu gibi açıkca bize "File Uplaod" zafiyetim var diye bağırmakta ve dosyamızın adınında "shell.php" olduğu açıkca görülüyor

<hr>

### Eğer dosyanın içeriğini kontrol sağlarsak 4.Sorumuzun cevabını bulmuş oluruz

<img width="727" height="372" alt="image" src="https://github.com/user-attachments/assets/3eb47494-fab5-44fd-b345-455cf6b819d5" />

Resimdede görüldüğü üzere "uploadFile" Fonksiyonu bizlere cevabı vermiş bulunmakta

<hr>

### Bize garip gelen normal sistemlerde görmeyeceğimiz bir dosyada beraberinde bizle geliyor

<img width="579" height="233" alt="image" src="https://github.com/user-attachments/assets/5fae6fe6-8837-4eeb-90c8-1785d03f9208" />

<hr>

### İçerisini açıncada bizi diğer soruların cevapları orada bekliyor oluyor

<img width="698" height="318" alt="image" src="https://github.com/user-attachments/assets/2f15c808-3a13-44ea-8cd3-c5977d9ddafd" />

Resimdede görüldüğü gibi zip'lenen dosyanın adıyla **5.cevabını**

Altındaki satır ilede hangi domain sorusunun yani **6.sorunun cevabını bulmus olduk**
<hr>

### HERŞEY BU KADAR GOD'A EMANET OLUN BAŞKA CTF'LERDE GÖRÜŞMEK ÜZERE

<hr>
