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
    df['anio'] = df['fecha'].dt.year
    #df['mes'] = df['fecha'].dt.month
    df['mes'] = df['fecha'].dt.to_period('M')


    # Facturación por MES
    facturacion_mensual = df.groupby('mes')['total'].sum().reset_index()


    print("Análisis básico completado.\n")
    return producto_mas_vendido, cantidad_top,producto_mayor_facturacion, facturacion_mensual

#-------------PASO 3.  Persistencia en base de datos ------------
def guardar_en_db(df, facturacion_mensual):
    conexion = sqlite3.connect("db.sqlite3")

    # 🔹 Convertir fecha al formato de texto compatible
    if 'fecha' in df.columns:
        df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce').dt.strftime('%Y-%m-%d')

    # 🔹 Convertir columnas no soportadas
    for data in [df, facturacion_mensual]:
        for col in data.columns:
            # Si la columna contiene tipos complejos, conviértela a string
            if any(data[col].apply(lambda x: isinstance(x, (pd.Timestamp, pd.Period, list, dict)))):
                data[col] = data[col].astype(str)

    # Guardar en la base de datos
    df.to_sql("ventas", conexion, if_exists="replace", index=False)
    facturacion_mensual.to_sql("facturacion_mensual", conexion, if_exists="replace", index=False)

    conexion.close()
    print("Datos guardados correctamente en SQLite.\n")
#-------------PASO 4.   Visualización simple ------------

def generar_grafico(facturacion_mensual):
    plt.figure(figsize=(8, 5))
    plt.bar(facturacion_mensual['mes'].astype(str), facturacion_mensual['total'])
    plt.title("Facturación Total por Mes")
    plt.xlabel("Mes")
    plt.ylabel("Facturación (S/)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafico.png")
    plt.close()
    print("Gráfico generado y guardado como grafico.png\n")


if __name__ == "__main__":
    df = cargar_datos("ventas.csv")
    df = clean_datos(df)
    producto_mas_vendido,cantidad_top, producto_mayor_facturacion, facturacion_mensual = analisis_basico(df)
    print(facturacion_mensual)
    guardar_en_db(df,facturacion_mensual)
    generar_grafico(facturacion_mensual)
    print(f"a) El Producto más vendido es: {producto_mas_vendido} con {cantidad_top} unidades")
    print(f"b) El Producto con mayor facturación: {producto_mayor_facturacion}")
    print(f"c) La Facturacion total por mes es:\n")
    print(facturacion_mensual)