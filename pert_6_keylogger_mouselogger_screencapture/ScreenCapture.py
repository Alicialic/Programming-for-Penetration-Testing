import autopy
from datetime import datetime

# capture screen
capture = autopy.bitmap.capture_screen()

# menyimpan hasil capture screen dengan format penamaannya 
# berdasarkan tanggal dan waktu sekarang dengan ekstensi .jpeg
# Note:
# + untuk nama bebas menggunakan apa saja, disini digunakan datetime agar namanya unik saja
# + untuk ektensi bebas, selama ekstensi yang digunakan adalah untuk gambar
capture.save('{}.jpeg'.format(datetime.now()))