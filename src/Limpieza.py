import pandas as pd

ruta = "Dataset_Talento.csv"

def cargar_y_limpiar_datos(ruta):
    """
    Carga un dataset conservando todas las columnas,
    limpia valores nulos reemplazando con el promedio de la columna
    y guarda correctamente en UTF-8 con acentos.
    """

    # Leer el CSV original usando codificación UTF-8
    df = pd.read_csv(ruta, encoding="utf-8")

    # Reemplazar NaN numéricos con el promedio de su columna
    columnas_numericas = df.select_dtypes(include=["float64", "int64"]).columns
    for col in columnas_numericas:
        promedio = df[col].mean()
        df[col] = df[col].fillna(promedio)

    # Rellenar valores faltantes categóricos
    if "fallo_detectado" in df.columns:
        df["fallo_detectado"] = df["fallo_detectado"].fillna("No")
    if "tipo_fallo" in df.columns:
        df["tipo_fallo"] = df["tipo_fallo"].fillna("Sin_fallo")

    # Convertir columnas relevantes a tipo categoría
    columnas_categoricas = ["turno", "operador_id", "maquina_id", "producto_id", "fallo_detectado", "tipo_fallo"]
    for col in columnas_categoricas:
        if col in df.columns:
            df[col] = df[col].astype("category")

    # Guardar el archivo limpio en UTF-8
    df.to_csv("Dataset_Talento_Limpio_UTF8.csv", index=False, encoding="utf-8")

    return df

# Ejecutar limpieza
cargar_y_limpiar_datos(ruta)