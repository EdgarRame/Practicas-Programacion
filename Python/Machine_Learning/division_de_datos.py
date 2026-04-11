import pandas as pd
from sklearn.model_selection import train_test_split

# Llamado al Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df['Embarked'] = df['Embarked'].map({'C': 0, 'S': 1, 'Q': 2})
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1}) # Se mapea el dataset convirtiento los valores a valores númericos
df = df[['Pclass', 'Sex', 'Age', 'Embarked','Survived']].dropna()

df.to_csv('preprosesado.csv', index = False)

# División para el train y test
X = df.drop('Survived', axis = 1) #Variable donde le indicó que eliminara toda la columna entregada y se usara el resto de columnas
y = df['Survived']# Variable donde se le indica que columna sera utilizada

# Variables para el uso de entrenamiento y prueba del modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Datos que se usaran para las pruebas: ", X_test.shape)
print("Datos que se usaran para el entrenamiento: ", X_train.shape)