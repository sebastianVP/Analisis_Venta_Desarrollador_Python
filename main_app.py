import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#1. CARGANDO DATOS
def cargar_datos(ruta_archivo):
    df = pd.read_csv(ruta_archivo)
    print("Datos cargados correctamente.")
    return df

#2. LIMPIEZA DE DATOS
def clean_datos(df):
    # Eliminar filas  valores nulos
    df = df.dropna()

    # Eliminar filas cantidad o precio negativo
    df = df[(df['cantidad'] > 0) & (df['precio_unitario'] > 0)]

    # Columna 'total'
    df['total'] = df['cantidad'] * df['precio_unitario']

    print("Datos limpiados correctamente.")
    return df

if __name__ == "__main__":
    df = cargar_datos("ventas.csv")
    df = clean_datos(df)
    print(df)