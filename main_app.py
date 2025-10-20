import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#-------------PASO 1.  Carga y limpieza de datos------------

def cargar_datos(ruta_archivo):
    """
    §  Lea el archivo usando pandas.
    """
    df = pd.read_csv(ruta_archivo)
    print("\nDatos cargados correctamente.\n")
    return df

#  LIMPIEZA DE DATOS
def clean_datos(df):
    """
    §  Limpie filas con datos nulos o inconsistentes (ej. cantidad negativa).
    §  Genere una columna total = cantidad * precio_unitario.
    """
    # Eliminar filas  valores nulos
    df = df.dropna()

    # Eliminar filas cantidad o precio negativo
    df = df[(df['cantidad'] > 0) & (df['precio_unitario'] > 0)]

    # Columna 'total'
    df['total'] = df['cantidad'] * df['precio_unitario']

    print("Datos limpiados correctamente.\n")
    return df

#-------------PASO 2.  Análisis básico ------------
def analisis_basico(df):
    """
    a) El producto más vendido por cantidad -> PMV.
    b) El producto con mayor facturación total-> PMFT.
    c) La facturación total por mes -> FTM.
    """
    producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
    producto_mayor_facturacion = df.groupby('producto')['total'].sum().idxmax()
    cantidad_top               = df.groupby('producto')['total'].sum().max()
    # Facturación por mes- Creamos la columna  del Mes ->AÑO 2023(UNICO AÑO)
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['Mes'] = df['fecha'].dt.to_period('M')
    facturacion_mensual = df.groupby('Mes')['total'].sum().reset_index()

    print("Análisis básico completado.\n")
    return producto_mas_vendido, cantidad_top,producto_mayor_facturacion, facturacion_mensual

#-------------PASO 3.  Persistencia en base de datos ------------




if __name__ == "__main__":
    df = cargar_datos("ventas.csv")
    df = clean_datos(df)
    producto_mas_vendido,cantidad_top, producto_mayor_facturacion, facturacion_mensual = analisis_basico(df)
    print(f"a) El Producto más vendido es: {producto_mas_vendido} con {cantidad_top} unidades")
    print(f"b) El Producto con mayor facturación: {producto_mayor_facturacion}")
    print(f"c) La Facturacion total por mes es:\n")
    print(facturacion_mensual)
    #print(df)