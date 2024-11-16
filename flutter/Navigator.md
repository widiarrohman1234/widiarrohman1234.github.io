Di Flutter, ada beberapa jenis metode navigasi yang dapat digunakan untuk berpindah antar halaman (route). Berikut ini adalah berbagai cara menggunakan `Navigator` dan metode navigasi lainnya di Flutter:

### 1. **Navigator.push**

`Navigator.push` digunakan untuk menambahkan halaman (route) baru ke tumpukan navigasi. Halaman baru akan muncul di atas halaman saat ini, dan pengguna bisa kembali dengan tombol kembali.

```dart
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => HalamanBaru()),
);
```

### 2. **Navigator.pop**

`Navigator.pop` digunakan untuk menutup halaman atau dialog saat ini dan kembali ke halaman sebelumnya di tumpukan.

```dart
Navigator.pop(context);
```

### 3. **Navigator.pushReplacement**

`Navigator.pushReplacement` menggantikan halaman saat ini dengan halaman baru. Hal ini berarti halaman sebelumnya dihapus dari tumpukan, dan pengguna **tidak bisa kembali ke halaman sebelumnya**.

```dart
Navigator.pushReplacement(
  context,
  MaterialPageRoute(builder: (context) => HalamanPengganti()),
);
// atau
Navigator.pushReplacementNamed(context, '/transaction');

```

### 4. **Navigator.pushAndRemoveUntil**

`Navigator.pushAndRemoveUntil` memungkinkan Anda untuk menambahkan halaman baru dan menghapus semua halaman sebelumnya dari tumpukan hingga kondisi tertentu terpenuhi.

```dart
Navigator.pushAndRemoveUntil(
  context,
  MaterialPageRoute(builder: (context) => HalamanBaru()),
  (Route<dynamic> route) => false, // Menghapus semua halaman sebelumnya
);
```

Contoh lain, untuk tetap menyimpan satu halaman tertentu:

```dart
Navigator.pushAndRemoveUntil(
  context,
  MaterialPageRoute(builder: (context) => HalamanBaru()),
  ModalRoute.withName('/halaman_utama'), // Menyimpan halaman tertentu di tumpukan
);
```

### 5. **Navigator.popUntil**

`Navigator.popUntil` mengeluarkan halaman dari tumpukan hingga mencapai halaman tertentu yang sudah ada di tumpukan. Berguna ketika Anda ingin kembali ke halaman sebelumnya tanpa membuka halaman baru.

```dart
Navigator.popUntil(context, ModalRoute.withName('/halaman_tujuan'));
```

### 6. **Navigator.pushNamed**

`Navigator.pushNamed` digunakan untuk navigasi berdasarkan nama rute yang sudah didefinisikan. Hal ini sering digunakan untuk aplikasi yang menggunakan rute terpusat.

```dart
Navigator.pushNamed(context, '/nama_route');
```

### 7. **Navigator.pushReplacementNamed**

`Navigator.pushReplacementNamed` serupa dengan `pushReplacement`, tetapi menggunakan nama rute.

```dart
Navigator.pushReplacementNamed(context, '/nama_route');
```

### 8. **Navigator.pushNamedAndRemoveUntil**

`Navigator.pushNamedAndRemoveUntil` serupa dengan `pushAndRemoveUntil`, tetapi menggunakan nama rute.

```dart
Navigator.pushNamedAndRemoveUntil(
  context,
  '/nama_route',
  (Route<dynamic> route) => false,
);
```

### 9. **Navigator.popWithResult**

Jika Anda perlu mengembalikan data dari halaman yang baru saja ditutup, Anda bisa menggunakan `Navigator.pop` dengan parameter data.

```dart
Navigator.pop(context, hasilData); // Kembali dengan data
```

Di halaman awal, Anda dapat menangkap hasilnya:

```dart
final hasilData = await Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => HalamanBaru()),
);
```

### 10. **Navigator.canPop**

Metode ini digunakan untuk memeriksa apakah ada halaman lain di tumpukan yang dapat ditutup. Ini berguna untuk mencegah pengguna keluar dari aplikasi secara tidak sengaja.

```dart
if (Navigator.canPop(context)) {
  Navigator.pop(context);
} else {
  // Tidak ada halaman lain untuk ditutup
}
```

### 11. **Navigator.maybePop**

`Navigator.maybePop` mencoba untuk menutup halaman saat ini jika memungkinkan. Jika tidak ada halaman lain di tumpukan, maka halaman tidak akan ditutup.

```dart
Navigator.maybePop(context);
```

### 12. **Navigator.restorablePush**

`restorablePush` adalah versi dari `Navigator.push` yang mendukung state restoration, memungkinkan aplikasi mengembalikan posisi halaman saat pengguna menutup dan membuka kembali aplikasi. 

```dart
Navigator.restorablePush(context, halamanBuilder);
```

### 13. **showDialog** dan **showModalBottomSheet**

Meskipun tidak langsung terkait dengan `Navigator`, kedua metode ini memungkinkan Anda menampilkan konten di atas halaman utama tanpa berpindah halaman secara penuh.

#### Contoh `showDialog`

```dart
showDialog(
  context: context,
  builder: (context) => AlertDialog(
    title: Text("Dialog"),
    content: Text("Ini adalah dialog."),
  ),
);
```

#### Contoh `showModalBottomSheet`

```dart
showModalBottomSheet(
  context: context,
  builder: (context) => Container(
    padding: EdgeInsets.all(16.0),
    child: Text("Ini adalah modal bottom sheet."),
  ),
);
```

### Memilih Navigator yang Tepat
Pemilihan metode navigasi tergantung pada skenario aplikasi. Jika aplikasi Anda memiliki rute yang sangat sederhana, `Navigator.push` dan `Navigator.pop` sudah cukup. Sedangkan untuk navigasi yang lebih kompleks, seperti login yang menggantikan halaman utama atau alur aplikasi dengan banyak tahap, gunakan `Navigator.pushReplacement`, `pushAndRemoveUntil`, atau `pushNamed`.