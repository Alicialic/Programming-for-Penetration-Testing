import sys
import getopt
from queue import Queue
from threading import Thread
import requests

URL = ''
WORD_FILE = ''
EXTENSION_FILE = ''
WORD_QUEUE = Queue()
WORDS = []
EXTENSIONS = []

def check_url_path(path):
    try:
        response = requests.get(f'http://{URL}/{path}') # mencoba untuk merequest ke url. Jika berhasil, maka hasil request akan mengembalikan response dan response tersebut ditampung oleh variabel response
        status_code = response.status_code # mendapatkan status code dari response dan ditampung oleh variabel status_code
    except:
        print('URL not found')
        sys.exit(0)

    if status_code == 404: # jika status code adalah 404
        print(f"File/path not found: {path}") # jika hanya ingin memprint file/path yang ditemukan, maka code ini boleh dikomen
        return False
    elif status_code == 200: # jika status code adalah 200
        print(f'[*] File/path found: {path}')
        return True
    elif status_code == 403: # jika status code adalah 403
        print(f'Forbidden file/path found: {path}')
        return True

    return False

def get_queue():
    while not WORD_QUEUE.empty(): # meloop sampai tidak ada value pada list WORD_QUEUE
        word = WORD_QUEUE.get() # mendapatkan item dari WORD_QUEUE, kemudian menghapusnya dari queue

        if check_url_path(word): # mengecek path
            add_brutelist(word) # jika ternyata path ditemukan (check_url_path() mengembalikan nilai True), maka akan dilakukan pengecekan ke dalam path lebih dalam lagi

def run_thread():
    threads = []

    # membuat thread sebanyak 10
    # jumlah thread yang ingin dibuat tidak harus 10, tetapi dapat diubah sesuai kebutuhan
    for _ in range(10):
        t = Thread(target=get_queue) # memanggil fungsi get_queue()
        t.start() # menjalankan thread
        threads.append(t) # memasukkan thread ke list threads

    for t in threads: # meloop thread yang ada di list threads
        t.join() # menunggu sampai thread berakhir

def file_with_extension(path):
    files = []

    for extension in EXTENSIONS: # meloop semua ekstensi dari list EXTENSIONS
        # memasukkan kombinasi dari path dan juga ektensi ke files
        # contoh hasil kombinasi:
        # /css/style.css
        # /index.html
        files.append(f'{path}.{extension}')

    return files # mengembalikan list files kepada pemanggil

def add_brutelist(path):
    global WORD_QUEUE

    for word in WORDS: # meloop semua value yang ada di WORDS
        # memasukkan kombinasi dari path dan juga word ke WORD_QUEUE
        # contoh hasil kombinasi:
        # /css
        # /assets/image
        WORD_QUEUE.put(f'{path}/{word}') 

        # memanggil fungsi file_with_extension()
        # dari fungsi tersebut dikembalikan list dari kombinasi path, word dan ekstensi
        # kemudian hasil kombinasi tersebut diloop
        for file in file_with_extension(f'{path}/{word}'):
            WORD_QUEUE.put(file) # hasil kombinasi dimasukkan ke dalam WORD_QUEUE

def read_file(filename):
    temp_list = []
    read_file = open(filename, 'r') # membaca file berdasarkan filename dan ditampung oleh read_file

    # meloop semua isi dari file yang dibaca
    # kemudian menambahkan ke dalam temp_list
    for file in read_file:
        temp_list.append(file.strip())
    read_file.close() # menutup file yang sudah selesai dibaca

    return temp_list # mengembalikan list temp_list kepada pemanggil

def initialize_dirbuster():
    global WORDS
    global EXTENSIONS

    WORDS = read_file(WORD_FILE) # memanggil fungsi read_file dan mengembalikan list kata, hasil pengembalian ditampung oleh WORDS
    EXTENSIONS = read_file(EXTENSION_FILE) # memanggil fungsi read_file dan mengembalikan list ekstensi, hasil pengembalian ditampung oleh EXTENSIONS
    
    add_brutelist('')
    run_thread()

def main():
    global URL
    global WORD_FILE
    global EXTENSION_FILE

    try:
        # memparse command line options dan parameter list, kemudian menampung ke variabel "args"
        args, _ = getopt.getopt(sys.argv[1:], "u:w:e:")
    except:
        # jika tidak sesuai yang diminta, maka akan memberikan contoh pemakaian
        print("Usage: dirbuster.py -u 127.0.0.1/web -w wordlist.txt -e extensionlist.txt")
        return

    # meloop semua value yang ada pada variabel "args"
    # karena variabel "args" ini memiliki key dan value, maka kita akan memisah value menjadi key dan value
    for key, value in args:
        if key == "-u": # jika keynya adalah -u
            URL = value
        elif key == "-w": # jika keynya adalah -w
            WORD_FILE = value
        elif key == "-e": # jika keynya adalah -e
            EXTENSION_FILE = value

    initialize_dirbuster()

# mengecek apakah fungsi yang dipanggilnya itu bernama "main"
# - jika bernama main, akan mengembalikan nilai True sehingga fungsi "main" dijalankan
# - jika tidak bernama main, akan mengembalikan nilai False sehingga fungsi "main" tidak dijalankan
if __name__ == "__main__":
    main() # memanggil fungsi main