# Quickstart
Berikut adalah **cheatsheet Jenkins Pipeline** untuk membantu Anda memulai dengan Jenkinsfile dan memahami dasar-dasar syntax dan fungsi yang digunakan:

---

### **Dasar-Dasar Jenkinsfile**

- Jenkinsfile ditulis dalam formaet **Declarative Pipeline** atau **Scripted Pipeline**.
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

# Macam-macam `triggers`
Penggunaan **`triggers`** di Jenkinsfile memungkinkan Anda untuk mengatur pipeline agar berjalan secara otomatis berdasarkan jadwal tertentu, perubahan kode, atau pemicu eksternal. **`triggers`** didefinisikan dalam blok **pipeline** untuk mengotomatisasi proses CI/CD.

---

## **Dasar Penggunaan `triggers`**

- **Deklarasi**: Didefinisikan di dalam blok **pipeline**.
- **Format**:
    
    ```groovy
    pipeline {
        agent any
        triggers {
            // Definisi trigger
        }
        stages {
            stage('Example') {
                steps {
                    echo 'Triggered build!'
                }
            }
        }
    }
    ```
    

---

## **Jenis-Jenis Triggers**

|**Trigger**|**Deskripsi**|**Contoh**|
|---|---|---|
|`cron`|Menjadwalkan build berdasarkan waktu menggunakan format CRON.|`cron('H 0 * * *')`|
|`pollSCM`|Memeriksa perubahan pada source code repository secara berkala.|`pollSCM('H/15 * * * *')`|
|`upstream`|Memicu build berdasarkan keberhasilan build dari job upstream (proyek lain).|`upstream(upstreamProjects: 'job1', threshold: hudson.model.Result.SUCCESS)`|
|`githubPush` (plugin)|Memicu build otomatis saat push dilakukan pada repository GitHub (memerlukan plugin GitHub Integration).|`githubPush()`|
|`gitlab` (plugin)|Memicu build berdasarkan webhook dari GitLab (memerlukan plugin GitLab).|`gitlab()`|

---

## **Cheatsheet: Contoh Penggunaan Triggers**

### **1. Menjadwalkan Build dengan `cron`**

Menjalankan pipeline setiap hari pada jam 2 pagi:

```groovy
pipeline {
    agent any
    triggers {
        cron('H 2 * * *') // Format CRON
    }
    stages {
        stage('Scheduled Task') {
            steps {
                echo 'Pipeline triggered by cron schedule.'
            }
        }
    }
}
```

- **Format CRON**:
    - `H`: Waktu acak dalam interval (disarankan untuk distribusi beban server Jenkins).
    - `*`: Semua nilai.
    - Contoh lainnya:
        - `H 0 * * 0`: Setiap Minggu pada jam 12 malam.
        - `H/15 * * * *`: Setiap 15 menit.

---

### **2. Memeriksa Perubahan dengan `pollSCM`**

Memicu build setiap 10 menit jika ada perubahan di repository SCM:

```groovy
pipeline {
    agent any
    triggers {
        pollSCM('H/10 * * * *')
    }
    stages {
        stage('SCM Polling') {
            steps {
                echo 'Pipeline triggered by SCM changes.'
            }
        }
    }
}
```

- Pastikan Jenkins terhubung dengan repository SCM Anda.

---

### **3. Memicu Build dengan `upstream`**

Pipeline ini akan berjalan jika build dari job upstream berhasil:

```groovy
pipeline {
    agent any
    triggers {
        upstream(upstreamProjects: 'job1', threshold: hudson.model.Result.SUCCESS)
    }
    stages {
        stage('Upstream Trigger') {
            steps {
                echo 'Triggered by upstream job.'
            }
        }
    }
}
```

---

### **4. Build Otomatis pada Push ke GitHub (`githubPush`)**

Memicu pipeline setiap kali push dilakukan ke repository GitHub:

```groovy
pipeline {
    agent any
    triggers {
        githubPush() // Memerlukan plugin GitHub Integration
    }
    stages {
        stage('GitHub Push') {
            steps {
                echo 'Pipeline triggered by GitHub push.'
            }
        }
    }
}
```

- **Langkah Tambahan**:
    - Konfigurasikan webhook di GitHub repository Anda untuk mengarahkan ke URL Jenkins.
    - Pastikan plugin **GitHub Integration** terpasang.

---

### **5. Build Otomatis pada Event GitLab (`gitlab`)**

Memicu pipeline berdasarkan webhook dari GitLab:

```groovy
pipeline {
    agent any
    triggers {
        gitlab() // Memerlukan plugin GitLab
    }
    stages {
        stage('GitLab Trigger') {
            steps {
                echo 'Pipeline triggered by GitLab event.'
            }
        }
    }
}
```

