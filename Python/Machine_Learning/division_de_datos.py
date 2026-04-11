import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df['Embarked'] = df['Embarked'].map({'C': 0, 'S': 1, 'Q': 2})
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1}) # Se mapea el dataset convirtiento los valores a valores númericos
df = df[['Pclass', 'Sex', 'Age', 'Embarked','Survived']].dropna()

df.to_csv('preprosesado.csv', index = False)
