# Catatan Perintah Docker

## A. PERINTAH DOCKER DASAR
1.	Image
    1) lihat	
        ```
        docker image ls
        ```
    2)	download
        ```
        docker pull redis:latest 
        ```
    3)	hapus
        ```
        docker image rm redis:latest
        ```
2.	Container
    1)	melihat semua kontainer
        ```
        docker container ls -a
        ```
    2)	melihat kontainer yang berjalan saja
        ```
        docker container ls
        ```
    3)	membuat container
        ```
        docker container create --name namacontainer namaimage:tag
        ```
    4)	menjalankan container
        ```
        docker container start namacontainer
        ```
    5)	menghentikan container
        ```
        docker container stop namacontainer
        ```
    6)	hapus container
        ```
        docker container rm namacontainer
        ```
    7)	melihat log container
        ```
        docker container logs namacontainer
        ```
    8)	melihat log container dengan berjalan terus
        ```
        docker container logs -f namacontainer
        ```
3.	Cotainer exec
    1)	edit file didalam container
        ```
        docker container exec -i -t namacontainer /bin/bash
        ```
4.	container port forwarding
    1)	perintah
        > docker container create --name namacontainer --publish porthost:portcontainer image:tad
    2)	contoh
        ```
        docker container create --name contohnginx --publish 8080:80 nginx:latest
        ```
5.	container environment variable
    1)	perintah
        ```
        docker container create --name namacontainer --env KEY="value" --env KEY2="value" image:tag
        ```
    2)	contoh : 
        ```
        docker container create --name contohmongo --publish 27017:27017 --env MONGO_INITDB_ROOT_USERNAME="root" --env MONGO_INITDB_ROOT_PASSWORD="example" mongo:latest
        ```
6.	container stats (statistik)
    1) statistik source yang terpakai
        ```
        docker container stats
        ```
7.	container resource limit
    memory 100(k(kb),m(mb),g(gb))
    cpus 0.5 / 1
    1)	contoh:
        ```
        docker container create --name smallnginx --memory 100m --cpus 0.5 --publish 8081:80 nginx:latest
        ```
8.	Bind Mounts
    (sharing file&/folder dari host-container atau container-host)
    parameter mount
    1)	`type` = bind atau volume
    2)	`source` = lokasi file/folder di host
    3)	`destination` = lokasi file/folder di container
    4)	`readonly` = file/folder hanya bisa dibaca di container dan tidak bisa ditulis
    5)	perintah
        ```
        docker container create --name namacontainer --mount "type=bind,source=folderhost,destination=foldercontainer,readonly" image:tag
        ```
    6)	contoh :
        ```
        docker container create --name mongodata --publish 27018:27017 --mount "type=bind,source=C:\Users\widia\Downloads\datadockermongodb,destination=/data/db" --env MONGO_INITDB_ROOT_USERNAME="root" --env MONGO_INITDB_ROOT_PASSWORD="example" mongo:latest
        ```
9.	Docker Volume
    1)	melihat volume
        ```
        docker volume ls
        ```
    2)	membuat volume
        ```
        docker volume create namavolume
        ```
    3)	menghapus volume (container harus distop dan delete agar bisa hapus volume)
        ```
        docker volume rm namavolume
        ```
10.	Container Volume
    `type` = volume
    1)	buat volume
        ```
         docker volume create mongodata
        ```
    2)	buat container
        ```
        docker container create --name mongovolume --publish 27019:27017 --mount "type=volume,source=mongodata,destination=/data/db" --env MONGO_INITDB_ROOT_USERNAME="root" --env MONGO_INITDB_ROOT_PASSWORD="example" mongo:latest
        ```
