# Catatan Dokumentasi Laravel
instalasi awal
```
composer create-project laravel/laravel scrapping-telegram-laravel
```



## Migrasi
migrate
```
php artisan migrate
```

membuat migrasi:

contoh 1
```
php artisan make:migration create_product_import_temp_table --create=product_import_temp
```
contoh 2
```
php artisan make:migration create_product_table --create=product
```

* `ID` = $table->id();
* `String` = $table->string('name');
* `Int` = $table->integer('age');
* `Boolean` = $table->boolean('is_active');
* `Text` & nullable = $table->text('description')->nullable();
* `Date` = $table->date('birth_date');
* `Datetime` = $table->dateTime('created_at');
* `Timestamp` = $table->timestamps();
* $table->foreign('id_vendor')->references('id')->on('vendor')->onDelete('cascade');
* $table->unsignedBigInteger('id_product'); //hanya bilangan integer positif dari 0 hingga 18,446,744,073,709,551,615.
* $table->primary(['id_product', 'id_vendor']); //2 kolom menjadi primary
* `$table->decimal('price', 10, 2);` menyimpan angka desimal dengan total 10 digit, di mana 2 digit terakhir untuk angka di belakang koma. Misalnya `12345678,99`. Penggunaan tipe data `decimal` lebih disarankan daripada tipe data `float` atau `double` untuk menyimpan nilai-nilai keuangan, karena `decimal` dapat menyimpan nilai dengan presisi yang lebih baik dan menghindari masalah pembulatan yang umum terjadi dalam perhitungan keuangan.

macam-macam perintah `migrate`
* `php artisan migrate`: menjalankan semua migrasi yang belum dijalankan sebelumnya
* `php artisan migrate:install`: membuat tabel migrasi yang diperlukan oleh Laravel
* `php artisan migrate:rollback`: membatalkan migrasi terakhir yang telah dijalankan
* `php artisan migrate:reset`: membatalkan semua migrasi yang telah dijalankan dan menghapus semua tabel yang dibuat oleh migrasi.
* `php artisan migrate:refresh`:membatalkan dan menjalankan ulang semua migrasi. Ini sama dengan menjalankan perintah migrate:reset dan kemudian migrate.
* `php artisan migrate:status`: menampilkan status migrasi, yaitu migrasi mana yang telah dijalankan dan migrasi mana yang belum dijalankan.
* `php artisan make:migration NamaMigrasi`: membuat file migrasi baru dengan nama tertentu di direktori `database/migrations` 
* ```php artisan migrate:refresh --path=database/migrations/2014_10_12_000000_create_users_table.php``` : menjalankan 1 file migrasi saja
* ```php artisan migrate --path=database/migrations/2023_08_19_084706_create_denom_table.php``` : Hanya menjalankan 1 migrasi baru/diinginkan tanpa menganggu yang lainnya.

# templating
memanggil folder di `/public`
```
<link rel="stylesheet" href="{{ asset('plugins/fontawesome-free/css/all.min.css') }}">
```

struktur penyimpanan
1. cara 1
```
resources/
└── views/
    ├── admin/
    │   ├── layouts/
    │   │   ├── app.blade.php
    │   │   └── sidebar.blade.php
    │   ├── dashboard.blade.php
    │   └── users/
    │       ├── index.blade.php
    │       ├── create.blade.php
    │       └── edit.blade.php
    ├── front/
    │   ├── layouts/
    │   │   ├── app.blade.php
    │   │   └── header.blade.php
    │   ├── home.blade.php
    │   ├── about.blade.php
    │   └── contact.blade.php
    └── welcome.blade.php

```

2. cara 2
```
resources/
└── views/
    ├── layouts/
    │   ├── app.blade.php
    │   └── sidebar.blade.php
    ├── pages/
    │   ├── home.blade.php
    │   ├── about.blade.php
    │   └── contact.blade.php
    ├── auth/
    │   ├── login.blade.php
    │   └── register.blade.php
    └── admin/
        ├── dashboard.blade.php
        └── users/
            ├── index.blade.php
            ├── create.blade.php
            └── edit.blade.php
```

