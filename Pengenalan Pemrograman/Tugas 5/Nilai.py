def hitung_nilai_akhir(nilai_ujian, nilai_tugas):
  """
  Fungsi untuk menghitung nilai akhir siswa.

  Args:
    nilai_ujian: Nilai ujian siswa.
    nilai_tugas: Nilai tugas siswa.

  Returns:
    Nilai akhir siswa.
  """
  nilai_akhir = (nilai_ujian * 0.7) + (nilai_tugas * 0.3)
  return nilai_akhir

# Program utama
nilai_ujian = float(input("Masukkan nilai ujian: "))
nilai_tugas = float(input("Masukkan nilai tugas: "))

nilai_akhir = hitung_nilai_akhir(nilai_ujian, nilai_tugas)

print("Nilai akhir siswa adalah:", nilai_akhir)