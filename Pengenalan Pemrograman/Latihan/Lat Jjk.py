Nama=input("Masukan Nama Karyawan: ")
JJK=int(input("Masukan Jumlah Jam Kerja: "))

if(JJK<=48):
    Upah=2000*JJK
else:
    Lembur=(JJK-48)*3000
    Upah=(2000*48)+Lembur
print("upahnya adalah", Upah)
