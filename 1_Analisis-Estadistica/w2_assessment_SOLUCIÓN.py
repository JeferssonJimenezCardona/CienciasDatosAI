
# coding: utf-8

# En este cuaderno, le pediremos que busque resúmenes numéricos para un determinado conjunto de datos. Utilizará los valores de lo que encuentre en esta tarea para responder preguntas en el cuestionario que sigue (hemos notado dónde se solicitarán valores específicos en el cuestionario, para que pueda registrarlos).

# In[109]:


import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 100)
path = "nhanes_2015_2016.csv"


# In[82]:


# # Primero, debe importar los datos de la ruta dada arriba
df = pd.read_csv(path) # usando pandas, lea los datos csv encontrados en la url definida por 'ruta'
# df.head(2)


# In[83]:


# Next, look at the 'head' of our DataFrame 'df'. 
df.head(2)


# * ¿Cuántas filas puedes ver cuando no pones un argumento en el método anterior?
# * ¿Cuántas filas puedes ver si usas un int como argumento?
# * ¿Puedes usar un flotador como argumento?

# In[84]:


# # Consideremos solo la característica (o variable) 'BPXSY2'
bp = df['BPXSY2']
bp = df['BPXSY2'].shape
bp


# ## Resúmenes numéricos
# ### Encuentra la media (nota esto para el cuestionario que sigue)

# In[85]:


# ¿Cuál es la media de 'BPXSY2.mean()'?
bp_mean =df['BPXSY2'].sum()
bp_mean =df['BPXSY2'].mean()
bp_mean


# En el método que utilizó anteriormente, ¿cómo se tratan las filas de datos faltantes?
# ¿Están totalmente excluidos? ¿Se cuentan como ceros? ¿Algo más?
# Si usó una función de biblioteca, intente buscar la documentación usando el código:
# ```
# ayuda (función_que_usó)
# ```
# Por ejemplo:
# ```
# ayuda (np. suma)
# ```
# 

# #### .dropna()
# Para asegurarnos de que no estamos tratando los datos faltantes de formas que no queremos, sigamos adelante y eliminemos todos los nans de nuestra Serie 'bp'

# In[89]:


# bp = bp.dropna()
bp=df.dropna(subset=["BPXSY2"])


# In[90]:


print(pd.isnull(bp.BPXSY2).sum())


# ### Encuentra el:
# * mediana
# * Máx.
# * Mín.
# * Desviación Estándar
# * Varianza
# 
# 
# Puede implementar cualquiera de estos desde python base (es decir, sin ninguno de los paquetes importados), pero hay funciones simples y con nombres intuitivos en la biblioteca numpy para todos estos. También podría usar el hecho de que 'bp' no es solo una lista, sino que es pandas.Series. Puede encontrar atributos y métodos de pandas.Series [here](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.Series.html).
# 
# Una gran parte de la programación es poder encontrar las funciones que necesita y comprender el formato de la documentación para que pueda implementar el código usted mismo, por lo que le recomendamos que busque en Internet cuando no esté seguro.

# ### Ejemplo:
# Encuentre la diferencia de un elemento en 'pb' en comparación con el elemento anterior en 'pb'.

# In[91]:


# Using the fact that 'bp' is a pd.Series object, can use the pd.Series method diff()
# call this method by: pd.Series.diff()
diff_by_series_method = bp.diff() 
# note that this returns a pd.Series object, that is, it had an index associated with it
diff_by_series_method.values # only want to see the values, not the index and values


# In[92]:


# Now use the numpy library instead to find the same values
# np.diff(array)
diff_by_np_method = np.diff(bp)
diff_by_np_method
# note that this returns an 'numpy.ndarray', which has no index associated with it, and therefore ignores
# the nan we get by the Series method


# In[93]:


# We could also implement this ourselves with some looping
diff_by_me = [] # create an empty list
for i in range(len(bp.values)-1): # iterate through the index values of bp
    diff = bp.values[i+1] - bp.values[i] # find the difference between an element and the previous element
    diff_by_me.append(diff) # append to out list
np.array(diff_by_me) # format as an np.array


# ### Su turno (tenga en cuenta estos valores para el cuestionario que sigue)

# In[94]:


bp_median =bp['BPXSY2'].sum()
bp_median


# In[98]:


bp_max = bp['BPXSY2'].max()
bp_max


# In[97]:


bp_min = bp['BPXSY2'].min()
bp_min


# In[95]:


bp_std = bp['BPXSY2'].std()
bp_std


# In[96]:


bp_var = bp['BPXSY2'].var()
bp_var


# ### Cómo encontrar el rango intercuartílico (nota este valor para el cuestionario que sigue)
# Esta vez necesitamos usar la biblioteca scipy.stats que importamos arriba con el nombre 'stats'

# In[100]:


bp_iqr = stats.iqr(bp)
bp_iqr


# In[102]:


Q1 = bp["BPXSY2"].quantile(0.25)
Q3 = bp["BPXSY2"].quantile(0.75)
IQR = Q3 - Q1
print("El rango intercuartílico de la columna 'nombre_columna' es:", IQR)


# ## Visualizando los datos
# A continuación, usaremos lo que ha aprendido del video *Tablas, histogramas, diagramas de caja en Python*

# In[105]:


# usar el método Series.describe() para ver algunas estadísticas descriptivas de nuestra Serie 'bp'
bp_descriptive_stats = bp
bp_descriptive_stats.describe()


# In[111]:


# Hacer un histograma de nuestros datos 'bp' usando la biblioteca seaborn
sns.distplot(bp["BPXSY2"], kde = False).set_title("Histogram of Total Bill")
plt.show()


# Is your histogram labeled and does it have a title?
# If not, try appending 
# ```
# .set(title='your_title', xlabel='your_x_label', ylabel='your_y_label')
# ```
# or just
# ```
# .set(title='your_title')
# ```
# to your graphing function

# In[112]:


# Haz un diagrama de caja de nuestros datos 'bp' usando la biblioteca seaborn. ¡Asegúrate de que tenga un título y etiquetas!
sns.boxplot(bp["BPXSY2"]).set_title("Box plot of the Total Bill")
plt.show()

