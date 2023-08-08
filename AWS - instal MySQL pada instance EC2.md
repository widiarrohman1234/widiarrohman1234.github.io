Untuk menginstal MySQL pada instance EC2 yang menjalankan Ubuntu di AWS, Anda dapat mengikuti langkah-langkah berikut:

1. SSH ke instance EC2 Anda menggunakan klien SSH seperti Terminal atau PuTTY.

2. Pastikan sistem Ubuntu diupdate dengan menjalankan perintah berikut:
   ```
   sudo apt update
   sudo apt upgrade
   ```

3. Install MySQL Server dengan menjalankan perintah berikut:
   ```
   sudo apt install mysql-server
   ```

4. Selama instalasi, Anda akan diminta untuk memasukkan password untuk pengguna root MySQL. Masukkan password yang Anda inginkan dan konfirmasi.

5. Setelah instalasi selesai, jalankan perintah berikut untuk melakukan pengaturan keamanan awal MySQL:
   ```
   sudo mysql_secure_installation
   ```

   Anda akan diminta untuk mengonfigurasi beberapa opsi keamanan seperti menghapus pengguna anonim, menonaktifkan akses root jarak jauh, menghapus database tes, dan memuat ulang hak istimewa pengguna. Ikuti petunjuk yang diberikan selama proses ini.

6. Setelah pengaturan keamanan selesai, Anda dapat memulai layanan MySQL dengan menjalankan perintah:
   ```
   sudo systemctl start mysql
   ```

   Anda juga dapat memastikan bahwa layanan MySQL berjalan dengan baik dengan menjalankan perintah:
   ```
   sudo systemctl status mysql
   ```

   Jika layanan berjalan dengan baik, Anda akan melihat pesan yang menunjukkan status "active" atau "running".

7. Secara opsional, Anda dapat mengatur MySQL untuk memulai secara otomatis saat boot dengan menjalankan perintah berikut:
   ```
   sudo systemctl enable mysql
   ```

Selamat, Anda telah berhasil menginstal MySQL pada instance EC2 Ubuntu di AWS. Sekarang Anda dapat menggunakan MySQL dan mengelola database sesuai kebutuhan Anda.