11.	Backup Volume
    Tahapan backup volume
    1)	matikan container yang menggunakan volume yang ingin di bakcup
    2)	buat container baru dengan 2 mount, volume yang ingin dibackup masukkan ke container baru ini, buat bind mount untuk menyimpan ke host
    3)	masuk ke container....
    4)	?????

    -	cara 1
        1)	docker container create --name nginxbackup --mount "type=bind,source=C:\Users\widia\backup,destination=/backup" --mount "type=volume,source=mongodata,destination=/data" nginx:latest
        2)	docker container start nginxbackup
        3)	docker container exec -i -t nginxbackup /bin/bash //untuk cek folder
        4)	tar cvf /backup/backup.tar.gz /data  //membuat file backup data
        5)	docker container stop nginxbackup //stop container backup
        6)	docker container rm nginxbackup //hapus container backup
        7)	docker container start mongovolume //jalankan container lama(asli)

    -   cara 2 (hanya 1 perintah)
        1)	stop container yang akan di backup
            ```
            docker container stop mongovolume
            ```
        2)	perintah
            ```
            docker container run --rm --name ubuntubackup --mount "type=bind,source=C:\Users\widia\backup,destination=/backup" --mount "type=volume,source=mongodata,destination=/data" ubuntu:latest tar cvf /backup/backup-ubuntu.tar.gz /data
            ```
12.	restore volume
    1)	Langkah-langkah
        -	buat volume baru untuk lokasi restore backup (kosong)
        -	buat container baru dengan 2 mount, volume baru untuk restore bakcup dan bind mount folder dari sistem host yang berisi file backup
        -	lakukan restore menggunakan container dengan cara meng-extract ini backup file ke dalam volume
        -	isi file backup sekarang sudah di restore ke volume
        -	delete container yang kita gunakan untuk melakukan restore
        -	volume baru yang berisi data backup siap digunakan oleh container baru

    2)  Perintah
        - 1	
            ```
            docker volume create mongorestore
            ```
        -	2
            ```
            docker container run --rm --name ubunturestore --mount "type=bind,source=C:\Users\widia\backup,destination=/backup" --mount "type=volume,source=mongorestore,destination=/data" ubuntu:latest bash -c "cd /data && tar xvf /backup/backup-ubuntu.tar.gz --strip 1"
            ```
        -	3
            ```
            docker container create --name mongorestore --publish 27020:27017 --mount "type=volume,source=mongorestore,destination=/data/db" --env MONGO_INITDB_ROOT_USERNAME="root" --env MONGO_INITDB_ROOT_PASSWORD="example" mongo:latest
            ```
13.	docker network
    
    (membuat jaringan didalam docker untuk menghubungkan antar container)
    network driver populer:
    - `bridge` = container-container
    - `host` = host-container *khusus linux, Mac dan Windows tidak bisa
    - `none` = driver untuk membuat network yang tidak bisa berkomunikasi
    
    1)	perintah
        ```
        docker network ls
        docker network create --driver namadriver namanetwork
        ```
    2)  contoh: 
        ```
        docker network create --driver bridge contohnetwork
        docker network rm namanetwork 
        ```
        > **(pastikan tidak ada container yang menggunakan network)**
    
14.	container network
    (mongodb-mongoexspress)
    1)	1
        ```
        docker network create --driver bridge mongonetwork
        ```
    2)	2
        ```
        docker container create --name mongodb --network mongonetwork --env MONGO_INITDB_ROOT_USERNAME="root" --env MONGO_INITDB_ROOT_PASSWORD="example" mongo:latest
        ```
    3)	3
        ```
        docker image pull mongo-express:latest
        ```
    4)	4
        ```
        docker container create --name mongodbexpress --network mongonetwork --publish 8081:8081 --env ME_CONFIG_MONGODB_URL="mongodb://root:example@mongodb:27017" mongo-express:latest
        ```
        > (root=user, example=password, mongo=namakontainer, 27017=port container)
    5)	5
        ```
        docker container start mongodb
        ```
    6)	6
        ```
        docker container start mongodbexpress
        ```
15.	menghapus container dari network
    1)	perintah
        ```
        docker network disconnect namanetowrk namacontainer
        ```
    2)	contoh :
        ```
        docker network disconnect mongonetwork mongodb
        ```
