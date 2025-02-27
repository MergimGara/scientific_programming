import pandas as pd

# Laden Sie die Big Mac Daten
file_path = './data/BigmacPrice.csv'  # Angepasster Pfad
df = pd.read_csv(file_path)
print("Erste Zeilen der Big Mac Daten:")
print(df.head())  # Debug-Ausgabe

# Filtern Sie die Daten für die Schweiz und die USA
print("Filtern der Daten für die Schweiz und die USA...")
switzerland = df[(df['name'] == 'Switzerland') & (df['date'].str.startswith('2002') | df['date'].str.startswith('2022'))]
usa = df[(df['name'] == 'United States') & (df['date'].str.startswith('2002') | df['date'].str.startswith('2022'))]
print("Gefilterte Daten für die Schweiz:")
print(switzerland)  # Debug-Ausgabe
print("Gefilterte Daten für die USA:")
print(usa)  # Debug-Ausgabe

# Berechnen Sie die Preisänderungen
if not switzerland.empty and not usa.empty:
    switzerland_change = switzerland[switzerland['date'].str.startswith('2022')]['dollar_price'].values[0] - switzerland[switzerland['date'].str.startswith('2002')]['dollar_price'].values[0]
    usa_change = usa[usa['date'].str.startswith('2022')]['dollar_price'].values[0] - usa[usa['date'].str.startswith('2002')]['dollar_price'].values[0]

    print(f"Preisänderung in der Schweiz (2002-2022): {switzerland_change}")
    print(f"Preisänderung in den USA (2002-2022): {usa_change}")

    # Vergleichen Sie die Preisänderungen
    if switzerland_change > usa_change:
        print("Die Preissteigerung in der Schweiz ist höher als in den USA.")
    else:
        print("Die Preissteigerung in den USA ist höher als in der Schweiz.")
else:
    print("Daten für die Jahre 2002 und 2022 fehlen.")