3. cara 3, untuk proyek yang memiliki halaman frontend(guest) dan backend(admin)
```
resources/
└── views/
    ├── layouts/
    │   ├── app.blade.php
    │   ├── header.blade.php
    │   ├── sidebar.blade.php
    │   └── footer.blade.php
    ├── frontend/
    │   ├── home.blade.php
    │   ├── about.blade.php
    │   └── contact.blade.php
    ├── backend/
    │   ├── dashboard.blade.php
    │   ├── products/
    │   │   ├── index.blade.php
    │   │   ├── create.blade.php
    │   │   └── edit.blade.php
    │   └── users/
    │       ├── index.blade.php
    │       ├── create.blade.php
    │       └── edit.blade.php
    └── errors/
        ├── 404.blade.php
        └── 500.blade.php

```
4. contoh 4
```
resources/
└── views/
    ├── layouts/
    │   ├── app.blade.php
    │   ├── header.blade.php
    │   └── footer.blade.php
    ├── components/
    │   ├── alerts/
    │   │   ├── success.blade.php
    │   │   ├── error.blade.php
    │   │   └── warning.blade.php
    │   └── forms/
    │       ├── input.blade.php
    │       ├── textarea.blade.php
    │       └── button.blade.php
    ├── pages/
    │   ├── home.blade.php
    │   ├── about.blade.php
    │   └── contact.blade.php
    └── admin/
        ├── dashboard.blade.php
        ├── products/
        │   ├── index.blade.php
        │   ├── create.blade.php
        │   └── edit.blade.php
        └── users/
            ├── index.blade.php
            ├── create.blade.php
            └── edit.blade.php

```

mengisi konten halaman
```
@yield('content')
@yield('content', 'Konten Default')
```
```
@extends('layouts.app')

@section('content')
    <!-- Konten halaman -->
@endsection
```

# Authentication
```
php artisan make:controller AuthController
```

* `register()`: Untuk menampilkan halaman pendaftaran pengguna.
* `create()`: Untuk memproses data pendaftaran pengguna.
* `login()`: Untuk menampilkan halaman login.
* `authenticate()`: Untuk memproses data login pengguna.
* `logout()`: Untuk melakukan proses logout pengguna.

# Controller
perintah
```
php artisan make:controller NamaController
```

* `--resource` atau `-p`: Membuat controller dengan metode-metode RESTful, mirip dengan `-r`.
* `--model[=MODEL]`: Mengaitkan controller dengan model yang ada, sehingga metode-metode CRUD dapat digunakan secara otomatis dengan memanfaatkan model tersebut.
* `--api`: Membuat controller untuk digunakan dalam API, dengan metode-metode yang sesuai untuk pemrosesan permintaan API.

# Route
```
// Read - Menampilkan daftar pengguna
Route::get('/users', [UserController::class, 'index'])->name('users.index');

// Create - Menampilkan form pembuatan pengguna baru
Route::get('/users/create', [UserController::class, 'create'])->name('users.create');

// Store - Menyimpan pengguna baru ke dalam database
Route::post('/users', [UserController::class, 'store'])->name('users.store');

// Read - Menampilkan detail pengguna berdasarkan ID
Route::get('/users/{id}', [UserController::class, 'show'])->name('users.show');

// Update - Menampilkan form edit pengguna berdasarkan ID
Route::get('/users/{id}/edit', [UserController::class, 'edit'])->name('users.edit');

// Update - Mengupdate data pengguna berdasarkan ID
Route::put('/users/{id}', [UserController::class, 'update'])->name('users.update');

// Delete - Menghapus pengguna berdasarkan ID
Route::delete('/users/{id}', [UserController::class, 'destroy'])->name('users.destroy');
```

## Logging
Selain tingkat log `debug`, `info`, dan `warning`, Laravel juga menyediakan tingkat log lainnya, yaitu:

1. `error`: Tingkat log ini digunakan untuk mencatat kesalahan (errors) yang terjadi dalam aplikasi. Biasanya digunakan untuk mencatat kesalahan fatal yang menghentikan aliran normal aplikasi.

2. `emergency`: Tingkat log ini digunakan untuk mencatat kondisi darurat (emergency) yang mengindikasikan kegagalan total sistem. Tingkat log ini jarang digunakan dan biasanya digunakan dalam situasi kritis yang memerlukan tindakan segera.

3. `notice`: Tingkat log ini digunakan untuk mencatat peristiwa penting atau perubahan dalam aplikasi. Ini dapat mencakup pemberitahuan tentang kejadian khusus yang layak dicatat tetapi tidak termasuk dalam tingkat log `warning` atau `error`.

4. `critical`: Tingkat log ini digunakan untuk mencatat kesalahan kritis yang membutuhkan tindakan segera. Biasanya digunakan untuk mencatat kesalahan yang dapat menyebabkan aplikasi tidak berfungsi atau berdampak serius pada pengguna.

