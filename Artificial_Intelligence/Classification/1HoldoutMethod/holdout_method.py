from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def main():
    # Asumsikan data sudah dalam bentuk X (fitur) dan y (label)
    data = pd.read_csv('../iris.csv')
    X = data.iloc[:, :-1] #data
    y = data.iloc[:, -1] #label
    #print(X,y)
    
    # Bagi data menjadi data latih dan data uji
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
    
    # Buat model KNN
    knn = KNeighborsClassifier(n_neighbors=5)
    
    # Latih model
    knn.fit(X_train, y_train)
    
    # Prediksi pada data uji
    y_pred = knn.predict(X_test)
    
    # Hitung akurasi
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Akurasi Holdout Method: {accuracy*100}%")
    
if __name__ == "__main__":
    main()