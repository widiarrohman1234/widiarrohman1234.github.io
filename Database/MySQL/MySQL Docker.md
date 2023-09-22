# MySQL With Docker

## install docker mysql
```
docker run -d --name mysql-1 -e MYSQL_ROOT_PASSWORD=your_password -p 3306:3306 mysql
```

## install phpmyadmin and auto connect to mysql docker
```
docker run --name phpmyadmin -d --link mysql-1:db -p 8080:80 phpmyadmin
```

## Akses MySQL dengan Docker Exec di terminal
```
docker exec -it mysql-1 mysql -u root -p
```

## login/konek ke docker container
ganti `some-mysql` dengan nama container
```
docker exec -it some-mysql bash
```

## lihat log mysql container
```
docker logs some-mysql
```

---
<br>

# install MySQL menggunakan docker compose
## buat file docker-compose.yml
```
root@vps-sidafa:/home/sidafa/docker# mkdir mysql
root@vps-sidafa:/home/sidafa/docker# cd mysql
root@vps-sidafa:/home/sidafa/docker/mysql# nano docker-compose.yml
```
isi file `docker-compose.yml` dengan perintah dibawah:
```
version: '3'

services:
  mysql:
    image: mysql
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: ********
    ports:
      - "3306:3306"
```
## install docker compose
```
root@vps-sidafa:/home/sidafa/docker/mysql# docker-compose up -d
```
## buka port firewall
```
ufw allow 3306
```

## selesai