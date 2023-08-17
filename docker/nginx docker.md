# Install NGINX with Docker

## Studi Kasus
- saya memiliki folder `/home/sammy/ftp/files`
- folder ini terhubung dengan konfigurasi FTP
- saya ingin folder ini terhubung ke NGINX Docker agar bisa public

## create nginx.conf in folder `/home/sammy/ftp/files`
Buat berkas dengan nama nginx.conf di dalam folder /home/sammy/ftp/files dengan konten berikut:
```
server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}
```
## Membuat Container Docker Nginx
```
docker run -d --name nginx-container -v /home/sammy/ftp/files:/usr/share/nginx/html -v /home/sammy/ftp/files/nginx.conf:/etc/nginx/conf.d/default.conf -p 80:80 nginx
```
## Ubah hak akses folder pada host
```
sudo chmod -R 755 /home/sammy/ftp/files
```

## Periksa Hak Akses Nginx di Dalam Container
```
docker exec -it nginx-1 /bin/bash
```
```
ls -l /usr/share/nginx
```

## restart docker 
```
docker restart nginx-1
```