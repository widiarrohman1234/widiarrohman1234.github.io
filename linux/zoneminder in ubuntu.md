# Instalasi & Configuration Zone Minder in Ubuntu
Zoneminder is application for monitoring CCTV

## Instalastion with Docker image
```Docker
docker run -d -t -p 1080:80 \
    -e TZ='Europe/London' \
    -v ~/zoneminder/events:/var/cache/zoneminder/events \
    -v ~/zoneminder/images:/var/cache/zoneminder/images \
    -v ~/zoneminder/mysql:/var/lib/mysql \
    -v ~/zoneminder/logs:/var/log/zm \
    --shm-size="512m" \
    --name zoneminder \
    zoneminderhq/zoneminder:latest-ubuntu18.04
```

for more information, please visit this page: [https://hub.docker.com/r/zoneminderhq/zoneminder](https://hub.docker.com/r/zoneminderhq/zoneminder)

## Enable authentication user login to Zoneminder
1. on the menu above, click `Option`
2. on menu list in right, select `System`
3. on list configuration, select `OPT_USE_AUTH` and enable `Authenticate user logins to ZoneMinder (?)`

after this configuration, you will be logged out. and enter username and password to log back in. and the configuration is successful