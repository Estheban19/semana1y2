import pandas as pd

tabla= { 
    'Nombre': [ 'juan', 'jhoy', 'alex'],
    'DNI': [98745632, 98746321, 1478532],
    'NUMERO': [1,2,3]
}
DF = pd.DataFrame(tabla)

print(DF.head(1))