16.	menambah container ke network
    1)	perintah
        ```
        docker network connect namanetwork namacontainer
        ```
    2)	contoh:
        ```
        docker network connect mongonetwork mongodb
        ```
17.	inspect

    melihat detail dari `image/container/volume/network`
    1)	image
        ```
        docker image inspect namaimage
        ```
    2)	container
        ```
        docker container inspect namacontainer
        ```
    3)	volume
        ```
        docker volume inspect namavolume
        ```
    4)	network
        ```
        docker network inspect namanetwork
        ```
18.	prune
    
    menghapus image, container, volume, network yang sudah stop/tidak diperlukan lagi.
    1)	menghapus semua container yang sudah stop
        ```
        docker container prune
        ```
    2)	menghapus semua image yang tidak digunakan container
        ```
        docker image prune
        ```
    3)	menghapus semua network yang tidak digunakan container
        ```
        docker network prune
        ```
    4)	menghapus volume yang tidak digunakan container
        ```
        docker volume prune
        ```
    5)	menghapus image, container, network tapi tidak untuk volume
        ```
        docker system prune
        ```

----------
 
## B. Docker Dockerfile
1.	Membuat image
    ```
    docker build -t widiarrohman/from from
    ```
    * widiarrohman adalah username di hub.docker.com
    * widiarrohman/from adalah nama dan lokasi di docker
    * from adalah nama folder file Dockerfile
2.	Menghapus image
    ```
    docker image rm widiarrohman/run
    ```
3.	From Instruction
    ```
    FROM image:version
    ```
    Ex : 
    ```
    #from instruction
    FROM alpine:3
    (alpine ada OS linux yang paling kecil) 
    *buat file Dockerfile, masukkan syntax diatas
    docker build -t widiarrohman/from from
    ```
4.	Run Instruction
    ```
    #from instruction
    FROM alpine:3
    
    #run instruction
    RUN mkdir hello
    RUN echo "Hello world" > "hello/world.txt"
    RUN cat "hello/world.txt"
    docker build -t widiarrohman/run run --progress=plain --no-cache
    ```
5.	Commad instruction
    ```
    #from instruction
    FROM alpine:3

    #run instruction
    RUN mkdir hello
    RUN echo "Hello world" > "hello/world.txt"
    
    CMD cat "hello/world.txt"
    docker build -t widiarrohman/command command
    docker image inspect widiarrohman/command
    ```
6.	Label Instruction
    1) perintah
        ```
        LABEL <key>=<value>
        ```
    2) Ex :
        ```
        LABEL author=widi country=Indonesia
        ```
        ```
        #from instruction
        FROM alpine:3
        
        #Label Instruction
        LABEL author="Widi Arrohman"
        LABEL webste="widiarrohman.sidafa.id" company="PENS"
        
        #run instruction
        RUN mkdir hello
        RUN echo "Hello world" > "hello/world.txt"
        
        #Command Instruction
        CMD cat "hello/world.txt"
        ```
        ```
        docker build -t widiarrohman/label label
        docker image inspect widiarrohman/label label
        ```
 
7.	Add instruction

    Menambahkan file dari source (host/website) ke dalam folder destination di Docker image
    * jika data dalam bentuk archive (tar.gz/gzip) maka akan di ekstrak secara otomatis
        ```
        ADD source destination
        ```
    * source berasal dari host atau link download
    * destination adalah tujuan file akan di add pada image
    
    Ex : 
    ```
    ADD world.txt hello #menambahkan file world.txt ke folder hello
    ADD *.txt hello #menambahkan semua file .txt ke folder hello
    FROM alpine:3
    
    RUN mkdir hello
    ADD text/*.txt hello
    #ADD text/* hello  //akan memasukkan semua jenis file dari host ke image
    
    CMD cat "hello/world.txt"
    ```
    ```
    docker build -t widiarrohman/add add
    docker container create --name add widiarrohman/add
    docker container start add
    docker container logs add
    ```
 
