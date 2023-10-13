# Dart OOP

## dasar-dasar OOP yang harus diketahui
A. Class
B. Object
C. Attribut dan Metode
D. Encapsulation
E. Inheritence
F. Polymorphism
G. Abstaction

## penamaan OOP
```
//PascalCase untuk penamaan class
class MyClass {
}

//camelCase untuk nama variable dan nama function/method
int myVariable;
void myFunction() {
  // ...
}

//UPPER_CASE untuk variable constanta
final int MAX_VALUE = 100;
```

## Object
```
class Person{
    String name;
    int age;
    
    Person(this.name, this.age);
}
```

## A. Class
```
class Person{ //class
    String name; //attribut
    int age;
    
    Person(this.name, this.age); //constructor
    
    void sayHello(){ // method/function
        print("Hello, my name is $name and I am $age years old");
    }
}
```
## B. Object
```
void main(){
    Person person1 = Person("Widi", 21); //object
    Person person2 = Person("Wira", 11);
    
    person1.sayHello();
    person2.sayHello();
}
```

## C. Attribut dan Metode
 sudah dijelaskan pada class
## D. Encapsulation
 Enkapsulasi adalah konsep dalam OOP yang menyembunyikan rincian internal suatu objek dari dunia luar dan membatasi akses ke bagian-bagian tertentu dari objek tersebut.
```
class BankAccount{
    double _balance = 0;
    
    void deposit(double amount){
        if(amount > 0){
            _balance += amount;
            print("Berhasil Deposit, Saldo anda: $_balance");
        } else {
            print("Invalid deposit");
        }
    }
    
    void withraw(double amount){
        if(amount > 0 && amount <= _balance){
            _balance -= amount;
            print("Withdraw successful, New balance: $_balance");
        }else{
            print("Insufficient balance or invalid withdrawal amount");
        }
    }
    
    double getBalance(){
        return _balance;
    }
}

void main(){
    BankAccount account = BankAccount();
    account.deposit(1000); //Berhasil Deposit, Saldo anda: 1000
    account.withraw(500); //Withdraw successful, New balance: 500
    account.withraw(800); //Insufficient balance or invalid withdrawal amount
    double balance = account.getBalance();
    print("Current balance: $balance"); //Current balance: 500
}
```
## E. Inheritence
```
class Animal{
    String name;
    int age;
    
    Animal(this.name, this.age);
    
    void makeSound(){
        print("Animal makes a sound");
    }
}

class Dog extends Animal{
    String breed;
    
    Dog(String name, int age, this.breed) : super(name, age);
    
    @override
    void makeSound(){
        print("Dog barks");
    }
}

void main(){
    Animal animal = Animal("Generic animal", 5);
    Dog dog = Dog("Buddy", 4,"Golden Retrivier");
    
    animal.makeSound(); //Animal makes a sound
    dog.makeSound(); //Dob barks
}
```


## F. Polymorphism
Polimorfisme adalah kemampuan suatu objek untuk memiliki banyak bentuk atau perilaku yang berbeda. 
```
class Cat extends Animal{
    Cat(String name, int age) : super(name, age);
    
    @override
    void makeSound(){
        print("Cat meows");
    }
}

void main(){
    Animal animal = Animal("Generic Animal", 5);
    Dog dog = Dog("Buddy", 2, "Golder Retriever");
    Cat cat = Cat("Whiskers", 3);
    
    animal.makeSound(); //Animal makes a sound
    dog.makeSound(); // Dog barks
    cat.makeSound(); // Cat meows
}
```
contoh lainnya:
```
class Employee{
    String name;
    Employee(this.name);
}

class Manager extends Employee{
    Manager(String name) : super(name);
}

class VicePrecident extends Employee{
    VicePrecident(String name) : super(name);
}

void sayHello(Employee employee){
    print('Hello ${employee.name}');
}

void main(){
    sayHello(Employee('Widi'));
    sayHello(Manager('Widi'));
    sayHello(VicePrecident('Widi'));
}
```

