import os
from data_awal import jenis_permen, katalog_permen

def delete_admin():
    os.system("cls")
    print("=== ADMIN - DELETE ===")
    print("1. Hapus Salah Satu Menu")
    print("2. Hapus Salah Satu Variasi Rasa")
    print("3. Hapus Semua Menu")
    pilih = input("Pilih (1/2/3): ").strip()

    if pilih == "1":
        for i, item in enumerate(katalog_permen, start=1):
            print(f"{i}. {item['nama']} ({item['varian']})")
        idx = int(input("Pilih nomor menu yang dihapus: ")) - 1
        if 0 <= idx < len(katalog_permen):
            katalog_permen.pop(idx)
            print("Menu berhasil dihapus.")
        else:
            print("Nomor menu tidak valid.")

    elif pilih == "2":
        daftar_jenis = list(jenis_permen.keys())
        for i, j in enumerate(daftar_jenis, start=1):
            print(f"{i}. {j}: {', '.join(jenis_permen[j])}")
        idx_j = int(input("Pilih nomor jenis permen: ")) - 1
        if 0 <= idx_j < len(daftar_jenis):
            jenis_dipilih = daftar_jenis[idx_j]
            varians = jenis_permen[jenis_dipilih]
            for i, v in enumerate(varians, start=1):
                print(f"{i}. {v}")
            idx_v = int(input("Pilih nomor varian yang dihapus: ")) - 1
            if 0 <= idx_v < len(varians):
                varians.pop(idx_v)
                print("Variasi rasa berhasil dihapus.")
            else:
                print("Nomor varian tidak valid.")
        else:
            print("Nomor jenis tidak valid.")

    elif pilih == "3":
        katalog_permen.clear()
        print("Semua menu berhasil dihapus.")

    else:
        print("Pilihan tidak valid.")

    input("\nTekan Enter untuk lanjut...")