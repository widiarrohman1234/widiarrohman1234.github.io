# Instalasi Hapi.js dan CRUD sederhana MySQL
## A. membuat package.json
Ini akan membuat file package.json yang akan berisi informasi tentang proyek Anda dan dependensi yang akan diinstal.
```
npm init
```

jika setelah melakukan clone maka jalankan perintah berikut untuk menginstall package
```
npm install
```

## B. install Hapi.js
```
npm install @hapi/hapi
```

## C. index.js
```
const Hapi = require('@hapi/hapi');

const init = async () => {
  const server = Hapi.server({
    port: 3000,
    host: 'localhost'
  });

  // Tambahkan rute atau pengaturan server lainnya disini
  server.route({
    method: "GET",
    path: "/",
    handler: (request, h) => {
      return "Hello world";
    },
  });

  await server.start();
  console.log('Server berjalan di', server.info.uri);
};

process.on('unhandledRejection', (err) => {
  console.log(err);
  process.exit(1);
});

init();

```

## D. Running
```
node index.js
```

## E. Nodemon
Lakukan instalasi
```
npm install --save-dev nodemon
```
update `package.json`
```
"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon index.js"
  },
```
jalankan
```
npm start
```

## F. Koneksi Hapi.js to MySQL
install packaage mysql
```
npm i mysql
```
add package
```
const mysql = require('mysql');
```
konfigurasi koneksi
```
const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "sidafa_testing",
});

connection.connect((err) => {
    if(err){
        console.error("Koneksi Ke database gagal:", err)
        process.exit(1)
    }
    console.log("Terhubung ke database MySQL")
})
```
## G. CRUD Hapi.js to MySQL
1. **getAll**
```
  // Get all user
  server.route({
    method: "GET",
    path: "/user",
    handler: (request, h) => {
      return new Promise((resolve, reject) => {
        connection.query("SELECT * FROM user", (error, results) => {
          if (error) {
            reject(
              h.response({
                status: "failed",
                message: "gagal get all data",
                data: error,
              })
            );
          } else {
            resolve(
              h.response({
                status: "success",
                message: "Berhasil get all data",
                data: results,
              })
            );
          }
        });
      });
    },
  });
```

2. **getById**
```
  // Get user by Id
  server.route({
    method: "GET",
    path: "/user/{id}",
    handler: (request, h) => {
      const userId = request.params.id;
      return new Promise((resolve, reject) => {
        connection.query(
          "SELECT * FROM user where id=?",
          [userId],
          (error, results) => {
            if (error) {
              reject(error);
            } else {
              resolve(
                h
                  .response({
                    status: "success",
                    message: "Berhasil get data by Id",
                    data: results[0],
                  })
                  .code(200)
              );
            }
          }
        );
      });
    },
  });
```