- **Langkah Tambahan**:
    - Tambahkan webhook di GitLab repository.
    - Pastikan plugin **GitLab** diinstal di Jenkins.

---

## **Kombinasi Triggers**

Anda dapat menggabungkan beberapa trigger sekaligus, seperti berikut:

```groovy
pipeline {
    agent any
    triggers {
        cron('H 1 * * *')          // Jadwal harian
        pollSCM('H/15 * * * *')    // Perubahan SCM
    }
    stages {
        stage('Combined Triggers') {
            steps {
                echo 'Triggered by multiple conditions.'
            }
        }
    }
}
```

---

## **Tips dan Best Practices**

1. **Gunakan `H` pada CRON**:
    - Distribusi beban server lebih merata dibandingkan waktu tetap (misalnya, "H 2 * * *" lebih baik daripada "0 2 * * *").
2. **Monitor Beban Server**:
    - Jangan gunakan `pollSCM` dengan interval terlalu sering, seperti setiap menit, karena dapat membebani server.
3. **Webhook untuk Perubahan Real-Time**:
    - Jika memungkinkan, gunakan webhook (GitHub/GitLab) daripada `pollSCM` untuk mendapatkan respon real-time dari perubahan kode.
4. **Gunakan `upstream` untuk Orkestrasi Job**:
    - Pemicu upstream cocok untuk pipeline multi-job atau pipeline yang bergantung pada hasil job lain.
5. **Debugging**:
    - Pastikan webhook atau konfigurasi SCM Anda berfungsi dengan benar jika trigger tidak berjalan.

---

Dengan **`triggers`**, Jenkins pipeline Anda dapat berjalan otomatis dan tetap sinkron dengan perubahan kode atau jadwal yang telah diatur! 🚀

# Environment Credentials
Menggunakan **environment credentials** di Jenkins memungkinkan Anda untuk menyimpan informasi sensitif, seperti username, password, API keys, atau secret tokens dengan aman di dalam Jenkins Credential Store. Anda dapat mengakses informasi ini dalam pipeline menggunakan deklarasi **environment** atau dalam blok **steps**.

Berikut adalah cara menggunakan **environment credentials** di Jenkins:

---

## **1. Menambahkan Credentials di Jenkins**

1. Masuk ke Jenkins.
2. Pergi ke **Manage Jenkins > Credentials > (Global or Folder-Specific Credentials)**.
3. Klik **Add Credentials**.
4. Pilih tipe credential, seperti:
    - **Username with password** (untuk kombinasi username dan password).
    - **Secret text** (untuk API keys atau token).
    - **SSH username with private key**.
    - **Certificate**.
5. Isi kolom yang diminta, termasuk **ID** (nama unik untuk credential tersebut).
6. Simpan credential.

---

## **2. Mengakses Environment Credentials di Jenkinsfile**

### **a. Menggunakan `environment` Secara Deklaratif**

Anda dapat mendeklarasikan credential di blok **environment**. Credential akan diekspor sebagai variabel lingkungan di dalam pipeline.

#### Contoh: Secret Text

Misalnya, Anda memiliki credential dengan ID **`MY_SECRET_KEY`**:

```groovy
pipeline {
    agent any
    environment {
        SECRET_KEY = credentials('MY_SECRET_KEY') // Mengakses credential
    }
    stages {
        stage('Use Credentials') {
            steps {
                sh 'echo $SECRET_KEY' // Menggunakan credential dalam perintah
            }
        }
    }
}
```

#### Contoh: Username dan Password

Misalnya, Anda memiliki credential dengan ID **`MY_CREDENTIALS`**:

```groovy
pipeline {
    agent any
    environment {
        USERNAME_PASSWORD = credentials('MY_CREDENTIALS') // Mengakses credential
    }
    stages {
        stage('Use Credentials') {
            steps {
                script {
                    def (username, password) = USERNAME_PASSWORD.split(':')
                    echo "Username is $username"
                    // Gunakan password dengan hati-hati
                }
            }
        }
    }
}
```

---

### **b. Menggunakan `withCredentials` di Blok Script**

Blok `withCredentials` digunakan dalam pipeline untuk mengakses credential sementara hanya untuk langkah tertentu.

#### Contoh: Secret Text

```groovy
pipeline {
    agent any
    stages {
        stage('Use Secret Text') {
            steps {
                withCredentials([string(credentialsId: 'MY_SECRET_KEY', variable: 'SECRET_KEY')]) {
                    sh 'echo "The secret key is $SECRET_KEY"'
                }
            }
        }
    }
}
```

#### Contoh: Username dan Password

