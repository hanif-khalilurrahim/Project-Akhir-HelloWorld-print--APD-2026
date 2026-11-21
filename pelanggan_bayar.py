import os
from prettytable import PrettyTable
from data_awal import katalog_permen, shopping_list

def bayar_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - BAYAR ===")
    if not shopping_list:
        print("Shopping list masih kosong, tidak ada yang dibayar.")
        input("\nTekan Enter untuk lanjut...")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Permen", "Varian", "Qty", "Harga/pcs", "Subtotal"]
    tabel.align["No"] = "c"
    tabel.align["Nama Permen"] = "l"
    tabel.align["Varian"] = "l"
    tabel.align["Qty"] = "r"
    tabel.align["Harga/pcs"] = "r"
    tabel.align["Subtotal"] = "r"

    total = 0
    for i, entry in enumerate(shopping_list, start=1):
        item = katalog_permen[entry["menu_index"]]
        subtotal = item["harga"] * entry["qty"]
        total += subtotal
        tabel.add_row([
            i,
            item["nama"],
            entry["varian"],
            entry["qty"],
            "Rp" + f"{item['harga']:,}".replace(",", "."),
            "Rp" + f"{subtotal:,}".replace(",", "."),
        ])

    print(tabel)
    print("Total yang harus dibayar: Rp" + f"{total:,}".replace(",", "."))
    uang = int(input("Masukkan jumlah uang bayar: "))
    if uang < total:
        print("Uang tidak mencukupi.")
    else:
        for entry in shopping_list:
            item = katalog_permen[entry["menu_index"]]
            item["stok"] = max(0, item["stok"] - entry["qty"])
        kembalian = uang - total
        shopping_list.clear()

        os.system("cls")
        print("==========================================")
        print("          STRUK BELANJA TOKO PERMEN       ")
        print("==========================================")
        print(tabel)
        print("Total Belanja : Rp" + f"{total:,}".replace(",", "."))
        print("Uang Bayar    : Rp" + f"{uang:,}".replace(",", "."))
        print("Kembalian     : Rp" + f"{kembalian:,}".replace(",", "."))
        print("==========================================")
        print("   Terima kasih sudah berbelanja! :)     ")
        print("==========================================")

    input("\nTekan Enter untuk lanjut...")