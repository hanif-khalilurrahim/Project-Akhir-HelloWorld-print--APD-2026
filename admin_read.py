import os
from data_awal import jenis_permen, katalog_permen

def read_admin():
    os.system("cls")
    print("=== ADMIN - READ ===")
    if not katalog_permen:
        print("Belum ada data menu permen.")
    else:
        for no, item in enumerate(katalog_permen, start=1):
            status = "TERSEDIA" if item["stok"] > 0 else "HABIS"
            print(f"\n[Menu ke-{no}]")
            print(f"1. Nama Permen: {item['nama']}")
            print(f"2. Harga Permen: Rp{item['harga']:,}".replace(",", ".") + "/pcs")
            print(f"3. Jumlah Stok: {item['stok']} pcs")
            print(f"4. Jenis Permen: {item['jenis'].upper()}")
            print(f"5. Varian Rasa: {item['varian']}")
            print(f"6. Status: {status}")

    print("\n--- Daftar Jenis & Variasi Rasa ---")
    for jenis, varians in jenis_permen.items():
        print(f"{jenis}: {', '.join(varians)}")

    input("\nTekan Enter untuk lanjut...")