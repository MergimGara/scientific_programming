import os
import json
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

# Laden Sie die Kaggle-API-Anmeldeinformationen
with open('/home/vscode/.config/kaggle/kaggle.json') as f:
    kaggle_data = json.load(f)

os.environ['KAGGLE_USERNAME'] = kaggle_data['username']
os.environ['KAGGLE_KEY'] = kaggle_data['key']

# Authentifizieren Sie die Kaggle API
api = KaggleApi()
api.authenticate()

# Laden Sie das Titanic-Dataset herunter
dataset = 'yasserh/titanic-dataset'
file_name = 'Titanic-Dataset.csv'
api.dataset_download_file(dataset, file_name, path='./challenge')

# Entpacken Sie die heruntergeladene Datei
with zipfile.ZipFile(f'./challenge/{file_name}.zip', 'r') as zip_ref:
    zip_ref.extractall('./challenge')

# Laden Sie das Titanic-Dataset
df = pd.read_csv('./challenge/Titanic-Dataset.csv')

# Identifizieren Sie die Datentypen
print(df.dtypes)

# Transformieren Sie die Variable 'Sex'
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
print(df[['Sex']].head())

# Erstellen Sie ein Teilset der Titanic-Daten
subset = df[(df['Survived'] == 1) & 
            ((df['Sex'] == 1) & (df['Age'] > 45) | 
             (df['Sex'] == 0) & (df['Age'] < 20))]
print(subset.head())

# Zählen Sie die Anzahl der ausgewählten Passagiere
num_selected_passengers = subset.shape[0]
print(f"Anzahl der ausgewählten Passagiere: {num_selected_passengers}")