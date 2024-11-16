# Restore Database
Untuk melakukan restore database MySQL dari file backup, Anda bisa menggunakan perintah `mysql` seperti berikut:

```bash
mysql -h 00.00.00.00 -P 000 -u usernya -p namadatabase < inibackupnya.sql
```

### Penjelasan Parameter

- **`mysql`**: Perintah untuk menjalankan query di MySQL.
- **`-h 00.00.00.00`**: Alamat IP atau hostname dari server MySQL tempat database akan di-restore (gantilah `00.00.00.00` dengan alamat server Anda).
- **`-P 000`**: Nomor port dari server MySQL (gantilah `000` dengan nomor port yang benar).
- **`-u usernya`**: Username untuk login ke MySQL (gantilah `usernya` dengan nama user yang sesuai).
- **`-p`**: Menginstruksikan `mysql` untuk meminta password.
- **`namadatabase`**: Nama database yang akan di-restore. Pastikan database ini sudah ada sebelumnya atau buat database terlebih dahulu jika belum ada.
- **`< inibackupnya.sql`**: File backup yang akan di-restore (`inibackupnya.sql`).

### Langkah-langkah

1. **Buat Database (Jika Belum Ada)**:
   Jika database yang ingin di-restore belum ada, buatlah database terlebih dahulu:

   ```sql
   CREATE DATABASE namadatabase;
   ```

   Anda bisa menjalankan perintah ini di MySQL CLI atau MySQL client sebelum menjalankan perintah restore.

2. **Jalankan Perintah Restore**:
   Masukkan perintah di atas di terminal. Anda akan diminta memasukkan password setelah menjalankan perintah ini.

3. **Masukkan Password**:
   Setelah memasukkan perintah, ketikkan password dari user MySQL yang Anda gunakan (`-u usernya`), kemudian tekan Enter.

4. **Proses Restore**:
   MySQL akan membaca file `inibackupnya.sql` dan memasukkan semua data ke dalam `namadatabase`.

### Contoh dengan Data Lengkap

Misalnya, jika Anda ingin merestore ke server dengan IP `192.168.1.10`, port `3306`, user `admin`, password `1234`, dan nama database `mydatabase`, maka perintahnya akan menjadi:

```bash
mysql -h 192.168.1.10 -P 3306 -u admin -p mydatabase < inibackupnya.sql
```

Anda akan diminta memasukkan password (`1234`), dan data dari `inibackupnya.sql` akan di-import ke dalam database `mydatabase`.

### Catatan Penting:

- **Database Harus Ada**: Pastikan database (`namadatabase`) sudah ada sebelum melakukan restore. Jika belum, buat database terlebih dahulu.
- **Akses**: Anda harus memiliki akses untuk menulis data ke database tersebut.
- **File Backup**: Pastikan `inibackupnya.sql` ada di direktori tempat Anda menjalankan perintah tersebut atau berikan path lengkap ke file tersebut.

Ini akan mengembalikan data dari file backup ke database yang Anda tentukan.

# Restore MySQL Docker
Agar MySQL yang berjalan di dalam Docker bisa mengakses file backup yang ada di host, Anda perlu melakukan **bind mount** dari file tersebut ke dalam container. Berikut adalah langkah-langkahnya:

1. **Buat Bind Mount ke Direktori Host**:
   Anda bisa me-mount direktori host di mana file backup Anda berada ke dalam container MySQL.

   Misalnya, jika file backup Anda ada di `/home/sidafa/`, Anda dapat menjalankan container MySQL dengan bind mount ke direktori ini. Misalkan nama container MySQL Anda adalah `mysql`, Anda bisa menghentikan lalu menjalankannya kembali dengan bind mount, atau Anda bisa langsung menggunakan `docker cp` untuk menyalin file tersebut.

2. **Menggunakan `docker cp` untuk Menyalin File Backup ke Container**:
   Anda bisa menyalin file backup langsung ke dalam container tanpa perlu bind mount:

   ```bash
   sudo docker cp /home/sidafa/inibackupnya_sidafaid_sidafa21.sql mysql:/inibackupnya_sidafaid_sidafa21.sql
   ```

3. **Akses File di Container dan Jalankan Restore**:
   Setelah file ada di dalam container, Anda bisa menjalankan perintah restore seperti biasa:

   ```bash
   sudo docker exec -it mysql bash -c "mysql -u sidafa -p sidafa_db < /inibackupnya_sidafaid_sidafa21.sql"
   ```

   Masukkan password saat diminta, dan proses restore akan berjalan.

Jika Anda sering melakukan backup dan restore, Anda bisa mempertimbangkan mount otomatis direktori host setiap kali container berjalan agar akses file lebih mudah.