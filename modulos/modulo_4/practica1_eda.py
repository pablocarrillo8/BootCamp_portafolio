import pandas as pd
import numpy as np 
import matplotlib as plt
import seaborn as sns
import matplotlib.pyplot as plt

# Paso 1. Cargo de datos. Load the dataset
df = pd.read_csv('empleados_150.csv')

#Paso 2 .Inspeccion  Inicial
print("---------Primera filas del dataframe")
print(df.head(10))
print(df.describe())
print("+++++++++Informacion del dataframe")
print(df.info())

#Paso3 . Indentificacion de problemas 
print("Valor faltantes por columna")
print(df.isnull().sum())
print("Filas duplicadas",df.duplicated().sum())
print("Tipo de datos por columna")
print(df.dtypes)

#Paso4  Limpieza de los datos
df = df.drop_duplicates() #eliminar duplicados
df['Edad'] = pd.to_numeric(df['Edad'] , errors='coerce')
df['Edad'].fillna(df['Edad'].median(), inplace=True)
df['Salario'].fillna(df['Salario'].median(), inplace=True)

#Paso5 Estadistica descriptiva
print("\n Medidas de tendecia central (Edad):")
print("Media", df["Edad"].mean())
print("Mediana", df["Edad"].median())
print("Moda", df["Edad"].mode())

print("\n Medidas de dispersion (Salario)")
print("Rango", df["Salario"].max)
print("Media", df["Salario"].median())
print("Desviacion estandard:", df["Salario"].std())

#Paso6 Visualizacion
#5.1 Histogramas de edades
sns.histplot(df['Edad'],kde=True)
plt.title("Distribuccion de edad")
plt.xlabel("Edad")
plt.ylabel("Frencuencia")
plt.show()


#5.2 Boxplot de Salario
sns.boxplot(x=df['Salario'])
plt.title("Boxplot de Salario")
plt.xlabel("Salario")
plt.show()



# 5.3 correlacion entre variable
#scatterplot de edad versus salario
sns.scatterplot(x='Edad', y='Salario', data=df)
plt.title('Scatterplot de Edad vs Salario') 
plt.xlabel('Edad')
plt.ylabel('Salario')
#plt.show()

# 5.4 Analisis multivariado visual ---> pairplot
sns.pairplot(df[['Edad', 'Salario']])
plt.suptitle("Distribucion y relacion entre Edad y Salario", y=1.02)

"""
help(sns.pairplot)
>>> Help on function pairplot in module seaborn.axisgrid:

pairplot(
    data,
    *,
    hue=None,
    hue_order=None,
    palette=None,
    vars=None,
    x_vars=None,
    y_vars=None,
    kind='scatter',
    diag_kind='auto',
    markers=None,
    height=2.5,
    aspect=1,
    corner=False,
    dropna=False,
    plot_kws=None,
    diag_kws=None,
    grid_kws=None,
    size=None
)
    Plot pairwise relationships in a dataset.

    By default, this function will create a grid of Axes such that each numeric
    variable in ``data`` will by shared across the y-axes across a single row and
    the x-axes across a single column. The diagonal plots are treated
    differently: a univariate distribution plot is drawn to show the marginal
    distribution of the data in each column.

    It is also possible to show a subset of variables or plot different
    variables on the rows and columns.

    This is a high-level interface for :class:`PairGrid` that is intended to
    make it easy to draw a few common styles. You should use :class:`PairGrid`
    directly if you need more flexibility.

    Parameters
    ----------
    data : `pandas.DataFrame`
        Tidy (long-form) dataframe where each column is a variable and
        each row is an observation.
    hue : name of variable in ``data``
        Variable in ``data`` to map plot aspects to different colors.
    hue_order : list of strings
        Order for the levels of the hue variable in the palette
    palette : dict or seaborn color palette
        Set of colors for mapping the ``hue`` variable. If a dict, keys
        should be values  in the ``hue`` variable.
    vars : list of variable names
        Variables within ``data`` to use, otherwise use every column with
        a numeric datatype.
    {x, y}_vars : lists of variable names
        Variables within ``data`` to use separately for the rows and
        columns of the figure; i.e. to make a non-square plot.
    kind : {'scatter', 'kde', 'hist', 'reg'}
        Kind of plot to make.
    diag_kind : {'auto', 'hist', 'kde', None}
        Kind of plot for the diagonal subplots. If 'auto', choose based on
        whether or not ``hue`` is used.
    markers : single matplotlib marker code or list
        Either the marker to use for all scatterplot points or a list of markers
        with a length the same as the number of levels in the hue variable so that
        differently colored points will also have different scatterplot
        markers.
    height : scalar
        Height (in inches) of each facet.
    aspect : scalar
        Aspect * height gives the width (in inches) of each facet.
    corner : bool
        If True, don't add axes to the upper (off-diagonal) triangle of the
        grid, making this a "corner" plot.
    dropna : boolean
        Drop missing values from the data before plotting.
    {plot, diag, grid}_kws : dicts
        Dictionaries of keyword arguments. ``plot_kws`` are passed to the
        bivariate plotting function, ``diag_kws`` are passed to the univariate
        plotting function, and ``grid_kws`` are passed to the :class:`PairGrid`
        constructor.

    Returns
    -------
    grid : :class:`PairGrid`
        Returns the underlying :class:`PairGrid` instance for further tweaking.

    See Also
    --------
    PairGrid : Subplot grid for more flexible plotting of pairwise relationships.
    JointGrid : Grid for plotting joint and marginal distributions of two variables.

    Examples
    --------

    .. include:: ../docstrings/pairplot.rst

"""

plt.show()