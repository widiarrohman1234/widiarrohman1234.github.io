# OOP Java

## Class dan Object
```
public class Main {
    int x = 5;

    public static void main(String[] args) {
        {
            Main myObj1 = new Main();
            Main myObj2 = new Main();

            int tambah = myObj2.x+5;

            System.out.println(myObj1.x);
            System.out.println(tambah);
        }
    }

}
```
## Class attributes
```
public class Main {
    String firstName = "widi";
    String lastName = "arrohman";
    int age = 5;

    public static void main(String[] args) {
        {
            Main mahasiswa = new Main();
            Main santri = new Main();

            int tambahUmur = santri.age+5;

            System.out.println("Mahasiswa: first name: "+mahasiswa.firstName+" "+"last name: "+mahasiswa.lastName+" "+"age: "+mahasiswa.age);      
            System.out.println("Santri: first name: " + mahasiswa.firstName + " " + "last name: " + mahasiswa.lastName + " " + "age: " + tambahUmur);
        }
    }
}
```
## Java Class Methods
```
public class JavaClassMethods {
    public static void main(String[] args) {
        System.out.println("Welcome");
        System.out.println(helloWorld());
    }

    static String helloWorld() {
        return "hello world";
    }
}
```




