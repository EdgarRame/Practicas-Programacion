import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df['Embarked'] = df['Embarked'].map({'C': 0, 'S': 1, 'Q': 0}) # Se mapea el dataset convirtiento los valores a valores númericos

df.to_csv('preprosesado.csv', index = False)
