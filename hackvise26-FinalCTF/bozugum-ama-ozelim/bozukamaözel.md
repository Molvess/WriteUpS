# Bozuğum Ama Özelim
> Bozuk arşivin magic byte'larını onarıp flag'e ulaş.
>
> **Flag formatı:** hackwiseCTF{...}

Verilen ipucundan aslında çok bariz şekilde görülen ilk akla gelen o şeyi yaparak zipi açmaya çalışıyoruz fakat bize zip dosyası sorunlu hatası dönüyor.
bizde *ya öyleyse* diye düşünerek;
Zip dosyasımızın hex koduna bakmak için

<a href="https://hexed.it/">Mükemmel site</a>

Yukarıdaki siteye girerek zip dosyamızı atıyoruz magic byte bizim dosyamızın ne tür olduğunu kilitleyen sihirli bit sayılarıdır aslında

<img width="680" height="247" alt="resim" src="https://github.com/user-attachments/assets/6dfb8525-2e85-4607-ba09-ff43a7475f8d" />
<img width="680" height="400" alt="resim" src="https://github.com/user-attachments/assets/6fdfd46e-99ed-49d4-bc13-bb4d0cf96ccf" />
<hr>

Bytelarımızı olması gerektiği gibi değiştirerek exportumuzu sağlıyoruz sonrasında zip içerisinde bizi bir dosya karşılıyor

<img width="800" height="62" alt="resim" src="https://github.com/user-attachments/assets/4bb357f8-6b9d-4314-8333-d76e5ef2341f" />

Hemen dosyayı açıyoruz **ODA NE**

<img width="208" height="127" alt="resim" src="https://github.com/user-attachments/assets/2dfd28ac-b100-4e19-833c-21bac2fd74d1" />

Evet artık bildiğiniz gibi gene o harika siteye attığımızda *kontrollerde gördüğümüz üzere*;

<img width="591" height="185" alt="resim" src="https://github.com/user-attachments/assets/5dcc0de5-c237-41cc-ac41-39ec3c87810e" />
<img width="948" height="56" alt="resim" src="https://github.com/user-attachments/assets/3f0d95b0-5099-4da2-8018-01f550af745f" />

### Düzeltilmiş hali ###

<img width="595" height="306" alt="resim" src="https://github.com/user-attachments/assets/e0defa14-534c-4a53-82ac-406feb0f722c" />

Ve en sonunda flagimiz bizleri karşılıyor resimi açınca

<img width="1386" height="604" alt="benigor" src="https://github.com/user-attachments/assets/7ba1c048-9c2c-4296-99d3-7df9ea0324b8" />

<hr>

```
hackwiseCTF{d0sy4_1mz4_4n4l1z1}
```

