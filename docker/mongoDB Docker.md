Berikut adalah langkah-langkah untuk menginstal MongoDB menggunakan Docker pada Ubuntu:

1. Pastikan Docker sudah terinstal dan berjalan pada instance EC2 Ubuntu Anda. Jika belum, ikuti langkah-langkah instalasi Docker yang telah disebutkan sebelumnya.

2. Buka terminal SSH dan akses instance EC2 Ubuntu Anda.

3. Jalankan perintah berikut untuk mengunduh dan menjalankan container MongoDB:

   ```bash
   sudo docker run --name mongodb -d -p 27017:27017 mongo
   ```

   Penjelasan perintah:
   - `--name mongodb`: Menetapkan nama kontainer sebagai "mongodb". Anda dapat mengganti "mongodb" dengan nama lain jika diinginkan.
   - `-d`: Menjalankan kontainer di dalam mode detached (di latar belakang).
   - `-p 27017:27017`: Meneruskan port 27017 dari host (instance EC2) ke dalam kontainer MongoDB. Port ini adalah port default untuk koneksi MongoDB.
   - `mongo`: Menunjukkan nama gambar Docker yang digunakan untuk menjalankan kontainer. Jika gambar tidak ada di sistem Anda, Docker akan mengunduhnya secara otomatis.

4. Setelah perintah di atas dijalankan, Docker akan mengunduh gambar MongoDB (jika belum ada) dan menjalankan kontainer MongoDB. Anda dapat memeriksa status kontainer dengan perintah:
   ```bash
   sudo docker ps
   ```

   Jika kontainer MongoDB sedang berjalan, Anda akan melihat entri yang mencantumkan kontainer dengan nama "mongodb".

Anda sekarang telah berhasil menginstal MongoDB menggunakan Docker pada Ubuntu. Kontainer MongoDB dapat diakses melalui port 27017 pada instance EC2 Anda. Anda dapat menggunakan alamat IP publik instance EC2 dan port 27017 untuk menghubungkan aplikasi Anda ke MongoDB yang berjalan di dalam kontainer Docker.

# MongoDB Install docker-compose
1. instalasi
```
version: '3.1'

services:
  mongodb:
	container_name: mongodb_test
    image: mongo:4.4
    restart: always
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
    volumes:
      - mongodb_data:/data/db

volumes:
  mongodb_data:
```

2. koneksi internal via docker
	`docker exec -it mongodb_test /bin/bash`
3. koneksi eksternal
	`mongodb://root:*****@103.175.219.171:27017`
4. done