## G. Abstaction
```
// Abstract class representing authentication
abstract class Auth {
  Future<String> getToken(String username, String password);
}

// Concrete implementation of Auth using API
class ApiAuth implements Auth {
  @override
  Future<String> getToken(String username, String password) async {
    // Implement the API call to get the token here
    // For simplicity, we'll use hardcoded credentials and token
    if (username == "user" && password == "password") {
      // Simulate API call delay
      await Future.delayed(Duration(seconds: 2));
      return "some_secure_token";
    } else {
      return null;
    }
  }
}

class Screen {
  Auth _auth;
  String _token;

  Screen(this._auth, String username, String password);

  Future<bool> initialize() async {
    _token = await _auth.getToken(username, password);
    return _token != null;
  }

  bool isAuthorized() {
    return _token != null;
  }
}

class HomeScreen extends Screen {
  HomeScreen(Auth auth, String username, String password) : super(auth, username, password);

  Future<void> showHome() async {
    bool initialized = await initialize();
    if (initialized) {
      print("Welcome to HomeScreen!");
      // Perform your API operations using the token here
    } else {
      print("Authorization failed. Redirecting to login screen.");
      // Add your authorization failure handling logic here
    }
  }
}

class UserScreen extends Screen {
  UserScreen(Auth auth, String username, String password) : super(auth, username, password);

  Future<void> showUserProfile() async {
    bool initialized = await initialize();
    if (initialized) {
      print("Welcome to UserScreen!");
      // Perform your API operations using the token here
    } else {
      print("Authorization failed. Redirecting to login screen.");
      // Add your authorization failure handling logic here
    }
  }
}

class CartScreen extends Screen {
  CartScreen(Auth auth, String username, String password) : super(auth, username, password);

  Future<void> showCart() async {
    bool initialized = await initialize();
    if (initialized) {
      print("Welcome to CartScreen!");
      // Perform your API operations using the token here
    } else {
      print("Authorization failed. Redirecting to login screen.");
      // Add your authorization failure handling logic here
    }
  }
}

void main() {
  Auth auth = ApiAuth();
  String username = "user";
  String password = "password";

  HomeScreen homeScreen = HomeScreen(auth, username, password);
  UserScreen userScreen = UserScreen(auth, username, password);
  CartScreen cartScreen = CartScreen(auth, username, password);

  homeScreen.showHome();
  userScreen.showUserProfile();
  cartScreen.showCart();
}

```

## method extension (on)
Extension method adalah fitur yang memungkinkan kita menambahkan metode ke kelas yang sudah ada tanpa harus memodifikasi kode sumber asli dari kelas tersebut. 
```
class Person {
  String name;
  int age;

  Person(this.name, this.age);
}

// Membuat extension method untuk kelas Person
extension PersonExtension on Person {
  // Metode untuk menampilkan informasi person
  void displayInfo() {
    print("Name: ${this.name}, Age: ${this.age}");
  }

  // Metode untuk mengecek apakah person dewasa (usia di atas 18 tahun)
  bool isAdult() {
    return this.age >= 18;
  }
}

void main() {
  Person person1 = Person("John", 25);
  Person person2 = Person("Alice", 15);

  // Menggunakan extension method displayInfo() pada objek Person
  person1.displayInfo(); // Output: "Name: John, Age: 25"
  person2.displayInfo(); // Output: "Name: Alice, Age: 15"

  // Menggunakan extension method isAdult() pada objek Person
  bool isPerson1Adult = person1.isAdult();
  bool isPerson2Adult = person2.isAdult();

  print("Is person1 an adult? $isPerson1Adult"); // Output: "Is person1 an adult? true"
  print("Is person2 an adult? $isPerson2Adult"); // Output: "Is person2 an adult? false"
}

```

## constructor
```
class Person {
  String? name;
  int? age;
  
  // Default Constructor
  //Person() {
  //  print("Default Constructor");
  //}
  
  // Constructor dengan Parameter
  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }
  
  // Named Constructor
  Person.withName(String name) {
    this.name = name;
    this.age = 0;
  }

  Person.withAge(int age) {
    this.name = "Unknown";
    this.age = age;
  }
}

void main() {
  //var person = Person();
 
  var person = Person("John", 30);
  print("Name: ${person.name}, Age: ${person.age}"); // Output: "Name: John, Age: 30"
  
  var person1 = Person.withName("Alice");
  print("Name: ${person1.name}, Age: ${person1.age}"); // Output: "Name: Alice, Age: 0"

  var person2 = Person.withAge(25);
  print("Name: ${person2.name}, Age: ${person2.age}"); // Output: "Name: Unknown, Age: 25"
}

```