8.	Copy instruction

    * jika file archive maka tidak bisa diekstrak tapi hanya dicopy saja
    * jika source dari link, maka tidak bisa didownload
        ```
        COPY source destination
        ```
    * source berasal dari host atau link download
        ```
        FROM alpine:3
        RUN mkdir hello
        COPY text/*.txt hello
        CMD cat "hello/widi.txt"
        ```
        ```
        docker build -t widiarrohman/copy copy
        docker container create --name copy widiarrohman/copy
        docker container start copy
        docker container logs copy
        ```
9.	Dockerignore file

    File atau direktori yang tidak ingin dimasukkan ke Image maka bisa di atur didalam .dockerignore 
    ```
    FROM alpine:3
    RUN mkdir hello
    COPY text/*.txt hello
    CMD ls -l hello
    ```
    ```
    docker build -t widiarrohman/ignore ignore
    docker container create --name ignore widiarrohman/ignore
    docker container start ignore
    docker container logs ignore
    ```

10.	Expose Instruction

    EXPOSE adalah intruksi untuk memberitahu bahwa container akan listen port pada nomor dan protocol tertentu.
    ```
    EXPOSE port #defaultnya menggunakan TCP
    EXPOSE port/tcp
    EXPOSE port/udp
    FROM golang:1.18-alpine
    RUN mkdir app
    COPY main.go app
    EXPOSE 8080
    CMD go run app/main.go
    ```
    ```
    docker build -t widiarrohman/expose expose
    Docker image inspect widiarrohman/expose
    docker container create --name expose -p 8080:8080 widiarrohman/expose
    docker container start expose
    docker container logs expose
    ```
 
11.	Environment Variable Instruction
    ```
    Docker container create –env key=value
    ```
    ```
    ENV key=value
    ENV key1=value1 key2=value2
    FROM golang:1.18-alpine
    ENV APP_PORT=8080
    
    RUN mkdir app
    COPY main.go app
    
    EXPOSE ${APP_PORT}
    CMD go run app/main.go
    ```
    ```
    docker build -t widiarrohman/env env
    docker image inspect widiarrohman/env
     
    docker container create --name env --env APP_PORT=9090 -p 9090:9090 widiarrohman/env
    
    docker container start env
    docker container logs env
    ```

12.	Volume Instruction
    * VOLUME /lokasi/folder
    * VOLUME /lokasi/folder1 /lokasi/folder2 ...
    * VOLUME [“/lokasi/folder1”,” /lokasi/folder2”,”...”]
    ```
    FROM golang:1.18-alpine
    ENV APP_PORT=8080
    ENV APP_DATA=/log
    
    RUN mkdir ${APP_DATA}
    RUN mkdir app
    COPY main.go app
    EXPOSE ${APP_PORT}
    VOLUME ${APP_DATA}
    
    CMD go run app/main.go 
    ```
    ```
    docker build -t widiarrohman/volume volume
    docker image inspect widiarrohman/volume
     
    docker container create --name volume --env APP_PORT=9090 -p 9090:9090 widiarrohman/volume
    
    docker container start volume
    docker container logs volume
    docker container inspect volume
    ```
     
    “fda2178e3269206956b16452858cfe495f8445a9e90e8101b6c43007531603d7”
    ```
    Docker volume ls
    ```
 
13.	Working Directory Instruction

    WORKDIR adalah instruksi untuk menentukan `direktori/folder` untuk menjalankan instruksi `RUN`, `CMD`, `ENTRYPOINT`, `COPY` dan `ADD`.
    
    - `WORKDIR /app` #artinya working directory-nya adalah /app (absolut path)
    - `WORKDIR docker` #artinya working directory-nya adalah /app/docker (relatif path)
    - `WORKDIR /home/app` #sekarang working directory-nya adalah /home/app
    ```
    FROM golang:1.18-alpine
    
    WORKDIR /app
    COPY main.go /app
    
    EXPOSE 8080
    CMD go run main.go
    ```
    ```
    docker build -t widiarrohman/workdir workdir
    docker container create --name workdir -p 8080:8080 widiarrohman/workdir
    docker container start workdir
    docker container exec -i -t workdir /bin/sh
    ```
