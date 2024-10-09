def calculate_savings(salary, savings_rate, months, semi_annual_raise, annual_return):
    current_savings = 0.0
    for month in range(months):
        current_savings += current_savings * (annual_return / 12)  # Return investasi per bulan
        current_savings += (salary / 12) * savings_rate  # Tabungan bulanan
        if month % 6 == 5:  # Setiap 6 bulan
            salary += salary * semi_annual_raise  # Kenaikan gaji setiap 6 bulan
    return current_savings

def find_best_savings_rate(starting_salary, house_cost, down_payment_percent, semi_annual_raise, annual_return, months):
    down_payment = down_payment_percent * house_cost  # Menghitung jumlah DP
    print(f"Down Payment: {down_payment}")  # Debugging line

    # Cek apakah gaji awal lebih besar atau sama dengan harga rumah
    if starting_salary >= house_cost:
        print("Anda bisa langsung membeli rumah tanpa menabung.")
        return

    low, high = 0, 10000  # Rentang awal untuk tabungan (0% hingga 100%)
    steps, best_rate = 0, None

    while low <= high:
        steps += 1
        guess = (low + high) // 2  # Cek tabungan pada tebakan pertengahan
        savings_rate = guess / 10000.0  # Ubah menjadi bentuk desimal (misalnya 0.05 untuk 5%)
        
        current_savings = calculate_savings(starting_salary, savings_rate, months, semi_annual_raise, annual_return)
        print(f"Guess: {savings_rate:.4f}, Current Savings: {current_savings:.2f}")  # Debugging line

        if abs(current_savings - down_payment) < 100:  # Jika selisih < $100
            best_rate = savings_rate
            break
        elif current_savings < down_payment:  # Jika tabungan kurang dari DP
            low = guess + 1  # Naikkan tebakan
        else:  # Jika tabungan lebih dari DP
            high = guess - 1  # Turunkan tebakan

    if best_rate is not None:
        print(f"Tingkat tabungan terbaik: {best_rate:.4f}")
        print(f"Jumlah langkah pencarian: {steps}")
    else:
        print("Tidak mungkin mencapai uang DP dalam waktu yang diberikan.")

if __name__ == "__main__":
    # Input dari pengguna
    biaya_rumah = float(input("Masukkan biaya rumah: "))
    uang_dp = float(input("Masukkan persen uang muka (misal 0.25 untuk 25%): "))
    kenaikan_gaji_tahunan = float(input("Masukkan kenaikan gaji setengah tahun (misal 0.07 untuk 7%): "))
    laba = float(input("Masukkan laba investasi tahunan (misal 0.04 untuk 4%): "))
    waktu_menabung = int(input("Masukkan jumlah bulan menabung: "))
    gaji_awal = float(input("Masukkan gaji awal: "))

    find_best_savings_rate(gaji_awal, biaya_rumah, uang_dp, kenaikan_gaji_tahunan, laba, waktu_menabung)
