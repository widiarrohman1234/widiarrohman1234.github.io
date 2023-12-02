Berikut adalah langkah-langkah untuk menginstal Docker pada Ubuntu:

1. Pastikan Anda telah masuk ke sistem Ubuntu sebagai pengguna dengan hak akses root atau pengguna dengan hak akses sudo.

2. Perbarui indeks paket apt dengan menjalankan perintah berikut:
   ```
   sudo apt update
   ```

3. Install paket yang diperlukan agar apt dapat menggunakan repositori melalui HTTPS:
   ```
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

4. Tambahkan kunci GPG resmi Docker dengan menjalankan perintah berikut:
   ```
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

5. Tambahkan repositori Docker ke sumber perangkat lunak apt dengan perintah berikut:
   ```
   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

6. Perbarui indeks paket apt sekali lagi:
   ```
   sudo apt update
   ```

7. Terakhir, instal Docker dengan menjalankan perintah berikut:
   ```
   sudo apt install docker-ce docker-ce-cli containerd.io docker-compose
   ```

8. Setelah instalasi selesai, Docker akan dijalankan secara otomatis. Anda dapat memeriksa status Docker dengan menjalankan perintah berikut:
   ```
   sudo systemctl status docker
   ```

   Jika statusnya "active" (berarti Docker berjalan), maka instalasi telah berhasil.

9. (Opsional) Jika Anda ingin menjalankan Docker sebagai pengguna non-root, tambahkan pengguna ke grup "docker":
   ```bash
   sudo usermod -aG docker $USER
   ```

Setelah menambahkan pengguna ke grup "docker", Anda perlu keluar dari sesi saat ini dan masuk kembali untuk perubahan tersebut diterapkan.

Selamat! Anda telah berhasil menginstal Docker pada Ubuntu. Anda sekarang dapat menggunakan perintah-perintah Docker untuk mengelola kontainer dan menjalankan aplikasi dalam lingkungan terisolasi.