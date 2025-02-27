import pandas as pd
import random

# Listen mit möglichen Werten für die Variablen
makes = ['Apple', 'Samsung', 'Google', 'OnePlus', 'Sony']
models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']

# Erstellen des Datensets
data = {
    'make': [random.choice(makes) for _ in range(1000)],
    'model': [random.choice(models) for _ in range(1000)],
    'price': [round(random.uniform(300, 1200), 2) for _ in range(1000)],
    'camera_resolution': [random.randint(8, 108) for _ in range(1000)],
    'battery_life_hours': [random.randint(10, 48) for _ in range(1000)],
    'storage_size': [random.randint(32, 512) for _ in range(1000)],
    'screen_size': [round(random.uniform(4.7, 6.9), 1) for _ in range(1000)]
}

# Erstellen eines DataFrames
df = pd.DataFrame(data)

# Anzeigen der ersten Zeilen des DataFrames
print(df.head())

# Schreiben des DataFrames in eine Excel-Datei
df.to_excel('smartphones.xlsx', index=False)