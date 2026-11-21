import os
from data_awal import jenis_permen, katalog_permen, shopping_list

def update_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - UPDATE SHOPPING LIST ===")
    if not shopping_list:
        print("Shopping list kosong.")
        input("\nTekan Enter untuk lanjut...")
        return

    for i, entry in enumerate(shopping_list, start=1):
        item = katalog_permen[entry["menu_index"]]
        print(f"{i}. {item['nama']} | Varian: {entry['varian']} | Qty: {entry['qty']}")

    idx = int(input("Pilih nomor item belanjaan: ")) - 1
    if not (0 <= idx < len(shopping_list)):
        print("Nomor item tidak valid.")
        input("\nTekan Enter untuk lanjut...")
        return

    entry = shopping_list[idx]
    item = katalog_permen[entry["menu_index"]]

    print("1. Atur Kuantitas")
    print("2. Ubah Varian Rasa")
    pilih = input("Pilih (1/2): ").strip()

    if pilih == "1":
        qty_baru = int(input("Masukkan kuantitas baru: "))
        if 0 < qty_baru <= item["stok"]:
            entry["qty"] = qty_baru
            print("Kuantitas berhasil diubah.")
        else:
            print("Kuantitas tidak valid atau melebihi stok.")

    elif pilih == "2":
        varians = jenis_permen.get(item["jenis"], [item["varian"]])
        for i, v in enumerate(varians, start=1):
            print(f"{i}. {v}")
        idx_v = int(input("Pilih nomor varian baru: ")) - 1
        if 0 <= idx_v < len(varians):
            entry["varian"] = varians[idx_v]
            print("Varian rasa berhasil diubah.")
        else:
            print("Nomor varian tidak valid.")

    else:
        print("Pilihan tidak valid.")

    input("\nTekan Enter untuk lanjut...")