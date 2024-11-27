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

# Macam-macam `steps`
**Steps** dalam Jenkinsfile adalah blok atau perintah yang dijalankan di setiap **stage**. Mereka mewakili tindakan yang akan dilakukan oleh pipeline, seperti menjalankan skrip, mengarsipkan file, atau memicu build lain. Dokumentasi lengkap, silahkan kunjungi halaman ini [LINK](https://www.jenkins.io/doc/pipeline/steps/)

Berikut adalah berbagai jenis **steps** yang sering digunakan dalam Jenkinsfile:

---

## **1. Menjalankan Perintah**

### **a. `sh` (Shell Command)**

- Menjalankan perintah di shell (Linux/Mac).

```groovy
steps {
    sh 'echo "Hello from Shell!"'
}
```

### **b. `bat` (Batch Command)**

- Menjalankan perintah di Windows Command Prompt.

```groovy
steps {
    bat 'echo Hello from Windows!'
}
```

- **Kapan digunakan**:  
    Untuk menjalankan skrip atau perintah OS, seperti membangun kode, menginstal dependensi, atau menjalankan layanan.

---

## **2. Echo/Print**

### **a. `echo`**

- Mencetak pesan ke konsol log Jenkins.

```groovy
steps {
    echo 'Hello Jenkins!'
}
```

- **Kapan digunakan**:  
    Untuk debugging atau menampilkan status dalam pipeline.

---

## **3. Input (Konfirmasi Manual)**

### **a. `input`**

- Meminta konfirmasi atau data dari pengguna sebelum melanjutkan pipeline.

```groovy
steps {
    input 'Proceed to Deployment?'
}
```

- **Kapan digunakan**:  
    Untuk meminta persetujuan manual sebelum tahap sensitif seperti produksi.

---

## **4. Checkout Repository**

### **a. `checkout scm`**

- Mengambil kode sumber dari sistem kontrol versi (default SCM yang didefinisikan).

```groovy
steps {
    checkout scm
}
```

### **b. `git`**

- Menarik kode dari repositori Git.

```groovy
steps {
    git url: 'https://github.com/user/repo.git', branch: 'main'
}
```

- **Kapan digunakan**:  
    Untuk mengambil kode sumber dari repositori sebelum memulai proses build atau pengujian.

---

## **5. Mengarsipkan dan Menyimpan File**

### **a. `archiveArtifacts`**

- Menyimpan file dari workspace ke Jenkins untuk diakses nanti.

```groovy
steps {
    archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
}
```

- **Kapan digunakan**:  
    Untuk menyimpan build hasil, log, atau file penting lainnya.

### **b. `stash` dan `unstash`**

- **`stash`**: Menyimpan file sementara untuk digunakan nanti.

```groovy
steps {
    stash includes: 'build/**', name: 'build-files'
}
```

- **`unstash`**: Mengambil file yang disimpan oleh `stash`.

```groovy
steps {
    unstash 'build-files'
}
```

- **Kapan digunakan**:  
    Ketika Anda ingin berbagi file antar stage dalam pipeline.

---

## **6. Mengirim Notifikasi**

### **a. `mail`**

- Mengirim email.

```groovy
steps {
    mail to: 'team@example.com',
         subject: 'Build Notification',
         body: 'The build has finished!'
}
```

### **b. Notifikasi ke Integrasi Lain**

- Misalnya, menggunakan plugin Slack.

```groovy
steps {
    slackSend channel: '#builds', message: 'Build completed!'
}
```

- **Kapan digunakan**:  
    Untuk memberi tahu tim tentang status pipeline.

---

## **7. Membangun atau Memicu Proyek Lain**

### **a. `build`**

- Memicu build lain di Jenkins.

```groovy
steps {
    build job: 'other-pipeline', parameters: [string(name: 'param1', value: 'value1')]
}
```

- **Kapan digunakan**:  
    Untuk membangun proyek terkait atau pipeline yang bergantung.

---

## **8. Menguji dan Menyimpan Hasil**

### **a. `junit`**

- Mengarsipkan hasil pengujian JUnit.

```groovy
steps {
    junit 'target/surefire-reports/*.xml'
}
```

- **Kapan digunakan**:  
    Untuk menyimpan hasil tes unit atau laporan pengujian lainnya.

---

## **9. Menentukan Timeout**

### **a. `timeout`**

- Membatasi waktu eksekusi untuk blok tertentu.

```groovy
steps {
    timeout(time: 5, unit: 'MINUTES') {
        sh 'long-running-task.sh'
    }
}
```

- **Kapan digunakan**:  
    Untuk mencegah tugas berjalan tanpa batas waktu.

---

## **10. Error Handling**

### **a. `error`**

- Menghentikan pipeline dengan pesan error.

```groovy
steps {
    error 'This stage failed!'
}
```

### **b. `catchError`**

- Menangkap error tanpa menghentikan pipeline.

```groovy
steps {
    catchError(buildResult: 'SUCCESS') {
        sh 'exit 1'
    }
}
```

- **Kapan digunakan**:  
    Untuk mengelola error dalam pipeline tanpa menghentikan semua proses.

---

## **11. Conditional Steps**

### **a. `script`**

- Menjalankan kode Groovy dalam langkah.

```groovy
steps {
    script {
        if (env.BRANCH_NAME == 'main') {
            echo 'Running on main branch!'
        }
    }
}
```

- **Kapan digunakan**:  
    Untuk menambahkan logika yang lebih kompleks dalam langkah.

---

## **12. Parallel**

- Menjalankan langkah secara paralel.

```groovy
steps {
    parallel(
        'Unit Tests': {
            sh 'run-unit-tests.sh'
        },
        'Integration Tests': {
            sh 'run-integration-tests.sh'
        }
    )
}
```

- **Kapan digunakan**:  
    Untuk mempercepat pipeline dengan menjalankan tugas independen secara bersamaan.

---

## **13. Custom Steps**

- Membuat langkah khusus dengan mendefinisikannya sebagai fungsi.

```groovy
def myCustomStep() {
    echo 'This is a custom step!'
}

steps {
    script {
        myCustomStep()
    }
}
```

- **Kapan digunakan**:  
    Untuk modularisasi pipeline.

---

### **Tips Menggunakan Steps**

1. **Prioritaskan Modularisasi**: Gabungkan langkah serupa dalam fungsi untuk mengurangi pengulangan.
2. **Gunakan Debugging**: Tambahkan langkah `echo` untuk membantu mendeteksi masalah selama pengembangan pipeline.
3. **Integrasi Plugin**: Manfaatkan plugin Jenkins untuk langkah tambahan seperti Slack, JUnit, atau Docker.

Dengan menguasai berbagai **steps** ini, Anda dapat membangun pipeline Jenkins yang efisien dan fleksibel! 🚀

# Macam-macam `post`
Dalam **Jenkinsfile**, blok **`post`** digunakan untuk menentukan tindakan yang harus dilakukan setelah tahap tertentu atau setelah pipeline selesai dijalankan. Blok **`post`** mendukung berbagai kondisi yang memungkinkan Anda menangani berbagai skenario hasil eksekusi pipeline.

---

### **Struktur Umum Blok `post`**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
    }
    post {
        always {
            echo 'This will always run.'
        }
        success {
            echo 'This will run only if the pipeline succeeds.'
        }
        failure {
            echo 'This will run only if the pipeline fails.'
        }
    }
}
```

---

### **Macam-Macam Blok `post`**

#### **1. `always`**

- **Deskripsi**:  
    Eksekusi perintah di dalam blok ini selalu dijalankan, tidak peduli apakah pipeline berhasil atau gagal.
- **Contoh**:
    
    ```groovy
    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
    ```
    
- **Kapan digunakan**:  
    Untuk operasi seperti membersihkan lingkungan, mengarsipkan log, atau langkah pembersihan lainnya.

---

#### **2. `success`**

- **Deskripsi**:  
    Eksekusi perintah di dalam blok ini dijalankan hanya jika pipeline selesai dengan sukses.
- **Contoh**:
    
    ```groovy
    post {
        success {
            echo 'Pipeline succeeded! Sending notifications...'
        }
    }
    ```
    
- **Kapan digunakan**:  
    Untuk tindakan yang hanya relevan jika pipeline berhasil, seperti mengirim notifikasi atau memicu langkah berikutnya.

---

#### **3. `failure`**

- **Deskripsi**:  
    Eksekusi perintah di dalam blok ini dijalankan hanya jika pipeline gagal.
- **Contoh**:
    
    ```groovy
    post {
        failure {
            echo 'Pipeline failed! Sending alerts...'
        }
    }
    ```
    
- **Kapan digunakan**:  
    Untuk menangani kegagalan, seperti mengirim notifikasi ke tim terkait atau menyimpan log error.

---

#### **4. `unstable`**

- **Deskripsi**:  
    Eksekusi perintah di dalam blok ini dijalankan hanya jika pipeline berada dalam status **unstable** (contohnya: terdapat peringatan, tetapi bukan kegagalan total).
- **Contoh**:
    
    ```groovy
    post {
        unstable {
            echo 'Pipeline is unstable. Check test results.'
        }
    }
    ```
    
- **Kapan digunakan**:  
    Untuk menangani situasi di mana ada peringatan atau masalah kecil yang tidak menyebabkan pipeline gagal sepenuhnya.

---

#### **5. `aborted`**

- **Deskripsi**:  
    Eksekusi perintah di dalam blok ini dijalankan hanya jika pipeline dibatalkan (misalnya, oleh pengguna).
- **Contoh**:
    
    ```groovy
    post {
        aborted {
            echo 'Pipeline was aborted by the user.'
        }
    }
    ```
    
- **Kapan digunakan**:  
    Untuk mencatat atau membersihkan jika pipeline dihentikan sebelum selesai.

---

#### **6. `changed`**

- **Deskripsi**:  
    Eksekusi perintah di dalam blok ini dijalankan hanya jika status pipeline berubah dari sukses ke gagal, atau sebaliknya.
- **Contoh**:
    
    ```groovy
    post {
        changed {
            echo 'Pipeline status has changed since the last run.'
        }
    }
    ```
    
- **Kapan digunakan**:  
    Untuk memberikan notifikasi jika ada perubahan status dibandingkan dengan eksekusi sebelumnya, seperti mengirim peringatan atau pemberitahuan keberhasilan.

---

### **Blok `post` di Tingkat `stage`**

Blok **`post`** juga dapat digunakan di dalam blok `stage` untuk menangani tindakan pasca eksekusi pada tingkat tahap tertentu.

```groovy
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
            post {
                success {
                    echo 'Tests passed successfully!'
                }
                failure {
                    echo 'Tests failed! Check the logs.'
                }
            }
        }
    }
}
```

---

### **Contoh Kombinasi**

Menggabungkan beberapa blok `post` untuk menangani berbagai hasil pipeline.

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'exit 1' // Simulasi kegagalan
            }
        }
    }
    post {
        always {
            echo 'Pipeline has finished running.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed! Please check the logs.'
        }
        unstable {
            echo 'Pipeline is unstable due to warnings.'
        }
        aborted {
            echo 'Pipeline was manually aborted.'
        }
    }
}
```

