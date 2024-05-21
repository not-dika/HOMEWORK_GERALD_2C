import modul8 as db

database = []
print("Program Manajemen Stock Barang")
print("Pilihan:")
print("1. Tambah Data Barang")
print("2. Edit Data Barang")
print("3. Hapus Data Barang")
print("4. Cari Data Barang")
print("5. Tampilkan Semua Data Barang")
print("6. Tampilkan Jumlah Data Tersimpan")
print("7. Keluar\n")
while True:
    choise = input("Masukan Pilihan : ")
    if choise == "1" or choise.lower() == "tambah data barang":
        nama = input("Masukan nama barang: ")
        stock = int(input("Masukan stock barang: "))
        db.tambah_data(database, nama, stock)
        print("")
    elif choise == "2" or choise.lower() == "edit data barang":
        nama = input("Masukan nama barang: ")
        db.edit_data(database, nama)
        print("")
    elif choise == "3" or choise.lower() == "hapus data barang":
        nama = input("Masukan nama barang: ")
        db.hapus_data(database, nama)
        print("")
    elif choise == "4" or choise.lower() == "cari data barang":
        nama = input("Masukan nama barang: ")
        db.tampilkan_data(database, nama)
        print("")
    elif choise == "5" or choise.lower() == "tampilkan semua data barang":
        db.tampilkan_data(database, "semua")
        print("")
    elif choise == "6" or choise.lower() == "tampilkan jumlah data tersimpan":
        print(f"Jumlah Data Tersimpan: {len(database)} Barang")
        print("")
    elif choise == "7" or choise.lower() == "keluar":
        print("Bye Bye!")
        exit()
    else:
        print("Program Manajemen Stock Barang")
        print("Pilihan:")
        print("1. Tambah Data Barang")
        print("2. Edit Data Barang")
        print("3. Hapus Data Barang")
        print("4. Cari Data Barang")
        print("5. Tampilkan Semua Data Barang")
        print("6. Tampilkan Jumlah Data Tersimpan")
        print("7. Keluar\n")
        print("Pilihan Tidak Valid!")