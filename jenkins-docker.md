# Instalasi jenkins menggunakan docker

Untuk menginstal Jenkins menggunakan Docker dan mengarahkan port 49000 pada host ke port 8080 di container, Anda dapat mengikuti langkah-langkah berikut:

1. **Pastikan Docker Terinstal**:
   Pastikan Docker sudah terinstal di sistem Anda. Anda dapat mengunduh dan menginstal Docker dari situs resmi Docker (https://docs.docker.com/get-docker/).

2. **Membuat Container Jenkins**:
   Gunakan perintah berikut untuk membuat dan menjalankan container Jenkins:

   ```bash
   docker run -d -p 49000:8080 --name jenkins jenkins/jenkins
   ```

   - `-d`: Menjalankan container dalam mode latar belakang.
   - `-p 49000:8080`: Meneruskan port 49000 pada host ke port 8080 di dalam container.
   - `--name jenkins`: Memberi nama container sebagai "jenkins".
   - `jenkins/jenkins`: Ini adalah nama gambar Jenkins yang diambil dari Docker Hub.

3. **Mengecek Log Awal Jenkins**:
   Anda dapat melihat log awal Jenkins dengan perintah berikut:

   ```bash
   docker logs jenkins
   ```

   Pada log awal ini, Anda akan menemukan password awal yang dibutuhkan untuk mengakses Jenkins melalui browser.

4. **Mengakses Jenkins dari Browser**:
   Buka browser dan akses Jenkins melalui `http://localhost:49000` atau `http://<your-host-ip>:49000`. Di sana, Anda akan diminta memasukkan password awal yang ditemukan di langkah sebelumnya.

5. **Instal Plugin dan Konfigurasi**:
   Lanjutkan proses konfigurasi dan instalasi plugin seperti biasa saat mengatur Jenkins. Ikuti petunjuk di antarmuka web untuk menyelesaikan proses instalasi.

6. **Unlock Jenkins**:
   Setelah instalasi selesai, Anda perlu membuka Jenkins dengan menggunakan password yang diberikan pada langkah 3. Ikuti instruksi di antarmuka web untuk membuka Jenkins.

Pastikan port 49000 pada host tidak digunakan oleh aplikasi lain dan pastikan Anda menggantinya dengan port yang tersedia jika diperlukan. Juga, perhatikan bahwa menggunakan Docker memungkinkan Anda untuk dengan mudah mengelola dan menghapus container sesuai kebutuhan.

> saya memiliki container jenkins, apakah bisa menginstall npm/node.js didalamnya. agar proses build repository dari github bisa dilakukan?

Ya, Anda bisa menginstall npm (Node Package Manager) dan Node.js di dalam Jenkins container untuk memungkinkan proses build repository dari GitHub yang memerlukan lingkungan Node.js. Berikut adalah langkah-langkah umum yang bisa Anda ikuti:

1. **Buka Jenkins Container:**
   Pastikan container Jenkins sedang berjalan dan Anda dapat mengakses antarmukanya melalui browser.

2. **Buka Terminal di Dalam Container:**
   Anda perlu masuk ke dalam container Jenkins untuk dapat menjalankan perintah-perintah instalasi. Anda bisa menggunakan perintah seperti `docker exec -it <container_name> /bin/bash` (sesuaikan dengan nama container Jenkins Anda).

3. **Install Node.js dan npm:**
   Di dalam terminal container Jenkins, Anda dapat menjalankan perintah-perintah berikut untuk menginstall Node.js dan npm:

   ```
   curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
   apt-get install -y nodejs
   ```

   Pastikan perintah-perintah tersebut berhasil dijalankan dan Node.js beserta npm terinstall dengan baik.

4. **Konfigurasi Build Job:**
   Setelah Node.js dan npm terinstall di dalam container Jenkins, Anda bisa membuat atau mengonfigurasi job build Anda. Biasanya, dalam langkah konfigurasi, Anda bisa menambahkan tahap (stage) di mana Anda menjalankan perintah-perintah npm untuk menginstall dependensi dan menjalankan proses build dari repository GitHub Anda.

5. **Tambahkan Perintah npm dalam Tahap Build:**
   Dalam konfigurasi tahap build, tambahkan langkah-langkah yang diperlukan, seperti perintah untuk menginstall dependensi menggunakan npm dan menjalankan proses build. Contoh:

   ```
   stage('Install Dependencies') {
       steps {
           sh 'npm install'
       }
   }

   stage('Build') {
       steps {
           sh 'npm run build'
       }
   }
   ```

   Pastikan untuk menyesuaikan perintah-perintah di atas dengan struktur proyek dan perintah yang sebenarnya digunakan dalam repository GitHub Anda.

6. **Simpan dan Jalankan Job:**
   Simpan konfigurasi build job Anda dan jalankan job tersebut. Jenkins akan menjalankan langkah-langkah yang Anda definisikan dalam tahapan build.

Pastikan Anda memiliki pemahaman dasar tentang cara kerja Jenkins, penggunaan Docker (jika Anda menggunakan Docker untuk menjalankan Jenkins dalam container), serta konfigurasi build jobs dalam Jenkins. Jika Anda menghadapi kendala atau masalah selama proses ini, pastikan untuk merujuk kepada dokumentasi resmi Jenkins, Docker, Node.js, dan npm.