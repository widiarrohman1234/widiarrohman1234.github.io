from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def main():
    print("Random subsampling")
    # Asumsikan data sudah dalam bentuk X (fitur) dan y (label)
    data = pd.read_csv('../iris.csv')
    X = data.iloc[:, :-1] #data
    y = data.iloc[:, -1] #label
    # Buat model KNN
    model = KNeighborsClassifier(n_neighbors=3)
    
    # Perform random subsampling multiple times
    n_iterations = 30
    accuracy_scores = []

    for i in range(n_iterations):
        # Split data menjadi training dan validation set (80% training, 20% validation)
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=i)
        #print("X_train\n",X_train)
        #print("y_train\n",y_train)
        #break
        # Train the model
        model.fit(X_train, y_train)
        
        # Predict on validation set
        y_pred = model.predict(X_val)
        
        # Calculate accuracy
        accuracy = accuracy_score(y_val, y_pred)
        accuracy_scores.append(accuracy*100)
        
    # Rata-rata hasil akurasi
    average_accuracy = np.mean(accuracy_scores)
    
    print("Akurasi per iterasi:", accuracy_scores)
    print("Rata-rata akurasi:", average_accuracy)


if __name__ == "__main__":
    main()