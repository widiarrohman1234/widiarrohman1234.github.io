Berikut adalah **cheatsheet Jenkins Pipeline** untuk membantu Anda memulai dengan Jenkinsfile dan memahami dasar-dasar syntax dan fungsi yang digunakan:

---

### **Dasar-Dasar Jenkinsfile**

- Jenkinsfile ditulis dalam format **Declarative Pipeline** atau **Scripted Pipeline**.
- Direkomendasikan untuk menggunakan **Declarative Pipeline** karena lebih mudah dipelajari dan lebih terstruktur.

---

### **Struktur Dasar Declarative Pipeline**

```groovy
pipeline {
    agent any            // Menentukan di mana pipeline akan berjalan (any = semua node)
    
    stages {             // Blok berisi tahapan pekerjaan
        stage('Build') { // Nama tahap
            steps {      // Langkah-langkah dalam tahap ini
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
```

---

### **Blok Utama**

1. **`pipeline`**
    
    - Blok utama yang membungkus semua konfigurasi pipeline.
2. **`agent`**
    
    - Menentukan executor node. Contoh:
        - `agent any`: Jalankan di node mana saja.
        - `agent none`: Tidak menggunakan agent global.
        - `agent { docker 'image_name' }`: Jalankan dalam container Docker tertentu.
3. **`stages`**
    
    - Mengelompokkan tahapan pekerjaan.
    - Masing-masing tahap didefinisikan dalam blok `stage`.
4. **`steps`**
    
    - Berisi perintah atau skrip yang akan dieksekusi di setiap `stage`.

---

### **Contoh Blok Advanced**

#### **Menggunakan Kondisi (When)**

```groovy
stage('Deploy') {
    when {
        branch 'main'     // Hanya berjalan di branch 'main'
    }
    steps {
        echo 'Deploying to Production...'
    }
}
```

#### **Menggunakan Environment Variables**

```groovy
pipeline {
    agent any
    environment {
        ENV_VAR = 'value'
    }
    stages {
        stage('Example') {
            steps {
                echo "Environment variable is: ${ENV_VAR}"
            }
        }
    }
}
```

#### **Menyimpan Artifact**

```groovy
stage('Archive') {
    steps {
        archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
    }
}
```

#### **Parallel Stages**

```groovy
stage('Parallel Tests') {
    parallel {
        stage('Test A') {
            steps {
                echo 'Running Test A...'
            }
        }
        stage('Test B') {
            steps {
                echo 'Running Test B...'
            }
        }
    }
}
```

---

### **Pipeline Scripted (Alternatif)**

```groovy
node {
    stage('Build') {
        echo 'Building...'
    }
    stage('Test') {
        echo 'Testing...'
    }
    stage('Deploy') {
        echo 'Deploying...'
    }
}
```

---

### **Tips**

- Gunakan **Blue Ocean** untuk mempermudah pembuatan pipeline.
- Pastikan menyimpan Jenkinsfile di repositori source control (misalnya GitHub).
- Gunakan **`input`** untuk meminta konfirmasi manual:
    
    ```groovy
    stage('Approval') {
        steps {
            input 'Proceed to Deploy?'
        }
    }
    ```
    

---

### **Command Utility**

- **`sh 'command'`**: Menjalankan perintah shell.
- **`bat 'command'`**: Menjalankan perintah di Windows.
- **`checkout scm`**: Checkout kode dari source control.
- **`timeout(time: x, unit: 'MINUTES')`**: Mengatur batas waktu untuk suatu blok.

---

Dengan cheatsheet ini, Anda bisa lebih cepat membuat dan memodifikasi pipeline di Jenkins. Untuk proyek besar, pertimbangkan menggunakan library pipeline untuk modularisasi! 🚀