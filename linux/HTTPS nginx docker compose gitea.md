# Konfigurasi HTTPS nginx ubuntu docker-compose gitea
Dokumentasi pembelajaran devsecops untuk membuat server git.\
saya menggunakan:
- ubuntu sebagai OS server
- let's encrypt untuk sertifikat SSL
- docker-compose untuk Nginx
- gitea sebagai server git

> ## Dokumentasi adalah teman terbaik ketika bingung/lupa/stres 😁❤️.

## Buat sertifikat SSL
```shell
root@VPS-1-Testing-WA:/etc/letsencrypt/live# certbot certonly --standalone -d gitea.widiarrohman.my.id
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Requesting a certificate for gitea.widiarrohman.my.id

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Could not bind TCP port 80 because it is already in use by another process on
this system (such as a web server). Please stop the program in question and then
try again.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(R)etry/(C)ancel: R

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/gitea.widiarrohman.my.id/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/gitea.widiarrohman.my.id/privkey.pem
This certificate expires on 2024-01-02.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
 * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
 * Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

root@VPS-1-Testing-WA:/etc/letsencrypt/live/gitea.widiarrohman.my.id# ls
README  cert.pem  chain.pem  fullchain.pem  privkey.pem
```

## Atur subdomain di `conf.d`
```shell
root@VPS-1-Testing-WA:/home/widiarrohman1234/docker/nginx-1/conf.d# cat gitea.conf
server {
    listen 80;
    server_name gitea.widiarrohman.my.id;

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name gitea.widiarrohman.my.id;

    ssl_certificate /etc/nginx/ssl/gitea/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/gitea/privkey.pem;

    location / {
        proxy_pass http://103.175.219.171:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
root@VPS-1-Testing-WA:/home/widiarrohman1234/docker/nginx-1/conf.d#
```

## Pengaturan `docker-compose.yml`
> ### Pastikan directory `/etc/nginx/ssl/gitea/` sudah ada pada docker nginx
```shell
root@VPS-1-Testing-WA:/home/widiarrohman1234/docker/nginx-1# cat docker-compose.yml
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
      - /etc/letsencrypt/live/gitea.widiarrohman.my.id/fullchain.pem:/etc/nginx/ssl/gitea/fullchain.pem
      - /etc/letsencrypt/live/gitea.widiarrohman.my.id/privkey.pem:/etc/nginx/ssl/gitea/privkey.pem
    ports:
      - "80:80"
      - "443:443"
    command: /bin/bash -c "cp /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.backup && nginx -g 'daemon off;'"
root@VPS-1-Testing-WA:/home/widiarrohman1234/docker/nginx-1#
```
```shell
root@VPS-1-Testing-WA:/home/widiarrohman1234/docker/nginx-1# docker-compose up -d
root@VPS-1-Testing-WA:/home/widiarrohman1234/docker/nginx-1# docker container restart nginx-2

```

## Hasil
![Alt text](../image/httpsgitrawidiarrohman.png)


## Selesai
