#menentukan berapa lama waktu untuk meabung
#uamg dp = 25% dari total harga rumah 
#Asumsikan bahwa investasi Anda menghasilkan pengembalian r = 0,04 (4%).

gaji_pertahun = float(input("masukkan gaji pertahun: " ))
presentase_tabungan = float(input("masukkan presentasi tabungan yang akan disimpan , tuliskan desimal (10% = .10) : "))
total_biaya_rumah = float(input("total harga rumah impian : " ))

uang_dp_rumah = 0.25 # 25% dari total harga rumah
tabungan= 0.0
pengembalian_r = 0.04
gaji_bulanan = gaji_pertahun/12
dp = total_biaya_rumah * uang_dp_rumah
bulan = 0

#menghitung tabungan awal
while tabungan < dp :
    tabungan += tabungan * (pengembalian_r/12 ) + presentase_tabungan * gaji_bulanan
    bulan += 1

print(f"berapa bulan:{bulan}")