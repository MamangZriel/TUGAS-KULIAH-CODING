def tambah(a, b):
  """Mengembalikan hasil penjumlahan a + b."""
  return a + b

def kurang(a, b):
  """Mengembalikan hasil pengurangan a - b."""
  return a - b

def kali(a, b):
  """Mengembalikan hasil perkalian a * b."""
  return a * b

def bagi(a, b):
  """Mengembalikan hasil pembagian a / b. Jika b sama dengan nol, tampilkan pesan error: "Pembagian dengan nol tidak diperbolehkan."."""
  if b == 0:
    return "Pembagian dengan nol tidak diperbolehkan."
  else:
    return a / b

# Program Utama
a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))
operasi = input("Masukkan operasi (+, -, *, /): ")

if operasi == "+":
  hasil = tambah(a, b)
elif operasi == "-":
  hasil = kurang(a, b)
elif operasi == "*":
  hasil = kali(a, b)
elif operasi == "/":
  hasil = bagi(a, b)
else:
  hasil = "Operasi tidak valid"

print(f"Hasil: {hasil}")