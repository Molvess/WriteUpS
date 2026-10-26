#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SecureAsWise - Sunucu Durum Kontrol Scripti
Anka Migrasyon Projesi için basit bir sağlık kontrolü.
"""

import socket
import datetime

SUNUCULAR = [
    {"isim": "anka-web-01", "ip": "10.0.1.10", "port": 80},
    {"isim": "anka-web-02", "ip": "10.0.1.11", "port": 80},
    {"isim": "anka-db-01",  "ip": "10.0.2.10", "port": 5432},
    {"isim": "anka-cache",  "ip": "10.0.3.10", "port": 6379},
]

def kontrol_et(sunucu):
    """Belirtilen sunucuya TCP bağlantısı dener."""
    try:
        sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sok.settimeout(3)
        sonuc = sok.connect_ex((sunucu["ip"], sunucu["port"]))
        sok.close()
        return sonuc == 0
    except socket.error:
        return False

def rapor_olustur():
    """Tüm sunucuların durumunu raporlar."""
    print(f"SecureAsWise Sunucu Durum Raporu")
    print(f"Tarih: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    for s in SUNUCULAR:
        durum = "✓ AKTIF" if kontrol_et(s) else "✗ ERİŞİLEMİYOR"
        print(f"  {s['isim']:20s} ({s['ip']:>12s}:{s['port']:<5d}) {durum}")
    print("-" * 50)

if __name__ == "__main__":
    rapor_olustur()


def bakim_modu_kontrol():
    """Bakım modundaki sunucuları listeler."""
    print("\nBakım modundaki sunucular kontrol ediliyor...")
    # TODO: Bakım modu API'si entegre edilecek
    print("  Şu an bakım modunda sunucu yok.")
