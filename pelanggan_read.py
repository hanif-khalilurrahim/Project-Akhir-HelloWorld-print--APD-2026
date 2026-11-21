import os
from data_awal import katalog_permen, shopping_list

def read_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - READ ===")
    print("1. Lihat Menu Toko Permen")
    print("2. Lihat Isi Belanjaan Saat Ini")
    pilih = input("Pilih (1/2): ").strip()

    if pilih == "1":
        for no, item in enumerate(katalog_permen, start=1):
            status = "TERSEDIA" if item["stok"] > 0 else "HABIS"
            print(f"\n[Menu ke-{no}]")
            print(f"1. Nama Permen: {item['nama']}")
            print(f"2. Harga Permen: Rp{item['harga']:,}".replace(",", ".") + "/pcs")
            print(f"3. Jumlah Stok: {item['stok']} pcs")
            print(f"4. Jenis Permen: {item['jenis'].upper()}")
            print(f"5. Varian Rasa: {item['varian']}")
            print(f"6. Status: {status}")

    elif pilih == "2":
        if not shopping_list:
            print("Shopping list masih kosong.")
        else:
            total = 0
            for i, entry in enumerate(shopping_list, start=1):
                item = katalog_permen[entry["menu_index"]]
                subtotal = item["harga"] * entry["qty"]
                total += subtotal
                print(
                    f"{i}. {item['nama']} | Varian: {entry['varian']} | "
                    f"Qty: {entry['qty']} | Subtotal: Rp{subtotal:,}".replace(",", ".")
                )
            print("Total Belanja: Rp" + f"{total:,}".replace(",", "."))

    else:
        print("Pilihan tidak valid.")

    input("\nTekan Enter untuk lanjut...")