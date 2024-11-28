import numpy as np
import pandas as pd
from sklearn.model_selection import LeaveOneOut
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    # Data yang diberikan
    data = pd.read_csv('Classification/data/iris.csv')
    # Pisahkan fitur dan label
    X = data.iloc[:, :-1].values # Menggunakan .iloc untuk mengakses semua kolom kecuali yang terakhir
    y = data.iloc[:, -1].values # Mengakses kolom terakhir sebagai label
    # Inisialisasi model
    model = KNeighborsClassifier(n_neighbors=19)
    # Inisialisasi Leave-One-Out Cross Validation
    loo = LeaveOneOut()
    accuracy_scores = []
    # Looping untuk setiap fold
    for train_index, test_index in loo.split(X):
        # Bagi dataset menjadi training dan testing set
        X_train, X_test= X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        # Train the model
        model.fit(X_train, y_train)
        # Predict on test set
        y_pred = model.predict(X_test)
        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_scores.append(accuracy)
    # Rata-rata hasil akurasi
    average_accuracy = np.mean(accuracy_scores)
    
    print("Accuracy per iteration:", accuracy_scores)
    print("Average Accuracy LOOCV:", average_accuracy*100)

if __name__ == "__main__":
    main()
    
    