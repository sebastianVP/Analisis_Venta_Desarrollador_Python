# Análisis de Ventas – Proyecto de Python  
Repositorio: [Analisis_Venta_Desarrollador_Python](https://github.com/sebastianVP/Analisis_Venta_Desarrollador_Python)


## Descripción
Este proyecto tiene como objetivo realizar un análisis de datos de ventas a partir de un archivo `ventas.csv`. Se efectúan los siguientes pasos:  
- Carga de datos con Pandas  
- Limpieza de datos (filas nulas, cantidades/ precios inválidos)  
- Cálculo de nueva columna `total = cantidad × precio_unitario`  
- Análisis básico:
  - Producto más vendido por cantidad  
  - Producto con mayor facturación  
  - Facturación total por mes (o año‑mes)  
- Persistencia de resultados en base de datos SQLite  
- Generación de un gráfico (con Matplotlib) que muestra la facturación por mes  
- Inclusión de prueba automatizada (con pytest)  
- Script SQL para consultar los 3 productos más vendidos

## Estructura del proyecto  
```
Analisis_Venta_Desarrollador_Python/
│
├── ventas.csv                      ← Archivo de datos de entrada  
├── main_app.py                     ← Script principal de análisis  
├── consultas_productos.sql         ← Script SQL para consultar productos más vendidos  
├── db.sqlite3                      ← Base de datos SQLite generada (output)  
├── grafico.png                     ← Gráfico generado (output)  
├── test_funciones.py               ← Prueba(s) automatizada(s) con pytest  
├── requirements.txt                ← Dependencias del proyecto  
└── README.md                       ← Este archivo  
```

## 🛠 Instalación y requisitos  
### 1. Clonar el repositorio  
```bash
git clone https://github.com/sebastianVP/Analisis_Venta_Desarrollador_Python.git
cd Analisis_Venta_Desarrollador_Python
```

### 2. Crear y activar un entorno virtual (opcional pero recomendado)  
```bash
python3 -m venv venv
source venv/bin/activate   # En Linux/macOS
# o en Windows:
# venv\Scripts\activate
```
### 3. Instalar las dependencias  
```bash
pip install -r requirements.txt
```
---

## 🚀 Cómo ejecutar el script principal  
```bash
python main_app.py
```
Este comando realizará todo el flujo de trabajo:
- Leer el archivo `ventas.csv`  
- Limpiar los datos  
- Añadir la columna `total`  
- Calcular los indicadores solicitados  
- Crear columnas `anio`, `mes` si corresponde  
- Guardar los resultados en `db.sqlite3`  
- Generar el gráfico `grafico.png`  
- Imprimir en la consola los resultados clave (producto más vendido, etc.)

---

## 📊 Generar el gráfico  
Al ejecutar el script principal, se genera automáticamente un archivo `grafico.png` que muestra la facturación total por mes (o por período año‑mes).  
Puedes abrir este archivo para visualizar el resultado gráfico del análisis.

---

## 🧪 Correr los tests  
Se incluye archivo de pruebas `test_funciones.py`.  
Para ejecutar las pruebas, simplemente corre:
```bash
pytest
```
o  
```bash
pytest test_funciones.py
```
Se comprobará al menos que la función de cálculo del total (`cantidad × precio_unitario`) funciona correctamente.

---

## 🗃 Persistencia en base de datos & consultas  
### Estructura de la base de datos  
Se utiliza SQLite y se generan al menos dos tablas:  
- `ventas`: contiene el detalle de cada venta (fecha, producto, cantidad, precio_unitario, total, anio, mes)  
- `facturacion_mensual`: contiene datos agregados por mes (o año/mes) con columnas `anio`, `mes`, `total`

### Consulta SQL de ejemplo  
Se incluye el archivo `consultas_productos.sql` que contiene la instrucción para obtener los 3 productos más vendidos.  
Puedes ejecutarlo desde la terminal así:
```bash
sqlite3 db.sqlite3 < consultas_productos.sql
```
Contenido ejemplo:
```sql
SELECT producto,
       SUM(cantidad) AS total_vendida
FROM ventas
GROUP BY producto
ORDER BY total_vendida DESC
LIMIT 3;
```

---