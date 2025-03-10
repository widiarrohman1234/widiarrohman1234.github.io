Untuk membuat program yang secara otomatis menghapus file backup yang lebih dari 7 hari, Anda bisa menulis skrip bash yang melakukan pengecekan terhadap usia file dan menghapus file yang sudah lebih dari 7 hari.

Berikut adalah contoh program untuk mencapai hal tersebut:

### **1. Program Bash untuk Menghapus Backup yang Lebih dari 7 Hari**

```bash
#!/bin/bash

# Folder tempat menyimpan backup
BACKUP_FOLDER="/home/widiarrohman1234/backup_db"

# Usia maksimum backup yang diizinkan (dalam hari)
MAX_AGE=7

# Cari file backup yang lebih tua dari MAX_AGE dan hapus
find $BACKUP_FOLDER -name "sidafa_db_*.sql" -type f -mtime +$MAX_AGE -exec rm -f {} \;

# Log proses penghapusan
echo "Proses penghapusan backup lebih dari $MAX_AGE hari selesai. $(date)" >> $BACKUP_FOLDER/backup_cleanup.log
```

```
chmod +x backup_cleanup.sh
```
### **Penjelasan Program:**

- **`BACKUP_FOLDER`**: Variabel ini berisi direktori tempat file backup disimpan. Anda bisa menyesuaikan sesuai dengan path direktori Anda.
- **`MAX_AGE=7`**: Menentukan batas usia backup dalam hari. Backup yang lebih tua dari 7 hari akan dihapus.
- **`find $BACKUP_FOLDER -name "sidafa_db_*.sql" -type f -mtime +$MAX_AGE -exec rm -f {} \;`**:
    - Perintah `find` mencari file dengan pola nama `sidafa_db_*.sql` di dalam direktori backup.
    - **`-mtime +$MAX_AGE`** berarti mencari file yang dimodifikasi lebih dari 7 hari yang lalu.
    - **`-exec rm -f {}`**: Jika ditemukan file yang lebih tua dari 7 hari, file tersebut akan dihapus.
- **`>> $BACKUP_FOLDER/backup_cleanup.log`**: Menambahkan log ke file `backup_cleanup.log` di dalam direktori backup untuk mencatat waktu dan tanggal penghapusan.

### **2. Mengatur Skrip untuk Berjalan Secara Terjadwal dengan Cron**

Agar skrip ini berjalan otomatis setiap hari, Anda bisa menambahkan cron job untuk menjalankannya. Berikut adalah cara untuk menambahkan cron job yang menjalankan skrip ini setiap hari (misalnya pada pukul 03:00 AM):

1. **Edit crontab** untuk user yang sesuai (misalnya root):
    
    ```bash
    crontab -e
    ```
    
2. **Tambahkan baris berikut** untuk menjalankan skrip setiap hari pada pukul 03:00 AM:
    
    ```bash
    0 3 * * * /bin/bash /home/widiarrohman1234/backup_db/backup_cleanup.sh
    ```
    
    - **`0 3 * * *`**: Menjadwalkan cron untuk berjalan setiap hari pada pukul 03:00 AM.
    - **`/bin/bash /home/widiarrohman1234/backup_db/backup_cleanup.sh`**: Menjalankan skrip bash yang sudah Anda buat.
3. **Simpan dan keluar** dari editor crontab.
    

Dengan cara ini, cron akan menjalankan skrip Anda setiap hari pada pukul 03:00 AM, dan secara otomatis menghapus file backup yang lebih dari 7 hari.

### **3. Verifikasi Skrip dan Cron Job**

- Pastikan skrip **`backup_cleanup.sh`** dapat dijalankan dengan perintah:
    
    ```bash
    /bin/bash /home/widiarrohman1234/backup_db/backup_cleanup.sh
    ```
    
    Ini akan menghapus file backup yang lebih dari 7 hari dan mencatatnya dalam log.
    
- Untuk memastikan cron job bekerja dengan baik, Anda bisa melihat log cron dengan:
    
    ```bash
    grep CRON /var/log/syslog  # Untuk Debian/Ubuntu
    ```
    
    Di log ini, Anda akan melihat apakah cron job berhasil dijalankan.
    

### **Ringkasan:**

- Skrip di atas menghapus file backup yang lebih dari 7 hari secara otomatis untuk efisiensi storage.
- Anda dapat mengatur cron job untuk menjalankan skrip ini setiap hari.
- Log penghapusan akan dicatat dalam file `backup_cleanup.log` untuk referensi.

Dengan cara ini, Anda dapat mengelola backup otomatis dan memastikan hanya ada backup dalam 7 hari terakhir di server Anda.