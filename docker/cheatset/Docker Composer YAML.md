Dokumentasi resmi: https://docs.docker.com/reference/compose-file/

Berikut adalah dokumentasi inti atau cheatsheet untuk `docker-compose.yml`, mencakup semua komponen yang paling umum digunakan dalam file Docker Compose. Cheatsheet ini akan membantu Anda dalam memahami dan menulis file `docker-compose.yml` dengan berbagai opsi konfigurasi.

```yaml
# Docker Compose Cheatsheet: docker-compose.yml

# Level 1: Basic Information
version: '3'  # Versi Docker Compose yang digunakan (misal '2', '3', atau '3.8')

services:    # Deklarasi semua service
  # Nama service (misal: web, db, redis)
  web:
    image: nginx:latest   # Image yang digunakan oleh service
    build:                # Build service menggunakan Dockerfile
      context: ./path     # Path ke Dockerfile
      dockerfile: Dockerfile.dev   # (Opsional) Dockerfile spesifik yang digunakan
    ports:
      - "8080:80"         # Map port host:container
    environment:          # Variabel lingkungan untuk container
      - NODE_ENV=production
    command: node server.js  # Jalankan perintah saat container dimulai
    healthcheck:          # Mengecek apakah service dalam kondisi sehat
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 1m30s
      timeout: 10s
      retries: 3
      start_period: 40s
    volumes:              # Mount volume ke dalam container
      - ./local_path:/container_path
    labels:               # Label metadata pada container
      com.example.description: "Web service for accounting app"
    networks:             # Masukkan container ke dalam network tertentu
      - frontend
      - backend
    depends_on:           # Mengatur urutan startup antar service
      - db
    restart: always       # Policy restart (no, always, on-failure, unless-stopped)
    dns:                  # DNS server yang digunakan oleh container
      - 8.8.8.8
      - 8.8.4.4
    extra_hosts:          # Tambahkan host DNS ke /etc/hosts
      - "somehost:192.168.1.100"
    links:                # Link ke service lain di Docker Compose (Deprecated)
      - db
    external_links:       # Link ke service dari luar Docker Compose project
      - redis_1
    user: "1000:1000"     # Tentukan pengguna dan grup yang menjalankan container
    devices:              # Tambahkan perangkat host ke container
      - "/dev/ttyUSB0:/dev/ttyUSB0"

  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: example
    volumes:
      - dbdata:/var/lib/mysql
    networks:
      - backend

networks:                 # Deklarasi network
  frontend:               # Definisi jaringan 'frontend'
    driver: bridge        # Tipe driver (bridge, overlay)
  backend:
    external: true        # Menggunakan network eksternal

volumes:                  # Deklarasi volume
  dbdata:                 # Volume bernama 'dbdata'
    driver: local         # Driver (local, nfs, etc.)

# Level 2 and 3 Details

# Level 2: Service Details
#   build: Untuk membangun image dari Dockerfile
#     context: Path yang digunakan sebagai context build
#     dockerfile: Nama file Dockerfile spesifik yang digunakan

#   ports: Mapping port untuk menghubungkan container dengan host
#     - "host_port:container_port"

#   volumes: Mengelola mount volume lokal ke container
#     - ./local_path:/container_path
#     - namavolume:/container_path (volume yang didefinisikan di luar service)

#   environment: Menambahkan variabel lingkungan ke dalam container
#     - KEY=value

#   healthcheck: Mengecek apakah container dalam keadaan sehat
#     test: Perintah yang dijalankan untuk pengecekan
#     interval: Interval waktu antar pengecekan
#     timeout: Waktu maksimal untuk menunggu hasil pengecekan
#     retries: Jumlah percobaan ulang jika gagal
#     start_period: Waktu untuk memulai pengecekan setelah container aktif

#   labels: Menambahkan label metadata untuk container
#     key: value

#   depends_on: Mengatur urutan container yang harus dijalankan terlebih dahulu

#   restart: Mengatur kebijakan restart container
#     - no
#     - always
#     - on-failure
#     - unless-stopped

#   dns: Mengatur DNS server untuk container
#     - IP_address

#   extra_hosts: Mengubah /etc/hosts pada container
#     - "hostname:IP_address"

#   user: Menentukan UID:GID untuk menjalankan container

#   devices: Membagikan perangkat dari host ke container
#     - "/dev/device:/dev/device"

#   links: (Deprecated) Menghubungkan container satu dengan yang lain
#     - servicename

#   external_links: Menghubungkan ke container di luar Docker Compose
#     - container_name

# Level 3: Detail Lainnya
networks:  # Deklarasi network untuk digunakan oleh container
  # Membuat network custom untuk komunikasi antar container
  network_name:
    driver: bridge     # Jenis driver (default: bridge)

volumes:  # Deklarasi volume untuk persistent storage
  volume_name:
    driver: local      # Driver volume (local, nfs, etc.)

# Contoh Penggunaan DNS, Hosts, dan Network
  redis:
    image: redis:alpine
    dns:
      - 8.8.8.8
    extra_hosts:
      - "myhost:127.0.0.1"
    networks:
      - mynetwork
```

### Penjelasan Singkat Perintah `docker-compose.yml`

1. **version**: Menentukan versi syntax docker-compose yang digunakan. Umumnya `3` atau `3.x`.
2. **services**: Mendeklarasikan layanan/container yang akan dijalankan.
3. **build**: Membangun container dari Dockerfile.
    - `context`: Direktori untuk Docker build.
    - `dockerfile`: Nama Dockerfile spesifik yang digunakan.
4. **ports**: Mapping port dari container ke host.
5. **volumes**: Mengelola storage persisten antara host dan container.
6. **environment**: Variabel lingkungan yang diteruskan ke dalam container.
7. **healthcheck**: Mengecek status kesehatan container.
8. **labels**: Metadata tambahan untuk container.
9. **networks**: Jaringan untuk container (bisa internal atau eksternal).
10. **depends_on**: Mengatur urutan startup antara beberapa service.
11. **restart**: Kebijakan restart container (misal: selalu, hanya saat gagal).
12. **dns**: Mengatur DNS yang digunakan oleh container.
13. **extra_hosts**: Menambahkan mapping DNS ke file `/etc/hosts` dalam container.
14. **user**: Tentukan pengguna/grup untuk menjalankan proses di container.
15. **devices**: Membagikan perangkat host tertentu ke container.
16. **links**: Menghubungkan container satu dengan yang lain (sudah deprecated).
17. **external_links**: Menghubungkan container dengan container yang berjalan di luar file Compose.

Cheatsheet ini mencakup hampir semua konfigurasi umum dalam `docker-compose.yml` dan dapat digunakan sebagai referensi saat mengembangkan file Compose Anda. Semoga bermanfaat!