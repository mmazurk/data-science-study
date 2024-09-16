# Python Review

- Splitting a string
- Using .format()
- Make a tuple of the numbers 1 - 10
- Return the domain only from an email address
- Use lambda expressions and the filter() function to filter out words from a list

# Juypter Notebooks

- What does ipykernel do?
- Why do you install it in a venv?
- How do you regisger a kernel and why would you do that? (using `python -m ipykernel install --user --name=<kernel_name> --display-name "<Display Name>`)
- Do you have to register a kernel?

# Numpy

- Create an array of zeros
- Create an array of ones
- Create an array of fives
- Create a 3 x 3 matrix with values 0 to 9
- Generate an array of 25 numbers sampled from a standard normal distribution
- Create an array of 20 linearly spaced points between 0 and 1
- for the array below, sum the columns

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
