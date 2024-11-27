# Nama: Azril Anggra Atmoko
# NIM: 241351096
# Kelas: Pagi A

def shoping_total():
    harga_satuan = float(input("Masukkan harga satuan barang: "))
    jumlah_barang = int(input("Masukkan jumlah barang: "))

    total_harga = harga_satuan * jumlah_barang
    print(f"Harga Total Belanja: {total_harga}")


shoping_total()