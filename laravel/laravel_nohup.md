Anda dapat menggunakan perintah `nohup` untuk menjalankan perintah PHP Artisan di latar belakang. Berikut adalah contoh cara menjalankan `php artisan serve` dengan `nohup`:

```bash
nohup php artisan serve --host=103.175.219.171 --port=8001 > /dev/null 2>&1 &
```

Penjelasan dari perintah tersebut:

- `nohup`: Memungkinkan Anda menjalankan perintah di latar belakang dan mempertahankan proses setelah sesi terminal ditutup.
- `php artisan serve --host=103.175.219.171 --port=8001`: Perintah untuk menjalankan server PHP Artisan.
- `> /dev/null 2>&1 &`: tidak akan memblokir terminal dan tidak akan menyimpan output atau pesan kesalahan di file log atau tempat lainnya, karena file log sudah menggunakan bawaan laravel.
- `&`: Menjalankan perintah di latar belakang.

Dengan menggunakan perintah di atas, server PHP Artisan akan dijalankan di latar belakang, dan output serta errornya akan ditulis ke file log yang telah Anda tentukan. Pastikan untuk menggantikan jalur file log dengan yang sesuai dengan kebutuhan Anda.

Perintah yang kamu jalankan dengan `nohup` mengeksekusi aplikasi Laravel menggunakan `php artisan serve` di background pada IP **103.175.219.171** dan port **8001**. Output dari proses ini diarahkan ke `/dev/null`, jadi tidak ada output yang terlihat di terminal.

### Cara Melihat Apakah Proses Sedang Berjalan

Untuk melihat apakah proses tersebut berjalan, kamu bisa menggunakan beberapa metode:

1. **Cek menggunakan `ps`**:
   Gunakan perintah berikut untuk melihat daftar proses yang berjalan, termasuk yang menggunakan `php artisan`:

   ```bash
   ps aux | grep "php artisan"
   ```

   Ini akan menampilkan daftar proses yang terkait dengan perintah `php artisan serve`. Outputnya akan terlihat seperti ini:

   ```
   root     12345  0.1  1.5 123456 12345 ?        S    12:34   0:00 php artisan serve --host=103.175.219.171 --port=8001
   root     12346  0.0  0.0  1234  5678 pts/0    S+   12:34   0:00 grep php artisan
   ```

   Dari output tersebut, perhatikan **PID** (Process ID) dari proses `php artisan serve`. Misalnya, jika PID-nya adalah **12345**, kamu bisa menggunakan PID ini untuk memantau atau menghentikan proses.

2. **Cek apakah port sedang digunakan**:
   Kamu bisa memeriksa apakah aplikasi Laravel sudah mendengarkan pada port **8001** dengan perintah:

   ```bash
   sudo netstat -tuln | grep 8001
   ```

   Jika Laravel berjalan dengan benar, kamu akan melihat sesuatu seperti ini:

   ```
   tcp        0      0 103.175.219.171:8001      0.0.0.0:*               LISTEN
   ```

### Cara Mematikan Proses

Untuk menghentikan proses, gunakan PID yang didapat dari perintah `ps` sebelumnya. Kamu bisa menghentikan proses dengan perintah:

```bash
sudo kill -9 <PID>
```

Misalnya, jika PID dari proses adalah **12345**, perintahnya menjadi:

```bash
sudo kill -9 12345
```

Ini akan mematikan proses Laravel yang berjalan di background.

### Alternatif: Menggunakan `nohup` Output

Jika kamu ingin melihat log dari proses `nohup`, kamu bisa mengarahkannya ke file, bukan `/dev/null`, saat menjalankan `nohup`. Misalnya:

```bash
nohup php artisan serve --host=103.175.219.171 --port=8001 > /path/to/logfile.log 2>&1 &
```

Kemudian kamu bisa melihat output proses dengan:

```bash
tail -f /path/to/logfile.log
```