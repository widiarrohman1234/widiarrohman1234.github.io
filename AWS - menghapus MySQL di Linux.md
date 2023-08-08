Untuk menghapus MySQL di Linux, Anda dapat mengikuti langkah-langkah berikut:

1. Pastikan Anda memiliki hak administratif atau akses root pada sistem Linux.

2. Buka terminal atau shell di Linux.

3. Jalankan perintah berikut untuk menghapus paket MySQL beserta dependensinya:
   - Pada distribusi berbasis Debian (seperti Ubuntu):
     ```
     sudo apt-get remove --purge mysql-server mysql-client mysql-common
     sudo apt-get autoremove
     sudo apt-get autoclean
     ```
   - Pada distribusi berbasis Red Hat (seperti CentOS):
     ```
     sudo yum remove mysql-server mysql-client
     sudo yum autoremove
     sudo yum clean all
     ```

4. Selanjutnya, Anda perlu menghapus direktori dan file yang terkait dengan MySQL. Jalankan perintah berikut:
   ```
   sudo rm -rf /var/lib/mysql
   sudo rm -rf /etc/mysql
   ```

5. Terakhir, hapus juga konfigurasi MySQL jika ada:
   ```
   sudo rm -rf /root/.mysql_history
   sudo rm -rf /root/.mysql_secret
   ```

Setelah langkah-langkah di atas selesai, MySQL seharusnya sudah dihapus dari sistem Linux Anda. Pastikan untuk melakukan langkah-langkah ini dengan hati-hati, karena menghapus MySQL akan menghapus semua database dan data yang terkait. Pastikan Anda memiliki salinan cadangan yang diperlukan sebelum melanjutkan.