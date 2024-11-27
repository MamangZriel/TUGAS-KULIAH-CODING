# Meminta input total pembelian dari pengguna
total_pembelian = float(input("Masukkan total pembelian: "))

# Menentukan diskon berdasarkan total pembelian
if total_pembelian > 100000:
    diskon = 20
elif 50000 <= total_pembelian <= 100000:
    diskon = 15
elif 10000 <= total_pembelian < 50000:
    diskon = 10
else:
    diskon = 0

# Menghitung jumlah diskon dalam bentuk nominal
jumlah_diskon = (diskon / 100) * total_pembelian

# Menghitung total harga yang harus dibayar setelah diskon
harga_setelah_diskon = total_pembelian - jumlah_diskon

# Menampilkan persentase diskon, jumlah diskon, dan harga setelah diskon
print(f"Diskon yang diperoleh: {diskon}%")
print(f"Jumlah diskon: Rp {jumlah_diskon}")
print(f"Harga yang harus dibayar: Rp {harga_setelah_diskon}")