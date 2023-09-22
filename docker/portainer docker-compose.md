# Install Portainer dengan docker compose

- root@vps-sidafa:/home/sidafa# mkdir docker
- root@vps-sidafa:/home/sidafa# cd docker
- root@vps-sidafa:/home/sidafa/docker# mkdir portainer
- root@vps-sidafa:/home/sidafa/docker# cd portainer/
- root@vps-sidafa:/home/sidafa/docker/portainer# nano docker-compose.yml

```
version: '3'

services:
  portainer:
    image: portainer/portainer-ee:latest
    container_name: portainer
    restart: always
    ports:
      - "8000:8000"
      - "9443:9443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data

volumens:
  portainer_data:
```
- root@vps-sidafa:/home/sidafa/docker/portainer# docker-compose up -d
