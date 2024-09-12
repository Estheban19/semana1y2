import pandas as pd

data = {
    'Nombre': ['Juan', 'Ana', 'Luis','Pedro'],
    'Edad': [15, 14, 16,15],
    'Promedio': [8.5, 9.0, 7.5,8.0]
}

df = pd.DataFrame(data)

print(df.head(1))