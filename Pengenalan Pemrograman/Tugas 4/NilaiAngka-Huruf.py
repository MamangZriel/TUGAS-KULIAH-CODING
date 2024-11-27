# Meminta input nilai angka dari pengguna
nilai = int(input("Masukkan nilai angka (0-100): "))

# Menentukan nilai huruf berdasarkan nilai angka
if 0 <= nilai <= 20:
    print("Nilai huruf: E")
elif 21 <= nilai <= 40:
    print("Nilai huruf: D")
elif 41 <= nilai <= 60:
    print("Nilai huruf: C")
elif 61 <= nilai <= 80:
    print("Nilai huruf: B")
elif 81 <= nilai <= 100:
    print("Nilai huruf: A")
else:
    print("Nilai tidak valid. Masukkan nilai antara 0-100.")
