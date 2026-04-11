import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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

# Impresión para ver cuantos datos se usan para que motivo
print("Datos que se usaran para las pruebas: ", X_test.shape)
print("Datos que se usaran para el entrenamiento: ", X_train.shape)

#Instanciamiento del arbol de decisión
arbol = DecisionTreeClassifier(random_state = 42)

# Entrenamiento
arbol.fit(X_train, y_train)

# Prueba
prueba = arbol.predict(X_test)

# Impresión de la presición del modelo
print("La precisión es: ", accuracy_score(y_test, prueba))

columnas = X_train.columns # Se piden los nombres de las columnas
peso = arbol.feature_importances_ # Se pide el peso de los valores

# Creación de una tabla para un mejor control
resultado = pd.DataFrame({
    'Caracteristicas': columnas, # Se iguala Caracteristicas con la variable columnas
    'Peso': peso # Se iguala Peso con la variable peso
    })

resultado = resultado.sort_values(by= 'Peso', ascending= False) #Se ordenan los valores por peso de mayor a menor

# Impresión del peso
print("\nEl peso es: ")
print(resultado)

# Manejo de matriz de confución
print("\nLa cantidad de errores es de: ")
matriz = confusion_matrix(y_test, prueba)
print(matriz)

# Manejo de Reporte integral
print("\nEl reporte: ")
reporte = (classification_report(y_test, prueba))
print(reporte)


posibilidad = pd.DataFrame({
    'Pclass': [3],
    'Sex': [1],
    'Age': [27],
    'Embarked': [0]
})

# Usamos la variable 'modelo' (que ya está entrenada gracias al paso 5)
resultado = arbol.predict(posibilidad)

if resultado[0] == 1:
    print("El modelo indica que sobrevivirias")
else:
    print("El modelo indica que moririas")