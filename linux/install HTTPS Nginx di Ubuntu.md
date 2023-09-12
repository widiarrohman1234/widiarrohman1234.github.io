# Install SSL pada nginx ubuntu menggunakan certbot

link referensi
- [certbot instructions](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal)
- [installing-snap-on-ubuntu](https://snapcraft.io/docs/installing-snap-on-ubuntu)
- [Dokumentasi PDF](https://letsencrypt.org/documents/LE-SA-v1.3-September-21-2022.pdf)

## instalasi snapd
```
sudo apt update
sudo apt install snapd
```

## testing snapd
```
sudo snap install hello-world
hello-world
```

## install cerbot
```
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

## jika Nginx diinstall pada host
### dapatkan dan install sertifikat
```
sudo cerbot --nginx
```
### hanya mendapatkan sertifikat saja
```
sudo certbot certonly --nginx
```
## Jika Nginx diinstall menggunakan docker
```
sudo certbot certonly --standalone -d widiarrohman.my.id
```
## sudah mendapatkan sertifikat
```
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/widiarrohman.my.id/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/widiarrohman.my.id/privkey.pem
This certificate expires on 2023-12-11.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.
```

## pemasangan ke contianer nginx
```
docker exec -it nginx-2 ln -s /etc/letsencrypt/live/widiarrohman.my.id/fullchain.pem /etc/nginx/ssl/fullchain.pem
```
```
docker exec -it nginx-2 ln -s /etc/letsencrypt/live/widiarrohman.my.id/privkey.pem /etc/nginx/ssl/privkey.pem
```
`buat terlebih dahulu folder ssl pada /etc/nginx dengan perintah **mkdir /etc/nginx/ssl**`

## konfigurasi docker-compose.yml
tambahkan port 443 dan link ke fullchain dan privkey
```
version: "3"

services:
  nginx-1:
    container_name: nginx-2
    image: nginx
    volumes:
      - /var/www/html:/usr/share/nginx/html
      - /home/widiarrohman1234/docker/nginx-1/conf.d:/etc/nginx/conf.d
      - /etc/letsencrypt/live/widiarrohman.my.id/fullchain.pem:/etc/nginx/ssl/fullchain.pem
      - /etc/letsencrypt/live/widiarrohman.my.id/privkey.pem:/etc/nginx/ssl/privkey.pem
    ports:
      - "80:80"
      - "443:443"
    command: /bin/bash -c "cp /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.backup && nginx >
```
## buka firewall
```
ufw allow 80
ufw allow 443
```

## konfigurasi default.conf
/etc/nginx/nginx.conf
```
server {
    listen 443 ssl;
    server_name widiarrohman.my.id;

    ssl_certificate /etc/nginx/ssl/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/privkey.pem;

    # Konfigurasi lainnya
    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}
```

## hapus, buat dan mulai docker compose
```
docker compose down
docker compose create
docker compose start
```

## berhasil







