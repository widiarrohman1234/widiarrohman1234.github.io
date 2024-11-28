# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:03:25 2024

@author: widia
"""

from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

def main():
    # Asumsikan data sudah dalam bentuk X (fitur) dan y (label)
    data = pd.read_csv('../iris.csv')
    X = data.iloc[:, :-1] #data
    y = data.iloc[:, -1] #label
    # Buat model KNN
    knn = KNeighborsClassifier(n_neighbors=6)

    # Lakukan cross-validation dengan 5-fold
    scores = cross_val_score(knn, X, y, cv=5)

    # Hitung akurasi rata-rata
    print("Akurasi K-Fold Cross Validation:", scores.mean()*100)

if __name__ == "__main__":
    main()
    
    