import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df['Embarked'] = df['Embarked'].map({'C': 0, 'S': 1, 'Q': 0}) # Se mapea el dataset convirtiento los valores a valores númericos

df.to_csv('preprosesado.csv', index = False)
