import os
from data_awal import jenis_permen, katalog_permen

def create_admin():
    os.system("cls")
    print("=== ADMIN - CREATE ===")
    print("1. Tambah Menu Pilihan Baru")
    print("2. Tambah Jenis Variasi Rasa")
    pilih = input("Pilih (1/2): ").strip()

    if pilih == "1":
        nama = input("Nama Permen: ").strip()
        harga = int(input("Harga Permen (angka): "))
        stok = int(input("Jumlah Stok: "))

        daftar_jenis = list(jenis_permen.keys())
        for i, j in enumerate(daftar_jenis, start=1):
            print(f"{i}. {j}")
        idx_j = int(input("Pilih nomor jenis permen: ")) - 1
        jenis_dipilih = daftar_jenis[idx_j]

        daftar_varian = jenis_permen[jenis_dipilih]
        for i, v in enumerate(daftar_varian, start=1):
            print(f"{i}. {v}")
        idx_v = int(input("Pilih nomor varian rasa: ")) - 1
        varian_dipilih = daftar_varian[idx_v]

        katalog_permen.append({
            "nama": nama,
            "harga": harga,
            "stok": stok,
            "jenis": jenis_dipilih,
            "varian": varian_dipilih,
        })
        print("Menu berhasil ditambahkan.")

    elif pilih == "2":
        daftar_jenis = list(jenis_permen.keys())
        for i, j in enumerate(daftar_jenis, start=1):
            print(f"{i}. {j} -> {', '.join(jenis_permen[j])}")
        idx_j = int(input("Pilih nomor jenis permen: ")) - 1
        jenis_dipilih = daftar_jenis[idx_j]
        varian_baru = input("Nama varian rasa baru: ").strip()
        if varian_baru not in jenis_permen[jenis_dipilih]:
            jenis_permen[jenis_dipilih].append(varian_baru)
            print("Variasi rasa berhasil ditambahkan.")
        else:
            print("Variasi rasa sudah ada.")
    else:
        print("Pilihan tidak valid.")

    input("\nTekan Enter untuk lanjut...")