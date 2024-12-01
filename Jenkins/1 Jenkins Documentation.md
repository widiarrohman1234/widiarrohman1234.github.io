# Instalasi
1. Buat file docker compose
`docker-compose.yaml`
```yaml
version: '3.8'

services:
  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins
    restart: always
    ports:
      - "8080:8080"  # Port untuk akses web Jenkins
      - "50000:50000"  # Port untuk Jenkins slave agent
    volumes:
      - jenkins_home:/var/jenkins_home  # Volume untuk penyimpanan data Jenkins
    environment:
      - JAVA_OPTS=-Djenkins.install.runSetupWizard=false  # Opsional: untuk menonaktifkan setup wizard
    networks:
      - jenkins_network

volumes:
  jenkins_home:  # Mendefinisikan volume untuk penyimpanan data Jenkins

networks:
  jenkins_network:
    driver: bridge

```
2. jalankan
```
docker-compose up -d
```
3. check
```
http://localhost:8080
```
4. Unlock Jenkins
```
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```



