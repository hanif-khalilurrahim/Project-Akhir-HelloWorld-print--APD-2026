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