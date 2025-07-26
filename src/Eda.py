# src/eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generar_eda(df, output_dir="outputs/"):
    """
    Genera visualizaciones básicas del análisis exploratorio de datos (EDA):
    - Distribución de eficiencia
    - Mapa de correlación de variables numéricas
    - Boxplot de eficiencia según turno

    Parámetros:
    - df (pd.DataFrame): dataset limpio
    - output_dir (str): carpeta donde guardar los gráficos
    """

    # Asegurar que el directorio de salida existe
    os.makedirs(output_dir, exist_ok=True)
    
    sns.set(style="whitegrid")

    # 1. Histograma de eficiencia porcentual
    plt.figure(figsize=(8, 5))
    sns.histplot(df['eficiencia_porcentual'], kde=True, bins=30)
    plt.title('Distribución de la Eficiencia Porcentual')
    plt.xlabel('Eficiencia (%)')
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/hist_eficiencia.png")
    plt.close()

    # 2. Mapa de calor de correlación
    plt.figure(figsize=(10, 8))
    correlacion = df.select_dtypes(include=["float64", "int64"]).corr()
    sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Mapa de Correlación de Variables Numéricas')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/correlacion.png")
    plt.close()

    # 3. Boxplot de eficiencia según turno
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='turno', y='eficiencia_porcentual')
    plt.title('Eficiencia Porcentual según Turno')
    plt.xlabel('Turno')
    plt.ylabel('Eficiencia (%)')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/boxplot_turno.png")
    plt.close()

    print("✅ Visualizaciones EDA generadas y guardadas en:", output_dir)


if __name__ == "__main__":
    # Asegúrate de que el archivo limpio exista en la ruta esperada
    df = pd.read_csv("outputs/Dataset_Talento_Limpio_UTF8.csv", encoding="utf-8-sig")
    generar_eda(df)