5. `alert`: Tingkat log ini digunakan untuk mencatat kondisi yang memerlukan perhatian segera. Biasanya digunakan untuk situasi di mana tindakan segera diperlukan untuk menangani peristiwa atau kondisi tertentu.

6. `debug`: Fungsi `Log::debug()` digunakan untuk mencatat pesan log dengan tingkat `debug`. Pesan log dengan tingkat debug digunakan untuk mencatat informasi detail yang membantu dalam proses debugging dan analisis aplikasi. Biasanya, pesan log ini berisi detail tentang aliran eksekusi program, nilai variabel, atau langkah-langkah kritis dalam kode. Tingkat log debug biasanya digunakan selama pengembangan dan debugging, dan disarankan untuk tidak menyertakan pesan log tingkat debug dalam produksi aplikasi.

7. `info`: Fungsi `Log::info()` digunakan untuk mencatat pesan log dengan tingkat `info`. Pesan log dengan tingkat info digunakan untuk mencatat informasi yang berguna untuk pemantauan dan pemecahan masalah. Pesan log ini dapat berisi informasi penting tentang peristiwa, status, atau hasil dari operasi tertentu dalam aplikasi. Pesan log tingkat info umumnya digunakan untuk memberikan wawasan tentang aktivitas normal aplikasi, seperti penciptaan objek, permintaan HTTP yang sukses, atau operasi penting lainnya.

8. `warning`: Fungsi `Log::warning()` digunakan untuk mencatat pesan log dengan tingkat `warning`. Pesan log dengan tingkat warning digunakan untuk mencatat kondisi yang memerlukan perhatian, tetapi tidak termasuk sebagai kesalahan (error) yang menghentikan aliran normal aplikasi. Pesan log tingkat warning umumnya digunakan untuk mencatat kondisi yang mungkin menyebabkan masalah atau menghasilkan hasil yang tidak diharapkan, tetapi masih memungkinkan aplikasi untuk melanjutkan operasi normal. Contohnya dapat mencakup penggunaan fitur yang sudah usang (deprecated), masukan yang tidak valid, atau operasi yang membutuhkan perhatian lebih.

Dengan menggunakan fungsi-fungsi log ini, Anda dapat mencatat pesan log dengan tingkat yang sesuai dan menghasilkan informasi yang berguna saat memantau, debugging, dan memecahkan masalah dalam aplikasi Laravel Anda.

contoh penulisan
```
use Illuminate\Support\Facades\Log;
 
Log::debug('Accessed index method of VendorController');
Log::info('Vendor created successfully in store method of VendorController');
Log::warning('Validation failed in store method of VendorController');
Log::error('Call to a member function save() on null in VendorController@edit ');
Log::emergency('Database connection failed');
Log::notice('User logged in successfully');
Log::critical('Out of disk space');
Log::alert('Server CPU usage above threshold');
```

hasil yang ada di log file
```
[2023-07-14 10:30:15] local.DEBUG: Accessed index method of VendorController  
[2023-07-14 10:30:25] local.INFO: Vendor created successfully in store method of VendorController  
[2023-07-14 10:30:30] local.WARNING: Validation failed in store method of VendorController  
[2023-07-14 10:30:35] local.ERROR: Call to a member function save() on null in VendorController@edit  
[2023-07-14 10:30:40] local.EMERGENCY: Database connection failed  
[2023-07-14 10:30:45] local.NOTICE: User logged in successfully  
[2023-07-14 10:30:50] local.CRITICAL: Out of disk space  
[2023-07-14 10:30:55] local.ALERT: Server CPU usage above threshold  

```


<p dir="rtl" style="font-family: Amiri; line-height: 2.0;">
عَنْ أَبِي هُرَيْرَةَ رضي الله عنه قَالَ رَسُولُ اَللَّهِ صلى الله عليه وسلم حَقُّ اَلْمُسْلِمِ عَلَى اَلْمُسْلِمِ سِتٌّ: إِذَا لَقِيتَهُ فَسَلِّمْ عَلَيْهِ, وَإِذَا دَعَاكَ فَأَجِبْهُ, وَإِذَا اِسْتَنْصَحَكَ فَانْصَحْهُ, وَإِذَا عَطَسَ فَحَمِدَ اَللَّهَ فَسَمِّتْهُ وَإِذَا مَرِضَ فَعُدْهُ, وَإِذَا مَاتَ فَاتْبَعْهُ . رَوَاهُ مُسْلِمٌ
</p>

