# Input dari pengguna
gaji_pertahun = float(input("Masukkan gaji pertahun: "))
presentase_tabungan = float(input("Masukkan presentasi tabungan yang akan disimpan, tuliskan desimal (10% = .10): "))
total_biaya_rumah = float(input("Total harga rumah impian: "))
kenaikan_gaji = float(input("Masukkan kenaikan gaji berapa % /6 bulan, tuliskan desimal (10% = .10): "))

uang_dp_rumah = 0.25  # 25 persen dari harga rumah
pengembalian_r = 0.04  # Tingkat pengembalian investasi
gaji_bulanan = gaji_pertahun / 12
dp = total_biaya_rumah * uang_dp_rumah  # Uang muka yang dibutuhkan
tabungan = 0.0  # Total tabungan
bulan = 0  # Menghitung bulan

# Loop untuk menghitung bulan yang dibutuhkan
while tabungan < dp:
    tabungan += tabungan * (pengembalian_r / 12)  # Tambahkan bunga tabungan
    tabungan += presentase_tabungan * gaji_bulanan  # Menambah tabungan setiap bulan
    bulan += 1
    
    # Kenaikan gaji setiap 6 bulan
    if bulan % 6 == 0:
        gaji_pertahun += gaji_pertahun * kenaikan_gaji  # Kenaikan gaji
        gaji_bulanan = gaji_pertahun / 12  # Gaji bulanan disesuaikan

# Cetak hasil
print(f"Total berapa bulan: {bulan}")
