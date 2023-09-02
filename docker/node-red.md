# Cara instalasi Node-red menggunakan docker di linux

## 1. Instalasi menggunakan docker
```
docker run -it -p 1880:1880 -v node_red_data:/data --name nodered_1 nodered/node-red
```
## 2. buka firewall
```
ufw allow  1880
```

## 3. Akses node-red melalui browser
```
20.40.190.88:1880
```
> ganti dengan IP server atau localhost

## 4. Setting passwod pada node-red
1. step 1
    ```
    docker exec -it nodered_1 sh
    ```

2. step 2

    ```
    docker exec -it nodered_1 /bin/bash
    ```
3. Copy file `setting.js` agar memiliki bakcup

    ```
    cp /data/settings.js /data/settings.js.backup
    ```
4. step 4

    ```
    nano /data/settings.js
    ```
5. Buang garis miring pada:

    ```
    adminAuth: {
        type: "credentials",
        users: [{
            username: "admin",
            password: "$2a$08$zZWtXTja0fB1pzD4sHCMyOCMYz2Z6dNbM6tl8sJogENOMcxWV9DN.",
            permissions: "*"
        }]
    },
    ```
> ### username: `admin` password: `password`

5. Simpan pengaturan
    - `ctrl+x`
    - `y`
    - `enter`

5. restart docker
    ```
    docker restart nodered_1
    ```

5. (Opsional) tambahkan user baru
    ```
    docker exec -it nodered_1 /bin/bash
    ```
    ```
    node-red-admin hash-pw
    ```
    masukkan password, copy dan paste ke dalam file `/data/settings.js`
    ```
    adminAuth: {
        type: "credentials",
        users: [
        {
            username: "admin",
            password: "$2a$08$zZWtXTja0fB1pzD4sHCMyOCMYz2Z6dNbM6tl8sJogENOMcxWV9DN.",
            permissions: "*"
        },
        {
            username: "widi",
            password: "$2a$08$4dSq8lIBSjDvXDpUU4bex.WzPx3jMpT4dU62NNlG16K4EI4kZyQRe",
            permissions: "*"
        }
        ]
    },
    ```
5. simpan dan restart docker seperti step `5` dan `6`
5. Berhasil dan Selesai

