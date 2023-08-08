# Instalasi PostgreSQL

## 1. Download
* [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
## 2. Daftarkan ke ENV
```
C:\Program Files\PostgreSQL\15\bin
```

## 3. Running
Jalankan di terminal
```
psql -U postgres
```
masukkan password yang pernah dibuat ketika pertama kali instalasi

## 4. Create user and connect to database
```
CREATE USER widi WITH PASSWORD 'password';
```
```
\c nama_database;
```
```
GRANT ALL PRIVILEGES ON DATABASE nama_database TO widi;
```
```
psql -U widi -d nama_database
```

# Query PostgreSQL
- Hanya tanggal
```
SELECT DATE('2023-04-15 10:45:54.502572+07') AS date_only;
```
> 2023-04-15 10:45:54.502572+07 => 2023-04-15

- Selisih perbedaan detik dari timestamp
```
DATE_PART('second', date_update - date_trans) AS time_difference_seconds,
```
- BEETWEEN TIMESTAP
```
where date_trans BETWEEN '2023-04-15 00:00:00' AND '2023-04-15 23:59:59'
```
