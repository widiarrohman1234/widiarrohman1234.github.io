# Soal
Terdapat 3 kriteria utama yang harus Anda penuhi dalam mengerjakan proyek pertama ini.

# Kriteria 1: Membuat Berkas Shell Script
Berkaca pada skenario yang telah dijelaskan sebelumnya, Anda harus membuat sebuah berkas shell script dengan nama `script-<username_dicoding>.sh` untuk mengotomatiskan tugas. Berkas script yang Anda buat wajib berisi ketentuan berikut ini.

1. Menampilkan ukuran `memory` pada sistem dalam satuan `megabytes`.
2. Menampilkan penggunaan ruang disk pada filesystem dalam satuan gigabytes.
3. Menampilkan penggunaan ruang `disk` pada filesystem hanya untuk kolom `Filesystem` dan `Use%` (ditampilkan juga nama kolomnya) serta tanpa menyertakan tmpfs. Contohnya seperti ini.

```
Filesystem Use%
/dev/nvme0n1p4 28%
/dev/nvme0n1p1 15%
```
Perlu diingat bahwa tiga ketentuan di atas `wajib ada` di dalam berkas shell script Anda.

Selain itu, output dari script ini harus ditampilkan pada shell dengan rapi dan mudah dibaca, yakni dengan memenuhi hal-hal berikut.

* Setiap output perintah dari ketentuan di atas harus ditampilkan secara berurutan.
* Setiap output perintah dari ketentuan di atas harus diawali dengan teks berupa keterangan singkat tentang perintah yang dijalankan.
* Setiap output perintah dari ketentuan di atas harus diakhiri dengan baris baru agar saling terpisah dan tidak menumpuk.
* Setiap output perintah dari ketentuan di atas harus diberi jeda selama beberapa waktu agar dapat dianalisis dengan cermat oleh admin.

    * `3 detik` setelah perintah untuk ketentuan 1 berjalan.
    * `3 detik` setelah perintah untuk ketentuan 2 berjalan.
    * `1 menit` setelah perintah untuk ketentuan 3 berjalan. Khusus ketentuan ini, satuan yang ditulis pada berkas script harus 1 menit, bukan 60 detik).

Anda akan dianggap menyelesaikan Kriteria 1 apabila telah memenuhi semua ketentuan di atas.

# Kriteria 2: Melampirkan Berkas Berisi Command History
Setelah membuat berkas shell script (yang ketika dijalankan sukses memenuhi semua ketentuan pada kriteria 1), Anda juga harus melampirkan berkas dengan nama `history-<username_dicoding>`.txt yang berisi semua shell command history yang telah Anda lakukan. Ingat bahwa riwayat perintah yang diambil adalah dari perintah `history`, bukan dari berkas /home/<username>/.bash_history.

# Kriteria 3: Mengarsipkan dan Mengompresi Berkas
Oke, dengan mengerjakan kriteria 1 dan kriteria 2, artinya kini Anda memiliki 2 berkas: script-<username_dicoding>.sh dan history-<username_dicoding>.txt. Selanjutnya, Anda harus mengarsipkan dan mengompresi 2 berkas tersebut menjadi `ZIP melalui terminal` dengan nama `submission1-linux-<username_dicoding>.zip`.

Dalam rangka pembuktian, silakan lakukan `screenshot` terhadap terminal untuk menunjukkan bahwa Anda menjalankan beberapa perintah pembuatan ZIP.

# jawaban
## No.1
```
nano script-widi_arrohman.sh
```
isi file
```
#!/bin/bash

# Menampilkan ukuran memory pada sistem dalam satuan megabytes
echo "Ukuran Memory:"
free -m
sleep 3

# Menampilkan penggunaan ruang disk pada filesystem dalam satuan gigabytes
echo -e "\nPenggunaan Ruang Disk:"
df -BG --output=source,size,used,avail,pcent,target
sleep 3

# Menampilkan penggunaan ruang disk pada filesystem hanya untuk kolom Filesystem dan Use%
echo -e "\nPenggunaan Ruang Disk (Filesystem dan Use%):"
df -h | awk '!/tmpfs/ {print $1, $5}'
sleep 1m
```
```
chmod +x script-widi_arrohman.sh
```
jalankan
```
./script-widi_arrohman.sh
```
## No.2
```
history > history-widi_arrohman.txt
```
## No.3
```
zip submission1-linux-widi_arrohman.zip script-widi_arrohman.sh history-widi_arrohman.txt
```
