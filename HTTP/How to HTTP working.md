Berikut penjelasan cara kerja HTTP versi 1.0, 1.1, 2.0, dan 3.0, serta perbedaan utama di antara mereka:

---

### **1. HTTP 1.0**

#### **Cara Kerja:**

- **Sesi Terpisah untuk Setiap Permintaan**: Setiap file (misalnya, HTML, gambar, CSS, atau JavaScript) membutuhkan koneksi TCP yang baru.
- **Tanpa Persistensi**: Setelah satu objek dikirimkan, koneksi langsung ditutup.
- **Header Sederhana**: Header HTTP 1.0 hanya mendukung informasi dasar seperti metode permintaan (`GET`, `POST`, `HEAD`), status respons, dan metadata dasar.
- **Tidak Mendukung Host Header**: Tidak bisa membedakan beberapa domain di satu alamat IP.

#### **Kelemahan:**

- Membutuhkan banyak koneksi, membuat latensi tinggi dan tidak efisien.
- Tidak cocok untuk halaman web modern dengan banyak objek.

---

### **2. HTTP 1.1**

#### **Cara Kerja:**

- **Koneksi Persisten**: HTTP 1.1 memungkinkan koneksi TCP tetap terbuka untuk beberapa permintaan, sehingga lebih hemat waktu.
- **Pipelining**: Beberapa permintaan dapat dikirim tanpa menunggu respons sebelumnya, tetapi respons tetap harus diterima berurutan.
- **Host Header**: Mendukung beberapa domain pada satu alamat IP melalui header `Host`.
- **Caching yang Lebih Baik**: Menambahkan kontrol caching dengan header seperti `Cache-Control`.

#### **Keunggulan Dibanding HTTP 1.0:**

- Mengurangi waktu pembukaan koneksi TCP yang berulang.
- Lebih efisien untuk halaman web dengan banyak objek.

#### **Kelemahan:**

- Meskipun lebih baik dari HTTP 1.0, tetap mengalami latensi karena respons harus diterima berurutan.

---

### **3. HTTP 2.0**

#### **Cara Kerja:**

- **Multiplexing**: Menggunakan satu koneksi TCP untuk mengirimkan beberapa permintaan dan respons secara bersamaan tanpa harus menunggu urutan.
- **Header Compression**: Mengurangi ukuran header dengan kompresi (menggunakan algoritma HPACK).
- **Prioritas**: Memberikan prioritas pada konten tertentu untuk mempercepat waktu pemuatan.
- **Push Server**: Server dapat mengirimkan data (seperti CSS atau JavaScript) ke klien sebelum diminta.

#### **Keunggulan Dibanding HTTP 1.1:**

- Menghilangkan masalah "head-of-line blocking" di tingkat aplikasi.
- Lebih cepat dan efisien untuk halaman dengan banyak elemen.
- Mengurangi konsumsi bandwidth karena kompresi header.

#### **Kelemahan:**

- Tetap menggunakan TCP, yang memiliki masalah jika terjadi kehilangan paket (latensi meningkat karena retransmisi seluruh data).

---

### **4. HTTP 3.0**

#### **Cara Kerja:**

- **Menggunakan QUIC**: Beralih dari TCP ke QUIC, protokol transport berbasis UDP yang lebih cepat dan handal.
- **Stream Multiplexing**: Sama seperti HTTP/2, tetapi tanpa "head-of-line blocking" karena setiap stream independen.
- **Keamanan Bawaan**: QUIC mengintegrasikan enkripsi TLS 1.3, membuatnya lebih aman dan cepat tanpa negosiasi tambahan.
- **Pengurangan Latensi**: Koneksi lebih cepat karena menghindari 3-way handshake TCP dan mendukung 0-RTT untuk permintaan ulang.

#### **Keunggulan Dibanding HTTP 2.0:**

- Tidak terpengaruh oleh kehilangan paket karena setiap stream dikelola secara independen.
- Waktu respons lebih cepat karena pengaturan koneksi yang minimal.
- Cocok untuk jaringan tidak stabil seperti mobile atau Wi-Fi.

#### **Kelemahan:**

- Masih relatif baru, sehingga dukungan di beberapa server atau perangkat mungkin belum menyeluruh.

---
### Ilustrasi Visual

Untuk mencerminkan ini secara visual, berikut adalah gambaran yang bisa dibuat:

1. **HTTP 1.0**:
    
    - Gambar seorang pelanggan dengan satu kantong kecil masuk-keluar toko berulang kali.
    - Latar belakang: Toko sederhana.
2. **HTTP 2.0**:
    
    - Gambar seorang pelanggan dengan keranjang besar berisi banyak barang yang diambil sekaligus.
    - Latar belakang: Supermarket modern dengan jalur cepat.
3. **HTTP 3.0**:
    
    - Gambar pelanggan di jalur drive-thru dengan layanan otomatis yang cepat.
    - Latar belakang: Restoran cepat saji dengan beberapa jalur layanan.
### **Ringkasan Evolusi**

|Versi HTTP|Transport|Koneksi Persisten|Multiplexing|Header Compression|Keunggulan Utama|
|---|---|---|---|---|---|
|**HTTP 1.0**|TCP|Tidak|Tidak|Tidak|Sederhana untuk implementasi awal|
|**HTTP 1.1**|TCP|Ya|Tidak|Tidak|Koneksi persisten dan caching|
|**HTTP 2.0**|TCP|Ya|Ya|Ya|Multiplexing dan efisiensi tinggi|
|**HTTP 3.0**|UDP (QUIC)|Ya|Ya|Ya|Latensi rendah dan tanpa blocking|

---

### **Kesimpulan**

HTTP telah berkembang untuk mengatasi masalah latensi, efisiensi, dan keamanan. **HTTP/1.1** menjadi standar utama, **HTTP/2.0** memperkenalkan efisiensi tinggi, dan **HTTP/3.0** membawa perubahan fundamental dengan mengganti TCP ke QUIC untuk performa lebih baik.

# Gambar
![[Pasted image 20241125150941.png]]
Source Image: https://www.researchgate.net/publication/312560536_The_curious_case_of_parallel_connections_in_HTTP2