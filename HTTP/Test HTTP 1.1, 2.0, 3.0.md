Untuk menginstal web server berbasis Docker dengan dukungan HTTP/1.1, HTTP/2.0, dan HTTP/3.0, mengaksesnya melalui Chrome, dan menganalisis lalu lintas dengan Wireshark, berikut langkah-langkahnya:

---

### 1. **Persiapan Lingkungan**

- Pastikan Docker dan Wireshark telah terinstal di sistem Anda.
- Unduh dan instal browser Google Chrome versi terbaru.

---

### 2. **Konfigurasi Docker untuk Web Server**

Kita akan menggunakan **NGINX** sebagai contoh web server karena mendukung HTTP/1.1, HTTP/2, dan HTTP/3.

#### a. **Buat File Docker Compose**

Buat file `docker-compose.yml` dengan konfigurasi berikut:

```yaml
version: '3.8'
services:
  web:
    image: nginx:latest
    ports:
      - "80:80"       # HTTP/1.1
      - "443:443"     # HTTP/2 dan HTTP/3
    volumes:
      - ./conf.d:/etc/nginx/conf.d
      - ./certs:/etc/nginx/certs
```

#### b. **Buat File Konfigurasi NGINX**

Buat file `default.conf` di dalam direktori  `conf.d`:

```nginx
server {
   listen 80; # HTTP/1.1
   listen 443 ssl http2; # HTTP/2
   listen 443 quic reuseport; # HTTP/3
   ssl_certificate /etc/nginx/certs/server.crt;
   ssl_certificate_key /etc/nginx/certs/server.key;
   ssl_protocols TLSv1.3;
   ssl_prefer_server_ciphers off;
   add_header Alt-Svc 'h3-23=":443"; ma=86400';
   add_header X-Content-Type-Options nosniff;
   root /usr/share/nginx/html;
   index index.html;
}
```

#### c. **Sertifikat SSL**

Buat sertifikat SSL untuk mendukung HTTPS:

```bash
mkdir certs
openssl req -x509 -newkey rsa:2048 -keyout certs/server.key -out certs/server.crt -days 365 -nodes
```

---

### 3. **Jalankan Web Server**

Di terminal, jalankan:

```bash
docker-compose up
```

---
#### 3.1 Aktifkan Firewall
```bash
ufw enable
ufw allow 80
ufw allow 443
```
cek konfigurasi
```bash
$ ufw status
Status: active

To                         Action      From
--                         ------      ----
80                         ALLOW       Anywhere                  
443                        ALLOW       Anywhere                  
80 (v6)                    ALLOW       Anywhere (v6)             
443 (v6)                   ALLOW       Anywhere (v6) 
```
jika hasil seperti diatas, maka konfigurasi telah berhasil.
### 4. **Akses di Chrome**

- Buka Chrome dan akses `http://localhost` untuk HTTP/1.1.
- Gunakan `https://localhost` untuk HTTPS dengan HTTP/2 dan HTTP/3.

---

### 5. **Pantau Lalu Lintas di Wireshark**

1. Buka Wireshark dan pilih jaringan yang Anda gunakan (misalnya, Wi-Fi atau Ethernet).
2. Gunakan filter:
    - **HTTP/1.1**: `http`
    - **HTTP/2**: `http2` atau `tcp.port==443`
    - **HTTP/3**: `udp.port==443`
3. Akses URL di Chrome dan amati lalu lintas di Wireshark.

---

### 6. **Verifikasi Versi HTTP di Chrome**

- Buka **Developer Tools** di Chrome (tekan F12).
- Pergi ke tab **Network**.
- Muat ulang halaman dan perhatikan kolom **Protocol** untuk melihat apakah koneksi menggunakan HTTP/1.1, HTTP/2, atau HTTP/3.

Dengan langkah-langkah ini, Anda bisa menjalankan web server NGINX dalam Docker, mengamati perilaku protokol HTTP di browser Chrome, dan menganalisis lalu lintas menggunakan Wireshark.