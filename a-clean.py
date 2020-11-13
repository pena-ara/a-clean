#!/usr/bin/env python

import os

while True:
    print('''
 █████╗        ██████╗██╗     ███████╗ █████╗ ███╗   ██╗
██╔══██╗      ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║
███████║█████╗██║     ██║     █████╗  ███████║██╔██╗ ██║
██╔══██║╚════╝██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║
██║  ██║      ╚██████╗███████╗███████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝       ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ By Nestero
A-CLEAN adalah tool sederhana untuk membersihkan sistem Arch Linux
    ''')
    print("===== Menu =====")
    print(" (1)  Bersihkan Cache Manual")
    print(" (2)  Bersihkan Cache Otomatis ")
    print(" (3)  Daftar Bekas Paket App yang Sudah diUninstall")
    print(" (4)  Hapus Bekas Paket App yang Sudah diUninstall")
    print(" (5)  Bersihkan Cache Home Directory")
    print(" (6)  Daftar Duplikat, File Kosong, Folder Kosong, Symlink Rusak")
    print(" (7)  Hapus Daftar Duplikat, File Kosong, Folder Kosong, Symlink Rusak")
    print(" (8)  Cek File dan Folder Berukuran Besar # tekan 'q' untuk kembali kemenu A-CLEAN")
    print(" (9)  Hapus yang Ada di Tong Sampah")
    print(" (00) Update System")
    print(" (0)  Keluar \n")
    ac = input("Pilih Opsi = ")

    if ac == "0":
        break
    elif ac == "1":
        cmd = os.system("pacman -Scc")
    elif ac == "2":
        cmd1 = os.system("paccache -d")
        cmd2 = os.system("paccache -r")
    elif ac == "3":
        print("Daftar Sisa Paket : ")
        cmd = os.system("pacman -Qtdq")
    elif ac == "4":
        cmd = os.system("pacman -Rns $(pacman -Qtdq)")
    elif ac == "5":
        cmd1 = os.system("du -sh ~/.cache/")
        cmd2 = os.system("rm -rf ~/.cache/*")
    elif ac == "6":
        cmd = os.system("rmlint /home/$user")
    elif ac == "7":
        cmd1 = os.system("rmlint /home/$user")
        cmd2 = os.system("sh -c ~/rmlint.sh")
    elif ac == "8":
        cmd = os.system("ncdu")
    elif ac == "9":
        cmd = os.system("rm -rf ~/.local/share/Trash/*")
    elif ac == "00":
        cmd = os.system("pacman -Syyu")
   
