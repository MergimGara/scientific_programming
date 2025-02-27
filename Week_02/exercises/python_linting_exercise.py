"""This module demonstrates basic DataFrame operations using pandas."""

import pandas as pd

data = pd.DataFrame({
    'Name': ['tom', 'nick', 'krish', 'jack'],
    'Age': [20, 21, 19, 18]
})

# Create DataFrame
df = pd.DataFrame(data)
print(type(df))

# Print the output
print(df.head())
