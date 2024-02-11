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