```groovy
pipeline {
    agent any
    stages {
        stage('Use Username and Password') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'MY_CREDENTIALS', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo "The username is $USER and the password is $PASS"'
                }
            }
        }
    }
}
```

#### Contoh: Menggunakan SSH Private Key

```groovy
pipeline {
    agent any
    stages {
        stage('Use SSH Key') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'MY_SSH_KEY', keyFileVariable: 'SSH_KEY')]) {
                    sh 'ssh -i $SSH_KEY user@remote-server "ls -la"'
                }
            }
        }
    }
}
```

---

## **3. Tips dan Best Practices**

1. **Keamanan**: Jangan mencetak atau menyimpan credential dalam log atau file.
    - Hindari langsung mencetak `$SECRET_KEY` ke konsol karena ini berisiko mengungkap credential.
2. **Gunakan `withCredentials`**: Membatasi scope credential hanya untuk langkah tertentu untuk mencegah kebocoran di pipeline lainnya.
3. **Pilih Tipe Credential yang Tepat**:
    - Gunakan **Secret Text** untuk token atau API keys.
    - Gunakan **Username and Password** untuk otentikasi berbasis form.
4. **Modularisasi**: Bungkus akses credential dalam fungsi jika digunakan di banyak tempat.

---

## **4. Perbedaan `environment` vs `withCredentials`**

|**Fitur**|**environment**|**withCredentials**|
|---|---|---|
|Scope|Berlaku untuk seluruh stage atau pipeline|Berlaku hanya untuk blok langkah tertentu|
|Keamanan|Risiko bocor jika digunakan di luar stage|Lebih aman karena scope terbatas|
|Kompleksitas Penggunaan|Lebih sederhana|Sedikit lebih kompleks|

---

Dengan menggunakan pendekatan ini, Anda dapat memastikan bahwa credential sensitif dikelola dengan aman dan digunakan secara efisien dalam Jenkins pipeline Anda.

# Macam-macam `options`
Berikut adalah **cheatsheet** untuk penggunaan **`options`** pada Jenkinsfile. **`options`** adalah konfigurasi pipeline untuk mengontrol perilaku tertentu, seperti timeout, retry, atau menjaga log build.

---

## **Dasar Penggunaan `options`**

- **Deklarasi**: Digunakan dalam blok **pipeline** atau **stage**.
- **Format**:
    
    ```groovy
    pipeline {
        agent any
        options {
            // Pilihan global untuk pipeline
        }
        stages {
            stage('Example') {
                options {
                    // Pilihan lokal untuk stage ini
                }
                steps {
                    echo 'Hello, World!'
                }
            }
        }
    }
    ```
    

---

## **Cheatsheet: Pilihan-Pilihan `options`**

|**Option**|**Deskripsi**|**Contoh**|
|---|---|---|
|`buildDiscarder`|Menentukan kebijakan pembuangan build lama.|`buildDiscarder(logRotator(numToKeepStr: '5'))`|
|`disableConcurrentBuilds`|Mencegah eksekusi build paralel pada job yang sama.|`disableConcurrentBuilds()`|
|`skipDefaultCheckout`|Tidak secara otomatis melakukan checkout repository SCM.|`skipDefaultCheckout()`|
|`timeout`|Menghentikan build jika melebihi waktu tertentu.|`timeout(time: 10, unit: 'MINUTES')`|
|`retry`|Mencoba mengulang build jika gagal hingga jumlah tertentu.|`retry(3)`|
|`timestamps`|Menambahkan timestamp ke log konsol.|`timestamps()`|
|`ansiColor`|Memformat warna ANSI di log konsol.|`ansiColor('xterm')`|
|`disableResume`|Menonaktifkan kemampuan untuk melanjutkan build pipeline yang terputus.|`disableResume()`|
|`newContainerPerStage`|Untuk pipelines berbasis Kubernetes, membuat kontainer baru untuk setiap stage.|`newContainerPerStage()`|
|`preserveStashes`|Menyimpan stash meskipun build berhasil atau gagal.|`preserveStashes(buildCount: 5)`|
|`parallel`|Menentukan batas maksimum build paralel untuk job pipeline.|`parallel(3)`|
|`checkoutToSubdirectory`|Melakukan checkout ke subdirektori.|`checkoutToSubdirectory('source-code')`|

---

## **Contoh Implementasi**

### **1. Mengatur Timeout Global**

Membatalkan seluruh pipeline jika berjalan lebih dari 15 menit:

```groovy
pipeline {
    agent any
    options {
        timeout(time: 15, unit: 'MINUTES')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
    }
}
```

---

### **2. Mencegah Build Paralel**