14.	User Instruction

    USER adalah instruksi yang digunakan untuk mengubah user atau user group ketika docker imgae dijalankan
    * `USER user` #mengubah user
    * `USER user:group` #mengubah user dan user group
    
    ```
    FROM golang:1.18-alpine
    RUN mkdir /app
    RUN
    ```
    
    ```
    docker build -t widiarrohman/user user
    docker container create --name user -p 8080:8080 widiarrohman/user
    docker container start user
    docker container exec -i -t user /bin/sh
    ```
 
15.	Argument Instruction
    ```
    ARG
    FROM golang:1.18-alpine
    
    ARG app=main
    
    RUN mkdir app
    COPY main.go app
    
    RUN mv app/main.go app/${app}.go
    
    
    EXPOSE 8080
    CMD go run app/${app}.go
    ```
    ```
    docker build -t widiarrohman/arg arg --build-arg app=pzn
    docker container create --name arg -p 8080:8080 widiarrohman/arg
    docker container start arg
    docker image inspect widiarrohman/arg
    docker container exec -i -t arg /bin/sh
    ```
 
16.	Health Check Instruction

    * HEALTHCHECK untuk mengecek apakah container dalam keadaan baik atau tidak
    * `HEALTHCHECK NONE` #artinya disable health check
    * `HEALTHCHECK [OPTIONS] CMD command`
        - OPTIONS
            - -interval=DURATION (default: 30s)
            - -timeout=DURATION (defaulit: 30s)
            - -start-period=DURATION (default: 0s)
            - -retries=N (default: 3)
    
    ```
    FROM golang:1.18-alpine
    
    RUN apk --no-chache add curl
    RUN mkdir app
    COPY main.go app
    
    EXPOSE 8080
    
    HEALTHCHECK --interval=5s  --start-period=5s CMD curl -f http://localhost:8080/health
    CMD go run app/main.go
    ```
    
    ```
    docker build -t widiarrohman/health health 
    docker container create --name health -p 8080:8080 widiarrohman/health
    docker container start health
    docker container ls
     
    docker container inspect health
    ```

17.	Entrypoint Instuction

    ENTRYPOINT adalah instruksi untuk menentukan executable file yang akan dijalankan oleh container
    1) perintah 
        > ENTRYPOINT[“executable”,”param1”, ”param1”]
        
        > ENTRYPOINT executable param1 param2
        
        ```
        FROM golang:1.18-alpine
        RUN mkdir /app/
        COPY main.go /app/
        
        EXPOSE 8080
        
        ENTRYPOINT ["go", "run"]
        CMD ["/app/main.go"]
        ```
    2) contoh
        ```
        docker build -t widiarrohman/entrypoint entrypoint
        ```
        ```
        docker container create --name entrypoint -p 8080:8080 widiarrohman/entrypoint
        ```
        ```
        docker container start entrypoint
        ```

18.	Multi stage build
    ```
    FROM golang:1.18-alpine as builder
    WORKDIR /app/
    COPY main.go /app/
    RUN go build -o /app/main /app/main.go
    
    FROM alpine:3
    WORKDIR /app/
    COPY --from=builder /app/main /app/
    CMD /app/main
    ```
    ```
    docker build -t widiarrohman/multi multi
    docker container create --name multi -p 8080:8080 widiarrohman/multi
    docker container start multi
    ```

19.	Docker hub registry
    ```
    docker push widiarrohman/multi
    ```

20.	Digital Ocean Container Registry
    > tidak mengikuti karena meminta kartu kredit
    
21.	Selesai

