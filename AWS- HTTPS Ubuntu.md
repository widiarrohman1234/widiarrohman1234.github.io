# HTTPS instalation on Ubuntu 22.04
Proses instalasi HTTPS pada Ubuntu 22.04 atau versi Ubuntu lainnya melibatkan beberapa langkah, seperti menginstal dan mengonfigurasi server web (misalnya Apache atau Nginx) serta mengaktifkan sertifikat SSL. Berikut adalah langkah-langkah umum yang dapat Anda ikuti:

1. Perbarui sistem:
   Pastikan sistem Ubuntu Anda diperbarui dengan menjalankan perintah berikut di terminal:
   ```
   sudo apt update
   sudo apt upgrade
   ```

2. Instal server web:
   Pilih server web yang akan Anda gunakan, seperti Apache atau Nginx. Misalnya, untuk menginstal Apache, jalankan perintah berikut di terminal:
   ```
   sudo apt install apache2
   ```

3. Instal paket SSL:
   Untuk mengaktifkan HTTPS, Anda perlu menginstal paket SSL yang diperlukan. Misalnya, jika Anda menggunakan Apache, jalankan perintah berikut di terminal:
   ```
   sudo apt install openssl
   sudo apt install libssl-dev
   ```

4. Dapatkan sertifikat SSL:
   Ada beberapa cara untuk mendapatkan sertifikat SSL, termasuk dari penyedia sertifikat pihak ketiga atau menggunakan Let's Encrypt untuk mendapatkan sertifikat SSL gratis. Berikut adalah langkah-langkah untuk menggunakan Let's Encrypt dengan Certbot:

   - Instal Certbot:
     ```
     sudo apt install certbot
     ```

   - Peroleh dan pasang sertifikat SSL dengan Certbot:
     ```
     sudo certbot certonly --webroot -w /var/www/html -d domainanda.com
     ```

     Gantilah "domainanda.com" dengan nama domain atau subdomain Anda sendiri.

   - Setelah berhasil memperoleh sertifikat, Certbot akan memasangnya di direktori yang sesuai.

5. Konfigurasi server web:
   Konfigurasikan server web Anda untuk menggunakan sertifikat SSL yang telah Anda pasang. Untuk Apache, buka file konfigurasi default dengan perintah berikut:
   ```
   sudo nano /etc/apache2/sites-available/000-default.conf
   ```

   Tambahkan konfigurasi berikut ke dalam blok `<VirtualHost>`:
   ```
   <IfModule mod_ssl.c>
       <VirtualHost *:443>
           ServerAdmin webmaster@domainanda.com
           DocumentRoot /var/www/html

           SSLEngine on
           SSLCertificateFile /path/to/cert.pem
           SSLCertificateKeyFile /path/to/privkey.pem
           SSLCertificateChainFile /path/to/chain.pem
       </VirtualHost>
   </IfModule>
   ```

   Gantilah "/path/to/cert.pem", "/path/to/privkey.pem", dan "/path/to/chain.pem" dengan lokasi sertifikat SSL yang telah Anda dapatkan sebelumnya.

   Simpan perubahan dan tutup file.

6. Aktifkan modul SSL dan restart server web:
   Aktifkan modul SSL dengan menjalankan perintah berikut:
   ```
   sudo a2enmod ssl
   ```

   Kemudian, restart server Apache:
   ```
   sudo systemctl restart apache2
   ```

7. Verifikasi HTTPS:
   Buka browser dan akses situs web Anda melalui protokol HTTPS (https://domainanda.com). Pastikan sertifikat SSL terpasang dengan benar dan sit

us web dapat diakses melalui HTTPS.

Dengan langkah-langkah di atas, Anda telah berhasil menginstal HTTPS pada server Ubuntu 22. Pastikan untuk mengganti "domainanda.com" dengan domain atau subdomain yang sesuai dengan situs web Anda. Selain itu, ikuti petunjuk dan dokumentasi resmi yang relevan untuk server web dan penyedia sertifikat SSL yang Anda gunakan, karena langkah-langkah dan pengaturan yang tepat dapat bervariasi tergantung pada konfigurasi spesifik Anda.

> pelajari lebih lanjut di [sini](https://certbot.eff.org/instructions?ws=apache&os=ubuntufocal&tab=standard)