import os
from data_awal import jenis_permen, katalog_permen, shopping_list

def create_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - CREATE (SHOPPING LIST) ===")
    if not katalog_permen:
        print("Menu toko kosong.")
        input("\nTekan Enter untuk lanjut...")
        return

    for i, item in enumerate(katalog_permen, start=1):
        status = "TERSEDIA" if item["stok"] > 0 else "HABIS"
        print(f"{i}. {item['nama']} | Rp{item['harga']:,}".replace(",", ".") + f"/pcs | Stok: {item['stok']} | {status}")

    idx = int(input("Pilih nomor menu: ")) - 1
    if not (0 <= idx < len(katalog_permen)):
        print("Nomor menu tidak valid.")
        input("\nTekan Enter untuk lanjut...")
        return

    item = katalog_permen[idx]
    if item["stok"] <= 0:
        print("Stok menu sedang habis.")
        input("\nTekan Enter untuk lanjut...")
        return

    varians = jenis_permen.get(item["jenis"], [item["varian"]])
    for i, v in enumerate(varians, start=1):
        print(f"{i}. {v}")
    idx_v = int(input("Pilih nomor varian rasa: ")) - 1
    if not (0 <= idx_v < len(varians)):
        print("Nomor varian tidak valid.")
        input("\nTekan Enter untuk lanjut...")
        return

    varian_dipilih = varians[idx_v]
    qty = int(input("Masukkan jumlah beli: "))
    if qty <= 0 or qty > item["stok"]:
        print("Jumlah beli tidak valid atau melebihi stok.")
        input("\nTekan Enter untuk lanjut...")
        return

    shopping_list.append({
        "menu_index": idx,
        "varian": varian_dipilih,
        "qty": qty,
    })
    print("Berhasil ditambahkan ke shopping list.")
    input("\nTekan Enter untuk lanjut...")