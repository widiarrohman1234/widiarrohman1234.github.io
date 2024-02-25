JavaScript mendukung beberapa cara untuk menulis fungsi (functions). Berikut adalah beberapa cara umum untuk menuliskan fungsi dalam JavaScript:

### 1. **Deklarasi Fungsi (Function Declaration):**
   ```javascript
   function myFunction(parameter1, parameter2) {
     // Body of the function
     return parameter1 + parameter2;
   }
   ```

### 2. **Ekspresi Fungsi (Function Expression):**
   ```javascript
   const myFunction = function(parameter1, parameter2) {
     // Body of the function
     return parameter1 + parameter2;
   };
   ```

### 3. **Fungsi Panjang Penuh (Full Function Form):**
   ```javascript
   const myFunction = (parameter1, parameter2) => {
     // Body of the function
     return parameter1 + parameter2;
   };
   ```

### 4. **Fungsi Singkat (Shorter Function Form):**
   ```javascript
   const myFunction = (parameter1, parameter2) => parameter1 + parameter2;
   ```

### 5. **Fungsi Tanpa Parameter:**
   ```javascript
   function sayHello() {
     console.log('Hello!');
   }
   ```

### 6. **Fungsi Sebagai Metode:**
   ```javascript
   const myObject = {
     myMethod: function() {
       // Body of the method
     }
   };
   ```

### 7. **Fungsi Sebagai Metode Singkat:**
   ```javascript
   const myObject = {
     myMethod() {
       // Body of the method
     }
   };
   ```

### 8. **Fungsi Dalam Fungsi (Nested Functions):**
   ```javascript
   function outerFunction() {
     function innerFunction() {
       // Body of the inner function
     }

     innerFunction();
   }
   ```

### 9. **Fungsi Dengan Parameter Default:**
   ```javascript
   function greet(name = 'Guest') {
     console.log(`Hello, ${name}!`);
   }

   greet(); // Output: Hello, Guest!
   greet('John'); // Output: Hello, John!
   ```

### 10. **Fungsi Rest Parameters:**
   ```javascript
   function sum(...numbers) {
     return numbers.reduce((total, num) => total + num, 0);
   }

   console.log(sum(1, 2, 3, 4)); // Output: 10
   ```

### 11. **Fungsi Dengan Callback:**
   ```javascript
   function fetchData(callback) {
     // Fetch data from somewhere
     const data = 'Some data';
     callback(data);
   }

   fetchData((result) => {
     console.log(result);
   });
   ```

### 12. **Fungsi Dengan Promise:**
   ```javascript
   function fetchData() {
     return new Promise((resolve, reject) => {
       // Async operation
       const success = true;
       if (success) {
         resolve('Data fetched successfully');
       } else {
         reject('Error fetching data');
       }
     });
   }

   fetchData()
     .then((result) => console.log(result))
     .catch((error) => console.error(error));
   ```

Ini adalah beberapa cara umum untuk menulis fungsi dalam JavaScript. Pilihan cara penulisan fungsi tergantung pada konteks dan kebutuhan spesifik aplikasi atau proyek Anda.