# =========================================
# CHEMBUDDY - KALKULATOR KIMIA DIGITAL
# =========================================

# Data Ar unsur
data_ar = {
    "H": 1,
    "C": 12,
    "N": 14,
    "O": 16,
    "Na": 23,
    "Mg": 24,
    "Al": 27,
    "Si": 28,
    "P": 31,
    "S": 32,
    "Cl": 35.5,
    "K": 39,
    "Ca": 40,
    "Fe": 56,
    "Cu": 63.5,
    "Zn": 65
}

# =========================================
# FUNGSI INPUT ANGKA
# agar bisa pakai koma atau titik
# =========================================
def input_angka(teks):
    return float(input(teks).replace(",", "."))

print("🧪 CHEMBUDDY")
print("Kalkulator Kimia Digital")
print("=========================================")

while True:

    print("\nMENU PERHITUNGAN")
    print("1. Normalitas")
    print("2. Molaritas")
    print("3. BE (Berat Ekivalen)")
    print("4. BM (Berat Molekul)")
    print("5. Ar (Massa Atom Relatif)")
    print("6. Konversi Suhu")
    print("7. PPM")
    print("0. Keluar")

    pilihan = input("\nMasukkan pilihan: ")

    # =====================================
    # NORMALITAS
    # =====================================
    if pilihan == "1":

        print("\n=== KALKULATOR NORMALITAS ===")

        gram = input_angka("Masukkan massa zat (gram): ")
        be = input_angka("Masukkan Berat Ekivalen (BE): ")
        volume = input_angka("Masukkan volume larutan (mL): ")

        normalitas = (gram / be) / (volume / 1000)

        print(f"\nHasil Normalitas = {normalitas:.4f} N")

    # =====================================
    # MOLARITAS
    # =====================================
    elif pilihan == "2":

        print("\n=== KALKULATOR MOLARITAS ===")

        gram = input_angka("Masukkan massa zat (gram): ")
        bm = input_angka("Masukkan Berat Molekul (BM): ")
        volume = input_angka("Masukkan volume larutan (mL): ")

        molaritas = (gram / bm) / (volume / 1000)

        print(f"\nHasil Molaritas = {molaritas:.4f} M")

    # =====================================
    # BE
    # =====================================
    elif pilihan == "3":

        print("\n=== KALKULATOR BE ===")

        print("\n1. Hitung otomatis dari senyawa")
        print("2. Input BM manual")

        pilih_be = input("Pilih metode: ")

        # =========================
        # OTOMATIS DARI SENYAWA
        # =========================
        if pilih_be == "1":

            jumlah = int(input("\nBerapa jenis unsur dalam senyawa? "))

            total_bm = 0

            for i in range(jumlah):

                unsur = input(f"\nMasukkan simbol unsur ke-{i+1}: ")

                jumlah_atom = int(input("Jumlah atom: "))

                if unsur in data_ar:

                    ar = data_ar[unsur]

                    subtotal = ar * jumlah_atom

                    total_bm += subtotal

                    print(f"{unsur} = {ar} x {jumlah_atom} = {subtotal}")

                else:
                    print("Unsur tidak ditemukan")

            print(f"\nBM Senyawa = {total_bm}")

            valensi = input_angka("Masukkan valensi: ")

            be = total_bm / valensi

            print(f"\nBE = {be:.4f}")

        # =========================
        # INPUT BM MANUAL
        # =========================
        elif pilih_be == "2":

            bm = input_angka("\nMasukkan BM senyawa: ")

            valensi = input_angka("Masukkan valensi: ")

            be = bm / valensi

            print(f"\nBE = {be:.4f}")

    # =====================================
    # BM
    # =====================================
    elif pilihan == "4":

        print("\n=== KALKULATOR BM ===")

        jumlah = int(input("Berapa jenis unsur dalam senyawa? "))

        total_bm = 0

        for i in range(jumlah):

            unsur = input(f"\nMasukkan simbol unsur ke-{i+1}: ")

            jumlah_atom = int(input("Jumlah atom: "))

            if unsur in data_ar:

                ar = data_ar[unsur]

                subtotal = ar * jumlah_atom

                total_bm += subtotal

                print(f"{unsur} = {ar} x {jumlah_atom} = {subtotal}")

            else:
                print("Unsur tidak ditemukan")

        print(f"\nBM Senyawa = {total_bm}")

    # =====================================
    # AR
    # =====================================
    elif pilihan == "5":

        print("\n=== KALKULATOR Ar ===")

        unsur = input("Masukkan simbol unsur: ")

        if unsur in data_ar:

            print(f"\nAr {unsur} = {data_ar[unsur]}")

        else:
            print("\nUnsur tidak ditemukan")

    # =====================================
    # SUHU
    # =====================================
    elif pilihan == "6":

        print("\n=== KONVERSI SUHU ===")

        print("\n1. Celcius ke Fahrenheit")
        print("2. Celcius ke Kelvin")
        print("3. Celcius ke Reamur")

        print("4. Fahrenheit ke Celcius")
        print("5. Fahrenheit ke Kelvin")
        print("6. Fahrenheit ke Reamur")

        print("7. Kelvin ke Celcius")
        print("8. Kelvin ke Fahrenheit")
        print("9. Kelvin ke Reamur")

        print("10. Reamur ke Celcius")
        print("11. Reamur ke Fahrenheit")
        print("12. Reamur ke Kelvin")

        pilih_suhu = input("\nPilih konversi: ")

        suhu = input_angka("Masukkan suhu: ")

        # =========================
        # CELCIUS
        # =========================
        if pilih_suhu == "1":

            hasil = (suhu * 9/5) + 32
            print(f"\nHasil = {hasil:.2f} °F")

        elif pilih_suhu == "2":

            hasil = suhu + 273.15
            print(f"\nHasil = {hasil:.2f} K")

        elif pilih_suhu == "3":

            hasil = suhu * 4/5
            print(f"\nHasil = {hasil:.2f} °Re")

        # =========================
        # FAHRENHEIT
        # =========================
        elif pilih_suhu == "4":

            hasil = (suhu - 32) * 5/9
            print(f"\nHasil = {hasil:.2f} °C")

        elif pilih_suhu == "5":

            hasil = ((suhu - 32) * 5/9) + 273.15
            print(f"\nHasil = {hasil:.2f} K")

        elif pilih_suhu == "6":

            hasil = (suhu - 32) * 4/9
            print(f"\nHasil = {hasil:.2f} °Re")

        # =========================
        # KELVIN
        # =========================
        elif pilih_suhu == "7":

            hasil = suhu - 273.15
            print(f"\nHasil = {hasil:.2f} °C")

        elif pilih_suhu == "8":

            hasil = ((suhu - 273.15) * 9/5) + 32
            print(f"\nHasil = {hasil:.2f} °F")

        elif pilih_suhu == "9":

            hasil = (suhu - 273.15) * 4/5
            print(f"\nHasil = {hasil:.2f} °Re")

        # =========================
        # REAMUR
        # =========================
        elif pilih_suhu == "10":

            hasil = suhu * 5/4
            print(f"\nHasil = {hasil:.2f} °C")

        elif pilih_suhu == "11":

            hasil = (suhu * 9/4) + 32
            print(f"\nHasil = {hasil:.2f} °F")

        elif pilih_suhu == "12":

            hasil = (suhu * 5/4) + 273.15
            print(f"\nHasil = {hasil:.2f} K")

        else:

            print("\nPilihan tidak valid!")

    # =====================================
    # PPM
    # =====================================
    elif pilihan == "7":

        print("\n=== KALKULATOR PPM ===")

        massa = input_angka("Masukkan massa zat terlarut (mg): ")
        volume = input_angka("Masukkan volume larutan (L): ")

        ppm = massa / volume

        print(f"\nHasil PPM = {ppm:.4f} ppm")

    # =====================================
    # KELUAR
    # =====================================
    elif pilihan == "0":

        print("\nTerima kasih telah menggunakan ChemBuddy 🧪")
        break

    else:
        print("\nPilihan tidak valid!")
