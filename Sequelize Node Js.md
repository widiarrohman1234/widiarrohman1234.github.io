# Sequelize Node Js
## 1. instalasi
`'pg'` digunakan sebagai driver database PostgreSQL.
```
npm install sequelize pg
```
## link referensi belajar
[sql-to-sequelize-mapping-chart](https://fengmk2.github.io/blog/2014/10/sql-to-sequelize-mapping-chart.html)

## 2. Konfigurasi Database
Buatlah file `config.js` atau `config.json`
```
module.exports = {
  development: {
    username: 'username',
    password: 'password',
    database: 'database_development',
    host: 'localhost',
    dialect: 'postgres',
  },
  testing: {
    username: 'username',
    password: 'password',
    database: 'database_testing',
    host: 'localhost',
    dialect: 'postgres',
  },
  production: {
    username: 'username',
    password: 'password',
    database: 'database_production',
    host: 'localhost',
    dialect: 'postgres',
  },
  // Konfigurasi lainnya seperti production, testing, dll.
};

```

## 3. Inisialisasi Sequelize
Buat file `sequelize.js` yang berfungsi untuk inisialisasi koneksi dan cek koneksi ke database.
```
const Sequelize = require('sequelize');
const config = require('./config');

// Inisialisasi koneksi
const sequelize = new Sequelize(config.development.database, config.development.username, config.development.password, {
  host: config.development.host,
  dialect: config.development.dialect,
});

// Cek koneksi ke database
module.exports = {
sequelize
  .authenticate()
  .then(() => {
    console.log('Koneksi ke database berhasil');
  })
  .catch((err) => {
    console.error('Koneksi ke database gagal:', err);
  });
}
```
## 4. Definisi model
Buat file `./models/UserModel.js` untuk mendefinisikan model data yang akan digunakan. Misalnya, model `User` dengan kolom `id` dan `name`.
```
const { DataTypes } = require('sequelize');
const sequelize = require('./path/to/sequelize');

const User = sequelize.define('User', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  name: {
    type: DataTypes.STRING,
    allowNull: false,
  },
});

// Sinkronisasi model dengan database
User.sync();
```
## 5. Operasi CRUD
```
const User = require('./models/UserModel');
// Create
User.create({ name: 'John Doe' }).then((user) => {
  console.log('User berhasil dibuat:', user.toJSON());
});

// Read
User.findAll().then((users) => {
  console.log('Daftar pengguna:', users.map((user) => user.toJSON()));
});

// Update
User.update({ name: 'Jane Doe' }, { where: { id: 1 } }).then((result) => {
  console.log('Jumlah baris yang terupdate:', result[0]);
});

// Delete
User.destroy({ where: { id: 1 } }).then((result) => {
  console.log('Jumlah baris yang dihapus:', result);
});
```
## 6. Struktur penyimpanan
```
- app/
  - models/
    - userModel.js
    - postModel.js
  - controllers/
    - userController.js
    - postController.js
  - routes/
    - userRoutes.js
    - postRoutes.js
- config/
  - config.js
- migrations/
  - 20220101000001-create-users.js
  - 20220101000002-create-posts.js
- seeders/
  - 20220101000001-demo-users.js
  - 20220101000002-demo-posts.js
- index.js
- package.json
```
## 7. Perintah Sequelize
- instalasi
```
$ npm install --save pg pg-hstore # Postgres
$ npm install --save mysql2
$ npm install --save mariadb
$ npm install --save sqlite3
$ npm install --save tedious # Microsoft SQL Server
$ npm install --save oracledb # Oracle Database
```
- membuat migrasi
```
npx sequelize-cli migration:generate --name create_summary_performance_table
```
- Isi `up` dan `down`
```
"use strict";

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable("summary_performance", {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.BIGINT,
      },
      date_only: { allowNull: false, type: Sequelize.DATEONLY },
      id_vendor: { allowNull: false, type: Sequelize.INTEGER },
      id_agent: { allowNull: false, type: Sequelize.INTEGER },
      id_product: { allowNull: false, type: Sequelize.INTEGER },
      status: { allowNull: false, type: Sequelize.INTEGER },
      under_10: { allowNull: false, type: Sequelize.INTEGER },
      under_60: { allowNull: false, type: Sequelize.INTEGER },
      under_180: { allowNull: false, type: Sequelize.INTEGER },
      above_180: { allowNull: false, type: Sequelize.INTEGER },
      created_at: {
        allowNull: false,
        type: Sequelize.DATE,
        defaultValue: Sequelize.literal("CURRENT_TIMESTAMP"),
      },
    });
  },

  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable("summary_performance");
  },
};
```
- menjalankan semua migrasi
```
npx sequelize-cli db:migrate
```
- menjalankan migrasi tertentu
```
npx sequelize-cli db:migrate --to 20230607021621-create_summary_performance_table
```
## 8. blah
