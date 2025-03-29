import csv
from datetime import datetime

# Nama file untuk menyimpan aktivitas
filename = "aktivitas_harian.csv"

# Membuat file CSV dengan header (jika file belum ada)
def buat_file_csv():
    try:
        with open(filename, mode='x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Tanggal", "Waktu", "Aktivitas", "Deskripsi"])
    except FileExistsError:
        pass

# Fungsi untuk mencatat aktivitas baru
def catat_aktivitas():
    aktivitas = input("Masukkan nama aktivitas: ")
    deskripsi = input("Masukkan deskripsi aktivitas: ")
    waktu = datetime.now()
    tanggal_str = waktu.strftime("%Y-%m-%d")
    waktu_str = waktu.strftime("%H:%M:%S")

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal_str, waktu_str, aktivitas, deskripsi])
    
    print(f"Aktivitas '{aktivitas}' berhasil dicatat!")

# Fungsi untuk menampilkan semua aktivitas yang telah dicatat
def tampilkan_aktivitas():
    print("\n--- Daftar Aktivitas Harian ---")
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Lewati header
            for row in reader:
                print(f"[{row[0]} {row[1]}] - {row[2]}: {row[3]}")
    except FileNotFoundError:
        print("Belum ada aktivitas yang dicatat.")

# Fungsi utama untuk mengelola menu
def menu():
    buat_file_csv()
    while True:
        print("\n--- Menu Aktivitas Harian ---")
        print("1. Catat Aktivitas")
        print("2. Tampilkan Aktivitas")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            catat_aktivitas()
        elif pilihan == "2":
            tampilkan_aktivitas()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan pencatat aktivitas!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
if _name_ == "_main_":
    menu()