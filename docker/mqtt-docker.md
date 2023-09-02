# MQTT Docker

### 1. Install docker in ubuntu

### 2. Create folder mqtt
root@****:/home/widiarrohman1234# 

```    
mkdir mqtt-docker
cd mqtt-docker
mkdir config
cd config
nano mosquitto.conf
```

// mosquitto.conf
```
allow_anonymous false
listener 1883
listener 9001
protocol websockets
persistence true
password_file /mosquitto/config/pwfile
persistence_file mosquitto.db
persistence_location /mosquitto/data/
```
- save and exit: `ctrl+x` -> `y` -> `enter`

### 3. Create docker compose

```
root@*****:/home/*****/mqtt-docker/config# cd ..
root@*****:/home/*****/mqtt-docker#nano docker-compose.yml
```

docker-compose.yml
```

version: "3.7"
services:
  # mqtt5 eclipse-mosquitto
  mqtt5:
    image: eclipse-mosquitto
    container_name: mqtt5
    ports:
      - "1883:1883" #default mqtt port
      - "9001:9001" #default mqtt port for websockets
    volumes:
      - ./config:/mosquitto/config:rw
      - ./data:/mosquitto/data:rw
      - ./log:/mosquitto/log:rw

# volumes for mapping data,config and log
volumes:
  config:
  data:
  log:

networks:
  default:
    name: mqtt5-network
```
### 4. Create Docker compose

root@*****:/home/*****/mqtt-docker#
```
docker compose create
```

```

# login interactively into the mqtt container
root@VPS-1-Testing-WA:/home/widiarrohman1234/mqtt5# docker exec -it mqtt5 sh
/ # chmod 600 /mosquitto/config/pwfile
/ # chown root:root /mosquitto/config/pwfile
/ # mosquitto_passwd -c /mosquitto/config/pwfile mqtt_user1
Password:
Reenter password:
/ # exit
root@VPS-1-Testing-WA:/home/widiarrohman1234/mqtt5#
```

```
# delete user command format
mosquitto_passwd -D /mosquitto/config/pwfile <user-name-to-delete>
```

```
docker container restart mqtt5
```

```
sudo apt install mosquitto-clients
```

### Penerima
```
mosquitto_sub -v -t test/topic -u mqtt_user1 -P ******
```

### Pengirim
```
mosquitto_pub -L mqtt://mqtt_user1:****@103.175.219.171/test/topic -m "{humidity: 102.0}"
```


