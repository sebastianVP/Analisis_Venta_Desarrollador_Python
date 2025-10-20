import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#1. CARGANDO DATOS
def cargar_datos(ruta_archivo):
    df = pd.read_csv(ruta_archivo)
    print("Datos cargados correctamente.")
    return df


if __name__ == "__main__":
    df = cargar_datos("ventas.csv")
    print(df)