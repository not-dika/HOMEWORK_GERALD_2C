def tambah_data(db, item, stock):
    db.append({"Nama" : item, "Stock" : stock})
    print("Berhasil menambahkan data")

def tampilkan_data(db, item):
    if len(db) == 0:
        print("Data barang kosong.")
    elif item.lower() == "semua":
        print("List data barang yang tersimpan: ")
        for i in range(len(db)):
            print(f"- {db[i]['Nama']}, Stock: {db[i]['Stock']}")
    else:
        found = 0
        for i in range(len(db)):
            if item in db[i]['Nama']:
                if found == 0:
                    print(f"Data barang dengan nama {item}:")
                found += 1
                print(f"- {db[i]['Nama']}, Stock: {db[i]['Stock']}")
        if found == 0:
                print(f"Data barang dengan nama {item} tidak ditemukan")

def update_data(db, item):
    found = 0
    for i in range(len(db)):
        if db[i]['Nama'] == item:
            found += 1
            db[i]['Stock'] = int(input("Masukan Stock Baru: "))
            print("Berhasil mengedit data")
    if found == 0:
        print(f"Tidak ada barang bernama {item}")

def hapus_data(db, item):
    found = 0
    for i in range(len(db)):
        if db[i]['Nama'] == item:
            found += 1
            del db[i]
            print("Berhasil menghapus data")
    if found == 0:
        print(f"Tidak ada barang bernama {item}")