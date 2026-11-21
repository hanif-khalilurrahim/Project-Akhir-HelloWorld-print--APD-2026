import os
from data_awal import katalog_permen

def update_admin():
    os.system("cls")
    print("=== ADMIN - UPDATE STOK ===")
    if not katalog_permen:
        print("Belum ada menu untuk diupdate.")
        input("\nTekan Enter untuk lanjut...")
        return

    for i, item in enumerate(katalog_permen, start=1):
        status = "TERSEDIA" if item["stok"] > 0 else "HABIS"
        print(f"{i}. {item['nama']} | Stok: {item['stok']} pcs | Status: {status}")

    idx = int(input("Pilih nomor menu yang ingin diupdate stoknya: ")) - 1
    if 0 <= idx < len(katalog_permen):
        stok_baru = int(input("Masukkan jumlah stok baru: "))
        katalog_permen[idx]["stok"] = stok_baru
        print("Stok berhasil diupdate.")
    else:
        print("Nomor menu tidak ditemukan.")

    input("\nTekan Enter untuk lanjut...")