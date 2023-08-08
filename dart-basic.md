 # Dart
 
 ## variable
 ```
 // numerik
 int age = 25;
 double weight = 64.6;
 
 // string
 String name = "john doe";
 
 // boolean
 bool isLogged - true;

// List
List<int> numbers = [1,2,3,4,5,6];
List<String> fruits = ['apple','banana','orange'];

// Map
Map<String, int> scores = {'John': 95, 'Jane': 85, 'Bob': 78};

// Dynamic
var dynamicVariable = 'Hello';
dynamicVariable = 43; // tidak akan terjadi error, karena data dinamis

// Final dan Cost
// Variable yang nilainya tetap dan tidak dapat diubah setelah dideklarasikan. perbedaanya ada pada saat runtime
// 'final' akan diinisialisasi ketika diakses
// 'const' sudah diinisialisasi saat kompilasi

final int score = 100;
const double pi = 3.14;

// Nullable
String? nullableName = null;
int? nullableValue;

// Non-Nullable (Null Safety)
// menjamin variable tersebut tidak akan memiliki nilai null
String nonNullableName = 'Widi';
int nonNullableValue = 42;

// Late
// Untuk menuntda inisialisasi sebuah variabel hingga saat diperlukan.
// variable late digunakan ketika tahu variabel tersebut akan diinisialisasi sebelum diakses, tetapi tidak dapat dilakukan pada saat deklarasi.
late String description;
void initializeDescription(){
    description = 'This is a late variable';
}

// static
// variable yang terikan dengan kelas, bukan dengan instance dari kelas tersebut.
// ini berarti nilai bariable static bersifat bersama antara semua instace dari kelas yang sama.
class Counter{
    static int count=0;
    Counter(){
        count++;
    }
}
void main(){
  var counter1 = Counter();
  print(Counter.count); // 1
  
  var counter2 = Counter();
  print(Counter.count); //2
  
}
 ```
 
 ## Konversi data
 ```
 // Konversi int ke double
 int intValue = 10;
 double doubleValue = intValue.toDouble();

// Konversi double ke int 
double doubleValue = 10.5;
int intValue1 = doubleValue.toInt(); 
int intValue2 = int.parse(doubleValue.toString()); 

// Konversi String ke int
String numericString = "42";
int intValue = int.parse(numericString); 

// Konversi String ke double
double doubleValue = double.parse(numericString); 

// Konversi int ke String
int intValue = 42;
String intString = intValue.toString(); 

// Konversi double ke String
double doubleValue = 3.14;
String doubleString = doubleValue.toString(); 

// Konversi bool ke String ("true" atau "false")
bool isLoggedIn = true;
String loginStatus = isLoggedIn.toString(); 

String loginStatus = "true";
bool isLoggedIn1 = bool.fromEnvironment(loginStatus); // Konversi String ke bool (menggunakan fungsi)
bool isLoggedIn2 = (loginStatus == "true"); // Konversi String ke bool (menggunakan perbandingan)


 ```
 
 ## operator aritmatika
 ```
 int a = 1;
 int b = 2;
 
 int tambah = a+b;
 int kurang = a-b;
 int kali = a*b;
 double bagiHasilDouble = a/b; //hasil double
 int bagiHasilInt = a~/b; //hasil int
 int sisaBagi = a % b; 
 ```
 
 ## operator perbandingan
 ```
 int a = 5;
 int b = 8;
 bool samaDengan = a==b;
 bool tidakSamaDengan = a!=b;
 bool lebihDari = a > b;
 bool kurangDari = a < b;
 bool lebihDariSamaDengan = a >= b;
 bool kurangDariSamaDengan = a <= b;
 
 ```
 
 ## operator penugasan
 ```
 var a = 1;
 a += 10; //11
 a -= 1; //10
 a *= 10; // 100
 a /= 10; // 10
 a ~/= 10; // 1
 a %= 10; //0
 ```
 
 ## operator logika
 ```
 bool isTrue = true;
 bool isFalse = false;
 bool and = isTrue && isFalse; // false
 bool or = isTrue || isFlase; // true
 bool not = !isTrue; //false
 ```
 
 ## operator type test
 ```
 int number=50;
 bool isNotString = number is String; //false
 
 String text = 'Hello';
 bool isNotString = text is! String; // false
 ```
 
 # List
 ```
List<double> emptyList = List(); // List kosong

List<String> fruits = ['apple', 'banana', 'orange']; // List dengan nilai-nilai awal
fruits[0] = 'pear'; // Mengubah elemen pertama menjadi 'pear'
fruits.add('grape'); // Menambahkan 'grape' ke List

 List<int> numbers = [1, 2, 3, 4, 5]; // List dengan nilai-nilai awal
int thirdNumber = numbers[2]; // Mengakses elemen ketiga (3)
umbers.remove(3); // Menghapus angka 3 dari List
numbers.removeAt(1); // Menghapus elemen dengan indeks 1 (2) dari List
int lengthNumbers = numbers.length;

//iterasi List
List<String> fruits = ['apple', 'banana', 'orange'];
for (var fruit in fruits) {
  print(fruit); // Mencetak setiap elemen di List
}

fruits.forEach((fruit) => print(fruit)); // Alternatif iterasi menggunakan forEach()
 ```
 
 ## set
 - set tidak menerima duplikat, jika ada 2 data yang sama, maka data duplikat akan dihiruakan.
 - set tidak menjamin urutan data, list diurutkan dengan data tetapi tidak untuk list.
 ```
Set<double> emptySet = Set(); // Set kosong
 
Set<int> numbers = {1, 2, 3, 4, 5}; // Set dengan nilai-nilai awal
 numbers.remove(3); // Menghapus angka 3 dari Set
 int lengthNumbers = numbers.length; // Panjang Set
 
Set<String> fruits = {'apple', 'banana', 'orange'}; // Set dengan nilai-nilai awal
Set<String> fruits = {'apple', 'banana', 'orange'};
fruits.add('grape'); // Menambahkan 'grape' ke Set
fruits.add('apple'); // Tidak akan menambahkan 'apple' lagi karena sudah ada dalam Set

for (var fruit in fruits) {
  print(fruit); // Mencetak setiap elemen di Set
}

fruits.forEach((fruit) => print(fruit)); // Alternatif iterasi menggunakan forEach()

 ```
 
 ## Map
