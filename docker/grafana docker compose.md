# Install grafana docker compose
## buat file `docker-compose.yml`
```
root@vps-sidafa:/home/sidafa/docker# mkdir grafana
root@vps-sidafa:/home/sidafa/docker# cd grafana/
root@vps-sidafa:/home/sidafa/docker/grafana# nano docker-compose.yml
```

isi file `docker-compose.yml`
```
version: '3'

services:
  grafana:
    image: grafana/grafana-oss
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    restart: always

volumes:
  grafana_data:
```
## lakukan instalasi
```
root@vps-sidafa:/home/sidafa/docker/grafana# docker-compose up -d
```

## buka port firewall
```
ufw allow 3000
```

## first login
- link: http://IP.IP.IP.IP:3000/login
- user: `admin`
- pass: `admin`

## Selesai

## Sumber
https://hub.docker.com/r/grafana/grafana