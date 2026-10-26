# Kapı Bekçisi

nc 34.62.253.25 9001 <br> Kural: 8 haneli hex nonce → hex string'i ters çevir → her byte'ı 0x5A ile XOR → küçük harf hex geri gönder. 5 sn süre, tek deneme. <br>
**Flag formatı:** hackwiseCTF{...}

<img width="785" height="417" alt="resim" src="https://github.com/user-attachments/assets/c5ba61e4-aa24-43fc-a34a-e704fe1a6fda" />

Burada bizden istenen zaten verilen aşamalardan geçirip geri yollamak olacaktır fakat bunun için 5 saniyemiz var sadece aslında istenilen değerleri fonksiyonunu yazdırmamız yeterli olacaktır

```
import socket
import re

HOST = "34.62.253.25"  # Sunucu adresi
PORT = 9001            # Sunucu portu

def solve(nonce):
    reversed_hex = nonce[::-1]
    data = bytes.fromhex(reversed_hex)
    return bytes(b ^ 0x5A for b in data).hex()

#verilen değerleri işleyen kısımın kendisi

with socket.create_connection((HOST, PORT), timeout=5) as s:
    s.settimeout(5)
    buffer = b""

    while True:
        chunk = s.recv(4096)

        if not chunk:
            break

        buffer += chunk

        match = re.search(
            rb"Nonce:\s*([0-9a-fA-F]{8})",
            buffer,
            re.IGNORECASE
        )

        if match:
            nonce = match.group(1).decode()
            answer = solve(nonce)

            print(f"[+] Nonce: {nonce}")
            print(f"[+] Answer: {answer}")

            s.sendall((answer + "\n").encode())
            print("[+] Answer sent!")

            break

        #Eğer istenen sonuç gelirse sonucu basacak kısım

    # Sunucunun cevabını oku
    s.settimeout(3)

    try:
        while True:
            response = s.recv(4096)
            if not response:
                break
            print(response.decode(errors="replace"), end="")
    except socket.timeout:
        pass
```


<img width="704" height="175" alt="resim" src="https://github.com/user-attachments/assets/b69bb3d1-648b-4fc7-b867-cf2b4aaf307d" />

<hr>

```
hackwiseCTF{k4p1_b3kc1s1n1_g3ct1n}
```

<hr>
