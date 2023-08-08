Jika Anda ingin menginstal phpMyAdmin menggunakan curl, Anda dapat mengikuti langkah-langkah berikut:

1. Pastikan Anda memiliki curl terinstal di sistem Anda. Jika belum, Anda dapat menginstalnya dengan menjalankan perintah berikut:

   ```
   sudo apt-get install curl
   ```

2. Buka terminal dan jalankan perintah berikut untuk mengunduh arsip phpMyAdmin:

   ```
   curl -O -L https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.zip
   ```

   Perintah ini akan mengunduh arsip phpMyAdmin dalam format zip.

3. Setelah proses pengunduhan selesai, ekstrak arsip zip dengan menjalankan perintah berikut:

   ```
   apt install unzip
   unzip phpMyAdmin-5.2.1-all-languages.zip
   ```

   Ini akan membuat direktori `phpMyAdmin-5.2.1-all-languages` dengan isi arsip yang diekstrak.

4. Pindah ke direktori phpMyAdmin yang baru dibuat:

   ```
   cd phpMyAdmin-5.2.1-all-languages
   ```

5. Ubah nama direktori phpMyAdmin agar lebih mudah diakses:

   ```
   mkdir /var/www/html/phpmyadmin
   mv * /var/www/html/phpmyadmin
   ```

   Perintah di atas akan memindahkan semua file dan direktori dari direktori phpMyAdmin ke direktori `/var/www/html/phpmyadmin`.

6. Berikan hak akses yang tepat pada direktori phpMyAdmin:

    ```
    sudo chown -R www-data:www-data /var/www/html/phpmyadmin
    ```

    Perintah ini akan mengubah kepemilikan direktori phpMyAdmin ke pengguna dan grup `www-data` yang umumnya digunakan oleh server web seperti Apache atau Nginx.

7. Selesai! phpMyAdmin sekarang terinstal pada server Anda. Anda dapat mengaksesnya melalui browser dengan URL `http://<alamat-ip-server>/phpmyadmin`.

    Pastikan untuk mengganti `<alamat-ip-server>` dengan alamat IP publik atau alamat hostname dari server Anda.