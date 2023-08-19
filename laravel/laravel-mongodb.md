Jika Anda telah menginstal MongoDB di server dan masih menerima kesalahan "Unsupported driver [mongodb]" dalam Laravel, kemungkinan besar masalah terletak pada konfigurasi Laravel yang tidak benar untuk menggunakan driver MongoDB.

Berikut adalah beberapa solusi yang dapat Anda coba:

1. Pastikan Anda telah menginstal paket MongoDB untuk Laravel melalui Composer dengan menjalankan perintah berikut di direktori proyek Laravel Anda:
   ```bash
   composer require jenssegers/mongodb
   ```

2. Periksa file konfigurasi `config/database.php` di proyek Laravel Anda dan pastikan driver MongoDB telah dikonfigurasi dengan benar. Pastikan bahwa nilai `'default'` pada array `'connections'` mengacu pada koneksi MongoDB. Misalnya:
   ```php
   'default' => 'mongodb',
   ```

3. Periksa koneksi MongoDB di dalam array `'connections'` di file `config/database.php` dan pastikan pengaturan host, port, database, dan kredensial sesuai dengan konfigurasi MongoDB di server Anda. Contoh koneksi MongoDB yang mungkin terlihat seperti ini:
   ```php
   'mongodb' => [
       'driver'   => 'mongodb',
       'host'     => env('DB_HOST', 'localhost'),
       'port'     => env('DB_PORT', 27017),
       'database' => env('DB_DATABASE', 'your-database-name'),
       'username' => env('DB_USERNAME', 'your-username'),
       'password' => env('DB_PASSWORD', 'your-password'),
       'options'  => [
           'database' => 'admin' // Opsional, sesuaikan dengan nama database admin MongoDB
       ],
   ],
   ```

4. Pastikan Anda telah mengatur nilai yang tepat untuk variabel lingkungan (`env`) dalam file `.env` di proyek Laravel Anda. Pastikan nilai `DB_CONNECTION` disetel ke `'mongodb'` dan pastikan variabel lingkungan lain seperti `DB_HOST`, `DB_PORT`, `DB_DATABASE`, `DB_USERNAME`, dan `DB_PASSWORD` disesuaikan dengan konfigurasi MongoDB Anda.

5. Jika Anda telah mengubah file konfigurasi atau file `.env`, pastikan Anda menjalankan perintah `php artisan config:cache` untuk menghapus cache konfigurasi Laravel dan memuat ulang konfigurasi yang baru.

Setelah mengikuti langkah-langkah ini, restart server Laravel Anda dan periksa apakah kesalahan "Unsupported driver [mongodb]" masih muncul. Jika masih ada masalah, pastikan Anda memeriksa dokumentasi Laravel dan paket MongoDB untuk memastikan pengaturan dan konfigurasi yang benar untuk menggunakan MongoDB sebagai driver database di Laravel Anda.