a = int(input("Masukkan Bilangan Pertama : "))
b = int(input("Masukkan Bilangan Kedua : "))
c = int(input("Masukkan Bilangan Ketiga : "))

if a > b and a > c:
    print("Bilangan Terbesar adalah : ", a)
elif b > a and b > c:
    print("Bilangan Terbesar adalah : ", b)
else:
    print("Bilangan Terbesar adalah : ", c)