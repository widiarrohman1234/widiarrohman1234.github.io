To install PostgreSQL on Linux, you can follow these general steps:

Step 1: Update package lists
```
sudo apt update
```

Step 2: Install PostgreSQL
```
sudo apt install postgresql
```

Step 3: Verify the installation
```
psql --version
```

Step 4: Start the PostgreSQL service
```
sudo service postgresql start
```

By default, PostgreSQL creates a user named `postgres` with administrative privileges. You can access the PostgreSQL command-line interface using this user.

Step 5: Access the PostgreSQL shell
```
sudo -u postgres psql
```

Once you're in the PostgreSQL shell, you can interact with the database using SQL commands.

Note: The above steps assume you are using a Debian-based distribution such as Ubuntu. If you are using a different Linux distribution, the installation steps may vary slightly. Please refer to the official documentation or package manager specific to your distribution for the exact installation instructions.

Remember to secure your PostgreSQL installation by setting a strong password for the `postgres` user and configuring appropriate access controls based on your requirements.

---

# Menambahkan User

```
-- Membuat pengguna
-- 1 
CREATE USER "aws-user-waw" WITH PASSWORD 'q9R4B)OWm3/ERBTt';

-- 2 Memberikan hak akses
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, TRIGGER, USAGE ON ALL TABLES IN SCHEMA public TO "aws-user-waw";

--3
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO "aws-user-waw";

-- 4
CREATE DATABASE "aws-user-waw";

-- 5
GRANT ALL PRIVILEGES ON DATABASE "aws-user-waw" TO "aws-user-waw";
```

# File configuration
```
cd /etc/postgresql/14/main/postgresql.conf
```


