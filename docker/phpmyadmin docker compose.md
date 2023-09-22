# install phpmyadmin docker compose
## buat file docker-compose.yml
```
root@vps-sidafa:/home/sidafa/docker# mkdir phpmyadmin
root@vps-sidafa:/home/sidafa/docker# cd phpmyadmin
root@vps-sidafa:/home/sidafa/docker/phpmyadmin# nano docker-compose.yml
```
isi file `docker-compose.yml`
```
version: '3.1'

services:
  phpmyadmin:
    image: phpmyadmin
    restart: always
    ports:
      - "8080:80"
    environment:
      - PMA_ARBITRARY=1
```


## docker-compose up -d
```
root@vps-sidafa:/home/sidafa/docker/phpmyadmin# docker-compose up -d
```
