import os
from data_awal import katalog_permen, shopping_list

def delete_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - DELETE SHOPPING LIST ===")
    if not shopping_list:
        print("Shopping list kosong.")
        input("\nTekan Enter untuk lanjut...")
        return

    print("1. Hapus Salah Satu Kategori Pilihan Menu Tertentu")
    print("2. Hapus Semua Belanjaan")
    pilih = input("Pilih (1/2): ").strip()

    if pilih == "1":
        kategori = input("Masukkan nama jenis/kategori menu yang ingin dihapus (contoh: Lunak / Keras): ").strip().lower()
        sisa = [
            entry for entry in shopping_list
            if katalog_permen[entry["menu_index"]]["jenis"].lower() != kategori
        ]
        shopping_list.clear()
        shopping_list.extend(sisa)
        print("Item sesuai kategori berhasil dihapus dari shopping list.")

    elif pilih == "2":
        shopping_list.clear()
        print("Semua belanjaan berhasil dihapus.")

    else:
        print("Pilihan tidak valid.")

    input("\nTekan Enter untuk lanjut...")