Untuk membatalkan aturan `iptables` yang telah Anda tambahkan, Anda perlu menghapus aturan tersebut. Berikut adalah langkah-langkah yang bisa Anda ikuti:

### 1. Menampilkan Aturan `iptables` Saat Ini

Pertama, tampilkan aturan `iptables` saat ini untuk memastikan aturan mana yang perlu dihapus.

```bash
sudo iptables -L -v -n --line-numbers
```

Ini akan menampilkan daftar aturan saat ini dengan nomor baris di kolom paling kiri. Nomor baris ini diperlukan untuk menghapus aturan tertentu.

### 2. Menghapus Aturan `iptables`

Setelah Anda mengidentifikasi aturan yang ingin dihapus, gunakan nomor baris yang sesuai untuk menghapusnya. Misalnya, jika aturan untuk menolak koneksi dari publik berada di nomor baris 3 dan 4, gunakan perintah berikut untuk menghapusnya:

```bash
sudo iptables -D INPUT 3
sudo iptables -D INPUT 3
```

Setiap kali Anda menghapus aturan, nomor baris lainnya akan bergeser, jadi pastikan untuk menyesuaikannya jika Anda memiliki lebih dari satu aturan yang perlu dihapus.

### 3. Memverifikasi Penghapusan

Verifikasi bahwa aturan telah dihapus dengan menampilkan aturan `iptables` lagi:

```bash
sudo iptables -L -v -n
```

### Contoh Langkah-Langkah Lengkap

1. Tampilkan aturan `iptables`:

    ```bash
    sudo iptables -L -v -n --line-numbers
    ```

2. Identifikasi nomor baris dari aturan yang ingin dihapus (misalnya, nomor baris 3 dan 4).

3. Hapus aturan menggunakan nomor baris:

    ```bash
    sudo iptables -D INPUT 3
    sudo iptables -D INPUT 3
    ```

4. Verifikasi bahwa aturan telah dihapus:

    ```bash
    sudo iptables -L -v -n
    ```

Dengan langkah-langkah ini, Anda dapat membatalkan aturan `iptables` yang telah Anda tambahkan sebelumnya. Jika Anda ingin memastikan MongoDB dapat diakses kembali dari IP publik, Anda juga perlu memastikan bahwa konfigurasi Docker dan pengaturan MongoDB tidak membatasi akses tersebut.