---

### **Tips Menggunakan Blok `post`**

1. **Gunakan `always` untuk tugas yang wajib dijalankan**, seperti membersihkan workspace atau mengarsipkan log.
2. **Hindari menumpuk terlalu banyak tugas dalam satu blok `post`**; pisahkan logika ke blok yang relevan untuk menjaga pipeline tetap terstruktur.
3. **Integrasikan notifikasi** (misalnya, Slack, email) dalam blok `success`, `failure`, atau `changed` untuk memberi tahu tim Anda tentang status pipeline.

Dengan memanfaatkan blok `post` secara efektif, Anda dapat memastikan semua skenario pasca-eksekusi pipeline ditangani dengan baik.

# Macam-macam `condition`
Dalam **Jenkinsfile**, kondisi digunakan untuk mengontrol pelaksanaan **stage** tertentu berdasarkan keadaan tertentu. Hal ini berguna untuk mengurangi pekerjaan yang tidak perlu atau membuat pipeline lebih dinamis.

Berikut adalah berbagai macam **kondisi (when)** yang dapat digunakan dalam Jenkinsfile:

---

## **1. Kondisi Berdasarkan Branch**

Menjalankan **stage** hanya jika pipeline berjalan pada branch tertentu.

```groovy
stage('Deploy') {
    when {
        branch 'main'
    }
    steps {
        echo 'Deploying only on the main branch.'
    }
}
```

