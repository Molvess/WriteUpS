## Family

> Aile her şeydir. Bu diziyi gerçekten çok seviyorum …

Verilen sadece bir zip ve 3 pdf hatta bu pdflerin 2'si şifreli bir tanesinde şifre bulunmuyor o pdfi'de açacak olursak;

https://github.com/Molvess/WriteUpS/blob/19a3d73f8056291c914eb96227bebf6832a4c8ad/hackvise26-FinalCTF/iz-birakanlar/family/Modern_Family.pdf

*Pdfi açamayanlar için görsel aşağıdadır*

<img width="712" height="889" alt="resim" src="https://github.com/user-attachments/assets/8d3c4e3a-333d-4ff0-8820-63d034fbefe6" />

<hr>

Görselde birşey yok gibi gözüküyor değil mi evet aslında yok fakat `Ctrl + A` basarsak boşluğunda işaretlendiğini göreceğiz

<hr>

<img width="713" height="889" alt="resim" src="https://github.com/user-attachments/assets/86de769e-7623-4cb5-8752-b8a0c1cbebd5" />

Buradaki metnede `Kopyala` & `Yapıştır` işlemi ile ne olduğunu görebiliriz

<hr>

```
ctfhw2026
```

<hr>

Bunu aklınıza gelerek pdf'lerde denerseniz olmuyacağını göreceksinizdir 🥀

**Peki bu bilgiyi OSİNT olduğu için aklımıza direkt bir kullanıcı olabileceği geliyor**

https://instantusername.com/ Sitesine girerek bunu kontrollerimizi sağlıyoruz

<img width="1920" height="946" alt="resim" src="https://github.com/user-attachments/assets/aa87dcec-7000-46d5-9c6e-18218df7ad9e" />

<img width="1920" height="946" alt="resim" src="https://github.com/user-attachments/assets/abbcd846-bde5-49af-bd02-05c6790ed305" />

Bu hesabı buluyoruz ve bizleri 4 tane proje karşılıyor tek sorun hepsine teker teker bakacak olursan hepsinin boş olduğunu görebilirsin daha fazla uzatmamak adına cevapları direkt

```
s01_hackwise = [CatchoftheDay] https://github.com/ctfhw2026/CatchoftheDay/issues/1
s02_CTF = [s02_CTF] https://github.com/ctfhw2026/s02_CTF
s03_{m1l3y_ = [The_Long_Goodbye] https://github.com/ctfhw2026/The_Long_Goodbye/issues/1
s04_st3w4rt} = [TheClimb] https://github.com/ctfhw2026/TheClimb/wiki/Home/6d441591c6012daed3e96014218028a84684daca
```

<hr>

**hackwiseCTF{m1l3y_st3w4rt}**

<hr>

Olduğunu düşünüyorsanız şimdiden söyleyim yanlış .p [Evet yarışma sırasına fareyi kırdım]
Fakat şunu hatırlayın şifreli 2 pdf vardı hatırlarsanız, bu fakeflag olan `hackwiseCTF{m1l3y_st3w4rt}`i girince
final.pdf'i açılıyor ve bizleri bir kordinat karşılıyor `39.8925138, 32.7779265`

<img width="1256" height="486" alt="resim" src="https://github.com/user-attachments/assets/c90f9578-c8bc-47bb-bc45-863c6d1bab36" />

Bizleri Hackwise etkinliğinin ana merkezi olan ODTÜ ENFORMATİK ENSİTÜTÜSNDEKİ bir yeri veriyor biz zaten sınava "Cisco Lab"ında girdik hemen dışarı çıkıp o lokasyona bakmam gerekiyordu lokasyonu bulmam ve fırlamam bir oldu

**Normalde görmem gereken ama sınav esnasında görmediğim kağıtı bularak cevabı buldum fakat görmemişim gibi davranarak devam ediyoruz**

<img width="534" height="949" alt="resim" src="https://github.com/user-attachments/assets/ea18173e-29dc-46ea-b146-f1b40db44ab0" />

Burada bizlere **BİLGİSAYAR VE MAKİNE** Yazıyor buradan birşey aklınıza gelmesede o kısımda bulunan heykeller dünyada önemli sayılı kişiler ve orada *Alan Turing* heykelinin arkasına bakacak olursak

<img width="1687" height="949" alt="resim" src="https://github.com/user-attachments/assets/20927d89-334d-44a4-b838-c5236837914b" />

Evet tam olarak burada gördüğünüz şey bizlere cevabı sağlıyor 

> BU soru üzerine yaklaşık 45-50 dakika uğraştım kesinlikle değdi soruyu çözerken adrenali, bana bakışlar, üstüme toplanmaları yettide arttı kısacası `ai öl ya`

```
hackwiseCTF{R-Th1n-kM4ch!-N3-R8}
```