## redirect constructor
```
class Person {
  String? name;
  int? age;

  // Constructor dengan parameter
  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  // Redirect constructor ke constructor lain
  Person.withDefaultAge(String name) : this(name, 18);

  // Redirect constructor ke constructor lain
  Person.withDefaultName(int age) : this("Unknown", age);
}

void main() {
  var person1 = Person("John", 30);
  print("Name: ${person1.name}, Age: ${person1.age}"); // Output: "Name: John, Age: 30"

  var person2 = Person.withDefaultAge("Alice");
  print("Name: ${person2.name}, Age: ${person2.age}"); // Output: "Name: Alice, Age: 18"

  var person3 = Person.withDefaultName(25);
  print("Name: ${person3.name}, Age: ${person3.age}"); // Output: "Name: Unknown, Age: 25"
}
```

## initializer list
Initializer list adalah bagian dari sintaks Dart yang memungkinkan Anda melakukan inisialisasi awal pada atribut dalam kelas sebelum konstruktor utama dijalankan. Dengan menggunakan initializer list, Anda dapat memberikan nilai awal ke atribut kelas menggunakan ekspresi atau menginisialisasi atribut dengan hasil dari ekspresi atau fungsi.
```
class Rectangle {
  int width;
  int height;
  int area;

  // Initializer list
  Rectangle(int width, int height)
      : width = width,
        height = height,
        area = width * height {
    print("Initializer list executed.");
  }

  // Constructor tanpa initializer list
  Rectangle.withoutInitializer(int width, int height) {
    this.width = width;
    this.height = height;
    this.area = width * height;
    print("Constructor without initializer list executed.");
  }
}

void main() {
  Rectangle rectangle1 = Rectangle(5, 3);
  print("Area of rectangle1: ${rectangle1.area}"); // Output: "Area of rectangle1: 15"

  Rectangle rectangle2 = Rectangle.withoutInitializer(4, 6);
  print("Area of rectangle2: ${rectangle2.area}"); // Output: "Area of rectangle2: 24"
}

```

## constant constructor
Constant constructor adalah jenis constructor khusus dalam Dart yang digunakan untuk membuat objek yang memiliki nilai konstan
```
class Circle {
  final double radius;
  final double area;

  // Constant constructor
  const Circle(this.radius) : area = 3.14 * radius * radius;
}

void main() {
  const Circle circle1 = Circle(5.0);
  const Circle circle2 = Circle(7.0);

  print("Radius of circle1: ${circle1.radius}"); // Output: "Radius of circle1: 5.0"
  print("Area of circle1: ${circle1.area}");     // Output: "Area of circle1: 78.5"

  print("Radius of circle2: ${circle2.radius}"); // Output: "Radius of circle2: 7.0"
  print("Area of circle2: ${circle2.area}");     // Output: "Area of circle2: 153.86"
}

```

## factory contructor
Factory constructor adalah jenis constructor khusus dalam Dart yang bertanggung jawab untuk membuat dan mengembalikan objek dari kelas tanpa harus selalu membuat instance baru dari kelas tersebut. 
```
class Database{
    Database(){  
        print("Create new database");        
    }
    static Database database = Database();
    factory Database.get(){
        return database;
    }
}

void main(){
    var database1 = Database.get();
    var database2 = Database.get();
    print(database1 == database2);
}
```

## cascade notation
```
class User{
    String? username;
    String? name;
    String? email;
}

User? createUser(){
    return null;
}
void main(){
    var user = User()
     ..username = "widi331"
     ..name = "Widi Arrohman"
     ..email = "widiarrohman1234@gmai.com";

    User? user2 = createUser()
     ?..username = "widi331"
     ..name = "Widi Arrohman"
     ..email = "widiarrohman1234@gmai.com";
}
```

