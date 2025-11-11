import pandas as pd
import numpy as np

# 1. SETUP: DataFrame Base
print("### SETUP Y DATASET BASE ###")
datos = {
    'Nombre':  ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'Edad':    [25, 30, 22, None, 28],
    'Ciudad':  ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'Ingreso': [3000, 4500, 2800, 5000, None]}

df = pd.DataFrame(datos)
df.to_csv('actividad_semana5.csv', index=False)
print("DataFrame Base Creado y Guardado en 'actividad_semana5.csv':")
print(df)
print("-" * 50)

# --- 1) Series — crear y operar ---
print("### 1) SERIES ###")
s_lista = pd.Series([1, 2, 3, 4], name='Años')
s_dict = pd.Series({'Ene': 31, 'Feb': 28, 'Mar': 31}, name='Días')

print(f"Series desde lista:\n{s_lista}")
print(f"Acceso por clave 'Feb': {s_dict['Feb']}")
s_lista[0] = 10 # Modificar
print(f"Operación (* 2):\n{s_lista * 2}")
print("-" * 50)

# --- 2) DataFrame — crear y explorar ---
print("### 2) DATAFRAME - CREAR Y EXPLORAR ###")
df_simple = pd.DataFrame(datos) # Reutilizamos 'datos'
df_simple.columns = ['Nombre', 'Edad', 'Ciudad', 'Ingreso_mensual']
print("Tipos de datos (df.dtypes):")
print(df_simple.dtypes)
print("-" * 50)

# --- 3) Inspeccionar y explorar ---
print("### 3) INSPECCIONAR ###")
print("df.head(2):")
print(df.head(2))
print("\ndf.info():")
df.info()
print(f"\ndf.shape: {df.shape}")
print("\ndf.describe():")
print(df.describe())
print("-" * 50)

# --- 4) Acceder a columnas y filas ---
print("### 4) ACCEDER DATOS ###")
nombre_series = df['Nombre']
print("Columna Nombre (Series):\n", nombre_series)

fila_1_loc = df.loc[1]
print("\nFila con índice 1 (loc):\n", fila_1_loc)

valor_especifico = df.loc[1, 'Edad']
print(f"\nValor (fila 1, columna 'Edad'): {valor_especifico}")
print("-" * 50)

# --- 5) Operaciones básicas ---
print("### 5) OPERACIONES BÁSICAS ###")
df_op = df.copy()

# 5.1 Incrementa Edad en 5 años (rellenamos nulos temporalmente para la suma)
df_op['Edad_Nueva'] = df_op['Edad'].fillna(0) + 5
print("Edad + 5 (manejo de nulos temporal):\n", df_op[['Edad', 'Edad_Nueva']])

# 5.2 Ingreso_anual (maneja nulos con 0)
df_op['Ingreso_anual'] = df_op['Ingreso'].fillna(0) * 12
print("\nColumna Ingreso_anual:\n", df_op[['Ingreso', 'Ingreso_anual']])
print("-" * 50)

# --- 6) Filtrar datos ---
print("### 6) FILTRAR DATOS ###")
# Nota: La comparación con None/NaN resulta en False, por lo que no causa error.
print("Filtro: Edad > 30 (Resultado Vacío, ya que nadie es > 30):")
print(df_op[df_op['Edad'] > 30])

ciudades_filtro = ['Madrid', 'Lima']
df_ciudades = df_op[df_op['Ciudad'].isin(ciudades_filtro)]
print("\nFiltro: Ciudad es 'Madrid' o 'Lima':")
print(df_ciudades)
print("-" * 50)

# --- 7) Manejo de valores faltantes ---
print("### 7) MANEJO DE NULOS ###")
df_nulos = df.copy()
print("Nulos Iniciales:\n", df_nulos.isna().sum())

# Rellenar
mediana_ingreso = df_nulos['Ingreso'].median()

df_nulos['Edad'] = df_nulos['Edad'].fillna(0)
df_nulos['Ciudad'] = df_nulos['Ciudad'].fillna('Desconocido')
df_nulos['Ingreso'] = df_nulos['Ingreso'].fillna(mediana_ingreso)

print("\nDataFrame con Nulos Rellenados:")
print(df_nulos)
print("-" * 50)

# --- 8) Leer y guardar datos ---
print("### 8) LEER Y GUARDAR ###")
df_leido = pd.read_csv('actividad_semana5.csv')
print("CSV Leído (actividad_semana5.csv):\n", df_leido.head(2))

# Guardar un CSV con columnas seleccionadas
df_leido[['Nombre', 'Edad', 'Ciudad']].to_csv('datos_seleccionados.csv', index=False)
print("\nCSV 'datos_seleccionados.csv' guardado.")
print("-" * 50)

# --- 9) Ejercicio integrado ---
print("### 9) EJERCICIO INTEGRADO ###")
df_final = df.copy()

# 1. Ingreso Anual (convierte nulos a 0 para el cálculo)
df_final['Ingreso_anual'] = df_final['Ingreso'].fillna(0) * 12

# 2. Incrementa Edad en 5
df_final['Edad'] = df_final['Edad'].fillna(0) + 5

# 3. Filtra Ingreso_anual > 36000
df_filtrado = df_final[df_final['Ingreso_anual'] > 36000]

# 4. Ordena por Ingreso_anual descendente
df_ordenado = df_filtrado.sort_values(by='Ingreso_anual', ascending=False)

# 5. Guarda el resultado
df_ordenado[['Nombre', 'Edad', 'Ingreso', 'Ingreso_anual']].to_csv('personas_filtradas.csv', index=False)

print("Resultado final (Personas con Ingreso_anual > 36000, ordenado):")
print(df_ordenado)
print("El resultado se guardó en 'personas_filtradas.csv'.")