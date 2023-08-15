# Instalasi jenkins menggunakan docker

## Install docker di Ubuntu
1. **Persiapan:**


   ```bash
   sudo apt update
   ```

2. **Instal Prasyarat:**

   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

3. **Tambahkan Repository Docker:**

   Tambahkan repository Docker ke sistem Anda:

   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

4. **Instal Docker:**

   Setelah menambahkan repository, lakukan instalasi Docker:

   ```bash
   sudo apt update
   sudo apt install docker-ce
   ```

5. **Memeriksa Status Docker:**

   ```bash
   sudo systemctl status docker
   ```

6. **Menjalankan Docker Tanpa sudo (Opsional):**

   Secara default, Anda mungkin perlu menjalankan perintah Docker dengan `sudo`. Namun, Anda dapat menambahkan pengguna Anda ke grup "docker" untuk menjalankan Docker tanpa `sudo`:

   ```bash
   sudo usermod -aG docker $USER
   ```

   Setelah itu, Anda perlu keluar dan masuk lagi atau memulai ulang komputer agar perubahan ini berlaku.


## Install Jenkins di Docker
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

> cara menginstall docker jenkins dengan menggunakan Dockerfile yang didalamnya sudah sekalian menginstall npm didalam container jenkins

Untuk menginstal Jenkins dengan Docker dan dalam Dockerfile sudah termasuk instalasi npm, Anda perlu membuat Dockerfile kustom yang akan membangun gambar Docker berdasarkan gambar resmi Jenkins dan menambahkan langkah-langkah instalasi npm di dalamnya. Berikut adalah contoh langkah-langkahnya:

1. **Buat Direktori Proyek:**

   Buat direktori baru untuk proyek Anda, dan di dalamnya buat Dockerfile.

2. **Buat Dockerfile:**

   Buat sebuah Dockerfile di dalam direktori proyek Anda dengan teks editor favorit. Contoh Dockerfile berikut akan membangun gambar Jenkins dan menginstal npm di dalamnya:

   ```Dockerfile
   # Gunakan gambar Jenkins resmi sebagai dasar
   FROM jenkins/jenkins:latest

   # Ganti ke pengguna root untuk menginstal paket
   USER root

   # Instalasi paket npm
   RUN apt-get update && \
       apt-get install -y npm && \
       rm -rf /var/lib/apt/lists/*

   # Kembali ke pengguna Jenkins
   USER jenkins
   ```

   Pastikan Anda menyimpan Dockerfile ini di direktori proyek Anda.

3. **Bangun Gambar Docker:**

   Buka terminal dan arahkan ke direktori proyek Anda yang berisi Dockerfile. Jalankan perintah berikut untuk membangun gambar Docker:

   ```bash
   docker build -t jenkins-with-npm .
   ```

   Pastikan titik di akhir perintah di atas menunjukkan ke direktori tempat Dockerfile Anda berada.

4. **Jalankan Container Jenkins:**

   Setelah gambar Docker selesai dibangun, Anda dapat menjalankan kontainer Jenkins menggunakan perintah seperti berikut:

   ```bash
   docker run -p 8080:8080 -p 50000:50000 jenkins-with-npm
   ```

   Pastikan untuk mengganti port yang sesuai jika Anda ingin menggunakan port yang berbeda.

5. **Akses Jenkins:**

   Buka browser dan akses Jenkins melalui http://localhost:8080 atau sesuai dengan port yang Anda tentukan. Ikuti panduan untuk menyelesaikan instalasi dan mengatur Jenkins.

Perhatikan bahwa dengan menggabungkan Jenkins dan npm dalam satu gambar Docker, Anda menambahkan perangkat lunak yang perlu dikelola dan diperbarui ke dalam gambar tersebut. Pastikan Anda mempertimbangkan strategi pemeliharaan dan pengelolaan dalam jangka panjang.

Pastikan juga Anda memahami setiap langkah dan implikasinya saat menggunakan Docker. Menggunakan Docker memerlukan pemahaman tentang cara kerja Docker, gambar, dan kontainer.