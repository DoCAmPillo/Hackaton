import pandas as pd

# Cargar el dataset limpio
ruta = "Dataset_Talento_Limpio_UTF8.csv"
df = pd.read_csv(ruta)

# Columnas numéricas que vamos a revisar por outliers
columnas_numericas = [
    "eficiencia_porcentual", "temperatura", "vibración", "humedad",
    "tiempo_ciclo", "cantidad_producida", "unidades_defectuosas",
    "consumo_energia", "paradas_programadas", "paradas_imprevistas"
]

# Eliminar outliers con el método IQR
def eliminar_outliers_iqr(df, columnas):
    df_limpio = df.copy()
    for col in columnas:
        Q1 = df_limpio[col].quantile(0.25)
        Q3 = df_limpio[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        df_limpio = df_limpio[(df_limpio[col] >= limite_inferior) & (df_limpio[col] <= limite_superior)]
    return df_limpio

# Aplicar limpieza
df_sin_outliers = eliminar_outliers_iqr(df, columnas_numericas)

# Guardar el nuevo archivo limpio sin outliers
df_sin_outliers.to_csv("outputs/Dataset_Talento_Sin_Outliers.csv", index=False, encoding="utf-8")

print(f"Filas originales: {len(df)}")
print(f"Filas sin outliers: {len(df_sin_outliers)}")