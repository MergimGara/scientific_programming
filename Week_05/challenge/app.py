"""
This module implements a Flask web application that displays
average apartment prices, areas, and a histogram of price distribution.
"""

import io
import base64
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Daten laden
df = pd.read_csv('apartments_data_enriched_cleaned.csv')

# Durchschnittspreis und Durchschnittsfläche berechnen
average_price = df['price'].mean()
average_area = df['area'].mean()

# Preisverteilung als Histogramm erstellen
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=30, edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(True)

# Histogramm in Base64 kodieren
img = io.BytesIO()
plt.savefig(img, format='png')
img.seek(0)
plot_url = base64.b64encode(img.getvalue()).decode()

@app.route('/')
def index():
    return render_template('index.html', average_price=average_price, average_area=average_area, plot_url=plot_url, tables=[df.to_html(classes='data', header="true")])

if __name__ == '__main__':
    app.run(debug=True)