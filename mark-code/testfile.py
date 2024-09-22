
import pandas as pd
import numpy as np

# Make a dataset of Char, Code, and Rand as variables
# Use char codes from 65 to 90
# The rand can be any type of randon number
data = {
    "Code": list(range(65, 91)),
    "Char": [chr(x) for x in range(65, 91)],
    "Rand": [np.random.randn() for rand in range(65, 91)]
}

# Make a datagrame and add some NaN values
df = pd.DataFrame(data)
df

df.loc[df["Rand"] > 1.1, "Rand"] = np.nan
df

# Pick five random rows and copy them multiple times
for i in range(1, 20):
    num = np.random.randint(65, 90)
    row_copy = df.loc[df["Code"] == num]
    df = pd.concat([df, row_copy], ignore_index=True)

df

# Now do a group by
df.groupby("Char").mean()
