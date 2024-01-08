Menu = {
    "Ayam Goreng": 10000,
    "Nasi Uduk": 12000,
    "Soto Ayam": 15000,
    "Jus Mangga": 10000,
    "Es Teh": 5000
}
print("==================== Daftar Menu ====================")
for i in Menu:
    print("Daftar Menu : ", i,"\t Harga : ",Menu[i])
print("Pembelian diatas Rp50.000,- mendapatkan diskon 10%")
print("===================================================")    
beli = input("Pilih Menu : ")    
jumlah = int(input("Jumlah Pesanan : "))
bayar = jumlah * Menu[beli]

if bayar > 50000:
    diskon = bayar*10/100
    total = bayar - diskon
else:
    total = bayar
    
print("=================== Struk Pembayaran ===============")
print("Menu yang dipesan      : ",beli)
print("Jumlah yang dipesan      : ",jumlah) 
print("Total Biaya              : ",bayar)
print("Total yang harus dibayar : ",total)       