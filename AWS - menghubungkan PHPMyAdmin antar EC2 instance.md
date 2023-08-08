Untuk menghubungkan PHPMyAdmin yang terinstall di EC2 instance dengan nama ec2-source-code ke MySQL yang terinstall di EC2 instance dengan nama ec2-database, Anda perlu mengatur konfigurasi akses dan izin yang sesuai. Berikut langkah-langkah yang dapat Anda ikuti:

1. Masuk ke instance EC2 dengan nama ec2-database menggunakan SSH:
   ```
   ssh -i <key_pair.pem> ubuntu@<ec2-database-public-ip>
   ```
   Pastikan Anda mengganti `<key_pair.pem>` dengan nama file kunci key pair yang Anda gunakan, dan `<ec2-database-public-ip>` dengan alamat IP publik instance ec2-database.

2. Di dalam instance ec2-database, buka file konfigurasi MySQL dengan menggunakan editor teks, misalnya Nano:
   ```
   sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
   ```

3. Temukan baris berikut dan pastikan MySQL mendengarkan koneksi dari alamat IP instance ec2-source-code:
   ```
   bind-address = 0.0.0.0
   ```

4. Simpan perubahan yang Anda lakukan pada file konfigurasi, lalu restart layanan MySQL:
   ```
   sudo service mysql restart
   ```

5. Selanjutnya, buka halaman konfigurasi PHPMyAdmin di instance ec2-source-code dengan menggunakan editor teks:
```
cp /var/www/html/phpmyadmin/config.sample.inc.php /var/www/html/phpmyadmin/config.inc.php
```   
```
   sudo nano /var/www/html/phpmyadmin/config.inc.php
   ```

6. Temukan bagian konfigurasi berikut dan ubah nilainya sesuai dengan informasi koneksi MySQL di instance ec2-database:
   ```
   $cfg['Servers'][$i]['host'] = 'ec2-database-private-ip';
   $cfg['Servers'][$i]['port'] = '3306';
   $cfg['Servers'][$i]['user'] = 'mysql-username';
   $cfg['Servers'][$i]['password'] = 'mysql-password';
   ```
   Gantilah `ec2-database-private-ip` dengan alamat IP pribadi (Private IP) instance ec2-database, dan `mysql-username` serta `mysql-password` dengan informasi pengguna dan kata sandi yang telah Anda atur di MySQL.

7. Simpan perubahan yang Anda lakukan pada file konfigurasi PHPMyAdmin.

8. Setelah itu, Anda bisa mengakses PHPMyAdmin melalui web browser dengan menggunakan alamat IP publik instance ec2-source-code dan direktori `/phpmyadmin`, misalnya: `http://52.76.180.73/phpmyadmin`. Anda akan diarahkan ke antarmuka PHPMyAdmin yang terhubung ke MySQL di instance ec2-database.

Dengan mengikuti langkah-langkah di atas, Anda dapat menghubungkan PHPMyAdmin di EC2 instance ec2-source-code ke MySQL yang terinstall di EC2 instance ec2-database. Pastikan Anda telah mengatur izin akses yang sesuai pada MySQL agar koneksi PHPMyAdmin dapat berhasil dilakukan.