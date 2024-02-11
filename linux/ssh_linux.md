# Create .PEM
Anda dapat membuat kunci SSH dengan ekstensi `.pem` menggunakan perintah `ssh-keygen`. Berikut adalah langkah-langkahnya:

1. Buka terminal di sistem Anda.

2. Jalankan perintah berikut untuk membuat kunci SSH dengan algoritma RSA dan menyimpannya dalam format PEM:

    ```bash
    ssh-keygen -t rsa -b 2048 -m PEM -f ~/.ssh/nama_kunci.pem
    ```

    Gantilah `nama_kunci` dengan nama yang Anda inginkan untuk kunci SSH Anda.

    - `-t rsa`: Menentukan algoritma kunci RSA.
    - `-b 2048`: Menentukan panjang bit kunci (pilih sesuai kebutuhan Anda).
    - `-m PEM`: Menyimpan kunci dalam format PEM.
    - `-f ~/.ssh/nama_kunci.pem`: Menyimpan kunci di direktori `~/.ssh/` dengan nama yang Anda tentukan dan ekstensi `.pem`.

3. Anda akan diminta untuk memasukkan passphrase untuk kunci (opsional). Jika Anda tidak ingin menggunakan passphrase, cukup tekan Enter.

4. Proses tersebut akan menghasilkan dua berkas: `nama_kunci.pem` (kunci privat) dan `nama_kunci.pem.pub` (kunci publik).

Anda sekarang memiliki kunci SSH dalam format PEM dengan ekstensi `.pem`. Kunci privat (`nama_kunci.pem`) adalah yang sangat penting dan harus dijaga dengan baik, sementara kunci publik (`nama_kunci.pem.pub`) dapat dibagikan ke server atau layanan yang memerlukan otentikasi Anda. Pastikan untuk menyimpan kunci privat dengan aman dan tidak membagikannya kecuali jika diperlukan.

===============
# save sshpub in authorized_keys
Untuk menyimpan kunci publik (`pens-health.pub`) pada file `authorized_keys` di server, Anda dapat mengikuti langkah-langkah berikut:

1. Gunakan perintah `cat` atau `echo` untuk menampilkan isi kunci publik:

    ```bash
    cat ./pens-health.pem.pub
    ```

    atau

    ```bash
    echo "Isi_kunci_publik_anda_di_sini" > ./pens-health.pem.pub
    ```

2. Salin isi kunci publik tersebut.

3. SSH ke server Anda menggunakan kredensial Anda:

    ```bash
    ssh username@alamat_server
    ```

    Gantilah `username` dengan nama pengguna Anda dan `alamat_server` dengan alamat IP atau nama host server Anda.

4. Setelah masuk ke server, buat atau buka file `authorized_keys` pada direktori `.ssh` di direktori home pengguna Anda. Jika file ini belum ada, Anda dapat membuatnya.

    ```bash
    nano ~/.ssh/authorized_keys
    ```

    Gantilah `nano` dengan editor teks pilihan Anda (misalnya, `vi` atau `vim`).

5. Tempelkan isi kunci publik yang telah Anda salin pada langkah 2 ke dalam file `authorized_keys`.

6. Simpan perubahan dan keluar dari editor.

    - Jika Anda menggunakan `nano`, tekan `Ctrl + X`, kemudian `Y` untuk menyimpan perubahan, dan `Enter` untuk keluar.
    - Jika Anda menggunakan `vi` atau `vim`, tekan `Esc`, lalu ketik `:wq` dan tekan `Enter`.

Sekarang, kunci publik Anda telah ditambahkan ke dalam file `authorized_keys` di server. Dengan begitu, Anda sekarang dapat menggunakan kunci privat yang sesuai dengan kunci publik ini untuk melakukan otentikasi SSH tanpa memasukkan kata sandi setiap kali Anda terhubung.

========================
# SSH Agent untuk git clone gitlab

Berikut adalah beberapa langkah yang dapat Anda ikuti untuk menyelesaikan masalah ini:

1. **Mulai `ssh-agent` dan Tambahkan Kunci SSH:**
   Pastikan Anda menjalankan perintah `ssh-agent` dan menambahkan kunci SSH sebelum menjalankan perintah `git clone`. Gunakan perintah berikut:
   yang dimasukkan adalah private key

   ```bash
   eval $(ssh-agent)
   ssh-add /home/widiarrohman1234/ssh/gitlab-pens-health
   ```

   Setelah itu, coba lagi untuk menjalankan perintah `git clone`.