- **Kapan digunakan**:  
    Jika ingin membatasi tahap tertentu untuk branch spesifik (misalnya, `main` atau `develop`).

---

## **2. Kondisi Berdasarkan Perubahan File (Changeset)**

Menjalankan **stage** hanya jika file tertentu berubah.

```groovy
stage('Run Tests') {
    when {
        changeset '**/*.java' // Menjalankan hanya jika ada perubahan file .java
    }
    steps {
        echo 'Running tests for modified Java files.'
    }
}
```

- **Kapan digunakan**:  
    Jika ingin menjalankan tahap hanya ketika file atau direktori tertentu berubah.

---

## **3. Kondisi Berdasarkan Variabel Lingkungan**

Menjalankan **stage** berdasarkan nilai variabel lingkungan.

```groovy
stage('Deploy to Prod') {
    when {
        environment name: 'DEPLOY_ENV', value: 'production'
    }
    steps {
        echo 'Deploying to production environment.'
    }
}
```

- **Kapan digunakan**:  
    Jika ingin menjalankan tahap berdasarkan nilai variabel lingkungan tertentu.

---

## **4. Kondisi Berdasarkan Ekspresi (Expression)**

Menjalankan **stage** berdasarkan evaluasi ekspresi Groovy.

```groovy
stage('Approval Stage') {
    when {
        expression { return params.MANUAL_APPROVAL == true }
    }
    steps {
        echo 'Approval required for this stage.'
    }
}
```

