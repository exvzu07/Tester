saldo_awal = 10000
print('Saldo awal Anda adalah : ' + str(saldo_awal))
deposit = input('Masukkan saldo yang ingin di input : ')
saldo_total = int(saldo_awal) + int(deposit)
print('Saldo total Anda adalah : ' + str(saldo_total))
# User bisa melunasi hutang jika uangnya cukup
# User harus melakukan deposit ulang jika saldonya kurang
hutang = 75_000

while saldo_total < hutang:
    print('Hutang Masih Belum Lunas, Lakukan Deposit Ulang Hingga Lunas')
    saldo_total += int(input('Masukkan Saldo kembali : '))
    print('Saldo total Anda adalah : ' + str(saldo_total))

saldo_sisa = int(saldo_total) - int(hutang)
print('Saldo tersisa setelah membayar hutang adalah : ' + str(saldo_sisa))
print("---------------------------------------------")
print('Anda telah melunasi seluruh hutang')