2. **Pastikan Kunci SSH Ada dan Terdaftar di `ssh-agent`:**
   Pastikan bahwa kunci SSH yang ingin Anda gunakan (`/home/widiarrohman1234/ssh/gitlab-pens-health`) ada dan terdaftar di `ssh-agent`. Anda dapat memeriksa kunci yang terdaftar dengan perintah:

   ```bash
   ssh-add -L
   ```

   Jika kunci tidak terdaftar, tambahkan dengan menggunakan perintah `ssh-add` seperti yang ditunjukkan di atas.

3. **Perbarui Kunci SSH di GitLab:**
   Pastikan kunci SSH yang terkait dengan akun GitLab Anda telah ditambahkan ke pengaturan akun GitLab Anda. Anda dapat menyalin kunci publik (`/home/widiarrohman1234/ssh/gitlab-pens-health.pub`) dan menambahkannya ke pengaturan SSH di [GitLab SSH settings](https://gitlab.com/-/profile/keys).

   Jika Anda memperbarui atau menambahkan kunci SSH baru, pastikan Anda juga telah memberikan izin akses yang diperlukan di repositori GitLab.

4. **Periksa Izin Repositori:**
   Pastikan bahwa kunci SSH yang ditambahkan ke GitLab memiliki izin akses yang memadai untuk mengklon repositori. Anda dapat memeriksa dan mengonfigurasi izin akses di pengaturan repositori GitLab (Settings -> Repository -> Protected branches, tags, and paths).

5. **Gunakan URL HTTPS (Opsional):**
   Jika masalah persisten, Anda dapat mencoba menggunakan URL HTTPS untuk mengklon repositori sebagai gantinya. Pastikan Anda telah menyimpan kata sandi GitLab jika repositori menggunakan otentikasi dua faktor.

   ```bash
   git clone https://gitlab.com/pens-health-care/backend-api-dan-web.git
   ```

Coba langkah-langkah di atas, dan jika masalah masih berlanjut, periksa log detail dari `ssh-agent` dan Git untuk mendapatkan informasi lebih lanjut:

```bash
ssh-add -L
ssh -Tv git@gitlab.com
```

Perhatikan bahwa `git clone` menggunakan protokol SSH, sehingga memastikan kunci SSH berfungsi dengan baik penting untuk mengatasi masalah ini.


=============
# convert .pem to .ppk in putty application
Anda sudah berhasil membuat pasangan kunci SSH pada server Ubuntu Anda menggunakan perintah `ssh-keygen`. Sekarang, untuk menggunakan kunci tersebut dengan PuTTY, Anda perlu mengonversi kunci tersebut ke dalam format PPK (PuTTY Private Key).

Anda dapat menggunakan utilitas `puttygen` yang disertakan dengan aplikasi PuTTY untuk melakukan konversi tersebut. Berikut adalah langkah-langkahnya:

1. Buka aplikasi `puttygen`. Jika Anda belum menginstal PuTTY, Anda dapat mengunduhnya dari situs resmi PuTTY: [Download PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

2. Jalankan `puttygen` dan klik tombol "Load".

3. Pilih jenis file "All Files" dari daftar file dan pilih kunci privat yang telah Anda buat sebelumnya (`pens-health`).

4. Anda mungkin perlu mengubah jenis file yang ditampilkan di dialog kotak dialog "Load private key" untuk "All Files" agar Anda dapat melihat kunci privat yang telah Anda buat.

5. Setelah memilih kunci privat, klik "Open".

6. Puttygen akan meminta konfirmasi konversi. Klik "OK" untuk melanjutkan.

7. Selanjutnya, Anda dapat mengonversi kunci dengan menyimpannya sebagai file PPK. Klik tombol "Save private key".

8. Beri nama dan simpan file kunci PPK sesuai keinginan Anda.

Sekarang, Anda dapat menggunakan file kunci PPK ini dengan klien PuTTY untuk melakukan remote ke server Anda. Pastikan Anda telah menyimpan kunci publik (`pens-health.pub`) di file `authorized_keys` pada server tujuan agar kunci SSH dapat digunakan untuk otentikasi.