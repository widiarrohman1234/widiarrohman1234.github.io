# Konfigurasi https gitea dengan openSSL menggunakan docker di Debian 12

1. Menginstall repositori debian 

[https://www.linuxsec.org/2023/06/daftar-repository-debian-12-indonesia.html](https://www.linuxsec.org/2023/06/daftar-repository-debian-12-indonesia.html) 

```dart
deb [https://kebo.pens.ac.id/debian/](https://kebo.pens.ac.id/debian/) bookworm main contrib non-free
deb [https://kebo.pens.ac.id/debian/](https://kebo.pens.ac.id/debian/) bookworm-updates main contrib non-free
deb [https://kebo.pens.ac.id/debian-security/](https://kebo.pens.ac.id/debian-security/) bookworm/updates main contrib non-free
```

atau

```dart
deb [https://kebo.pens.ac.id/debian/](https://kebo.pens.ac.id/debian/) bookworm main contrib non-free
deb [https://kebo.pens.ac.id/debian/](https://kebo.pens.ac.id/debian/) bookworm-updates main contrib non-free
deb [https://kebo.pens.ac.id/debian-security/](https://kebo.pens.ac.id/debian-security/) bookworm/updates main contrib non-free
```

a) caranya : copas link tsb pada **nano /etc/apt/sources.list** kemudian jalankan **apt-get update**

1. Menginstall docker

a) `curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

b) `chmod +x /usr/local/bin/docker-compose`

c) `docker-compose --version`

1. Membuat container didalam direktori docker

a) Membuat direktori untuk service yg diperlukan dengan cara mkdir (nama folder)

![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled.png)

**Didalam docker**

1. Menginstall nginx
- membuat direktori nginx **mkdir nginx**
- didalamnya buat folder conf.d **mkdir conf.d dan**
- **file** docker-compose.yml **mkdir docker-compose.yml**

![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%201.png)

- isi dari docker-compose.yml

![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%202.png)

- untuk menginstall nginx jalankan perintah docker-compose up-d
- didalam folder conf.d buat layanan yang ingin diinginkan
- buat file default.conf dan gitea.conf
    
    ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%203.png)
    
- isi dari default.conf
    
    ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%204.png)
    
- isi dari gitea.conf
    
    ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%205.png)
    
    ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%206.png)
    
- Menjalankan nginx
    
    docker container start nginx
    
- Melihat layanan docker yang berjalan
    
    docker ps
    
    ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%207.png)
    
1. Menginstall phpmyadmin
    - buat direktori phpmyadmin
        
        ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%208.png)
        
    - buat file docker.compose.yml dan isi
        
        ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%209.png)
        
    - install phpmyadmin dengan "docker-compose up-d" maka akan terinstall
        
        ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2010.png)
        
2. Menginstall gitea
    - buat folder gitea
        
        ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2011.png)
        
    - buat file docker.compose.yml dan isi
        
        ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2012.png)
        
    - buat folder config dan data
    - install gitea dengan "docker-compose up-d" maka akan terinstall
    - untuk mengisi folder config dan data jalankan
    - sudo chown 1000:1000 /config /data
    - restart agar layanan berjalan
    - docker container restart gitea
    
    ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2013.png)
    
    - untuk membuat url gitea.localhost
        
        ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2014.png)
        
        copy default.conf menjadi gitea.conf, lalu ubah isinya menjadi seperti ini
        
        ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2015.png)
        
        ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2016.png)
        
3. Menginstall mysql
    - buat direktori mysql
        
        ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2017.png)
        
    - buat file docker.compose.yml dan isi
        
        ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2018.png)
        
    - install mysql dengan "docker-compose up-d" maka akan terinstall
    
    1. Memberikan izin agar port bisa diakses
        - ufw allow (port)
        - ex : ufw allow 3306 (u port gitea)
        - ufw status
        - te
            
            ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2019.png)
            
            1. Menginstall portainer
            - buat direktori portainer
                
                ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2020.png)
                
            - buat direktori portainer_data dan file docker-compose.yml dan isi
            
            ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2021.png)
            
        1. Membuat sertifikat
            - Membuat sertifikat
            
            openssl req -x509 -newkey rsa:4096 -keyout /home/minah/openssl/gitea.localhost.key -out /home/minah/openssl/gitea.localhost.crt -days 365
            
            - Memberikan password untuk sertifikat agar dpt diakses oleh docker
            
            openssl rsa -in /etc/ssl/private/gitea.localhost.key -out /etc/ssl/private/gitea.localhost.key
            
            - Mengatur alamat sertifikat
            
            ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2022.png)
            
            ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2023.png)
            
            ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2024.png)
            
            ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2025.png)
            
            ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2026.png)
            
            kemudian restart nginx
            
            ![Untitled](Konfigurasi%20https%20gitea%20dengan%20openSSL%20menggunakan%20d128b4b5e405455c9e81291290b785c4/Untitled%2027.png)