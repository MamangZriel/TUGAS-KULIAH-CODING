# Meminta input suhu dari pengguna
suhu = float(input("Masukkan temperatur air dalam derajat Celcius: "))

# Menentukan wujud air berdasarkan suhu
if suhu <= 0:
    print("Wujud air pada suhu tersebut adalah padat (es).")
elif 0 < suhu < 100:
    print("Wujud air pada suhu tersebut adalah cair.")   
else:
    print("Wujud air pada suhu tersebut adalah gas (uap).")
