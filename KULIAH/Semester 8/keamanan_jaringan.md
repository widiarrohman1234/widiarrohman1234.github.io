# Catatan Matkul Keamanan Jaringan
> Semester 8 Politeknik Eletronika Negeri Surabaya (PENS)
Dosen pengajar: Pak Isbat

## Nmap
Anda dapat menggunakan berbagai perintah `nmap` untuk melakukan pemindaian jaringan terhadap domain `widiarrohman.my.id` dengan IP `103.175.219.171`. Berikut adalah beberapa perintah `nmap` yang berguna:

1. **Pemindaian Dasar**:
   ```
   nmap widiarrohman.my.id
   ```

2. **Pemindaian Port Tertentu**:
   ```
   nmap -p 80,443 widiarrohman.my.id
   ```

3. **Menentukan Jenis Pemindaian**:
   ```
   nmap -sS widiarrohman.my.id
   ```

4. **Menampilkan Informasi Versi Layanan**:
   ```
   nmap -sV widiarrohman.my.id
   ```

5. **Deteksi Sistem Operasi**:
   ```
   nmap -O widiarrohman.my.id
   ```

6. **Pemindaian UDP**:
   ```
   nmap -sU widiarrohman.my.id
   ```

7. **Pemindaian Intensif**:
   ```
   nmap -A widiarrohman.my.id
   ```

8. **Menentukan Kecepatan Pemindaian**:
   ```
   nmap -T4 widiarrohman.my.id
   ```

9. **Menyimpan Hasil Pemindaian**:
   ```
   nmap -oN hasil.txt widiarrohman.my.id
   ```

10. **Pemindaian dengan Proxy**:
    ```
    nmap --proxy socks4://proxyserver:port widiarrohman.my.id
    ```

11. **Pemindaian dengan Skrip NSE (Nmap Scripting Engine)**:
    ```
    nmap --script <script> widiarrohman.my.id
    ```

12. **Pemindaian Subnet**:
    ```
    nmap 103.175.219.0/24
    ```

## Openvas

[https://forum.greenbone.net/t/ubuntu-and-gsa-installation/12980](https://forum.greenbone.net/t/ubuntu-and-gsa-installation/12980)

## membuat metasploitable menggunakan docker compose

1. **Buat Direktori Kerja**:
   Pertama, buat direktori kerja baru untuk proyek Metasploitable Anda. Misalnya, buat direktori baru dengan nama "metasploitable" dan pindah ke dalamnya.

    ```bash
    mkdir metasploitable
    cd metasploitable
    ```

2. **Buat File `docker-compose.yml`**:
   Buat file `docker-compose.yml` di dalam direktori proyek Anda untuk mendefinisikan layanan Metasploitable.

    ```yaml
    version: '3'
    
    services:
      metasploitable:
        image: metasploitframework/metasploit-framework
        ports:
          - "4444:4444"
        command: "msfconsole"
    ```

   Dalam file ini, kami menggunakan gambar Docker `metasploitframework/metasploit-framework` yang sudah ada sebagai dasar dan mendefinisikan layanan yang menjalankan Metasploit Console di port 4444 yang akan tersedia di host Anda.

3. **Jalankan Metasploitable**:
   Sekarang jalankan Metasploitable menggunakan perintah `docker-compose up`.

    ```bash
    docker-compose up
    ```

   Ini akan memulai Metasploit Console di dalam kontainer Docker. Anda akan dapat mengaksesnya dari host Anda dengan terhubung ke port 4444.

4. **Menggunakan Metasploit**:
   Anda sekarang dapat menggunakan Metasploit Framework seperti yang Anda lakukan dalam instalasi lokal. Terhubung ke console dengan perintah:

    ```bash
    msfconsole
    ```

   Dari sini, Anda dapat memulai tes penetrasi dan eksploitasi sesuai kebutuhan Anda.

## Instal metasploitable3 di ubuntu
- link dokumentasi [https://github.com/rapid7/metasploitable3](https://github.com/rapid7/metasploitable3)

## cooming soon