---
## C. DOCKER COMPOSE
1.	Membuat container
    version: "3.8"
    
    ```
    services:
      nginx-example:
        container_name: nginx-example
        image: nginx:latest
    ```
    
    ```
    docker compose create
    ```
    > harus berada didalam satu folder yang terdapat file docker-compose.yaml

2.	Menjalankan container
    ```
    docker compose start
    ```
    > hanya container yang berada didalam folder

3.	Melihat container
    * melihat semua container, baik yang dibuat compose dll
    Tapi ???
        ```
        Docker compose ls
        ```
    * hanya akan melihat 1 docker compose saja
        ```
        docker compose ps
        ```

4.	Menghentikan container menggunakan compose
    * hanya mengentikan saja, tidak menghapus container
        ```
        Docker compose stop
        ```

5.	Menghapus container
    * menghapus semua container didalam konfigurasi docker-compose.yaml
        ```
        Docker compose down
        ```

6.	Project name
    * melihat docker compose yang sedang berjalan
    ```
    Docker compose ls
    ```

7.	Service
    ```
    version: "3.8"
    services:
      nginx-example:
        container_name: nginx-example
        image: nginx:latest
        container_name: nginx-example
      mongodb-example:
        image: mongo:latest
        container_name: mongodb-example
    ```
    * akan membuat 2 container sekaligus
    ```
    Docker compose create
    Docker compose start
    ```

8.	Komentar
    ```
    # digunakan  untuk komentar
    ```

9.	Ports
    ```
    Short syntax = port HOST:CONTAINER
    Long syntax = 
    	target = port didalam container
    	published = port yang digunakan di host
    	protocol = protocol port (tcp atau udp)
    version: "3.8"
    
    services:
      #this is nginx example
      nginx-port1:
        container_name: nginx-port1
        image: nginx:latest
        ports:
          - protocol: tcp
            published: 8080
            target: 80
    
      #this is mongodb example
      nginx-port2:
        image: nginx:latest
        container_name: nginx-port2
        ports:
          - "8081:80"
    ```

    ```
    Docker compose create
    Docker compose start
    Docker compose ps
    ```
 

10.	Environment Variable
    ```
    version: "3.8"
    
    services:
      #this is nginx example
      mongodb-example:
        container_name: mongodb-example
        image: mongo:latest
        ports:
          - "27017:27017"
        environment:
          MONGO_INITDB_ROOT_USERNAME: widi
          MONGO_INITDB_ROOT_PASSWORD: widi
          MONGO_INITDB_DATABASE: admin
    ```
    * aplikasi Studio 3T for MongoDB
    ```
    Docker compose create
    Docker compose start
    ```

11.	Bind Mount

    1).	Short syntax
    
        ```
        SOURCE:TARGET:MODE
        Source = lokasi di host
        Target = lokasi di container
        Mode = ro untuk readonly, rw untuk read write (default)
        version: "3.8"
        
        services:
          mongodb1:
            image: mongo:latest
            container_name: mongodb1
            ports:
              - "27017:27017"
            environment:
              MONGO_INITDB_ROOT_USERNAME: widi
              MONGO_INITDB_ROOT_PASSWORD: widi
              MONGO_INITDB_DATABASE: admin
            volumes:
              - "./data-mongo1:/data/db"
        ```
        ```
        Docker compose create
        Docker compose start
        ```
 
    2.	Long syntax
    
        * `type` = tipe mount, volume atau bind.
        * `source` = sumber path di host atau nama volume
        * `target` = target path di container
        * `read_only` = defaultnya adalah false
        
        ```
        version: "3.8"
        services:
          mongodb1:
            image: mongo:latest
            container_name: mongodb1
            ports:
              - "27017:27017"
            environment:
              MONGO_INITDB_ROOT_USERNAME: widi
              MONGO_INITDB_ROOT_PASSWORD: widi
              MONGO_INITDB_DATABASE: admin
            volumes:
              - "./data-mongo1:/data/db"
        
          mongodb2:
            image: mongo:latest
            container_name: mongodb2
            ports:
              - "27018:27017"
            environment:
              MONGO_INITDB_ROOT_USERNAME: widi
              MONGO_INITDB_ROOT_PASSWORD: widi
              MONGO_INITDB_DATABASE: admin
            volumes:
              - type: "./data-mongo2"
                target: "/data/db"
                read_only: false
        ```
        
        ```
        Docker compose create
        Docker compose start
        ```
 

