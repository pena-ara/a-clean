#!/usr/bin/env python

from os import system
from os import chdir
from os import popen
#from getpass import getpass

#folder = popen("ls").read().strip().split("\n")
system("mkdir a-clean")
chdir("a-clean")
#u = popen("whoami").read()
l = '''
  █████╗        ██████╗██╗     ███████╗ █████╗ ███╗   ██╗
 ██╔══██╗      ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║
 ███████║█████╗██║     ██║     █████╗  ███████║██╔██╗ ██║
 ██╔══██║╚════╝██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║
 ██║  ██║      ╚██████╗███████╗███████╗██║  ██║██║ ╚████║
 ╚═╝  ╚═╝       ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ By Nestero
 A-CLEAN adalah tool sederhana untuk memebersihkan cacahe dan sampah di Arch Linux
'''

def menu():
    while True:
        system("clear")
        print(l)
        print("======= Menu =======")
        print(" [1] Cache")
        print(" [2] Paket Usang")
        print(" [3] Duplikat, File Kosong, Folder Kosong, Symlink Rusak")
        print(" [4] Tong Sampah")
        print(" [5] Update System")
        print(" [0] Keluar")
        print("====================")
        
        m = input("a-clean > ")
        system("clear")
        
        while m == "1":
            print(l)
            print(" [1] Bersihkan Cache Secara Manual")
            print(" [2] Bersihkan Cache Secara Otomatis")
            print(" [3] Bersihkan Cache Home Directory")
            print(" [0] Kembali")
            mc = input("a-cache > ")
            if mc == "1":
               cmd = system(f"sudo pacman -Scc")
            elif mc == "2":
               cmd = system("paccache -d")
               cmd2 = system("paccache -r")
            elif mc == "3":
               cmd = system("du -sh ~/.cache")
               cmd2 = system("rm -rf ~/.cache/*")
            elif mc == "0":
               menu()
            else:
               print("Tak ada dalam menu.....")

        while m == "2":
            print(l)
            print(" [1] Daftar Paket Usang")
            print(" [2] Unisntall Paket Usang")
            print(" [0] Kembali")
            mpu = input("a-paket-usang > ")
            if mpu == "1":
                print("Daftar Paket Usang :\n")
                cmd = system("pacman -Qtdq")
            elif mpu == "2":
                mpua = input("Yakin ingin menghapus paket usang (y/n) ? ")
                if mpua == "y":
                    cmd = system("sudo pacman -Rsucn $(pacman -Qtdq)")
                else:
                    menu()
            elif mpu == "0":
                menu()
            else:
                print("Tidak ada dalam menu.....")

        while m == "3":
            print(l)
            print(" [1] Daftar Duplikat, File / Folder Kosong, Symlink Rusak")
            print(" [2] Hapus Duplikat, File / Folder Kosong, Symlink Rusak")
            print(" [0] Kembali")
            mdfr = input("a-rusak > ")
            if mdfr == "1":
               cmd = system("rmlint /home/$user")
               cmd2 = system("vim rmlint.json")
            elif mdfr == "2":
                cmd = system("sh -c rmlint.sh")
            elif mdfr == "0":
                menu()
            else:
                print("Tidak ada dalam menu.....")

        while m == "4":
            cmd = system("rm -rf ~/.local/share/Trash/*")
            menu()

        while m == "5":
            cmd = system("sudo pacman -Syyu")
            menu()

        if m == "0":
            chdir("..")
            system("rm -rf a-clean")
            exit()
        else:
            print("Tidak ada dalam menu.....")

menu()
