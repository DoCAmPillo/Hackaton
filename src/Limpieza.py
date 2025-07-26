import pandas as pd

ruta = "Dataset_Talento.csv"

def cargar_y_limpiar_datos(ruta):
    """
    Carga un dataset conservando todas las columnas,
    limpia valores nulos y guarda correctamente en UTF-8 con acentos.
    """

    # Leer el CSV original usando la codificación compatible con acentos
    df = pd.read_csv(ruta, encoding="latin-1")  # <- lectura clave

    # Reemplazar NaN numéricos por 0 (especialmente sensores)
    columnas_a_cero = ["temperatura", "vibración", "humedad", "tiempo_ciclo"]
    for col in columnas_a_cero:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    # Reemplazar otras columnas numéricas con 0 si es necesario
    columnas_numericas = df.select_dtypes(include=["float64", "int64"]).columns
    columnas_extra = [col for col in columnas_numericas if col not in columnas_a_cero]
    df[columnas_extra] = df[columnas_extra].fillna(0)

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

    # Guardar el archivo limpio en UTF-8 (correctamente codificado)
    df.to_csv("outputs/Dataset_Talento_Limpio_UTF8.csv", index=False, encoding="utf-8")

    return df

cargar_y_limpiar_datos(ruta)