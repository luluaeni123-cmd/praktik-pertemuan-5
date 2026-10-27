# Praktik 1: Pengolahan String

kalimat = input("Masukkan sebuah kalimat: ")

kata = kalimat.split()
jumlah_kata = len(kata)
jumlah_karakter = len(kalimat)

if kata:
    kata_terpanjang = max(kata, key=len)
else:
    kata_terpanjang = ""

print("\n--- Hasil Pengolahan String ---")
print("Kalimat:", kalimat)
print("Jumlah kata:", jumlah_kata)
print("Jumlah karakter:", jumlah_karakter)
print("Kata terpanjang:", kata_terpanjang)
print("Title Case:", kalimat.title())