12.	Docker compose volume
    ```
    version: "3.9"
    services:
      mongodb1:
        image: mongo:latest
        container_name: mongodb1
        ports:
          - "27017:27017"
        environment:
          MONGO_INITDB_ROOT_USERNAME: widi
          MONGO_INITDB_ROOT_PASSWORD: widi
          MONGO_INITDB_DATABASE: admin
        volumes:
          - "mongo-data1:/data/db"
    
      mongodb2:
        image: mongo:latest
        container_name: mongodb2
        ports:
          - "27018:27017"
        environment:
          MONGO_INITDB_ROOT_USERNAME: widi
          MONGO_INITDB_ROOT_PASSWORD: widi
          MONGO_INITDB_DATABASE: admin
        volumes:
          - type: volume
            source: mongo-data2
            target: "/data/db"
            read_only: false
    volumes:
      mongo-data1:
        name: mongo-data1
      mongo-data2:
        name: mongo-data2
    ``` 
    * jika compose dihapus maka volume tidak terhapus, untuk menjaga dari kesalahan pengguna.
    * jika ingin menghapus volume, maka lakukan secara manual dengan `docker volume rm mongo-data1`

13.	Network
    * name: nama network
    * driver: (bridge, host atau none)
    
    ```
    version: "3.8"
    services:
      mongodb1:
        image: mongo:latest
        container_name: mongodb1
        ports:
          - "27017:27017"
        environment:
          MONGO_INITDB_ROOT_USERNAME: widi
          MONGO_INITDB_ROOT_PASSWORD: widi
          MONGO_INITDB_DATABASE: admin
        networks:
          - network_example
    
    networks:
      network_example:
        name: network_example
        driver: bridge
    ```
    
    ```
    docker compose create
    docker compose start
    docker container inspect mongodb-example
     
    docker network ls
    ```

14.	Depends on

    ```
    version: '3.8'
    services:
      mongodb-example:
        image: mongo:latest
        container_name: mongodb-example
        ports:
          - "27017:27017"
        environment:
          MONGO_INITDB_ROOT_USERNAME: root
          MONGO_INITDB_ROOT_PASSWORD: example
          MONGO_INITDB_DATABASE: admin
        networks:
          - network_example
    
      mongodb-express-example:
        image: mongo-express:latest
        container_name: mongodb-express-example
        depends_on:
          - mongodb-example
        ports:
          - "8081:8081"
        environment:
          ME_CONFIG_MONGODB_ADMINUSERNAME: root
          ME_CONFIG_MONGODB_ADMINPASSWORD: example
          ME_CONFIG_MONGODB_SERVER: mongodb-example
        networks:
          - network_example
    
    networks:
      network_example:
        name: network_example
        driver: bridge
    ```
    ```
    docker compose create
    docker compose start
    docker compose ps
    ```

