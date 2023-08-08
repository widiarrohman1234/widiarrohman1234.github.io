# Install Docker di Ubuntu
Berikut adalah langkah-langkah untuk menginstal Docker pada Ubuntu:

1. Buka terminal SSH dan akses instance EC2 Ubuntu Anda.

2. Perbarui repositori paket dengan menjalankan perintah berikut:
   ```bash
   sudo apt update
   ```

3. Instal paket yang diperlukan agar apt dapat menggunakan repositori melalui HTTPS:
   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

4. Tambahkan kunci GPG Docker ke sistem Anda dengan menjalankan perintah berikut:
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

5. Tambahkan repositori Docker ke sources.list.d:
   ```bash
   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

6. Perbarui kembali repositori paket:
   ```bash
   sudo apt update
   ```

7. Instal Docker dengan menjalankan perintah berikut:
   ```bash
   sudo apt install docker-ce docker-ce-cli containerd.io
   ```

8. Setelah instalasi selesai, Docker akan berjalan sebagai layanan. Anda dapat memeriksa statusnya dengan perintah berikut:
   ```bash
   sudo systemctl status docker
   ```

   Jika statusnya aktif (running), itu berarti Docker telah terinstal dan berjalan.

9. (Opsional) Jika Anda ingin menjalankan Docker sebagai pengguna non-root, tambahkan pengguna ke grup "docker":
   ```bash
   sudo usermod -aG docker $USER
   ```

   Setelah menambahkan pengguna ke grup "docker", Anda perlu keluar dari sesi saat ini dan masuk kembali untuk perubahan tersebut diterapkan.

Sekarang, Docker sudah terinstal pada Ubuntu Anda. Anda dapat menggunakan perintah-perintah Docker seperti `docker run`, `docker build`, dan lainnya untuk mengelola kontainer Docker. Pastikan untuk memeriksa dokumentasi Docker untuk mempelajari lebih lanjut tentang cara menggunakan Docker dengan baik.