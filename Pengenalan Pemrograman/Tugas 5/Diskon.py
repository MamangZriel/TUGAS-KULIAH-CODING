def hitung_diskon(total_belanja):
    """Menghitung nilai diskon berdasarkan total belanja."""
    if total_belanja < 100000:
        diskon = 0
    elif total_belanja <= 500000:
        diskon = total_belanja * 0.10  # Diskon 10%
    else:
        diskon = total_belanja * 0.20  # Diskon 20%
    return diskon

def hitung_total_bayar(total_belanja, diskon):
    """Menghitung total yang harus dibayar setelah diskon."""
    total_bayar = total_belanja - diskon
    return total_bayar

# Program utama
def main():
    # Meminta input total belanja dari pengguna
    total_belanja = float(input("Masukkan total belanja Anda: Rp"))
    
    # Menggunakan fungsi untuk menghitung diskon dan total yang harus dibayar
    diskon = hitung_diskon(total_belanja)
    total_bayar = hitung_total_bayar(total_belanja, diskon)
    
    # Menampilkan total belanja, diskon, dan total yang harus dibayar
    print(f"\nTotal Belanja: Rp{total_belanja:,.2f}")
    print(f"Diskon: Rp{diskon:,.2f}")
    print(f"Total yang harus dibayar: Rp{total_bayar:,.2f}")

# Memanggil program utama
if __name__ == "__main__":
    main()