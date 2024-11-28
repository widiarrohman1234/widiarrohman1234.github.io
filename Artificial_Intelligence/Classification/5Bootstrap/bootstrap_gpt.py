import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.utils import resample

# Fungsi untuk melakukan Bootstrap validation
def bootstrap_validation(X, y, model, n_iterations=100):
    n_samples = len(X)
    accuracy_scores = []

    # Lakukan iterasi bootstrap
    for i in range(n_iterations):
        # Ambil sample acak dengan replacement untuk training
        X_train, y_train = resample(X, y, n_samples=n_samples)
        
        # Data yang tidak terambil (out-of-bag) untuk testing
        oob_mask = np.ones(n_samples, dtype=bool)
        for idx in np.unique(X_train, axis=0):
            oob_mask[(X == idx).all(axis=1)] = False

        X_test, y_test = X[oob_mask], y[oob_mask]

        if len(X_test) > 0:
            # Train model
            model.fit(X_train, y_train)

            # Predict on out-of-bag data
            y_pred = model.predict(X_test)

            # Hitung akurasi
            accuracy = accuracy_score(y_test, y_pred)
            accuracy_scores.append(accuracy)
    
    # Rata-rata hasil akurasi dari bootstrap
    average_accuracy = np.mean(accuracy_scores)
    return accuracy_scores, average_accuracy

# Main function
def main():
    # Load dataset
    data = pd.read_csv('Classification/data/iris-example.csv')
    
    # Pisahkan fitur dan label
    X = data.iloc[:, :-1].values  # Mengonversi ke numpy array
    y = data.iloc[:, -1].values   # Mengonversi ke numpy array
    
    # Inisialisasi model KNN
    model = KNeighborsClassifier(n_neighbors=3)
    
    # Lakukan Bootstrap validation
    accuracy_scores, average_accuracy = bootstrap_validation(X, y, model, n_iterations=100)
    
    print("Accuracy per iteration:", accuracy_scores)
    print("Average Accuracy:", average_accuracy)

if __name__ == "__main__":
    main()
