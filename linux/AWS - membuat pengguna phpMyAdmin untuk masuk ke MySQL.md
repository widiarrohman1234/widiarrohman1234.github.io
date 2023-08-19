Untuk membuat pengguna yang dapat digunakan oleh phpMyAdmin untuk masuk ke MySQL database, Anda dapat mengikuti langkah-langkah berikut:

1. Buka terminal atau akses ke server MySQL Anda.

2. Masuk ke MySQL sebagai pengguna root:

   ```
   mysql -u root -p
   ```

3. Setelah masuk, buat pengguna baru dengan perintah berikut (ganti 'phpmyadminuser' dengan nama pengguna yang Anda inginkan dan 'password' dengan kata sandi yang kuat):

   ```
   CREATE USER 'phpmyadminuser'@'localhost' IDENTIFIED BY 'StressP4ssword123!@#';
   ```

4. Berikan hak akses yang diperlukan ke pengguna tersebut. Berikut adalah contoh perintah untuk memberikan hak akses penuh (ALL PRIVILEGES) ke semua database:

   ```
   GRANT ALL PRIVILEGES ON *.* TO 'phpmyadminuser'@'localhost' WITH GRANT OPTION;
   ```

   Jika Anda ingin membatasi hak akses hanya untuk database tertentu, ganti `*.*` dengan nama database yang diinginkan, misalnya `mydatabase.*`.

5. Setelah memberikan izin, terapkan perubahan dengan perintah berikut:

   ```
   FLUSH PRIVILEGES;
   ```

6. Keluar dari MySQL:

   ```
   exit
   ```

Setelah itu, pengguna 'phpmyadminuser' sekarang dapat digunakan oleh phpMyAdmin untuk terhubung ke MySQL database dengan menggunakan nama pengguna dan kata sandi yang telah Anda tentukan.

Pastikan untuk mengganti 'phpmyadminuser' dengan nama pengguna yang Anda inginkan dan 'password' dengan kata sandi yang kuat. Selain itu, pastikan untuk mengatur izin yang sesuai dengan kebutuhan aplikasi Anda untuk keamanan yang lebih baik.