15.	Restart
    - `no`: defaultnya tidak pernah restart
    - `always`: selalu direstart jika container berhenti
    - `on-failure`: restart jika container error dengan indikasi error ketika exit
    - `unless-stopped`: selalu restart container, kecuali ketika dihentikan manual
    
    ```
    version: '3.8'
    services:
      mongodb-example:
        image: mongo:latest
        container_name: mongodb-example
        ports:
          - "27017:27017"
        environment:
          MONGO_INITDB_ROOT_USERNAME: root
          MONGO_INITDB_ROOT_PASSWORD: example
          MONGO_INITDB_DATABASE: admin
        networks:
          - network_example
    
      mongodb-express-example:
        image: mongo-express:latest
        container_name: mongodb-express-example
        restart: always
        depends_on:
          - mongodb-example
        ports:
          - "8081:8081"
        environment:
          ME_CONFIG_MONGODB_ADMINUSERNAME: root
          ME_CONFIG_MONGODB_ADMINPASSWORD: example
          ME_CONFIG_MONGODB_SERVER: mongodb-example
        networks:
          - network_example
    
    networks:
      network_example:
        name: network_example
        driver: bridge
    ```
    
    *   untuk menghapus sebelumnya gunakan perintah
        ```
        docker compose down
        docker volume prune
        ```
    *   kemudian
        ```
        docker compose create
        docker compose start
        docker container logs mongodb-express-example
        ```
    *   cek localhost:8081 dan 27017

16.	Monitor docker events
    ```
    docker events --filter 'container=mongodb-express-example'
    ```

17.	Resource limit
    ```
    deploy:
      resources:
        reservations:
          cpus: "0.25"
          memory: 50M
        limits:
          cpus: "0.5"
          memory: 100M
    ```
    ```
    docker compose create
    docker compose start
    docker container stats #monitoring resource
    ```

18.	Build Dockerfile

    ```
    version: "3.8"
    services:
      app:
        container_name: app
        build:
          context: "./app"
          dockerfile: Dockerfile
        image: "app-golang:1.0.0"
        environment:
          - "APP_PORT=8080"
        ports:
          - "8080:8080"
    ```
    
    ```
    docker compose build
    docker image ls
    docker compose create
    docker compose start
    ```
19.	Menghapus image
    ```
    docker compose down
    docker image rm app-golang:1.0.0
    ```
20.	Build ulang
    
    ketika ada update program, maka tidak bisa langsung hot reload. Harus hapus compose kemudian buat dan jalankan.
    ```
    docker compose down
    docker compose create
    docker compose start
    ```

21.	Health Check
    - `test`: berisikan cara melakukan test health check
    - `interval`: interval melakukan health check
    - `timeout`: timeout melakukan health check
    - `restries`: total retry ketika gagal
    - `start_periode`: waktu memulai melakukan health check
    -
    ```
    version: "3.8"
    services:
      app:
        container_name: app
        build:
          context: "./app"
          dockerfile: Dockerfile
        image: "app-golang:1.0.0"
        environment:
          - "APP_PORT=8080"
        ports:
          - "8080:8080"
        healthcheck:
          test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
          interval: 5s
          timeout: 5s
          retries: 3
          start_period: 5s
    ```
    ```
    docker compose build
    docker compose create
    docker compose start
    docker container ls
    ```

22.	Extend service

    untuk menjalankan compose yang namanya bukan docker-compose.yaml
    docker-compose.yaml
    ```
    docker compose -f prod.yaml create 
    ```
    ```
    version: "3.9"
    
    services:
      app:
        container_name: app
        build:
          context: "./app"
          dockerfile: Dockerfile
        image: "app-golang:1.0.0"
        environment:
          - "APP_PORT=8080"
        ports:
          - "8080:8080"

    prod.yaml 
    version: "3.9"
    
    services:
      app:
        environment:
          - "MODE=prod"
    
    Local.yaml
    version: "3.9"
    
    services:
      app:
        environment:
          - "MODE=local"
    
    
    dev.yaml 
    version: "3.9"
    
    services:
      app:
        environment:
          - "MODE=dev"
    ```
    * untuk server produksi
        ```
        docker compose -f docker-compose.yaml -f prod.yaml create
        docker compose -f docker-compose.yaml -f prod.yaml start
        ```
    
    * untuk serving developer
        ```
        docker compose -f docker-compose.yaml -f dev.yaml create
        docker compose -f docker-compose.yaml -f dev.yaml start
        ```
    
    * untuk local
        ```
        docker compose -f docker-compose.yaml -f local.yaml create
        docker compose -f docker-compose.yaml -f local.yaml start
        ```

23.	Selesai
