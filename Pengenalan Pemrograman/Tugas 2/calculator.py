# Nama: Azril Anggra Atmoko
# NIM: 241351096
# Kelas: Pagi A

def main_calculator():
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    penjumlahan = angka1 + angka2
    pengurangan = angka1 - angka2
    perkalian = angka1 * angka2
    pembagian = angka1 / angka2 if angka2 != 0 else "Tidak bisa dibagi dengan 0"

    print(f"Penjumlahan: {penjumlahan}")
    print(f"Pengurangan: {pengurangan}")
    print(f"Perkalian: {perkalian}")
    print(f"Pembagian: {pembagian}")


main_calculator()