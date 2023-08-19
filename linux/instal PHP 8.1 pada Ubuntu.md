Untuk menginstal PHP 8.1 pada Ubuntu, Anda dapat mengikuti langkah-langkah berikut:

1. Pastikan sistem Ubuntu Anda diperbarui dengan menjalankan perintah berikut:
   ```
   sudo apt update
   sudo apt upgrade
   ```

2. Tambahkan repositori Ondřej Surý untuk PHP 8.1 dengan menjalankan perintah berikut:
   ```
   sudo add-apt-repository ppa:ondrej/php
   ```

3. Lakukan pembaruan paket setelah menambahkan repositori:
   ```
   sudo apt update
   ```

4. Instal PHP 8.1 dan paket-paket terkait dengan perintah berikut:
   ```
   sudo apt install php8.1
   ```

5. Anda juga dapat menginstal beberapa modul PHP yang umum digunakan. Misalnya, jika Anda membutuhkan modul MySQL, jalankan perintah berikut: (Optional)
   ```
   sudo apt install php8.1-mysql
sudo apt install php-mysql

   ```

6. Setelah selesai menginstal PHP 8.1, verifikasi instalasi dengan menjalankan perintah:
   ```
   php -v
   ```
7. simpan file phpinfo.php pada /var/www/html
```
nano phpinfo.php
```
```
<?php
// File: phpinfo.php

// Menampilkan semua informasi konfigurasi PHP
phpinfo();
?>

```
   Anda akan melihat informasi versi PHP 8.1 yang terinstal.

Selamat, Anda telah berhasil menginstal PHP 8.1 pada Ubuntu. Anda dapat menggunakan PHP 8.1 dengan menjalankan skrip PHP atau mengonfigurasi server web seperti Apache atau Nginx untuk menggunakan versi PHP yang baru diinstal.