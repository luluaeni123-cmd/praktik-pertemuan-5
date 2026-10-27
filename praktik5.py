# Praktik 5: Analisis Frekuensi Kata

import re
from collections import Counter

try:
    with open("teks.txt", "r", encoding="utf-8") as file:
        teks = file.read()

    # Mengambil kata dan mengubahnya menjadi huruf kecil
    kata = re.findall(r"\b\w+\b", teks.lower())

    frekuensi = Counter(kata)

    print("--- Hasil Analisis Teks ---")
    print("Jumlah seluruh kata:", len(kata))
    print("Jumlah kata unik:", len(frekuensi))

    print("\n10 kata paling sering muncul:")
    for nama_kata, jumlah in frekuensi.most_common(10):
        print(f"{nama_kata}: {jumlah}")

    hapax = [
        nama_kata
        for nama_kata, jumlah in frekuensi.items()
        if jumlah == 1
    ]

    print("\nKata yang muncul satu kali:")
    print(hapax)
    print("Jumlah hapax legomena:", len(hapax))

    if kata:
        ttr = len(frekuensi) / len(kata)
    else:
        ttr = 0

    print(f"Type-Token Ratio (TTR): {ttr:.4f}")

except FileNotFoundError:
    print("File teks.txt tidak ditemukan.")
    print("Pastikan teks.txt berada di folder tugas yang sama.")