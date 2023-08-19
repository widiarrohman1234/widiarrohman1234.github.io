Berikut adalah langkah-langkah untuk menginstal MongoDB pada instance EC2 Ubuntu dan cara mengaksesnya:

Instalasi MongoDB:

1. Buka terminal SSH dan akses instance EC2 Ubuntu Anda.

2. Perbarui repositori paket dengan menjalankan perintah berikut:
   ```bash
   sudo apt update
   ```

3. Instal MongoDB dengan menjalankan perintah berikut:
   ```bash
   sudo apt install mongodb
   ```

4. Setelah instalasi selesai, layanan MongoDB akan mulai secara otomatis. Anda dapat memeriksa statusnya dengan perintah berikut:
   ```bash
   sudo systemctl status mongodb
   ```

   Jika statusnya aktif, maka MongoDB telah terinstal dan berjalan.

Konfigurasi Akses:

1. Secara default, MongoDB hanya akan menerima koneksi dari localhost (loopback). Jika Anda ingin mengakses MongoDB dari luar instance EC2, Anda perlu mengkonfigurasi bind IP.

2. Buka file konfigurasi MongoDB dengan menggunakan editor teks seperti Nano:
   ```bash
   sudo nano /etc/mongodb.conf
   ```

3. Temukan baris yang berisi `bind_ip` dan komentari baris tersebut dengan menambahkan tanda pagar (#) di awal baris. Hal ini akan mengizinkan MongoDB menerima koneksi dari semua IP.

4. Simpan perubahan dengan menekan `Ctrl + X`, lalu ketik `Y` dan tekan Enter untuk menyimpan file dengan nama yang sama.

5. Restart layanan MongoDB agar perubahan konfigurasi diterapkan:
   ```bash
   sudo systemctl restart mongodb
   ```

Mengakses MongoDB:

1. Untuk mengakses MongoDB dari terminal, jalankan perintah berikut:
   ```bash
   mongo
   ```

   Perintah ini akan membuka shell MongoDB, yang memungkinkan Anda untuk berinteraksi dengan basis data MongoDB.

2. Jika Anda ingin mengakses MongoDB melalui aplikasi atau skrip PHP, Anda perlu menggunakan driver MongoDB untuk PHP. Anda dapat menginstalnya dengan menjalankan perintah berikut:
   ```bash
   sudo apt install php-mongodb
   ```

   Setelah itu, restart server web Anda untuk memuat ulang konfigurasi PHP.

3. Dalam aplikasi Laravel, pastikan Anda telah mengatur konfigurasi koneksi MongoDB di file `config/database.php` dan `.env` sesuai dengan detail yang diperlukan.

Dengan demikian, Anda telah berhasil menginstal MongoDB pada instance EC2 Ubuntu dan dapat mengaksesnya melalui shell MongoDB atau melalui aplikasi menggunakan driver MongoDB untuk PHP.