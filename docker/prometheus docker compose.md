# install prometheus menggunakan docker compose
## buat folder dan file `docker-prometheus.yml`
```
root@vps-sidafa:/home/sidafa/docker# mkdir prometheus
root@vps-sidafa:/home/sidafa/docker# cd prometheus/
root@vps-sidafa:/home/sidafa/docker/prometheus# nano docker-compose.yml
```

isi file `docker-compose.yml`

```
version: '3'

services:
  prometheus:
    image: ubuntu/prometheus:2.46.0-22.04_stable
    container_name: prometheus
    environment:
      - TZ=GMT+7
    ports:
      - "9090:9090"
    restart: always
    volumes:
      - /home/sidafa/docker/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
#      - /home/sidafa/docker/prometheus/alerts.yml:/etc/prometheus/alerts.yml
  node_exporter:
    image: prom/node-exporter
    container_name: node_exporter
    ports:
      - "9100:9100"
    restart: always

```
simpan dan keluar

## buat file prometheus.yml
install node exporter
```
root@vps-sidafa:/home/sidafa/docker/prometheus# nano prometheus.yml
```
```
scrape_configs:
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['103.175.219.109:9100']

  - job_name: 'prometheus-VPS-1'
    honor_timestamps: true
    scrape_interval: 15s
    scrape_timeout: 10s
    metrics_path: /metrics
    scheme: http
    follow_redirects: true
    enable_http2: true
    static_configs:
      - targets:
        - '103.175.219.109:9090'
```
simpan dan keluar

## jalankan docker-compose
```
root@vps-sidafa:/home/sidafa/docker/prometheus# docker-compose up -d
```
## buka port firewall
```
ufw allow 9090
ufw allow 9100
```

## selesai instalasi

# Dokumentasi

## exec container
```
docker exec -it prometheus-container /bin/bash
```



## sumber
https://hub.docker.com/r/ubuntu/prometheus