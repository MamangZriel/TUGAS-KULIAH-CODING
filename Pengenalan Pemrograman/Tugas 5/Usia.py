def tentukan_kategori_usia(umur):
  """
  Fungsi untuk menentukan kategori usia berdasarkan umur.

  Args:
    umur: Umur seseorang.

  Returns:
    String kategori usia.
  """
  if umur >= 0 and umur <= 12:
    return "Anak-anak"
  elif umur >= 13 and umur <= 17:
    return "Remaja"
  elif umur >= 18 and umur <= 64:
    return "Dewasa"
  elif umur >= 65:
    return "Lansia"
  else:
    return "Umur tidak valid"

# Program utama
umur = int(input("Masukkan umur: "))
kategori_usia = tentukan_kategori_usia(umur)
print("Kategori usia:", kategori_usia)
