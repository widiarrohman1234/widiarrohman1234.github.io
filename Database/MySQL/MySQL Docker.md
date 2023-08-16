# MySQL With Docker

## install docker mysql
```
docker run -d --name mysql-1 -e MYSQL_ROOT_PASSWORD=your_password -p 3306:3306 mysql
```

## install phpmyadmin and auto connect to mysql docker
```
docker run --name phpmyadmin -d --link mysql-1:db -p 8080:80 phpmyadmin
```

## Akses MySQL dengan Docker Exec di terminal
```
docker exec -it mysql-1 mysql -u root -p
```
