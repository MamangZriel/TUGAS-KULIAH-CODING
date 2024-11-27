# Meminta input nama, golongan, dan jumlah jam kerja
nama_karyawan = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan (A/B/C/D): ").upper()
jam_kerja = float(input("Masukkan jumlah jam kerja selama seminggu: "))

# Menentukan upah per jam berdasarkan golongan
if golongan == 'A':
    upah_per_jam = 4000
elif golongan == 'B':
    upah_per_jam = 5000
elif golongan == 'C':
    upah_per_jam = 6000
elif golongan == 'D':
    upah_per_jam = 7500
else:
    print("Golongan tidak valid.")
    exit()

# Menghitung gaji mingguan
if jam_kerja > 48:
    jam_lembur = jam_kerja - 48
    upah_lembur = jam_lembur * 3000
    gaji_mingguan = (48 * upah_per_jam) + upah_lembur
else:
    gaji_mingguan = jam_kerja * upah_per_jam

# Menampilkan hasil
print(f"\nNama Karyawan: {nama_karyawan}")
print(f"Total Gaji Mingguan: Rp {gaji_mingguan}")