3. **addNewUser**
```
  // add new user
  server.route({
    method: "POST",
    path: "/user",
    handler: (request, h) => {
      const {
        id_pondok,
        id_santri,
        id_kamar,
        username,
        email,
        password,
        level1,
        level2,
        status,
      } = request.payload;
      return new Promise((resolve, reject) => {
        connection.query(
          "INSERT INTO user (id_pondok,id_santri,id_kamar,username,email,password,level1,level2,status) VALUES (?,?,?,?,?,?,?,?,?)",
          [
            id_pondok,
            id_santri,
            id_kamar,
            username,
            email,
            password,
            level1,
            level2,
            status,
          ],
          (error, results) => {
            if (error) {
              console.log(error);
              reject(error);
            } else {
              resolve(
                h
                  .response({
                    status: "success",
                    message: "success create new data",
                    data: {
                      id: results.insertId,
                      id_pondok,
                      id_santri,
                      id_kamar,
                      username,
                      email,
                      password,
                      level1,
                      level2,
                      status,
                    },
                  })
                  .code(200)
              );
            }
          }
        );
      });
    },
  });
```
4. **editById**
```
  // edit user by id
  server.route({
    method: "PUT",
    path: "/user/{id}",
    handler: (request, h) => {
      const userId = request.params.id;
      const {
        id_pondok,
        id_santri,
        id_kamar,
        username,
        email,
        password,
        level1,
        level2,
        status,
      } = request.payload;
      return new Promise((resolve, reject) => {
        connection.query(
          "UPDATE user SET id_pondok=?,id_santri=?,id_kamar=?,username=?,email=?,password=?,level1=?,level2=?,status=? where id=?",
          [
            id_pondok,
            id_santri,
            id_kamar,
            username,
            email,
            password,
            level1,
            level2,
            status,
            userId,
          ],
          (error, results) => {
            if (error) {
              reject(error);
            } else {
              resolve(
                h
                  .response({
                    status: "success",
                    message: "success update data",
                    data: {
                      id: results.insertId,
                      id_pondok,
                      id_santri,
                      id_kamar,
                      username,
                      email,
                      password,
                      level1,
                      level2,
                      status,
                    },
                  })
                  .code(200)
              );
            }
          }
        );
      });
    },
  });
```
5. **deleteById**
```
  //delete user by id
  server.route({
    method: "DELETE",
    path: "/user/{id}",
    handler: (request, h) => {
      const userId = request.params.id;
      return new Promise((resolve, reject) => {
        connection.query("DELETE FROM user WHERE id = ?", [userId], (error) => {
          if (error) {
            reject(error);
          } else {
            resolve(
              h
                .response({
                  status: "success",
                  message: "Berhasil hapus data",
                  data: {
                    userId: userId,
                  },
                })
                .code(200)
            );
          }
        });
      });
    },
  });
```
## G. Full Code
```
const Hapi = require("@hapi/hapi");
const mysql = require("mysql");

const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "sidafa_testing",
});

connection.connect((err) => {
  if (err) {
    console.error("Koneksi Ke database gagal:", err);
    process.exit(1);
  }
  console.log("Terhubung ke database MySQL");
});

const init = async () => {
  const server = Hapi.server({
    port: 5000,
    host: "localhost",
  });

  // Tambahkan rute atau pengaturan server lainnya disini
  // Hello world
  server.route({
    method: "GET",
    path: "/",
    handler: (request, h) => {
      return "Hello world";
    },
  });

  // Get all user
  server.route({
    method: "GET",
    path: "/user",
    handler: (request, h) => {
      return new Promise((resolve, reject) => {
        connection.query("SELECT * FROM user", (error, results) => {
          if (error) {
            reject(
              h.response({
                status: "failed",
                message: "gagal get all data",
                data: error,
              })
            );
          } else {
            resolve(
              h.response({
                status: "success",
                message: "Berhasil get all data",
                data: results,
              })
            );
          }
        });
      });
    },
  });

  // Get user by Id
  server.route({
    method: "GET",
    path: "/user/{id}",
    handler: (request, h) => {
      const userId = request.params.id;
      return new Promise((resolve, reject) => {
        connection.query(
          "SELECT * FROM user where id=?",
          [userId],
          (error, results) => {
            if (error) {
              reject(error);
            } else {
              resolve(
                h
                  .response({
                    status: "success",
                    message: "Berhasil get data by Id",
                    data: results[0],
                  })
                  .code(200)
              );
            }
          }
        );
      });
    },
  });

  // add new user
  server.route({
    method: "POST",
    path: "/user",
    handler: (request, h) => {
      const {
        id_pondok,
        id_santri,
        id_kamar,
        username,
        email,
        password,
        level1,
        level2,
        status,
      } = request.payload;
      return new Promise((resolve, reject) => {
        connection.query(
          "INSERT INTO user (id_pondok,id_santri,id_kamar,username,email,password,level1,level2,status) VALUES (?,?,?,?,?,?,?,?,?)",
          [
            id_pondok,
            id_santri,
            id_kamar,
            username,
            email,
            password,
            level1,
            level2,
            status,
          ],
          (error, results) => {
            if (error) {
              console.log(error);
              reject(error);
            } else {
              resolve(
                h
                  .response({
                    status: "success",
                    message: "success create new data",
                    data: {
                      id: results.insertId,
                      id_pondok,
                      id_santri,
                      id_kamar,
                      username,
                      email,
                      password,
                      level1,
                      level2,
                      status,
                    },
                  })
                  .code(200)
              );
            }
          }
        );
      });
    },
  });

  // edit user by id
  server.route({
    method: "PUT",
    path: "/user/{id}",
    handler: (request, h) => {
      const userId = request.params.id;
      const {
        id_pondok,
        id_santri,
        id_kamar,
        username,
        email,
        password,
        level1,
        level2,
        status,
      } = request.payload;
      return new Promise((resolve, reject) => {
        connection.query(
          "UPDATE user SET id_pondok=?,id_santri=?,id_kamar=?,username=?,email=?,password=?,level1=?,level2=?,status=? where id=?",
          [
            id_pondok,
            id_santri,
            id_kamar,
            username,
            email,
            password,
            level1,
            level2,
            status,
            userId,
          ],
          (error, results) => {
            if (error) {
              reject(error);
            } else {
              resolve(
                h
                  .response({
                    status: "success",
                    message: "success update data",
                    data: {
                      id: results.insertId,
                      id_pondok,
                      id_santri,
                      id_kamar,
                      username,
                      email,
                      password,
                      level1,
                      level2,
                      status,
                    },
                  })
                  .code(200)
              );
            }
          }
        );
      });
    },
  });

  //delete user by id
  server.route({
    method: "DELETE",
    path: "/user/{id}",
    handler: (request, h) => {
      const userId = request.params.id;
      return new Promise((resolve, reject) => {
        connection.query("DELETE FROM user WHERE id = ?", [userId], (error) => {
          if (error) {
            reject(error);
          } else {
            resolve(
              h
                .response({
                  status: "success",
                  message: "Berhasil hapus data",
                  data: {
                    userId: userId,
                  },
                })
                .code(200)
            );
          }
        });
      });
    },
  });

  await server.start();
  console.log("Server running on", server.info.uri);
};

process.on("unhandledRejection", (err) => {
  console.log("error: ", err);
  process.exit(1);
});

init();

```

