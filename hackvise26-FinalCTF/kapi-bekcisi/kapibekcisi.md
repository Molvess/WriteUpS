# Kapı Bekçisi (ısınma)

nc 34.62.253.25 9001

Kural: 8 haneli hex nonce → hex string'i ters çevir → her byte'ı 0x5A ile XOR → küçük harf hex geri gönder. 5 sn süre, tek deneme.

**Flag formatı:** hackwiseCTF{...}
