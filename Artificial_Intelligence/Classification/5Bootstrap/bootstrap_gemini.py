import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

def main():
    # Load data (asumsi data sudah dalam bentuk X (fitur) dan y (label))
    data = pd.read_csv('Classification/data/iris.csv')
    # Pisahkan fitur dan label
    X = data.iloc[:, :-1].values # Menggunakan .iloc untuk mengakses semua kolom kecuali yang terakhir
    y = data.iloc[:, -1].values # Mengakses kolom terakhir sebagai label
    # Jumlah iterasi bootstrap
    n_iterations = 100

    # Inisialisasi list untuk menyimpan skor
    scores = []

    for i in range(n_iterations):
        # Buat dataset bootstrap
        X_bootstrap, y_bootstrap = resample(X, y)

        # Bagi data menjadi data latih dan data uji
        X_train, X_test, y_train, y_test = train_test_split(X_bootstrap, y_bootstrap, test_size=0.2)

        # Buat model KNN
        knn = KNeighborsClassifier(n_neighbors=3)

        # Latih model
        knn.fit(X_train, y_train)

        # Evaluasi model
        score = knn.score(X_test, y_test)
        scores.append(score)

    # Hitung rata-rata dan standar deviasi
    mean_score = np.mean(scores)
    std_score = np.std(scores)

    print("Mean accuracy:", mean_score)
    print("Standard deviation:", std_score)
    
if __name__ == "__main__":
    main()