---
# H. Struktur folder Hapi.js
## 1. Struktur Sederhana
Struktur sederhana yang sering digunakan untuk project kecil.
```
- src/
  - controllers/
  - routes/
  - models/
  - services/
  - middlewares/
- config/
- test/
- public/
- server.js
```
- Folder `src/` : Biasanya digunakan untuk menyimpan kode sumber aplikasi Hapi.js.
  -  `controllers/`: Folder ini berisi file-file yang berfungsi sebagai pengendali atau kontroler yang menangani logika bisnis dan interaksi dengan permintaan HTTP.
  - `routes/`: Folder ini berisi file-file yang mendefinisikan rute-rute aplikasi, termasuk metode HTTP yang     digunakan dan penanganan permintaan.
  - `models/`: Folder ini berisi definisi model atau skema data yang digunakan dalam aplikasi.
  - `services/`: Folder ini berisi logika bisnis yang kompleks atau layanan tambahan yang digunakan oleh kontroler atau rute.
  - `middlewares/` untuk middleware aplikasi
 
- Folder `config/`: Biasanya digunakan untuk menyimpan konfigurasi aplikasi seperti pengaturan server, koneksi database, atau konfigurasi lainnya. File konfigurasi ini dapat dibagi menjadi beberapa file tergantung pada kebutuhan.
- `tests/` untuk unit tes
- Folder `public/`: Digunakan untuk menyimpan file-file statis seperti gambar, CSS, JavaScript, atau berkas-berkas publik lainnya yang dapat diakses secara langsung oleh klien.
- File `server.js`: File ini merupakan titik masuk utama untuk menjalankan server Hapi.js. Di dalamnya, Anda akan mengonfigurasi dan menjalankan server Hapi.js.

## 2. Struktur folder Hapi.js type flat
```
- controllers/
- routes/
- models/
- services/
- middlewares/
- tests/
- config/
- public/
- server.js
```

## 3. Struktur folder Hapi.js type modular
```
- modules/
  - module1/
    - controllers/
    - routes/
    - models/
    - services/
    - middlewares/
    - tests/
  - module2/
    - controllers/
    - routes/
    - models/
    - services/
    - middlewares/
    - tests/
- config/
- public/
- server.js
```

## 4. Struktur folder Hapi.js type Domain
```
- domain1/
  - controllers/
  - routes/
  - models/
  - services/
  - middlewares/
  - tests/
- domain2/
  - controllers/
  - routes/
  - models/
  - services/
  - middlewares/
  - tests/
- config/
- public/
- server.js
```