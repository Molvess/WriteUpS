# [Venomous]([[https://app.hackviser.com/scenarios/anchor](https://app.hackviser.com/scenarios/hacktrace](https://app.hackviser.com/warmups/venomous)))

- CTF GÖRSELİ
<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/455a9a31-6197-4473-b213-40120c856d94" />
<br>

1. Hangi web sunucusu çalışıyor?
2. Bir faturayı görüntülemek için kullanılan GET parametresi nedir?
3. Sistemdeki passwd dosyasına erişmek için yaptığınız directory traversal saldırısının payloadı nedir?
4. LFI güvenlik açığının açılımı nedir?
5. Nginx access loglarının varsayılan yolu nedir?
6. Siteye ilk erişim sağlayan kişinin IP adresi nedir?
7. show-invoice.php dosyasının son değiştirildiği saat nedir?

## 1. Sorumuz için elbette bize verilen makineye nmap taraması atarak başlıyoruz

```
nmap -sV -p 21,22,443,80 [IP]
```
Ve bize kod satırımız şöyle bir sonuç getirerek ilk cevabı bizlere sağlıyor

<img width="1632" height="477" alt="image" src="https://github.com/user-attachments/assets/e0373af8-64b7-427e-b176-8e25f69a0d56" />

<br>

Bize port olarak 80/http döndü biz buradan ne anlıyoruz ? / Bu bir web sitesi hemen websitesine gidip diğer sorunun cevabını bulalım

<hr>

## 2.Soru için websitesinde faturayı indiriyoruz

<img width="1920" height="874" alt="image" src="https://github.com/user-attachments/assets/5b6cc61e-4885-432f-9314-59cacc85dc26" />

Parametreninde burada ******* olduğunu görüp diğer cevabımızı buluyoruz

<hr>

## 3.Sorumuz için teker teker deneyeceğiz 

```
/etc/passwd
../etc/passwd
../../etc/passwd
../../../etc/passwd
../../../../etc/passwd
../../../../../etc/passwd
../../../../../../etc/passwd
```

Ben direk size olanı söyiyeyim sandınız dimi


```
3.Cevabınız = HEKHEKHEKHEK/HEH/HEHEHE
```

<img width="1920" height="242" alt="image" src="https://github.com/user-attachments/assets/cceacdc0-a541-4c0a-8351-b83691556500" />

<br>

Şu sayfayı alınca diyoruz ki evet doğru yoldayız

<hr>

<br>

## 4.Sorumuz ve 5.Sorumuz için Hemen bir google araştırması yapalım bakalım

# 4.SORU <img width="843" height="668" alt="image" src="https://github.com/user-attachments/assets/3566de6e-2073-4c55-83ea-5a86d4f6e253" />

# 5.SORU <img width="816" height="402" alt="image" src="https://github.com/user-attachments/assets/3364eee4-fb93-4a78-acef-c4db0fc68f2b" />

<hr>

## 6.Soru icin bazı bilgiler lazım

Eski logları sayın nginx abimiz verdiği log dosyalarıınn sonuna ".1" / ".2" ekleyerek eski dosyaları saklıyor bizede soruda ilk giren IP diye geçiyor dizin içinde acces.log / acces.log.1 / acces.log.2 deniyoruz ve bingo

içeri sokan acces.log.1 dosyasında tam olarak IP'miz belli oluyor

<img width="1920" height="143" alt="image" src="https://github.com/user-attachments/assets/775ce854-6228-4778-8686-f81dc392ab4c" />

<hr>

## Soru 7 kısmı için writeup bırakıyorum - anlamadım hocam

Ama basit mantığı şöyle söyleyebiliriz dinliyoruz - Log Poisoning - Reverse Shell' açıklarını kullanarak işlemleri gerçekleştiriyoruz

### Çözüm için buraya [tıklayabilirsiniz]((https://storage.hackviser.com/file/hackviser-prod/scenarios/writeups/c38d853f2ddb4592ac5399e696465ad5.pdf))

<nr>

<hr>

### HERŞEY BU KADAR GOD'A EMANET OLUN BAŞKA CTF'LERDE GÖRÜŞMEK ÜZERE

<hr>
