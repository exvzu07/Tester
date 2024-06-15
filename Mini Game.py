import random

def main_game():
    lokasi_ular = random.randint(1, 5)

    print("I_I, I_I, I_I, I_I, I_I")

    tebakan = input('Tebak, di kotak mana ular berada? : [1] / [2] / [3] / [4] / [5] : ')
    konfirmasi = input(f'Anda telah memilih kotak nomor {tebakan}, apakah anda yakin (Ya, Tidak) : ')

    if konfirmasi.lower() == 'ya':
        if tebakan == str(lokasi_ular):
            print("Selamat, Jawaban Anda Benar, Lokasi ular berada di Kotak nomor " + str(lokasi_ular))
        else:
            print("Maaf, Jawaban Anda Salah, Lokasi ular berada di Kotak nomor " + str(lokasi_ular))
    else:
        print("Pilihan Anda tidak dikonfirmasi. Silakan coba lagi.")

# Minta username sekali di awal
welcome_message = "WELCOME TO THE GAME"

print("***********************")
print("**" + welcome_message + "**")
print("***********************")

New_User = input("Please, Enter Your Name : ")
print("Welcome, " + New_User)

# Main game loop
while True:
    main_game()
    ulang = input("Apakah Anda ingin bermain lagi? (Ya/Tidak) : ")
    if ulang.lower() != 'ya':
        print("Terima kasih sudah bermain!")
        break
