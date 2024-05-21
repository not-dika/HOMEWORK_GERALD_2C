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
    choise = int(input("Masukan Pilihan : "))
    if choise == 1:
        nama = input("Masukan nama barang: ")
        stock = int(input("Masukan stock barang: "))
        db.tambah_data(database, nama, stock)
        print("")
    elif choise == 2:
        nama = input("Masukan nama barang: ")
        db.hapus_data(database, nama)
        print("")
    elif choise == 3:
        nama = input("Masukan nama barang atau 'Semua' untuk semua barang: ")
        db.tampilkan_data(database, nama)
        print("")
    elif choise == 4:
        print("Bye Bye!")
        exit()
    else:
        print("Pilihan Tidak Valid!")