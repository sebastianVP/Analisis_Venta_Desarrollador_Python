import pandas as pd
from main_app import clean_datos

def test_calculo_total():
    data = {'cantidad': [2, 3], 'precio_unitario': [100, 200]}
    df = pd.DataFrame(data)
    df = clean_datos(df)
    assert all(df['total'] == [200, 600]), "Error en el cálculo del total"