## Super keyword
```
class Shape{
    int getCorner(){
        return 0;
    }
}
class Rectangle extends Shape{
    int getCorner(){
        return 4;
    }
    
    int getParentCorner(){
        return super.getCorner();
    }
}
void main(){
    var rectangle = Rectangle();
    print(rectangle.getCorner()); //4
    print(rectangle.getParentCorner()); //0
}
```

## super constructor
```
class Person{
    String name;
    
    Person(this.name){
        print("Person constructor is called");
    }
}
class Employee extends Person{
    String department;
    Employee(String name, this.department) : super(name){
        print("Employee contructor is called");
    }
}

void main(){
    var person = Person("Wahida");
    print(person.name);
    
    Employee employee = Employee("widi", "HR");
    print(employee.name);
}
```

## Getter dan Setter
```
class Person{
    String _name = "";
    int _age = 0;
    
    set name(String value) => _name = value;
    
    String get name =>  _name;
    
    set age(int value){
        if(value > 0 ){
            _age = value;
        } else {
            print("Age must be a non-negative value.");
        }
    }
    
    int get age =>   _age;
}
void main(){
    Person person = Person();
    person.name = "Widi";
    person.age = 21;
    
    print("Name ${person.name}");
    print("Age ${person.age}");
}
```

## Interface
```dart
class Car {
  String name = "";
  void drive() {}

  int getTier() {
    return 0;
  }
}

abstract class HasBrand{
    String getBrand();
}

class Avanza implements Car, HasBrand {
  String name = "";
  String getBrand() => "Toyota";

  void drive() {
    print("Car is running");
  }

  int getTier() {
    return 4;
  }
}

void main(){
  Car avanza = Avanza();
  avanza.drive();
  print("Number or tiers: ${avanza.getTier()}");
}
```

## Mixin (with)
Mixin adalah mekanisme yang digunakan dalam beberapa bahasa pemrograman berorientasi objek untuk menggabungkan kode dari beberapa kelas ke dalam satu kelas tanpa menggunakan pewarisan langsung. 
```
mixin Stoppable{
    void stop(){
        print("Stopped...");
    }
}
mixin Playable{
    void play(){
        print("Playing...");
    }
}

class Audio with Stoppable, Playable{
    String title;
    Audio(this.title);
}

class Video with Stoppable, Playable{
    String title;
    Video(this.title);
}

void main(){
    Audio audio = Audio("Song A");
    Video video = Video("Movie X");
    
    audio.play();
    video.play();
    
    audio.stop();
    video.stop();
}
```

## static
- Tidak perlu membuat object pada main, langsung tulis NamaClass.method untuk memanggil.
- untuk attribut static, harus diberi `final` agar nilai tidak bisa diubah/ditimpa pada class yang lain.
```
class Application{
    static final String name = "Belajar Dart OOP";
    static final String author = "Widi Arrohman";
}
class Math{
    static int sum(int first, int second) => first + second;
}
void main(){
    print(Application.name);
    print(Application.author);
    print(Math.sum(5,9));
}
```

## enum 
```
enum CustomerLevel{
    reguler,
    premium,
    vip
}
class Customer{
    String name;
    CustomerLevel level;
    
    Customer(this.name, this.level);
}

void main(){
    var customer = Customer("Widi Arrohman", CustomerLevel.vip);
    print(customer.name);
    print(customer.level);
    
    //untuk melihat list enum
    print(CustomerLevel.values);
}
```

## Exception
```
class ValidationException implements Exception{
    String message;
    ValidationException(this.message);
}

class Validation{
    static void validate(String username, String password){
        if(username == ""){
            throw ValidationException("Username is blank");
        }else if(password == ""){
            throw ValidationException("Password is blank");
        } else if(username != 'eko' || password != 'eko') {
            throw Exception('Login failed');
        }
        //valid
    }
}

void main(){
    try{
        Validation.validate("eko","salah");
    } on ValidationException catch (exception){
        print('Validation error : ${exception.message}');
    } catch(exception){
        print('Error : ${exception.toString()}');
    } finally {
        print("Finally");
    }
    print('Selesai');
}
```