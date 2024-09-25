# Python Review

How do you put a string into a list?

Show how you use .format()

Make a tuple of the numbers 1 - 10

Return the domain only from an email address

Use lambda expressions and the filter() function to filter out words from a list

# Juypter Notebooks


What does ipykernel do?

Why do you install it in a venv?

How do you regisger a kernel and why would you do that? (using `python -m ipykernel install --user --name=<kernel_name> --display-name "<Display Name>`)

Do you have to register a kernel?

# Numpy

Create an array of zeros

Create an array of ones

Create an array of fives

Create a 3 x 3 matrix with values 0 to 9

Generate an array of 25 numbers sampled from a standard normal distribution

Create an array of 20 linearly spaced points between 0 and 1
for the array below, sum the columns

```python
mat = np.arange(1,26).reshape(5,5)

array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])

```

# Pandas

Explain why one needs to use '&' instead of 'and' (or '|' instead of or) when subsetting like this in a dataframe in pandas:

```py
df[(df['W']>0) & (df['Y'] > 1)]
```

When do you use .loc and why are you using it twice here?

```python
df.loc["G1"].loc[1]
df.loc["G2"].loc[2]["B"].item()
```

When do you use

       df.dropna()
       df.fillna()
       df.groupby()
              .min()
              .max()
              .sum()
              .mean()
              .std()

What does df.groupby() create?

What is the difference between using pd.merge() and pd.join()?

Show an example of these

       df[].unique()
       df[].value_counts()
       df[].apply()

What does this do?

       df.loc[0:1][["col1", "col2"]].sum(axis=1)

What question does this answer?

       df.groupby("Year")["BasePay"].mean().apply(lambda x: round(x, 2))

What role does "en" play in this Series? In other words, what is it?

       df["Language"].value_counts()["en"].item()

What is this doing?

       top_domain_names = ecom['Email'].str.split('@').str[1].value_counts().head(5)

# Matplotlib

What % command allows you see plots in Juypter notebooks?

What is the difference between these two approaches:

       figure = plt.figure()
       fig, ax = plt.subplots()

If you used plt.figure(), how do you make a plot of x^2? (*Hint: you add an axis using a function notation for location*)

If you use plt.subplots(), how do you make a plot fo x^2? 

What is happening in this code?

```py
       x = np.linspace(0,5)
       y = x ** 2

       fig, axes = plt.subplots(nrows = 1, ncols = 2)

       for item in axes:
              item.plot(x,y)

       axes[0].set_title("First Plot")
       axes[1].set_title("Second Plot")
```

What does `plt.tight_layout()` do?

How do you add labels of the x and y axes?

How do you change the line color or style?

How do you create a plot with two subplots that show x^2 and x^3? 

Plot a normal distribution in purple

# Seaborn

Load the 'tips' dataset using sns.load_dataset("tips") and create the following:

       sns.histplot()
       sns.jointplot() with a scatterplot
       sns.jointplot() with regression line
       sns.pairplot() with different colors for gender

What does this do?
       
       sns.barplot(x='sex',y='total_bill',hue="sex",data=tips, palette={"Male": "grey", "Female": "pink"})

How is sns.barplot different from sns.countplot? 

       sns.boxplot()

HOw do you run a simpel correlation matrix with a heatmap?

       corrs = tips.corr(numeric_only=True)

Load the flights dataset in seaborn and do a pivot table that shows how many passengers were on flights by year.

Now create a heat map of this

       sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)

*start with grids*
