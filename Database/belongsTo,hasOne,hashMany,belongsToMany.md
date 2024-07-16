Mari kita lihat setiap jenis relasi dengan contoh yang lebih detail dan spesifik.

### 1. `belongsTo`
Contoh: Data `Product` yang hanya memiliki satu `Category`.

```javascript
// product.js
module.exports = (sequelize, DataTypes) => {
  const Product = sequelize.define('Product', {
    name: DataTypes.STRING
  });

  Product.associate = function(models) {
    Product.belongsTo(models.Category, {
      foreignKey: 'categoryId',
      as: 'category'
    });
  };

  return Product;
};

// category.js
module.exports = (sequelize, DataTypes) => {
  const Category = sequelize.define('Category', {
    name: DataTypes.STRING
  });

  Category.associate = function(models) {
    Category.hasMany(models.Product, {
      foreignKey: 'categoryId',
      as: 'products'
    });
  };

  return Category;
};
```
Penjelasan: `Product` memiliki satu `Category`, jadi kita menggunakan `belongsTo`. Di sisi `Category`, kita menggunakan `hasMany` untuk menunjukkan bahwa satu `Category` dapat memiliki banyak `Product`.

### 2. `hasOne`
Contoh: Data `User` dan `UserDetail`, artinya satu data `User` hanya memiliki satu `UserDetail`.

```javascript
// user.js
module.exports = (sequelize, DataTypes) => {
  const User = sequelize.define('User', {
    name: DataTypes.STRING
  });

  User.associate = function(models) {
    User.hasOne(models.UserDetail, {
      foreignKey: 'userId',
      as: 'userDetail'
    });
  };

  return User;
};

// userDetail.js
module.exports = (sequelize, DataTypes) => {
  const UserDetail = sequelize.define('UserDetail', {
    address: DataTypes.STRING,
    phoneNumber: DataTypes.STRING
  });

  UserDetail.associate = function(models) {
    UserDetail.belongsTo(models.User, {
      foreignKey: 'userId',
      as: 'user'
    });
  };

  return UserDetail;
};
```
Penjelasan: `User` memiliki satu `UserDetail`, jadi kita menggunakan `hasOne`. Di sisi `UserDetail`, kita menggunakan `belongsTo` untuk menunjukkan bahwa `UserDetail` milik satu `User`.

### 3. `hasMany`
Contoh: Satu `Author` bisa menulis banyak `Book`.

```javascript
// author.js
module.exports = (sequelize, DataTypes) => {
  const Author = sequelize.define('Author', {
    name: DataTypes.STRING
  });

  Author.associate = function(models) {
    Author.hasMany(models.Book, {
      foreignKey: 'authorId',
      as: 'books'
    });
  };

  return Author;
};

// book.js
module.exports = (sequelize, DataTypes) => {
  const Book = sequelize.define('Book', {
    title: DataTypes.STRING
  });

  Book.associate = function(models) {
    Book.belongsTo(models.Author, {
      foreignKey: 'authorId',
      as: 'author'
    });
  };

  return Book;
};
```
Penjelasan: `Author` dapat menulis banyak `Book`, jadi kita menggunakan `hasMany`. Di sisi `Book`, kita menggunakan `belongsTo` untuk menunjukkan bahwa `Book` ditulis oleh satu `Author`.

### 4. `belongsToMany`
Contoh: `Student` dan `Course` memiliki hubungan banyak-ke-banyak melalui tabel perantara `StudentCourses`.

```javascript
// student.js
module.exports = (sequelize, DataTypes) => {
  const Student = sequelize.define('Student', {
    name: DataTypes.STRING
  });

  Student.associate = function(models) {
    Student.belongsToMany(models.Course, {
      through: 'StudentCourses',
      as: 'courses',
      foreignKey: 'studentId'
    });
  };

  return Student;
};

// course.js
module.exports = (sequelize, DataTypes) => {
  const Course = sequelize.define('Course', {
    title: DataTypes.STRING
  });

  Course.associate = function(models) {
    Course.belongsToMany(models.Student, {
      through: 'StudentCourses',
      as: 'students',
      foreignKey: 'courseId'
    });
  };

  return Course;
};

// studentCourses.js (junction table)
module.exports = (sequelize, DataTypes) => {
  const StudentCourses = sequelize.define('StudentCourses', {
    studentId: {
      type: DataTypes.INTEGER,
      references: {
        model: 'Students',
        key: 'id'
      }
    },
    courseId: {
      type: DataTypes.INTEGER,
      references: {
        model: 'Courses',
        key: 'id'
      }
    }
  });

  return StudentCourses;
};
```
Penjelasan: `Student` dapat mengambil banyak `Course`, dan `Course` dapat diambil oleh banyak `Student`. Hubungan ini diatur melalui tabel perantara `StudentCourses`. 

Dengan contoh-contoh ini, Anda dapat melihat bagaimana berbagai jenis relasi digunakan untuk menggambarkan hubungan antara model dalam Sequelize.