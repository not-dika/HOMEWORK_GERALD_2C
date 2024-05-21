def tambah_data(db, item, stock):
    db.append({"Nama" : item, "Stock" : stock})
    print("Berhasil menambahkan data")

def hapus_data(db, item):
    found = 0
    for i in range(len(db)):
        if db[i]['Nama'] == item:
            found += 1
            del db[i]
            print("Berhasil menghapus data")
    if found == 0:
        print(f"Tidak ada barang bernama {item}")

def tampilkan_data(db, item):
    if item.lower() == "semua":
        print("List data barang yang tersimpan: ")
        for i in range(len(db)):
            print(db[i])
    else:
        found = 0
        for i in range(len(db)):
            if item in db[i]['Nama']:
                if found == 0:
                    print(f"Data barang dengan nama {item}:")
                found += 1
                print(db[i])
        if found == 0:
                print(f"Data barang dengan nama {item} tidak ditemukan")