# Buatlah sebuah program Python yang meminta pengguna untuk memasukkan sebuah bilangan bulat.
# Program tersebut harus mencetak apakah bilangan tersebut ganjil atau genap.

# Meminta pengguna memasukkan bilangan bulat
bilangan = int(input("Masukkan bilangan bulat: "))

# Memeriksa apakah bilangan ganjil atau genap
if bilangan % 2 == 0:
  print(f"Bilangan {bilangan} adalah bilangan genap.")
else:
  print(f"Bilangan {bilangan} adalah bilangan ganjil.")