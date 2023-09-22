# Install Portainer dengan docker compose

## membuat file docker-compose.yml
```
root@vps-sidafa:/home/sidafa# mkdir docker
root@vps-sidafa:/home/sidafa# cd docker
root@vps-sidafa:/home/sidafa/docker# mkdir portainer
root@vps-sidafa:/home/sidafa/docker# cd portainer
root@vps-sidafa:/home/sidafa/docker/portainer# nano docker-compose.yml
```
isi file `docker-compose.yml` sebagai berikut:
```
version: '3'

services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    restart: always
    ports:
      - "8000:8000"
      - "9443:9443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data

volumes:
  portainer_data:
```

## Running docker-compose up -d
jika belum ada `docker-compose`, maka install dulu. tapi jika sudah ada, maka lansung jalankan `docker-compose up -d`
- root@vps-sidafa:/home/sidafa/docker/portainer# `apt install docker-compose`
- root@vps-sidafa:/home/sidafa/docker/portainer# `docker-compose up -d`

> perintah `docker-compose up -d` hanya bisa berjalan pada file `docker-compose.yml` dalam 1 direktori

> Pastikan anda sudah membuka port 9443 dan 8000 menggunakan `ufw allow 9443` dan `ufw allow 8000`, pelajari lebih lanjut disini [https://github.com/widiarrohman1234/widiarrohman1234.github.io/blob/master/linux/firewall%20ubuntu%20(ufw).md](https://github.com/widiarrohman1234/widiarrohman1234.github.io/blob/master/linux/firewall%20ubuntu%20(ufw).md)

> Pastikan anda sudah menginstall web server seperti Nginx atau Apache

## Perhatian
> akses portainer menggunakan `https`, jika menggunakan `http` tidak bisa.