```
Map<String, dynamic> emptyMap = Map(); // Map kosong dengan tipe data dynamic
Map<int, String> students = {1: 'John', 2: 'Jane', 3: 'Bob'}; // Map dengan nilai-nilai awal

Map<String, int> scores = {'John': 95, 'Jane': 85, 'Bob': 78}; // Map dengan nilai-nilai awal
//Mengakses Nilai dalam Map
int johnScore = scores['John']; // Mengakses nilai untuk kunci 'John' (95)

//Menambah atau Mengubah Nilai dalam Map
scores['Jane'] = 90; // Mengubah nilai untuk kunci 'Jane' menjadi 90
scores['Alice'] = 88; // Menambahkan pasangan kunci-nilai baru ('Alice': 88) ke dalam Map

//Menghapus Pasangan Kunci-Nilai dari Map
scores.remove('Bob'); // Menghapus pasangan kunci-nilai dengan kunci 'Bob' dari Map

int lengthScores = scores.length; // Panjang Map
```

## if, else, else if
```
  int age = 19;
  bool isRegistered = false;

  if (age >= 18) {
    print("Anda cukup umur.");
    if (isRegistered) {
      print("Anda telah terdaftar.");
    } else if (isRegistered == false) {
      print("Anda belum terdaftar.");
    }
  } else {
    print("Anda belum cukup umur.");
  }
```

## switch
```
int day = 4;
String dayName;

switch (day) {
  case 1:
    dayName = "Senin";
    break;
  case 2:
    dayName = "Selasa";
    break;
  case 3:
    dayName = "Rabu";
    break;
  case 4:
    dayName = "Kamis";
    break;
  case 5:
    dayName = "Jumat";
    break;
  default:
    dayName = "Hari lainnya";
}

print("Hari ini adalah $dayName.");

```

