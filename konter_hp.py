menu_indosat = {
        '1.quota 3gb =' : 25000,
        '2.quota 5gb =' : 30000,
        '3.quota 7gb =' : 50000,
        '4.quota 10gb =': 100000
}
menu_Tri = {
        '1.quota 3gb =' : 20000,
        '2.quota 5gb =' : 35000,
        '3.quota 7gb =' : 40000,
        '4.quota 10gb =': 110000
}
menu_telkomsel = {
        '1.quota 3gb =' : 35000,
        '2.quota 5gb =' : 40000,
        '3.quota 7gb =' : 60000,
        '4.quota 10gb =': 120000
}
import os
os.system("cls")
def pilihan(operator,kuota, price):
    if operator == "indosat":
        if kuota == "1":
            harga_bayar = price - 25000
            print(harga_bayar)
        elif kuota == "2":
            harga_bayar = price - 30000
            print(harga_bayar)
        elif kuota == "3":
            harga_bayar = price - 50000
            print(harga_bayar)
        elif kuota == "4":
            harga_bayar = price - 100000
            print(harga_bayar)
        else:
            print("quota tidak ada")
    elif operator == "telkomsel":
        if kuota == "1":
            harga_bayar = price - 35000
            print(harga_bayar)
        elif kuota == "2":
            harga_bayar = price - 40000
            print(harga_bayar)
        elif kuota == "3":
            harga_bayar = price - 60000
            print(harga_bayar)
        elif kuota == "4":
            harga_bayar = price - 120000
            print(harga_bayar)
        else:
            print("quota tidak ada")
    elif operator == "Tri":
        if kuota == "1":
            harga_bayar = price - 20000
            print(harga_bayar)
        elif kuota == "2":
            harga_bayar = price - 35000
            print(harga_bayar)
        elif kuota == "3":
            harga_bayar = price - 40000
            print(harga_bayar)
        elif kuota == "4":
            harga_bayar = price - 110000
            print(harga_bayar)
        else:
            print("quota tidak ada")
    return harga_bayar
print('-' * 41 )
print('      Selamat datang di "ZAN CELL"')
print('-' * 41 )
print("daftar menu operator  ")
print("1.indosat\n2.telkomsel\n3.Tri\n")
nomor_hp = input("masukan nomor hp : ")
while True:
    operator = input("masukan operator : ")
    if operator == 'indosat':
        print("daftar harga quota indosat : ")
        for i,j in menu_indosat.items():
              print(i,j)
    elif operator == 'telkomsel':
        print("daftar harga quota telkomsel : ")
        for j,i in menu_telkomsel.items():
         print(j,i)
    elif operator == 'Tri':
        print("daftar harga quota Tri : ")
        for j,i in menu_Tri.items():
         print(j,i)
    kuota = input("masukan pilihan(1/2/3/4):")
    bayar = int(input("masukan nominal bayar : "))

    pilihan(operator, kuota, bayar)

    stop  = input("apakah ada yang mau di beli lagi? ")
    if stop == "tidak":
        print("\n\n~~~terimakasih~~~") 
        print('-' * 41) 
        break

