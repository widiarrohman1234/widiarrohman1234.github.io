# C# Basic Documentation

## Hello world
```c#
using System;
/*
ini adalah program pertama saya
menggunakan C#
*/
namespace HelloWorld{
    class Program{
        static void Main(string[] args){
            Console.WriteLine("Hello world");
            Console.WriteLine("I am Learning C#");
            Console.WriteLine("It is awesome!");
            // 3+3
            Console.WriteLine(3+3);
        }
    }
}
```
## C# Variables
> type variableName = value;

- `int`
- `double`
- `char`
- `string`
- `bool`
- `long`
- `float`

```C#
string name = "John";
Console.WriteLine(name);
int myNyum = 15;
Console.WriteLine(myNum);
myNum = 10;
Console.WriteLine(myNum);

double myDoubleNum = 5.99D;
char myLetter = 'D';
bool myBool = true;
long longNum = 15000000000L;
Console.WriteLine(longNum);
float myFloat = 5.75F;
float f1 = 35e3F;
double d1 = 12E4D;
Console.WriteLine(f1);
Console.WriteLine(d1);
```

## Constants
```C#
const int myNum = 15;
myNum = 20; //error 
```

## C# Display Variables
```C#
string name = "John";
Console.WriteLine("Hello "+name);

string firstName = "Widi";
string lastName = "Arrohman";
string fullName = firstName+lastName;
Console.WriteLine(fullName);

int x,y,z;
x = y = z = 50;
Console.WriteLine(x+y+z);
```

## C# Identifiers
```C#
// Good
int minutesPerHour = 60;
// Ok, but not so easy to understand what m actually is
int m = 60;
```

## C# Type Casting

- **Implicit Casting** (automatically) - converting a smaller type to a larger type size. `char`->`int`->`long`->`float`->`double`

- **Explicit Casting** (manualy) - converting a larger type to a smaller size type. `double`->`float`->`long`->`int`->`char`

### Implicit Casting
```C#
int myInt = 9;
double myDouble = myInt;
Console.WriteLine(myInt);
Console.WriteLine(myDouble);
```

### Explicit Casting
```C#
double myDouble = 9.78;
int myInt = (int)myDouble;

Console.WriteLine(myDouble);
Console.WriteLine(myInt);
```
### Type Coversion Methods
```C#
int myInt = 10;
double myDouble = 5.25;
bool myBool = true;
Console.WriteLine(Convert.ToString(myInt)); // int to string
Console.WriteLine(Convert.ToDouble(myInt)); // int to double
Console.WriteLine(Convert.ToInt32(myDouble)); // double to int
Console.WriteLine(Convert.ToString(myBool)); // bool to string
```

## C# User Input
```C#
Console.WriteLine("Enter username: ");
string userName = Console.ReadLine();
Console.WriteLine("Username is: "+ userName);
```
## C# Operators
- `+` = x+y
- `-` = x-y
- `*` = x*y
- `/` = x/y
- `%` = x%y
- `++` = x++
- `--` = x--

## C# Assignment Operators
```
int x = 10;
x += 5;
```
- =
- +=
- -=
- *=
- /=
- %=
- &=
- |=
- ^=
- >>=
- <<=

## Comparison Operators
```C#
int x = 5;
int y = 3;
Console.WriteLine(x > y);
```
- ==
- !=
- >
- <
- >= 
- <=

## Logical Operators
- &&
- ||
- !

## C# Strings
```C#
string greeting = "hello";
string greeting2 = "Nice to meet you!";
Console.WriteLine("Length "+ greeting2.length);
Console.WriteLine("ToUpper "+ greeting2.ToUpper());
Console.WriteLine("ToLower "+ greeting2.ToLower());
```

## C# String Concatenation
```C#
string firstName = "Widi";
string lastName = "Arrohman";
string name = firstName + lastName;
Console.WriteLine(name);
string name2 = string.Concat(firstName,lastName);
Console.WriteLine(name2);
```

## C# String Interpolation
```C#
string firstName = "Widi";
string lastName = "Arrohman";
string name = $"My full name is: {firstName} {lastName}";
Console.WriteLine(name);
```
## C# Access Strings
```C#
string myString = "Hello world";
Console.WriteLine(myStirng[0]); // "H"
Console.WriteLine(myStirng[1]); // "i"
int charPos = myString.IndexOf("w"); // "6"
string lastName = myString.Substring(charPos);
Console.WriteLine(lastName); // world
```

## C# If .. Else
```C#
int time = 20;
if(time>18){
    Console.WriteLine("20 is greater than 18");
} else if(time == 20){
    Console.WriteLine("time is equal 20");
} else {
    Console.WriteLine("Value is not available");
}
```

## C# Ternary operator
```C#
int time = 20;
string result = (time < 18) ? "Good day." : "Good evening";
Console.WriteLine(result);
```

## C# Switch
```C#
int day = 4;

switch(){
    case 1:
    Console.WriteLine("Sunday");
    break;
    case 2:
    Console.WriteLine("Monday");
    break;
    case 3:
    Console.WriteLine("Thuesday");
    break;
    default:
    Console.WriteLine("Nothing");
    break;
}
```

## C# while loop
- while
```C#
int i = 0;
while (i<5){
    Console.WriteLine(i);
    i++;
}
```

- do while
```C#
int i = 0;
do{
    Console.WriteLine(i);
    i++;
}
while (i < 5);
```

## C# for loop
```C#
for(int i =0; i<5 ; i++){
    Console.WriteLine(i);
}
```

## C# Foreach loop
```C#
string[] cars = {"nama", "saya","Widi","Arrohman"};
foreach(string i in cars){
    Console.WriteLine(i);
}
```

## Break and Continue
- break
```C#
for(int i=0; i < 10; i++){
    if(i == 4){
        break;
    }
    Console.WriteLine(i);
}
```

- continue
```C#
for(int i = 0; i < 10; i++){
    if(i == 4){
        continue;
    }
    Console.WriteLine(i);
}
```

## C# Arrays
```C#
string[] arrayString = {"nama","saya","widi","arrohman"};
int[] arrayNum = {1,2,3,4,5,6,7,8};
Console.WriteLine(arrayString[0]); // nama
Console.WriteLine(arrayString.Length); //4
```

## C# Loop through arrays
- for loop
```C#
string[] arrayString = {"nama","saya","widi","arrohman"};
for(int i = 0; i < cars.Length; i++){
    Console.WriteLine(cars[i]);
}
```

- foreach loop
```C#
string[] arrayString = {"nama","saya","widi","arrohman"};
foreach(int i in arrayString){
    Console.WriteLine(i);
}
```

## C# sort arrays
```C#
string[] arrayString = {"widi","wahida","wira","sanjuni","arrohman","hanifah"};
Array.Sory(arrayString);
foreach(string i in arrayString){
    Console.WriteLine(i);
}
```

## C# Multidimensional Arrays
```C#
int[,] numbers = {{1,4,5},{5,7,8}};
Console.WriteLine(numbers[0,2]); //5
numbers[0,1] = 3;
Console.WriteLine(number[0,1]); //3
```

## C# Loop through a 2D Array
```C#
int[,] numbers = {{1,4,5},{5,7,8}};
for (int i = 0; i < numbers.GetLength(0); i++){
    for(int j = 0; j < numbers.GetLength(1); i++){
        Console.WriteLine(numbers[i,j]);
    }
}
```





