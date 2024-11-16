Untuk membuat user MySQL dengan nama sidafa yang hanya bisa mengakses database sidafa_db melalui semua host (%), Anda bisa mengikuti langkah-langkah berikut:

1. *Login ke MySQL sebagai Root atau Akun dengan Hak Istimewa*:
```
   mysql -u root -p
```
   

2. *Buat Database* (Jika Belum Ada):
```
CREATE DATABASE sidafa_db;
```
   

3. **Buat User dan Berikan Hak Akses ke Database sidafa_db**:
  ```
CREATE USER 'sidafa'@'%' IDENTIFIED BY 'contohPassword1234';
GRANT ALL PRIVILEGES ON sidafa_db.* TO 'sidafa'@'%';
  ```
   

4. *Simpan Perubahan*:
   sql
```
   FLUSH PRIVILEGES;
```
   

5. *Keluar dari MySQL*:
   sql
```
   EXIT;
```
   

Dengan perintah di atas:
- User sidafa sekarang dapat terhubung ke database sidafa_db dari semua host (%).
- Hak akses ALL PRIVILEGES diberikan hanya untuk database sidafa_db, sehingga user sidafa tidak bisa mengakses database lain. 

