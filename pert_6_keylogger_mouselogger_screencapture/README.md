# Keylogger, MouseLogger, Screen Capture
### Keylogger
Keylogger atau dapat disebut juga sebagai keystroke logging adalah tindakan merekam/mencatat tombol yang ditekan pada keyboard dan biasanya secara tersembunyi, sehingga orang yang menggunakan keyboard tidak sadar bahwa tindakan mereka sedang dipantau. Data kemudian dapat diambil ketika program keylogger ini dijalankan.

### Mouselogger
Mouselogger adalah tindakan merekam/mencatat gerakan pada mouse dan biasanya secara tersembunyi, sehingga orang yang menggunakan mouse tidak sadar bahwa tindakan mereka sedang dipantau. Data kemudian dapat diambil ketika program mouselogger ini dijalankan.

### Screen Capture
Sesuai dengan namanya, kegunaannya adalah untuk screen capture.


## Note
* Karena library yang bisa dijalankan di Linux dan Windows berbeda, pastikan kodingan menggunakan library yang sesuai.
* Library yang akan digunakan untuk membuat keylogger dan mouselogger adalah pyxhook (untuk kali linux) ataupun pyhook (untuk windows), sedangkan library untuk screen capture adalah autopy.
* Kodingan untuk reverse tcp yang dicontohkan hanya untuk keylogger saja. Untuk reverse tcp mouselogger mirip dengan keylogger, bedanya hanya terletak pada event yang harus dipanggil saja.
