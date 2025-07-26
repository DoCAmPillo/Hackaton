#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
df = pd.read_csv('Dataset_Talento_Limpio_UTF8.csv')

df


# In[51]:


# Reemplazo en la columna "turno"
df["turno"] = df["turno"].replace({
    "MaÃ±ana": "Mañana",
    "Tarde": "Tarde",
    "Noche": "Noche"
})

# Reemplazo en la columna "tipo_fallo"
df["tipo_fallo"] = df["tipo_fallo"].replace({
    "ElÃ©ctrico": "Eléctrico",
    "MecÃ¡nico": "Mecánico",
    "Revisar calibraciÃ³n": "Revisar calibración",
    "Ninguno": "Ninguno"
})

# Reemplazo en la columna "observaciones"
df["observaciones"] = df["observaciones"].replace({
    "OperaciÃ³n normal": "Operación normal",
    "Sobrecalentamiento": "Sobrecalentamiento"
})

# Si tienes una columna de respuestas como "sí", corregimos eso también:
df = df.replace("SÃ­", "Sí")  # Aplica globalmente a todo el DataFrame

# Revisa que ya estén corregidos
print(df["turno"].unique())
print(df["tipo_fallo"].unique())
print(df["observaciones"].unique())

# Eliminar espacios antes y después, y reemplazar errores de codificación comunes
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Reemplazar texto mal codificado en todo el DataFrame
df = df.replace({
    "Revisar calibraciÃ³n": "Revisar calibración",
    "CalibraciÃ³n": "Calibración",
    "SÃ­": "Sí",
    "MaÃ±ana": "Mañana",
    "ElÃ©ctrico": "Eléctrico",
    "MecÃ¡nico": "Mecánico",
    "OperaciÃ³n normal": "Operación normal"
}, regex=False)

df.fillna("No registra", inplace=True)


# In[52]:


df


# In[58]:


df.to_csv("Dataset_Talento_Limpio_UTF8.csv", index=False, encoding="utf-8-sig")

