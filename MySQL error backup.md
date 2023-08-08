# MySQL XAMPP error not running

1. Bukan `C:\xampp\mysql`
2. Amankan folder `data` dengan cara copas menjadi `data_old`
3. Copas `backup` dan rename menjadi `data`
4. Ambil **SEMUA FOLDER DAN HANYA** file `ibdata1` pada folder `data_old` kecuali folder `["mysql", "performance_schema", "phpmyadmin", "test"]`
5. paste ke folder `data` (yang baru)

*) Pastikan MYSQL mati