Hanya satu instance pipeline yang boleh berjalan pada waktu tertentu:

```groovy
pipeline {
    agent any
    options {
        disableConcurrentBuilds()
    }
    stages {
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
    }
}
```

---

### **3. Mengatur Kebijakan Pembuangan Build**

Menyimpan hanya 10 build terakhir:

```groovy
pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    stages {
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
```

---

### **4. Menambahkan Timestamps**

Menambahkan timestamp ke setiap baris log konsol:

```groovy
pipeline {
    agent any
    options {
        timestamps()
    }
    stages {
        stage('Logging') {
            steps {
                echo 'This log has a timestamp!'
            }
        }
    }
}
```

---

### **5. Mengatur Warna ANSI**

Membuat log konsol mendukung warna ANSI (misalnya, untuk skrip berbasis CLI yang mencetak warna):

```groovy
pipeline {
    agent any
    options {
        ansiColor('xterm')
    }
    stages {
        stage('Output Colors') {
            steps {
                sh 'echo -e "\\033[32mThis is green text\\033[0m"'
            }
        }
    }
}
```

---

### **6. Menyimpan Stash**

Menyimpan hingga 3 stash terakhir meskipun build berhasil:

```groovy
pipeline {
    agent any
    options {
        preserveStashes(buildCount: 3)
    }
    stages {
        stage('Stash Example') {
            steps {
                stash name: 'example', includes: '**/*'
            }
        }
    }
}
```

---

### **7. Mencoba Ulang Build**

Mengulang langkah tertentu hingga 2 kali jika gagal:

```groovy
pipeline {
    agent any
    options {
        retry(2)
    }
    stages {
        stage('Retry Example') {
            steps {
                sh 'exit 1' // Simulasi kegagalan
            }
        }
    }
}
```

---

### **8. Kombinasi Beberapa `options`**

Menggunakan beberapa opsi sekaligus:

```groovy
pipeline {
    agent any
    options {
        disableConcurrentBuilds()
        timeout(time: 20, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '5'))
        timestamps()
    }
    stages {
        stage('Example') {
            steps {
                echo 'Running with multiple options...'
            }
        }
    }
}
```

---

Dengan **`options`**, Anda dapat mengonfigurasi pipeline agar lebih fleksibel, aman, dan efisien sesuai dengan kebutuhan.

# Macam-macam `parameters`

Berikut adalah **cheatsheet** untuk penggunaan **`parameters`** dalam Jenkinsfile. **`parameters`** digunakan untuk mendefinisikan input yang dapat diberikan saat menjalankan job Jenkins. Input ini memungkinkan pipeline lebih dinamis dan fleksibel.

---

## **Dasar Penggunaan `parameters`**

- **Deklarasi**: Diletakkan di dalam blok **pipeline**.
- **Format**:
    
    ```groovy
    pipeline {
        agent any
        parameters {
            // Definisi parameter di sini
        }
        stages {
            stage('Example') {
                steps {
                    echo "Parameter value: ${params.PARAM_NAME}"
                }
            }
        }
    }
    ```
    

---

## **Cheatsheet: Jenis Parameter**

|**Parameter**|**Deskripsi**|**Contoh**|
|---|---|---|
|`string`|Parameter berbasis string (teks).|`string(name: 'MY_PARAM', defaultValue: 'abc', description: 'String parameter')`|
|`booleanParam`|Parameter boolean (checkbox).|`booleanParam(name: 'MY_BOOL', defaultValue: true, description: 'Boolean parameter')`|
|`choice`|Parameter dengan pilihan dropdown.|`choice(name: 'MY_CHOICE', choices: ['Option1', 'Option2'], description: 'Choice parameter')`|
|`text`|Parameter berbasis teks panjang.|`text(name: 'MY_TEXT', defaultValue: 'Default text', description: 'Multiline text')`|
|`password`|Parameter untuk input password (tidak terlihat di log).|`password(name: 'MY_PASSWORD', defaultValue: 'secret', description: 'Password parameter')`|
|`file`|Parameter untuk mengunggah file.|`file(name: 'MY_FILE', description: 'File parameter')`|
|`run`|Memilih job atau build tertentu dari Jenkins.|`run(name: 'MY_RUN', job: 'MyJob', description: 'Select a job run')`|
|`credentials`|Mengambil credential tertentu dari Jenkins (tersimpan di Credential Store).|`credentials(name: 'MY_CREDENTIAL', description: 'Credential parameter')`|

---

## **Contoh Implementasi**

### **1. Parameter String**

