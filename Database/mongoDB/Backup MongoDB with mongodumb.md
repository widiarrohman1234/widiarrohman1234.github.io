Untuk melakukan backup MongoDB, Anda dapat menggunakan utilitas `mongodump` yang disediakan oleh MongoDB. `mongodump` menghasilkan dump dari data dalam format BSON yang dapat digunakan untuk memulihkan data dengan utilitas `mongorestore`.

### Langkah-langkah untuk Membuat Backup MongoDB

#### Menggunakan `mongodump` di Docker

1. **Jalankan `mongodump` dalam Kontainer Docker:**

   Anda bisa menjalankan perintah `mongodump` dalam kontainer Docker MongoDB Anda. Misalnya, jika kontainer Anda bernama `mongodb_prod`, Anda bisa menggunakan perintah berikut:

   ```bash
   docker exec -it mongodb_prod mongodump --out /backup --username root --password SbIxD1KSR3Eku5v --authenticationDatabase admin
   ```

   Perintah ini akan membuat backup dari semua database dalam direktori `/backup` di dalam kontainer.

2. **Salin Backup dari Kontainer ke Host:**

   Setelah backup selesai, Anda dapat menyalin data backup dari kontainer ke host menggunakan `docker cp`:

   ```bash
   docker cp mongodb_prod:/backup ./mongodb_backup
   ```

   Ini akan menyalin direktori `/backup` dari dalam kontainer ke direktori `./mongodb_backup` di host.

#### Menjadwalkan Backup dengan Cron Job

Anda bisa menjadwalkan backup otomatis menggunakan cron job di server host Anda. Berikut adalah contoh cron job untuk menjalankan backup setiap hari pada jam 2 pagi:

1. **Buat Skrip Backup:**

   Buat skrip shell yang akan menjalankan perintah `mongodump` dan `docker cp`:

   ```bash
   #!/bin/bash

   # Nama kontainer MongoDB
   CONTAINER_NAME=mongodb_prod

   # Direktori di dalam kontainer untuk menyimpan backup sementara
   BACKUP_DIR=/backup

   # Direktori di host untuk menyimpan backup
   HOST_BACKUP_DIR=./mongodb_backup

   # Buat backup di dalam kontainer
   docker exec $CONTAINER_NAME mongodump --out $BACKUP_DIR --username root --password SbIxD1KSR3Eku5v --authenticationDatabase admin

   # Salin backup dari kontainer ke host
   docker cp $CONTAINER_NAME:$BACKUP_DIR $HOST_BACKUP_DIR

   # Opsional: Hapus backup lama (misalnya lebih dari 7 hari)
   find $HOST_BACKUP_DIR -type d -mtime +7 -exec rm -rf {} \;
   ```

   Simpan skrip ini, misalnya dengan nama `backup_mongodb.sh`, dan berikan izin eksekusi:

   ```bash
   chmod +x backup_mongodb.sh
   ```

2. **Jadwalkan Cron Job:**

   Buka crontab untuk diedit:

   ```bash
   crontab -e
   ```

   Tambahkan entri berikut untuk menjalankan skrip setiap hari pada jam 2 pagi:

   ```plaintext
   0 2 * * * /path/to/backup_mongodb.sh
   ```

   Pastikan untuk mengganti `/path/to/backup_mongodb.sh` dengan path lengkap ke skrip backup yang Anda buat.

### Langkah-langkah untuk Memulihkan Backup MongoDB

#### Menggunakan `mongorestore` di Docker

1. **Salin Backup ke Kontainer:**

   Jika backup Anda ada di host, salin ke dalam kontainer:

   ```bash
   docker cp ./mongodb_backup mongodb_prod:/backup
   ```

2. **Jalankan `mongorestore`:**

   Jalankan perintah `mongorestore` di dalam kontainer untuk memulihkan data dari backup:

   ```bash
   docker exec -it mongodb_prod mongorestore --drop /backup --username root --password SbIxD1KSR3Eku5v --authenticationDatabase admin
   ```

   Opsi `--drop` akan menghapus koleksi yang ada sebelum memulihkan data dari backup.

Dengan langkah-langkah ini, Anda dapat dengan mudah membuat dan memulihkan backup MongoDB menggunakan Docker.