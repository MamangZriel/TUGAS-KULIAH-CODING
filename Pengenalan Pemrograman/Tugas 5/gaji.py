def hitung_gaji_pokok(jam_kerja, gaji_per_jam):
  """
  Menghitung gaji pokok karyawan berdasarkan jam kerja reguler.
  
  Args:
    jam_kerja: Jumlah jam kerja karyawan.
    gaji_per_jam: Gaji per jam karyawan.
  
  Returns:
    Gaji pokok karyawan.
  """
  
  if jam_kerja > 40:
    jam_kerja = 40
  return jam_kerja * gaji_per_jam

def hitung_lembur(jam_kerja, gaji_per_jam):
  """
  Menghitung gaji lembur karyawan berdasarkan jam kerja tambahan.
  
  Args:
    jam_kerja: Jumlah jam kerja karyawan.
    gaji_per_jam: Gaji per jam karyawan.
  
  Returns:
    Gaji lembur karyawan.
  """
  
  if jam_kerja > 40:
    jam_lembur = jam_kerja - 40
    return jam_lembur * gaji_per_jam * 1.5
  else:
    return 0

def hitung_total_gaji(gaji_pokok, gaji_lembur):
  """
  Menghitung total gaji karyawan dengan menjumlahkan gaji pokok dan gaji lembur.
  
  Args:
    gaji_pokok: Gaji pokok karyawan.
    gaji_lembur: Gaji lembur karyawan.
  
  Returns:
    Total gaji karyawan.
  """
  
  return gaji_pokok + gaji_lembur

def main():
  """
  Program utama yang meminta input dari pengguna dan menampilkan rincian perhitungan gaji.
  """
  
  jam_kerja = float(input("Masukkan jam kerja total: "))
  gaji_per_jam = float(input("Masukkan gaji per jam: "))
  
  gaji_pokok = hitung_gaji_pokok(jam_kerja, gaji_per_jam)
  gaji_lembur = hitung_lembur(jam_kerja, gaji_per_jam)
  total_gaji = hitung_total_gaji(gaji_pokok, gaji_lembur)

  print("Gaji Pokok: Rp", gaji_pokok)
  print("Gaji Lembur: Rp", gaji_lembur)
  print("Total Gaji: Rp", total_gaji)

if __name__ == "__main__":
  main()