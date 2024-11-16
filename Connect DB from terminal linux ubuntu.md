Untuk menghubungkan ke database MongoDB menggunakan terminal di Linux, Anda dapat menggunakan alat klien MongoDB yang bernama `mongo`. Berikut adalah langkah-langkah untuk melakukannya:

### 1. Instal MongoDB Shell (mongo)

Jika Anda belum menginstal MongoDB shell, Anda perlu menginstalnya terlebih dahulu. Jika Anda menggunakan Ubuntu atau distribusi berbasis Debian, Anda dapat mengikuti langkah-langkah berikut:

#### Menambahkan Repository MongoDB

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
```

#### Menginstal MongoDB Shell

```bash
sudo apt-get update
sudo apt-get install -y mongodb-org-shell
```

### 2. Menghubungkan ke MongoDB

Setelah `mongo` terinstal, Anda bisa menghubungkannya ke instans MongoDB Anda.

#### Menghubungkan ke MongoDB di Host Lokal

Jika MongoDB berjalan pada host lokal dengan port default (27017), cukup jalankan:

```bash
mongo
```

#### Menghubungkan ke MongoDB dengan Host dan Port Tertentu

Jika MongoDB berjalan pada host atau port tertentu, Anda bisa menggunakan perintah berikut:

```bash
mongo --host <hostname> --port <port>
```

Contoh:

```bash
mongo --host 172.17.0.2 --port 27017
```

#### Menghubungkan ke MongoDB dengan Autentikasi

Jika MongoDB dikonfigurasi dengan autentikasi, Anda perlu memasukkan nama pengguna, kata sandi, dan nama database admin:

```bash
mongo --host <hostname> --port <port> -u <username> -p <password> --authenticationDatabase <authDatabase>
```

Contoh:

```bash
mongo --host 192.168.0.1 --port 27017 -u root -p abcdefghi --authenticationDatabase admin
```

### 3. Contoh Penggunaan

Berikut adalah beberapa contoh perintah yang bisa Anda jalankan setelah terhubung ke MongoDB:

- **Melihat daftar database:**

  ```javascript
  show dbs
  ```

- **Menggunakan database tertentu:**

  ```javascript
  use mydatabase
  ```

- **Melihat koleksi dalam database:**

  ```javascript
  show collections
  ```

- **Menampilkan dokumen dalam koleksi:**

  ```javascript
  db.mycollection.find()
  ```

Dengan mengikuti langkah-langkah di atas, Anda akan bisa menghubungkan dan berinteraksi dengan MongoDB menggunakan terminal di Linux.