## ternary operator
```
int age = 18;

String status = age >= 18 ? "Dewasa" : "Anak-anak";
print("Status: $status"); // Output: "Status: Dewasa"

```

## for loop
```
for (int i = 1; i <= 5; i++) {
  print("Iterasi ke-$i");
}

```

## while loop
```
int i = 1;

while (i <= 5) {
  print("Iterasi ke-$i");
  i++;
}
```

## do while loop
```
int i = 1;

do {
  print("Iterasi ke-$i");
  i++;
} while (i <= 5);

```

## break
```
for (int i = 1; i <= 5; i++) {
  print("Iterasi ke-$i");
  if (i == 3) {
    break; // Perulangan berhenti ketika i == 3
  }
}
```
hasil
```
Iterasi ke-1
Iterasi ke-2
Iterasi ke-3
```

## continue
```
for (int i = 1; i <= 5; i++) {
  if (i == 3) {
    continue; // Melewati iterasi ketika i == 3
  }
  print("Iterasi ke-$i");
}
```
hasil
```
Iterasi ke-1
Iterasi ke-2
Iterasi ke-4
Iterasi ke-5
```

## for in
```
//menggunakan list
List <int> numbers= [1,2,3,4,5,6];
for(var number in numbers){
    print(number)
}

//menggunakan map
Map<String, int> scores =  {'John': 95, 'Jane': 85, 'Bob': 78};
for(var data in scores.entries){
    print('Nama: ${data.key}, nilai: ${data.value}');
}
```

## function
```
void great(){
    print('Hai, selamat pagi');
}

int addNumbers(int a, int b){
    return a+b;
}
void main(){
    greate();
    int sum = addNumbers(5,6);
    print('hasil : ${sum}');
}
```

### Named Optional Parameters (Parameter Opsional dengan Nama)
```
void printMessage({String message = "Hello", String name = "Guest"}) {
  print("$message, $name!");
}
```

### Positional Optional Parameters (Parameter Opsional dengan Posisi)
```
void printMessage(String message, [String name = "Guest"]) {
  print("$message, $name!");
}

void main() {
  printMessage("Hello"); // Output: Hello, Guest!
  printMessage("Hi", "John"); // Output: Hi, John!
}
```

## function return value
- setiap function selain void maka harus memiliki return
```
int addNumber(int a, int b){
    int sum = a+b;
    return sum;
}
```

## function short expression
```
// fungsi dengan satu parameter
int persegi(int number) => number * number;

// fungsi tanpa parameter
void greet() => print('hai...');

// fungsi dengan beberapa parameter
int addNumbers(int a, int b) => a+b;
void main(){
    int result = persegi(5);
    greet();
    int sum = addNumbers(6,1);
    print(sum);
}
```

## inner function
- function yang berada didalam function.
```
void outerFuntion(){
    print('ini adalah fungsi induk');
    
    void innerFunction(){
        print('ini adalah fungsi inner');
    }
    
    innerFunction();
}

void main(){
    outerFunction();
}
```

## higher order function
- function yang menjadi parameter bagi function lainnya
```
Function calculator(String operation){
  if(operation == "add"){
    return (int a, int b)=> a+b;
  } else if(operation == "subtract"){
    return (int a, int b) => a - b;
  } else {
    return (int a, int b) => a * b;
  }
}

void main(){
  Function add = calculator("add");
  Function subtract = calculator("subtract");

 print('Hasil penjumlahan: ${add(6,6)}'); 
 print('Hasil pengurangan: ${subtract(6,3)}'); 
}
```

## anonymous function
```
// anonymous function dengan return
var upperFunction = (String name){
    return name.toUpperCase();
};

//anonymous function tanpa return
var lowerFunction = (String name) => name.toLowerCase();
print(upperFunction('Widi'));
print(lowerFunction('Widi'));
```