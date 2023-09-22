# Perintah docker-compose

Perintah `docker-compose up -d` digunakan untuk menginisialisasi dan menjalankan semua layanan yang didefinisikan dalam file Docker Compose dalam mode detached (background).

1. **docker-compose down**: Perintah ini digunakan untuk menghentikan dan menghapus kontainer, jaringan, dan volume yang dibuat oleh Docker Compose.

   Contoh: `docker-compose down`

2. **docker-compose ps**: Perintah ini menampilkan status dari semua layanan yang didefinisikan dalam file Docker Compose Anda, termasuk apakah mereka sedang berjalan atau tidak.

   Contoh: `docker-compose ps`

3. **docker-compose logs**: Perintah ini digunakan untuk melihat log dari layanan yang berjalan.

   Contoh: `docker-compose logs`

4. **docker-compose exec**: Perintah ini memungkinkan Anda untuk menjalankan perintah dalam kontainer yang sedang berjalan. Ini berguna untuk debugging atau melakukan tugas-tugas administrasi.

   Contoh: `docker-compose exec myapp bash` (menjalankan shell dalam kontainer bernama "myapp")

5. **docker-compose build**: Perintah ini digunakan untuk membangun ulang gambar Docker yang didefinisikan dalam file Docker Compose Anda.

   Contoh: `docker-compose build`

6. **docker-compose restart**: Perintah ini digunakan untuk me-restart layanan yang didefinisikan dalam Docker Compose Anda.

   Contoh: `docker-compose restart`

7. **docker-compose pause** dan **docker-compose unpause**: Perintah ini digunakan untuk menangguhkan (pause) atau melanjutkan (unpause) layanan yang berjalan.

   Contoh: `docker-compose pause myservice`

8. **docker-compose pull**: Perintah ini digunakan untuk menarik gambar-gambar Docker yang didefinisikan dalam file Docker Compose Anda.

   Contoh: `docker-compose pull`
