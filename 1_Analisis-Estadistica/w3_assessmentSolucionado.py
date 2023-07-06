
# coding: utf-8

# En esta tarea, le pediremos que represente múltiples variables.
# 
# Usarás lo que encuentres en esta tarea para responder las preguntas en el cuestionario que sigue. Puede ser útil mantener este cuaderno al lado del cuestionario de esta semana en su pantalla.

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 100)
path = "Cartwheeldata.csv"


# In[4]:


# Primero, debe importar los datos de la rueda de carro desde la ruta dada arriba
df = pd.read_csv(path)# usando pandas, lea los datos csv encontrados en la url definida por 'ruta'


# In[5]:


# Next, look at the 'head' of our DataFrame 'df'. 
df.head(2)


# Si no puede recordar una función, abra un cuaderno o video anterior como referencia, o use su motor de búsqueda favorito para buscar una solución.

# ## Scatter plots

# Primero, veamos dos variables que esperamos tengan una fuerte relación, 'Height' y 'Wingspan'.

# In[7]:


# Haz un diagrama de dispersión de Seaborn con x = Height e y = Wingspan usando sns.scatterplot(x, y)
sns.scatterplot(x="Height", y="Wingspan", data=df)


# ¿Cómo describiría la relación entre 'Altura' y 'Envergadura'?
# Preguntas que puedes hacer:
# * ¿Es lineal?
# * ¿Hay valores atípicos?
# * ¿Son sus rangos similares o diferentes?
# 
# ¿De qué otra manera podrías describir la relación?

# Ahora veamos dos variables que aún no asumimos que tengan una relación fuerte, 'Wingspan' y 'CWDistance'

# In[13]:


# Haz un diagrama de dispersión de Seaborn con x = wingspan y =cartwheel distance
sns.scatterplot(x="Wingspan", y="CWDistance", data=df)


# ¿Cómo describiría la relación entre 'Wingspan' y 'CWDistance'?
# * ¿Es lineal?
# * ¿Hay valores atípicos?
# * ¿Son sus rangos similares o diferentes?
# 
# ¿De qué otra manera podrías describir la relación?

# Let hace la misma trama que la anterior, pero ahora incluya 'Género' como el esquema de color al incluir el argumento
# ```
# hue=df['Género']
# ```
# en la función Seaborn

# In[15]:


# Haz un diagrama de dispersión de Seaborn con x = wingspan  e y = CWDistance, y hue = gender
sns.scatterplot(x="Wingspan", y="CWDistance",hue="Gender",data=df)


# ¿Esta nueva información sobre la trama cambia su interpretación de la relación entre 'Wingspan' y 'CWDistance'?

# ## Barcharts
# Now lets plot barplots of 'Glasses'

# In[17]:


# Haz un gráfico de barras de Seaborn con x = glasses  y y = CWDistance
sns.barplot(x="Glasses", y="CWDistance", data=df)


# ¿Qué puedes decir sobre la relación de 'Glasses' y 'CWDistance'?

# In[20]:


# Make the same Seaborn boxplot as above, but include gender for the hue argument
sns.barplot(x="Glasses", y="CWDistance", hue="Gender",data=df)


# ¿Cómo cambia esta nueva trama su interpretación sobre la relación de 'Glasses' y 'CWDistance'?