Mendefinisikan parameter string sederhana:

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'USERNAME', defaultValue: 'guest', description: 'Enter your username')
    }
    stages {
        stage('Print Username') {
            steps {
                echo "The username is: ${params.USERNAME}"
            }
        }
    }
}
```

---

### **2. Parameter Boolean**

Mendefinisikan checkbox:

```groovy
pipeline {
    agent any
    parameters {
        booleanParam(name: 'DEPLOY', defaultValue: false, description: 'Deploy to production?')
    }
    stages {
        stage('Check Deployment') {
            steps {
                script {
                    if (params.DEPLOY) {
                        echo "Deploying to production..."
                    } else {
                        echo "Skipping deployment."
                    }
                }
            }
        }
    }
}
```

---

### **3. Parameter Dropdown Pilihan**

Membuat dropdown dengan opsi tertentu:

```groovy
pipeline {
    agent any
    parameters {
        choice(name: 'ENVIRONMENT', choices: ['Development', 'Staging', 'Production'], description: 'Select the environment')
    }
    stages {
        stage('Deploy') {
            steps {
                echo "Deploying to: ${params.ENVIRONMENT}"
            }
        }
    }
}
```

---

### **4. Parameter Multiline Text**

Membuat input teks panjang:

```groovy
pipeline {
    agent any
    parameters {
        text(name: 'RELEASE_NOTES', defaultValue: 'Write release notes here...', description: 'Provide release notes')
    }
    stages {
        stage('Display Notes') {
            steps {
                echo "Release Notes: ${params.RELEASE_NOTES}"
            }
        }
    }
}
```

---

### **5. Parameter Password**

Menyimpan input sensitif seperti password:

```groovy
pipeline {
    agent any
    parameters {
        password(name: 'ADMIN_PASS', defaultValue: 'defaultPass', description: 'Enter admin password')
    }
    stages {
        stage('Validate Password') {
            steps {
                echo "Password is hidden for security." // Jangan cetak password langsung
            }
        }
    }
}
```

---

### **6. Parameter File**

Memungkinkan pengguna mengunggah file sebagai parameter:

```groovy
pipeline {
    agent any
    parameters {
        file(name: 'UPLOAD_FILE', description: 'Upload your file')
    }
    stages {
        stage('Process File') {
            steps {
                sh 'ls -l ${params.UPLOAD_FILE}' // Menampilkan file yang diunggah
            }
        }
    }
}
```

---

### **7. Parameter Credentials**

Mengakses credentials dari Jenkins Credential Store:

```groovy
pipeline {
    agent any
    parameters {
        credentials(name: 'CRED_ID', description: 'Select credentials')
    }
    stages {
        stage('Use Credential') {
            steps {
                withCredentials([usernamePassword(credentialsId: params.CRED_ID, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo "Using username: $USER"'
                }
            }
        }
    }
}
```

---

### **8. Parameter Kombinasi**

Menggabungkan berbagai jenis parameter:

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'APP_NAME', defaultValue: 'my-app', description: 'Application name')
        booleanParam(name: 'ENABLE_FEATURE', defaultValue: false, description: 'Enable feature flag?')
        choice(name: 'DEPLOY_ENV', choices: ['Dev', 'QA', 'Prod'], description: 'Deployment environment')
    }
    stages {
        stage('Show Parameters') {
            steps {
                echo "App Name: ${params.APP_NAME}"
                echo "Enable Feature: ${params.ENABLE_FEATURE}"
                echo "Environment: ${params.DEPLOY_ENV}"
            }
        }
    }
}
```

---

## **Cara Pemanggilan**
Panggil menggunakan `params.???`, WAJIB menggunakan `params`
```Groovy
//pengaturan lainnya
	stage('Parameter') {
		steps {
			echo("Param string: ${params.USERNAME}")
			echo("Param booleanParam: ${params.DEPLOY}")
			echo("Param choice: ${params.ENVIRONMENT}")
			echo("Param text: ${params.RELEASE_NOTES}")
			echo("Param password: ${params.ADMIN_PASS}")
		}
	}
//pengaturan lainnya
```
## **Tips dan Best Practices**

1. **Validasi Parameter**: Gunakan blok **`script`** untuk memvalidasi input parameter sebelum digunakan.
2. **Keamanan**:
    - Jangan mencetak password atau credentials ke log.
    - Gunakan tipe **`credentials`** untuk mengelola data sensitif dengan aman.
3. **Parameter Default**: Selalu sediakan nilai default untuk parameter agar pipeline tidak gagal jika input tidak diberikan.
4. **Dokumentasi**: Gunakan deskripsi untuk menjelaskan tujuan setiap parameter kepada pengguna.

Dengan **`parameters`**, Anda dapat membuat Jenkins pipeline yang lebih interaktif, fleksibel, dan sesuai dengan kebutuhan pengguna. 🚀
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




# Macam-macam `when`
Di Jenkinsfile, **`when`** digunakan untuk menentukan kondisi tertentu di mana tahap (_stage_) akan dieksekusi. Hal ini memungkinkan pipeline menjadi lebih dinamis, hanya menjalankan tahap tertentu berdasarkan parameter, cabang, tag, atau kondisi lainnya.

Berikut adalah berbagai macam penggunaan **`when`** di Jenkinsfile:

---

## **Dasar Penggunaan `when`**

- **Deklarasi**: Diletakkan di dalam blok `stage`.
- **Format**:
    
    ```groovy
    pipeline {
        agent any
        stages {
            stage('Example') {
                when {
                    // Kondisi when
                }
                steps {
                    echo 'This stage ran!'
                }
            }
        }
    }
    ```
    

---

## **Cheatsheet: Macam-Macam `when`**

|**Jenis Kondisi**|**Deskripsi**|**Contoh**|
|---|---|---|
|`branch`|Mengeksekusi tahap jika pipeline berjalan di cabang tertentu.|`branch 'main'`|
|`not`|Membalikkan kondisi (negasi).|`not { branch 'main' }`|
|`allOf`|Semua kondisi harus benar (logika _AND_).|`allOf { branch 'main'; environment name: 'ENV', value: 'prod' }`|
|`anyOf`|Salah satu kondisi harus benar (logika _OR_).|`anyOf { branch 'main'; branch 'dev' }`|
|`environment`|Mengeksekusi jika variabel lingkungan (environment) memenuhi nilai tertentu.|`environment name: 'DEPLOY_ENV', value: 'prod'`|
|`equals`|Membandingkan dua nilai tertentu.|`equals expected: 'true', actual: params.DEPLOY`|
|`expression`|Mengevaluasi ekspresi Groovy.|`expression { return params.BUILD_ENV == 'staging' }`|
|`buildingTag`|Mengeksekusi jika pipeline berjalan untuk tag Git.|`buildingTag()`|
|`tag`|Mengeksekusi jika pipeline berjalan untuk tag Git tertentu.|`tag 'v1.*'`|
|`changelog`|Mengeksekusi jika ada perubahan di changelog yang sesuai dengan pola.|`changelog '.*HOTFIX.*'`|
|`changeset`|Mengeksekusi jika ada perubahan pada file/folder tertentu di SCM.|`changeset '**/*.js'`|
|`beforeAgent`|Menentukan kondisi sebelum mendeklarasikan agen (sangat berguna untuk pipeline yang kompleks).|`beforeAgent true`|

---

## **Contoh Implementasi**

### **1. Menjalankan Berdasarkan Cabang (`branch`)**

Hanya menjalankan tahap jika berada di cabang `main`:

```groovy
pipeline {
    agent any
    stages {
        stage('Run on Main Branch') {
            when {
                branch 'main'
            }
            steps {
                echo 'This runs only on the main branch!'
            }
        }
    }
}
```

---

### **2. Menjalankan Berdasarkan Variabel Lingkungan (`environment`)**

Hanya menjalankan tahap jika variabel lingkungan `DEPLOY_ENV` bernilai `prod`:

```groovy
pipeline {
    agent any
    environment {
        DEPLOY_ENV = 'prod'
    }
    stages {
        stage('Deploy to Production') {
            when {
                environment name: 'DEPLOY_ENV', value: 'prod'
            }
            steps {
                echo 'Deploying to production...'
            }
        }
    }
}
```

---

### **3. Menjalankan Berdasarkan Parameter Input (`equals`)**

Hanya menjalankan jika parameter `DEPLOY` bernilai `true`:

```groovy
pipeline {
    agent any
    parameters {
        booleanParam(name: 'DEPLOY', defaultValue: false, description: 'Should deploy?')
    }
    stages {
        stage('Conditional Deploy') {
            when {
                equals expected: true, actual: params.DEPLOY
            }
            steps {
                echo 'Deploying because DEPLOY is true!'
            }
        }
    }
}
```

---

### **4. Menjalankan Berdasarkan Ekspresi Logis (`expression`)**

Hanya menjalankan jika kondisi kompleks terpenuhi:

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'BUILD_ENV', defaultValue: 'staging', description: 'Environment to build')
    }
    stages {
        stage('Build Staging') {
            when {
                expression { return params.BUILD_ENV == 'staging' }
            }
            steps {
                echo 'Building for staging environment!'
            }
        }
    }
}
```

---

### **5. Menjalankan Jika Tag Git Tertentu (`tag`)**

Hanya menjalankan jika pipeline berjalan untuk tag `v1.*`:

```groovy
pipeline {
    agent any
    stages {
        stage('Run for Git Tag') {
            when {
                tag 'v1.*'
            }
            steps {
                echo 'This stage runs for Git tags like v1.0, v1.1, etc.'
            }
        }
    }
}
```

---

### **6. Menjalankan Jika Ada Perubahan File Tertentu (`changeset`)**

Hanya menjalankan jika ada perubahan pada file dengan ekstensi `.js`:

```groovy
pipeline {
    agent any
    stages {
        stage('Run for JS Changes') {
            when {
                changeset '**/*.js'
            }
            steps {
                echo 'Changes detected in JavaScript files!'
            }
        }
    }
}
```

---

### **7. Kombinasi Kondisi dengan `allOf` dan `anyOf`**

Menjalankan jika **semua** atau **salah satu** kondisi terpenuhi:

```groovy
pipeline {
    agent any
    stages {
        stage('All Conditions Met') {
            when {
                allOf {
                    branch 'main'
                    environment name: 'DEPLOY_ENV', value: 'prod'
                }
            }
            steps {
                echo 'All conditions met: on main branch and prod environment.'
            }
        }
        stage('Any Condition Met') {
            when {
                anyOf {
                    branch 'main'
                    branch 'dev'
                }
            }
            steps {
                echo 'This runs on either main or dev branch!'
            }
        }
    }
}
```

---

### **8. Menjalankan Sebelum Agent Ditetapkan (`beforeAgent`)**

Memeriksa kondisi sebelum agen diinisialisasi:

```groovy
pipeline {
    agent none
    stages {
        stage('Conditional Stage') {
            when {
                branch 'main'
                beforeAgent true
            }
            agent any
            steps {
                echo 'This runs only on the main branch, evaluated before agent initialization.'
            }
        }
    }
}
```

---

## **Tips dan Best Practices**

1. **Susun Logika dengan Baik**:
    - Gunakan **`allOf`** atau **`anyOf`** untuk logika kompleks.
    - Gunakan **`not`** untuk membalikkan kondisi dengan mudah.
2. **Gunakan Variabel Global**:
    - Pastikan variabel lingkungan atau parameter tersedia sebelum menggunakan **`when`**.
3. **Debugging**:
    - Tambahkan langkah cetak log atau debug jika ada masalah dengan kondisi **`when`**.
4. **Evaluasi Sebelum Agent**:
    - Gunakan **`beforeAgent`** untuk efisiensi, terutama jika kondisi kompleks.

Dengan **`when`**, Jenkins pipeline menjadi sangat fleksibel dan mampu menangani berbagai skenario dinamis! 🚀
# Macam-macam `input`
Di Jenkinsfile, **`input`** digunakan untuk meminta interaksi manual atau persetujuan pengguna sebelum melanjutkan eksekusi pipeline. Biasanya digunakan untuk operasi sensitif, seperti deployment ke production, atau untuk memilih opsi tertentu selama pipeline berjalan.

Berikut adalah macam-macam penggunaan **`input`** di Jenkinsfile:

---

## **1. Input Dasar**

Meminta konfirmasi sederhana dari pengguna:

```groovy
pipeline {
    agent any
    stages {
        stage('Approval') {
            steps {
                input message: 'Proceed to the next step?', ok: 'Yes, proceed'
            }
        }
        stage('Next Step') {
            steps {
                echo 'Continuing pipeline...'
            }
        }
    }
}
```

- **`message`**: Teks yang ditampilkan kepada pengguna.
- **`ok`**: Tombol yang harus diklik pengguna untuk melanjutkan.

---

## **2. Input dengan Parameter**

Meminta pengguna untuk memasukkan nilai tertentu:

```groovy
pipeline {
    agent any
    stages {
        stage('Input Example') {
            steps {
                script {
                    def userInput = input(
                        message: 'Enter deployment details:',
                        parameters: [
                            string(name: 'ENV', defaultValue: 'staging', description: 'Target environment'),
                            booleanParam(name: 'RELEASE', defaultValue: true, description: 'Release now?')
                        ]
                    )
                    echo "Environment: ${userInput.ENV}, Release: ${userInput.RELEASE}"
                }
            }
        }
    }
}
```

- **Parameter yang Didukung**:
    - `string`: Input teks.
    - `booleanParam`: Checkbox.
    - `choice`: Dropdown pilihan.
    - `password`: Input rahasia.

---

## **3. Input dengan Dropdown (Choice Parameter)**

Meminta pengguna memilih dari daftar opsi:

```groovy
pipeline {
    agent any
    stages {
        stage('Select Option') {
            steps {
                script {
                    def userChoice = input(
                        message: 'Choose an environment:',
                        parameters: [
                            choice(name: 'ENV', choices: ['Development', 'Staging', 'Production'], description: 'Target environment')
                        ]
                    )
                    echo "Selected Environment: ${userChoice}"
                }
            }
        }
    }
}
```

---

## **4. Input dengan Multi-Level Approval**

Memungkinkan persetujuan berlapis, misalnya persetujuan tim dan manajer:

```groovy
pipeline {
    agent any
    stages {
        stage('Team Approval') {
            steps {
                input message: 'Team approval required', ok: 'Approve'
            }
        }
        stage('Manager Approval') {
            steps {
                input message: 'Manager approval required', ok: 'Approve'
            }
        }
        stage('Proceed to Deploy') {
            steps {
                echo 'All approvals granted. Proceeding with deployment.'
            }
        }
    }
}
```

---

## **5. Input dengan User-Specific Approval**

Membatasi persetujuan hanya untuk pengguna tertentu:

```groovy
pipeline {
    agent any
    stages {
        stage('Restricted Approval') {
            steps {
                input(
                    message: 'Approval required from admin',
                    submitter: 'admin' // Hanya pengguna 'admin' yang dapat memberikan persetujuan
                )
            }
        }
        stage('Proceed') {
            steps {
                echo 'Approval received from admin.'
            }
        }
    }
}
```

- **`submitter`**: Nama pengguna Jenkins yang diizinkan memberikan persetujuan.

---

## **6. Input dengan Timeout**

Menambahkan batas waktu untuk respons pengguna:

```groovy
pipeline {
    agent any
    stages {
        stage('Approval with Timeout') {
            steps {
                script {
                    try {
                        input(
                            message: 'Approve within 1 minute',
                            ok: 'Approve',
                            timeout: 60 // Batas waktu dalam detik
                        )
                    } catch (err) {
                        echo 'Approval not received in time. Aborting...'
                        error 'Timeout reached'
                    }
                }
            }
        }
    }
}
```

---

## **7. Input dengan Penanganan Kesalahan**

Menangani skenario di mana pengguna tidak memberikan persetujuan:

```groovy
pipeline {
    agent any
    stages {
        stage('Approval with Error Handling') {
            steps {
                script {
                    try {
                        input message: 'Approve deployment?', ok: 'Approve'
                    } catch (err) {
                        echo 'Approval denied or not given. Aborting...'
                        error 'Pipeline aborted by user.'
                    }
                }
            }
        }
    }
}
```

---

## **8. Input dengan Kombinasi Parameter**

Meminta beberapa jenis input dalam satu dialog:

```groovy
pipeline {
    agent any
    stages {
        stage('Complex Input') {
            steps {
                script {
                    def userInput = input(
                        message: 'Provide deployment details:',
                        parameters: [
                            string(name: 'VERSION', defaultValue: '1.0.0', description: 'Version to deploy'),
                            choice(name: 'ENVIRONMENT', choices: ['Dev', 'QA', 'Prod'], description: 'Target environment'),
                            booleanParam(name: 'CONFIRM', defaultValue: true, description: 'Confirm deployment')
                        ]
                    )
                    echo "Version: ${userInput.VERSION}, Environment: ${userInput.ENVIRONMENT}, Confirm: ${userInput.CONFIRM}"
                }
            }
        }
    }
}
```

---

## **9. Input di dalam Conditional Stage**

Melakukan input hanya jika kondisi tertentu terpenuhi:

```groovy
pipeline {
    agent any
    stages {
        stage('Conditional Input') {
            steps {
                script {
                    if (params.DEPLOY_TO_PROD) {
                        input message: 'Approval required for production deployment', ok: 'Approve'
                    } else {
                        echo 'Skipping approval. Non-production environment.'
                    }
                }
            }
        }
    }
}
}
```

---

## **Tips dan Best Practices**

1. **Hindari Input Tidak Perlu**: Gunakan hanya jika benar-benar diperlukan untuk menghindari pipeline terhenti.
2. **Gunakan Timeout**: Selalu tambahkan timeout untuk mencegah pipeline menggantung jika tidak ada respons.
3. **Tentukan Submitter**: Batasi persetujuan pada pengguna atau grup tertentu untuk alasan keamanan.
4. **Gunakan Parameter Global**: Jika input sering digunakan, pertimbangkan untuk memindahkan logika ke parameter pipeline.
5. **Jangan Tampilkan Informasi Sensitif**: Hindari mencetak password atau input sensitif ke log.

Dengan **`input`**, Anda dapat membuat Jenkins pipeline yang lebih interaktif dan aman, memungkinkan kontrol manual dalam proses otomatisasi. 🚀
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