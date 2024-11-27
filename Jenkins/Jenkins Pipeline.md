# Quickstart
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

# Macam-macam `agent`
Dalam Jenkins Pipeline, **agent** digunakan untuk menentukan di mana pipeline atau tahapan tertentu akan dijalankan. Berikut adalah macam-macam nilai yang dapat digunakan untuk **agent** beserta penjelasannya:

---

### **1. `agent any`**

- **Deskripsi**:
    
    - Pipeline akan berjalan di sembarang node Jenkins yang tersedia.
- **Penggunaan**:
    
    ```groovy
    pipeline {
        agent any
    }
    ```
    
- **Kapan digunakan**:
    
    - Ketika Anda tidak memiliki preferensi spesifik untuk node.

---

### **2. `agent none`**

- **Deskripsi**:
    
    - Tidak ada agent default untuk seluruh pipeline. Anda harus menentukan agent secara eksplisit pada setiap `stage`.
- **Penggunaan**:
    
    ```groovy
    pipeline {
        agent none
        stages {
            stage('Build') {
                agent { label 'linux' }
                steps {
                    echo 'Running on a Linux agent.'
                }
            }
        }
    }
    ```
    
- **Kapan digunakan**:
    
    - Untuk pipeline dengan kebutuhan khusus pada setiap tahap.

---

### **3. `agent { label 'node_label' }`**

- **Deskripsi**:
    
    - Pipeline akan dijalankan pada node Jenkins dengan label tertentu.
- **Penggunaan**:
    
    ```groovy
    pipeline {
        agent { label 'linux' }
    }
    ```
    
- **Kapan digunakan**:
    
    - Jika Anda ingin menjalankan pipeline di node dengan spesifikasi tertentu, seperti OS, kapasitas, atau tools terpasang.

---

### **4. `agent { node { ... } }`**

- **Deskripsi**:
    
    - Memberikan lebih banyak kontrol pada alokasi node dengan berbagai opsi.
- **Penggunaan**:
    
    ```groovy
    pipeline {
        agent {
            node {
                label 'windows'
                customWorkspace '/custom/workspace'
            }
        }
    }
    ```
    
- **Kapan digunakan**:
    
    - Ketika Anda ingin menggunakan label dan menentukan workspace khusus.

---

### **5. `agent { docker 'image_name' }`**

- **Deskripsi**:
    
    - Pipeline akan dijalankan di dalam container Docker dengan image yang spesifik.
- **Penggunaan**:
    
    ```groovy
    pipeline {
        agent {
            docker 'maven:3.8.5-jdk-11'
        }
        stages {
            stage('Build') {
                steps {
                    sh 'mvn clean install'
                }
            }
        }
    }
    ```
    
- **Kapan digunakan**:
    
    - Ketika Anda ingin memastikan pipeline berjalan di lingkungan yang konsisten tanpa memerlukan konfigurasi di node host.

---

### **6. `agent { dockerfile true }`**

- **Deskripsi**:
    
    - Menjalankan pipeline di dalam container Docker yang dibangun dari `Dockerfile` di direktori proyek.
- **Penggunaan**:
    
    ```groovy
    pipeline {
        agent {
            dockerfile true
        }
        stages {
            stage('Build') {
                steps {
                    sh 'make build'
                }
            }
        }
    }
    ```
    
- **Kapan digunakan**:
    
    - Jika Anda ingin membangun image Docker khusus sebelum menjalankan pipeline.

---

### **7. `agent { kubernetes { ... } }`**

- **Deskripsi**:
    
    - Pipeline dijalankan di dalam pod Kubernetes.
- **Penggunaan**:
    
    ```groovy
    pipeline {
        agent {
            kubernetes {
                yaml '''
                apiVersion: v1
                kind: Pod
                spec:
                  containers:
                  - name: maven
                    image: maven:3.6.3-jdk-11
                    command:
                    - cat
                    tty: true
                '''
            }
        }
        stages {
            stage('Build') {
                steps {
                    sh 'mvn clean install'
                }
            }
        }
    }
    ```
    
- **Kapan digunakan**:
    
    - Jika Jenkins terintegrasi dengan Kubernetes untuk menjalankan pipeline di lingkungan container yang dinamis.

---

### **8. `agent { none` di dalam `stage` }**

- **Deskripsi**:
    
    - Tahap tertentu tidak memerlukan alokasi agent.
- **Penggunaan**:
    
    ```groovy
    stage('Approval') {
        agent none
        steps {
            input 'Proceed to Deploy?'
        }
    }
    ```
    
- **Kapan digunakan**:
    
    - Ketika hanya diperlukan tindakan manual atau logika non-eksekusi.

---

### **Kesimpulan**

Jenis **agent** yang dipilih tergantung pada kebutuhan spesifik pipeline:

1. **`any`**: Default, gunakan node yang tersedia.
2. **`none`**: Tidak ada agent default; tetapkan per stage.
3. **`label`**: Untuk node dengan karakteristik tertentu.
4. **`docker`/`dockerfile`**: Menjalankan di dalam container Docker.
5. **`kubernetes`**: Jalankan di dalam pod Kubernetes.

Pilih **agent** yang sesuai untuk memastikan pipeline Anda berjalan optimal! 🚀