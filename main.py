# Data Awal
Nama_admin = ["Bip", "Hanif", "Cinta", "Mulan"]
Pw_admin = "Tokopermen123"

Stok_permen_coklat = 10
Stok_permen_vanila = 10
Stok_permen_stroberi = 10
Stok_permen_mint = 10
Stok_permen_kopi = 10
Stok_permen_lemon_tea = 10

harga_permen_coklat = 3000
harga_permen_vanila = 2000
harga_permen_stroberi = 2000
harga_permen_mint = 2000
harga_permen_kopi = 2000
harga_permen_lemon_tea = 3000

jenis_permen = {
    "Lunak": ["Coklat", "Vanila", "Stroberi"],
    "Keras": ["Mint", "Kopi", "Lemon Tea"],
}

katalog_permen = [
    {
        "nama": "Permen Coklat",
        "harga": harga_permen_coklat,
        "stok": Stok_permen_coklat,
        "jenis": "Lunak",
        "varian": "Coklat",
    },
    {
        "nama": "Permen Vanila",
        "harga": harga_permen_vanila,
        "stok": Stok_permen_vanila,
        "jenis": "Lunak",
        "varian": "Vanila",
    },
    {
        "nama": "Permen Stroberi",
        "harga": harga_permen_stroberi,
        "stok": Stok_permen_stroberi,
        "jenis": "Lunak",
        "varian": "Stroberi",
    },
    {
        "nama": "Permen Mint",
        "harga": harga_permen_mint,
        "stok": Stok_permen_mint,
        "jenis": "Keras",
        "varian": "Mint",
    },
    {
        "nama": "Permen Kopi",
        "harga": harga_permen_kopi,
        "stok": Stok_permen_kopi,
        "jenis": "Keras",
        "varian": "Kopi",
    },
    {
        "nama": "Permen Lemon Tea",
        "harga": harga_permen_lemon_tea,
        "stok": Stok_permen_lemon_tea,
        "jenis": "Keras",
        "varian": "Lemon Tea",
    },
]

shopping_list = []



# Menu Login
from login import admin, pengguna
from data_awal import Nama_admin, Pw_admin
import os
import inquirer

def MenuUtama():
    os.system("cls")
    print("============ Selamat datang di toko permen =============")
    pilihan = [
        inquirer.List(
            "login",
            message="Login Sebagai",
            choices=["admin", "pengguna"],
        ),
    ]
    logins = inquirer.prompt(pilihan)

    if(logins["login"]) == "admin":
        logmin()
        os.system("cls")
    elif(logins["login"]) == "pengguna":
        pengguna()
        os.system("cls")

def logmin():
    os.system("cls")
    try:
        print("=========================")
        user = input("Masukkan Username: ").strip()
        password = input("Masukkan Password: ")
        print("=========================")
        if not ((user in Nama_admin and password == Pw_admin)):
            raise ValueError
    except ValueError:
        os.system("cls")
        logcoba()

    else:
        os.system("cls")
        if (user in Nama_admin and password == Pw_admin):
            admin()

def logcoba():
    pilihan = [
        inquirer.List(
            "pilih",
            message="Login Gagal",
            choices=["coba lagi", "kembali ke menu awal"],
        ),
    ]
    step = inquirer.prompt(pilihan)
    os.system("cls")
    if (step["pilih"]) == "coba lagi":
            logmin()
    elif (step["pilih"]) == "kembali ke menu awal":
            MenuUtama()

if __name__ == "__main__":
    MenuUtama()



# Login
import os
import inquirer
from admin_create import create_admin
from admin_read import read_admin
from admin_update import update_admin
from admin_delete import delete_admin
from admin_keluar import keluar_admin
from pelanggan_create import create_pelanggan
from pelanggan_read import read_pelanggan
from pelanggan_update import update_pelanggan
from pelanggan_delete import delete_pelanggan
from pelanggan_bayar import bayar_pelanggan
from pelanggan_keluar import keluar_pelanggan

def admin():
    jalan = True
    while jalan:
        os.system("cls")
        menu = [
            inquirer.List(
                "aksi",
                message="Menu Admin",
                choices=[
                    "create",
                    "read",
                    "update",
                    "delete",
                    "keluar",
                ],
            )
        ]
        pilih = inquirer.prompt(menu)
        if pilih["aksi"] == "create":
            create_admin()
        elif pilih["aksi"] == "read":
            read_admin()
        elif pilih["aksi"] == "update":
            update_admin()
        elif pilih["aksi"] == "delete":
            delete_admin()
        elif pilih["aksi"] == "keluar":
            jalan = keluar_admin()

def pengguna():
    jalan = True
    while jalan:
        os.system("cls")
        menu = [
            inquirer.List(
                "aksi",
                message="Menu Pelanggan",
                choices=[
                    "create",
                    "read",
                    "update",
                    "delete",
                    "bayar",
                    "keluar",
                ],
            )
        ]
        pilih = inquirer.prompt(menu)
        if pilih["aksi"] == "create":
            create_pelanggan()
        elif pilih["aksi"] == "read":
            read_pelanggan()
        elif pilih["aksi"] == "update":
            update_pelanggan()
        elif pilih["aksi"] == "delete":
            delete_pelanggan()
        elif pilih["aksi"] == "bayar":
            bayar_pelanggan()
        elif pilih["aksi"] == "keluar":
            jalan = keluar_pelanggan()



# Admin Create
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



# Admin Read
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



# Admin Update
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



# Admin Delete
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



# Admin Keluar
import os

def keluar_admin():
    os.system("cls")
    print("Keluar dari menu admin...")
    return False



# Pelanggan Create
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



# Pelanggan Read
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



# Pelanggan Update
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



# Pelanggan Delete
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



# Pelanggan Bayar
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



# Pelanggan Keluar
import os

def keluar_pelanggan():
    os.system("cls")
    print("Keluar dari menu pelanggan...")
    return False