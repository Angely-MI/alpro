def hitung_total(topping, ukuran, extra_cheese):
    """Fungsi untuk menghitung total harga pizza."""

    harga_topping = {
        'feta cheese': 5000,
        'pepperoni': 10000,
        'chicken mayo': 7000,
    }

    harga_ukuran = {
        'personal': 20000,
        'medium': 35000,
        'large': 55000,
    }

    total = harga_topping.get(topping, 0) + harga_ukuran[ukuran]

    if extra_cheese:
        total += 13000

    return total


def main():
    """Fungsi utama untuk menjalankan program pemesanan pizza."""

    print("Selamat datang di Pizza Kelompok 2!")

    # Memilih topping pizza
    topping = None
    while topping is None:
        pilihan_topping = input(
            "Pilih topping pizza (feta cheese, pepperoni, chicken mayo): "
        )
        if pilihan_topping.lower() in ('feta cheese', 'pepperoni', 'chicken mayo'):
            topping = pilihan_topping.lower()
        else:
            print("Pilihan topping tidak valid. Silahkan coba lagi.")

    # Memilih crust pizza
    crust = None
    while crust is None:
        pilihan_crust = input("Pilih crust pizza (thin crust, thick crust): ")
        if pilihan_crust.lower() in ('thin crust', 'thick crust'):
            crust = pilihan_crust.lower()
        else:
            print("Pilihan crust tidak valid. Silahkan coba lagi.")

    # Memilih ukuran pizza
    ukuran = None
    while ukuran is None:
        pilihan_ukuran = input("Pilih ukuran pizza (personal, medium, large): ")
        if pilihan_ukuran.lower() in ('personal', 'medium', 'large'):
            ukuran = pilihan_ukuran.lower()
        else:
            print("Pilihan ukuran tidak valid. Silahkan coba lagi.")

    # Menambahkan extra cheese
    extra_cheese = input("Tambahkan extra cheese? (ya/tidak): ")
    extra_cheese = extra_cheese.lower() == 'ya'

    # Menghitung total harga
    total_harga = hitung_total(topping, ukuran, extra_cheese)

    # Menampilkan total harga
    print(
        f"Total harga pizza dengan topping {topping}, crust {crust}, ukuran {ukuran}"
    )
    if extra_cheese:
        print("dengan extra cheese")
    print(f"adalah Rp.{total_harga:,}")
    print("Thank you for your order! We hope you like it")


if __name__ == "__main__":
    main()
    