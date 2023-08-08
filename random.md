# Random
## AWS Linux error and solution
- log code deploy agent
```
sudo cat /var/log/aws/codedeploy-agent/codedeploy-agent.log
```

- error `sh: /home/ec2-user/sidafa-be-hapi/node_modules/.bin/nodemon: Permission denied`

    - Solusi
        ```
        sudo chmod 777 -R /home/ec2-user/sidafa-be-hapi
        ```

- error `return process.dlopen(module, path.toNamespacedPath(filename));`
    - solusi (/home/ec2-user/sidafa-be-hapi)
    ```
    rm -rf node_modules/
    npm update
    ```

## Kerjaan-PostgreSQL
create table and SEQUENCE
```
-- drop table jika ada
DROP TABLE IF EXISTS summary_performance;

-- buat table
CREATE TABLE summary_performance (
    id bigint PRIMARY KEY,
    date_only date,
    id_vendor integer,
    id_agent integer,
    id_product integer,
    status integer,
    under_10 integer,
    under_60 integer,
    under_180 integer,
    above_180 integer,
    created_at TIMESTAMP 
);

ALTER TABLE summary_performance
ALTER COLUMN created_at SET DEFAULT CURRENT_TIMESTAMP;

-- Membuat sequence baru
CREATE SEQUENCE summary_performance_id_seq START WITH 1 INCREMENT BY 1;

-- Mengupdate kolom new_id dengan nilai yang di-generate dari sequence
UPDATE summary_performance SET id = nextval('summary_performance_id_seq');

-- Menghapus constraint dan sequence yang ada pada kolom id
ALTER TABLE summary_performance DROP CONSTRAINT summary_performance_pkey;
ALTER SEQUENCE summary_performance_id_seq OWNED BY NONE;

-- Menambahkan kembali constraint pada kolom id
ALTER TABLE summary_performance ADD PRIMARY KEY (id);

-- Menyetel sequence sebagai default value untuk kolom id
ALTER SEQUENCE summary_performance_id_seq OWNED BY summary_performance.id;
ALTER TABLE summary_performance ALTER COLUMN id SET DEFAULT nextval('summary_performance_id_seq');

-- Input data
INSERT INTO summary_performance (date_only, id_vendor, id_agent, id_product, status, under_10, under_60, under_180, above_180)
VALUES
    ('2023-06-01', 1, 101, 201, 1, 5, 15, 30, 10),
    ('2023-06-02', 2, 102, 202, 2, 8, 18, 35, 12),
    ('2023-06-03', 3, 103, 203, 1, 2, 10, 25, 8);
```
- truncate
    ```
    TRUNCATE TABLE summary_performance;
    ```
    
- delete data by date_only
    ```
    DELETE FROM summary_performance WHERE date_only = '2023-04-15';
    ```


# Catatan belajar dari Pak Fauzan
- Vue good table next: https://borisflesch.github.io/vue-good-table-next/guide/
- Sequelize: https://sequelize.org/docs/v6/core-concepts/model-querying-basics/


```
@if(env('APP_ENV', 'dev') === 'dev')
    <h1>Status server DEV</h1>
@elseif(env('APP_ENV', 'dev') === 'testing')
    <h1>Status server TESTING</h1>
@elseif(env('APP_ENV', 'dev') === 'main')
    <h1>Status server MAIN</h1>
@endif
```
```
mysql -h ec2-13-213-1-6.ap-southeast-1.compute.amazonaws.com -P3306 -u root -p
mysql -h 172.31.18.34 -P3306 -u root -p

sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
172.31.18.34

GRANT ALL PRIVILEGES ON *.* TO 'root'@'ip-172-31-31-41.ap-southeast-1.compute.internal' IDENTIFIED BY 'jkasjvsern' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'ip-172-31-31-41.ap-southeast-1.compute.internal' IDENTIFIED BY 'password' WITH GRANT OPTION;


mysql -h 172.31.18.34 -P3306 -u aws-client-mysql -p
aws-client-mysql
Gp()kZzgl7Q6hrzr

DROP USER 'aws-client-mysql'@'%';
CREATE USER 'aws-client-mysql'@'%' IDENTIFIED WITH caching_sha2_password BY 'Gp()kZzgl7Q6hrzr';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, FILE, INDEX, ALTER, CREATE TEMPORARY TABLES, CREATE VIEW, EVENT, TRIGGER, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EXECUTE ON *.* TO 'aws-client-mysql'@'%';
ALTER USER 'aws-client-mysql'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

aws-user-waw
q9R4B)OWm3/ERBTt
CREATE USER 'aws-user-waw'@'%' IDENTIFIED WITH caching_sha2_password BY 'q9R4B)OWm3/ERBTt';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, FILE, INDEX, ALTER, CREATE TEMPORARY TABLES, CREATE VIEW, EVENT, TRIGGER, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EXECUTE ON *.* TO 'aws-user-waw'@'%';
ALTER USER 'aws-user-waw'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;CREATE DATABASE IF NOT EXISTS `aws-user-waw`;
GRANT ALL PRIVILEGES ON `aws-user-waw`.* TO 'aws-user-waw'@'%';

CREATE USER 'nama_pengguna'@'host' IDENTIFIED BY 'pasasf!2A*word';
GRANT ALL PRIVILEGES ON aws-user-waw.* TO 'aws-user-waw'@'host';
FLUSH PRIVILEGES;
```

merubah .md menjadi .html
```
pandoc -f markdown -t html nama_file.md -o nama_file.html
```

# lokasi folder WSL windows 11
```
\\wsl$
```