- **Kapan digunakan**:  
    Jika membutuhkan kontrol kondisi lebih kompleks menggunakan skrip.

---

## **5. Kondisi Not (Kebalikan)**

Menjalankan **stage** hanya jika suatu kondisi tidak terpenuhi.

```groovy
stage('Skip Test') {
    when {
        not {
            branch 'main'
        }
    }
    steps {
        echo 'Running on non-main branch.'
    }
}
```

- **Kapan digunakan**:  
    Jika ingin memastikan **stage** berjalan hanya di luar kondisi tertentu.

---

## **6. Kondisi Semua (AllOf)**

Menjalankan **stage** jika semua kondisi di dalamnya terpenuhi.

```groovy
stage('Build & Test') {
    when {
        allOf {
            branch 'main'
            environment name: 'BUILD_ENV', value: 'test'
        }
    }
    steps {
        echo 'Building and testing on main branch in test environment.'
    }
}
```

- **Kapan digunakan**:  
    Jika ingin menggabungkan beberapa kondisi yang semuanya harus terpenuhi.

---

## **7. Kondisi Salah Satu (AnyOf)**

Menjalankan **stage** jika salah satu kondisi di dalamnya terpenuhi.

```groovy
stage('Deploy') {
    when {
        anyOf {
            branch 'main'
            branch 'develop'
        }
    }
    steps {
        echo 'Deploying on main or develop branch.'
    }
}
```

- **Kapan digunakan**:  
    Jika salah satu dari beberapa kondisi harus dipenuhi.

---

## **8. Kondisi Tag**

Menjalankan **stage** jika build saat ini berasal dari tag Git.

```groovy
stage('Release') {
    when {
        tag "v*"
    }
    steps {
        echo 'Running a release build for a Git tag.'
    }
}
```

- **Kapan digunakan**:  
    Untuk menjalankan tahap tertentu hanya jika build dipicu oleh tag Git.

---

## **9. Kondisi Perubahan Build (Building on Changeset)**

Menjalankan **stage** jika perubahan tertentu terjadi sejak build terakhir.

```groovy
stage('Build Changed') {
    when {
        changeset 'src/**'
    }
    steps {
        echo 'Changes detected in src directory.'
    }
}
```

- **Kapan digunakan**:  
    Untuk mengoptimalkan pipeline agar tidak selalu membangun ulang.

---

## **10. Kondisi Manual (Input)**

Menggunakan interaksi manual untuk menentukan apakah **stage** dijalankan.

```groovy
stage('Manual Approval') {
    steps {
        input 'Do you want to deploy to production?'
        echo 'Deploying to production...'
    }
}
```

- **Kapan digunakan**:  
    Jika ingin menambahkan konfirmasi manual sebelum melanjutkan pipeline.

---

## **Kombinasi Kondisi**

Anda dapat menggabungkan beberapa kondisi menggunakan `allOf` atau `anyOf`.

### Contoh Gabungan

```groovy
stage('Deploy Stage') {
    when {
        allOf {
            branch 'main'
            environment name: 'DEPLOY_ENV', value: 'production'
        }
    }
    steps {
        echo 'Deploying to production on main branch.'
    }
}
```

---

## **Tips Penggunaan**

- **Debugging**: Gunakan `echo` untuk mencetak informasi saat pipeline dijalankan, sehingga Anda tahu apakah kondisi terpenuhi.
- **Efisiensi**: Gunakan kondisi untuk menghindari pekerjaan yang tidak relevan, seperti pengujian di branch yang tidak membutuhkan tes.

Dengan memanfaatkan kondisi secara efektif, pipeline Jenkins dapat disesuaikan untuk berbagai skenario dan lingkungan dengan mudah.